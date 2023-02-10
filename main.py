# -*- coding: utf-8 -*-
# @Time： 2023/2/5 16:44 
# @FileName: main.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import time
from App.Push import message_push
from App.Live import start_live, stop_live, get_room_id
from App.Parameter import get_parameter, get_value

MID = get_value("DedeUserID")


def main():
    if get_parameter("user_info", "room_id"):
        start_time = time.time()
        start_live()
        time.sleep(3)
        stop_live()
        duration = time.time() - start_time
        info = f'直播完成，共耗时 {int(duration)} 秒'
        print(info)
        message_push(info)
    else:
        print("未填写 room_id, 正在尝试自动获取")
        if get_room_id(MID):
            print("获取成功")
            print("请重新启动程序以开始直播")
        else:
            print("获取失败")


if __name__ == '__main__':
    main()
