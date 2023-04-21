# -*- coding: utf-8 -*-
# @Time： 2023/2/5 19:21 
# @FileName: Live.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import requests
import time
from loguru import logger
from App.Parameter import get_parameter, get_value, save_config
from App.Stream import streaming

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
USER_INFO = get_parameter("user_info")
COOKIES = USER_INFO["cookies"]
ROOM_ID = USER_INFO["room_id"]
CSRF = get_value("bili_jct")
AREA = USER_INFO["area"]


def start_live():
    url = 'https://api.live.bilibili.com/room/v1/Room/startLive'
    headers = {'User-Agent': USER_AGENT, 'Cookie': COOKIES}
    params = {'room_id': ROOM_ID, 'area_v2': AREA, 'platform': "pc", 'csrf': CSRF}
    response = requests.post(url, headers=headers, params=params)
    json_data = response.json()
    logger.debug(json_data)
    if json_data["code"] == 0:
        addr = json_data['data']['rtmp']['addr']
        code = json_data['data']['rtmp']['code']
        logger.success("直播已开始")
        logger.success("开始推流")
        try:
            streaming(addr, code)
        except Exception as e:
            logger.error(f"发生错误: {e}")
    else:
        logger.error(f"开播失败, 错误码: {json_data['code']}")


def stop_live():
    url = 'https://api.live.bilibili.com/room/v1/Room/stopLive'
    headers = {'User-Agent': USER_AGENT, 'Cookie': COOKIES}
    params = {'room_id': ROOM_ID, 'csrf': CSRF}
    response = requests.post(url, headers=headers, params=params)
    json_data = response.json()
    logger.debug(json_data)
    if json_data["code"] == 0:
        logger.success("停播成功")
    else:
        logger.error(f"停播失败, 错误码: {json_data['code']}")


def get_live_receive():
    url = 'https://api.live.bilibili.com/xlive/anchor-task-interface/api/v1/GetAnchorTaskCenterReceiveReward'
    headers = {'User-Agent': USER_AGENT, 'Cookie': COOKIES}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    logger.debug(json_data)
    if json_data["code"] == 0:
        logger.success("获取奖励成功")
    else:
        logger.error(f"获取奖励失败, 错误码: {json_data['code']}")


def get_room_id(mid):
    url = 'https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld'
    headers = {'User-Agent': USER_AGENT}
    params = {'mid': mid}
    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()
    logger.debug(json_data)
    if json_data["code"] == 0:
        room_id = json_data["data"]["roomid"]
        save_config(room_id, "room_id")
        return True
    else:
        return False
