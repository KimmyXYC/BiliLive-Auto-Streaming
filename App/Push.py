# -*- coding: utf-8 -*-
# @Time: 2023/2/5 20:17
# @FileName: Push.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import requests
from datetime import datetime
from loguru import logger


class Pusher:
    def __init__(self, push_config):
        self.push_config = push_config

    def push(self, message):
        message = f"[{datetime.now().strftime('%H:%M:%S')}] {message}"
        try:
            if self.push_config["telegram"]["enable"]:
                self.telegram(message)
            if self.push_config["pushplus"]["enable"]:
                self.pushplus(message)
            if self.push_config["server"]["enable"]:
                self.server(message)
            if self.push_config["ijingniu"]["enable"]:
                self.ijingniu(message)
            if self.push_config["bark"]["enable"]:
                self.bark(message)
        except Exception as e:
            logger.error(f"推送发生错误: {e}")

    def telegram(self, message):
        bot_token = self.push_config["telegram"]["bot_token"]
        group_id = self.push_config["telegram"]["group_id"]
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={group_id}&text=【BiliLive】{message}"
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

    def pushplus(self, message):
        token = self.push_config["pushplus"]["token"]
        url = f"http://www.pushplus.plus/send/{token}?title=【BiliLive】&text={message}"
        response = requests.get(url)
        if response.status_code == 200:
            logger.success("【PushPlus推送】成功")
        else:
            logger.warning("【PushPlus推送】失败")

    def server(self, message):
        sendkey = self.push_config["server"]["sendkey"]
        url = f"https://sctapi.ftqq.com/{sendkey}.send?title=【BiliLive】&desp={message}"
        response = requests.post(url)
        if response.status_code == 200:
            logger.success("【Server酱推送】成功")
        else:
            logger.warning("【Server酱推送】失败")

    def ijingniu(self, message):
        channelkey = self.push_config["ijingniu"]["channelkey"]
        url = f"http://push.ijingniu.cn/send?key={channelkey}&head=【BiliLive】&body={message}"
        response = requests.get(url)
        if response.status_code == 200:
            logger.success("【及时达推送】成功")
        else:
            logger.warning("【及时达推送】失败")

    def bark(self, message):
        if self.push_config["bark"]["server"]:
            server = self.push_config["bark"]["server"]
        else:
            server = "https://api.day.app"
        key = self.push_config["bark"]["key"]
        url = f"{server}/{key}/【BiliLive】/{message}"
        response = requests.get(url)
        if response.status_code == 200:
            logger.success("【Bark】成功")
        else:
            logger.warning("【Bark】失败")
