# -*- coding: utf-8 -*-
# @Time: 2023/2/5 16:44
# @FileName: main.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import time
import sys
import signal
from loguru import logger
from App.Push import Pusher
from App.Live import BiliLive
from Utils.Parameter import get_value
from Utils.Tool import get_room_id
from Utils.Base import read_yaml_file


def signal_handler(signal, frame):
    logger.success("检测到终止信号, 开始停播")
    config = read_yaml_file()
    if config["user_info"]["room_id"]:
        BiliLive(config).stop_live()
    sys.exit(0)


def main():
    config = read_yaml_file()
    pusher = Pusher(push_config=config["push"])
    if not config["user_info"]["cookies"]:
        logger.error("Cookies 未填写, 无法执行直播任务")
        return
    if config["user_info"]["room_id"]:
        streamer = BiliLive(config, pusher=pusher)
        start_time = time.time()
        try:
            streamer.start_live()
        except Exception as e:
            logger.error(f"直播发生错误: {e}")
        time.sleep(3)
        streamer.stop_live()
        streamer.share_room()
        streamer.get_live_receive()
        duration = time.time() - start_time
        logger.success(f"直播完成, 共耗时 {int(duration)} 秒")
        pusher.push(f"直播完成, 共耗时 {int(duration)} 秒")
    else:
        logger.warning("room_id 未填写, 正在尝试自动获取……")
        mid = get_value("DedeUserID", config["user_info"]["cookies"])
        if get_room_id(mid):
            logger.success("获取成功")
            logger.info("请重启程序以开启自动直播任务")
        else:
            logger.error("获取失败, 请手动填写 room_id")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    logger.remove()
    handler_id = logger.add(sys.stderr, level="INFO")
    logger.add(sink='run.log',
               format="{time} - {level} - {message}",
               level="INFO",
               rotation="20 MB",
               enqueue=True)
    main()
