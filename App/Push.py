# -*- coding: utf-8 -*-
# @Time: 2023/2/5 20:17
# @FileName: Push.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import requests
from loguru import logger
from App.Parameter import get_parameter


def message_push(message):
    push_config = get_parameter("push")
    pusher = Push(message, push_config)
    try:
        if push_config["telegram"]["enable"]:
            pusher.telegram()
        if push_config["pushplus"]["enable"]:
            pusher.pushplus()
        if push_config["server"]["enable"]:
            pusher.server()
        if push_config["ijingniu"]["enable"]:
            pusher.ijingniu()
        if push_config["bark"]["enable"]:
            pusher.bark()
    except Exception as e:
        logger.error(f"推送发生错误: {e}")


class Push:
    def __init__(self, message, push_config):
        self.message = message
        self.push_config = push_config

    def telegram(self):
        bot_token = self.push_config["telegram"]["bot_token"]
        group_id = self.push_config["telegram"]["group_id"]
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={group_id}&text=【BiliLive】{self.message}"
        if self.push_config["telegram"]["proxy"]:
            proxies = {
                'http': self.push_config["telegram"]["proxy"],
                'https': self.push_config["telegram"]["proxy"]
            }
            response = requests.get(url, proxies=proxies)
        else:
            response = requests.get(url)
        if response.status_code == 200:
            logger.success("【Telegram推送】成功")
        else:
            logger.warning("【Telegram推送】失败")

    def pushplus(self):
        token = self.push_config["pushplus"]["token"]
        url = f"http://www.pushplus.plus/send/{token}?title=【BiliLive】&text={self.message}"
        response = requests.get(url)
        if response.status_code == 200:
            logger.success("【PushPlus推送】成功")
        else:
            logger.warning("【PushPlus推送】失败")

    def server(self):
        sendkey = self.push_config["server"]["sendkey"]
        url = f"https://sctapi.ftqq.com/{sendkey}.send?title=【BiliLive】&desp={self.message}"
        response = requests.post(url)
        if response.status_code == 200:
            logger.success("【Server酱推送】成功")
        else:
            logger.warning("【Server酱推送】失败")

    def ijingniu(self):
        channelkey = self.push_config["ijingniu"]["channelkey"]
        url = f"http://push.ijingniu.cn/send?key={channelkey}&head=【BiliLive】&body={self.message}"
        response = requests.get(url)
        if response.status_code == 200:
            logger.success("【及时达推送】成功")
        else:
            logger.warning("【及时达推送】失败")

    def bark(self):
        if self.push_config["bark"]["server"]:
            server = self.push_config["bark"]["server"]
        else:
            server = "https://api.day.app"
        key = self.push_config["bark"]["key"]
        url = f"{server}/{key}/【BiliLive】/{self.message}"
        response = requests.get(url)
        if response.status_code == 200:
            logger.success("【Bark】成功")
        else:
            logger.warning("【Bark】失败")
