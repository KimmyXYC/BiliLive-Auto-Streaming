# -*- coding: utf-8 -*-
# @Time: 2023/2/5 19:21
# @FileName: Live.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import requests
import time
from loguru import logger
from Utils.Parameter import get_value, appsign
from App.Stream import streaming


class BiliLive:
    def __init__(self, config, pusher=None):
        self.USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                          "Chrome/96.0.4664.110 Safari/537.36"
        self.COOKIES = config["user_info"]["cookies"]
        self.APPKEY = "1d8b6e7d45233436"
        self.APPSEC = "560c52ccd288fed045859ed18bffd973"
        self.ROOM_ID = config["user_info"]["room_id"]
        self.AREA = config["user_info"]["area"]
        self.CSRF = get_value("bili_jct", self.COOKIES)
        self.config = config
        self.pusher = pusher

    def start_live(self):
        url = 'https://api.live.bilibili.com/room/v1/Room/startLive'
        headers = {'User-Agent': self.USER_AGENT, 'Cookie': self.COOKIES}
        params = {'room_id': self.ROOM_ID, 'area_v2': self.AREA, 'platform': "pc", 'csrf': self.CSRF}
        response = requests.post(url, headers=headers, params=params)
        json_data = response.json()
        logger.debug(json_data)
        if json_data["code"] == 0:
            addr = json_data['data']['rtmp']['addr']
            code = json_data['data']['rtmp']['code']
            logger.success("直播已开始")
            self.pusher.push(f"直播已开始, 3秒后开始推流")
            time.sleep(3)
            try:
                logger.success("开始推流")
                streaming(addr, code, self.config["deploy"])
            except Exception as e:
                logger.error(f"发生错误: {e}")
        else:
            logger.error(f"开播失败, 错误码: {json_data['code']}")
            logger.debug(json_data)

    def stop_live(self):
        url = 'https://api.live.bilibili.com/room/v1/Room/stopLive'
        headers = {'User-Agent': self.USER_AGENT, 'Cookie': self.COOKIES}
        params = {'room_id': self.ROOM_ID, 'csrf': self.CSRF}
        response = requests.post(url, headers=headers, params=params)
        json_data = response.json()
        logger.debug(json_data)
        if json_data["code"] == 0:
            logger.success("停播成功")
        else:
            logger.error(f"停播失败, 错误码: {json_data['code']}")
            logger.debug(json_data)

    def get_live_receive(self):
        url = 'https://api.live.bilibili.com/xlive/anchor-task-interface/api/v1/GetAnchorTaskCenterReceiveReward'
        headers = {'User-Agent': self.USER_AGENT, 'Cookie': self.COOKIES}
        response = requests.get(url, headers=headers)
        json_data = response.json()
        logger.debug(json_data)
        if json_data["code"] == 0:
            logger.success("获取奖励成功")
        else:
            logger.error(f"获取奖励失败, 错误码: {json_data['code']}")
            logger.debug(json_data)

    def share_room(self):
        url = 'https://api.live.bilibili.com/xlive/app-room/v1/index/shareConf'
        headers = {'User-Agent': self.USER_AGENT, 'Cookie': self.COOKIES}
        params = {'room_id': self.ROOM_ID, 'platform': "android", 'ts': int(time.time())}
        params = appsign(params, self.APPKEY, self.APPSEC)
        response = requests.get(url, headers=headers, params=params)
        json_data = response.json()
        logger.debug(json_data)
        if json_data["code"] == 0:
            logger.success("分享直播间成功")
        else:
            logger.error(f"分享直播间失败, 错误码: {json_data['code']}")
            logger.debug(json_data)
