# -*- coding: utf-8 -*-
# @Time： 2023/2/5 19:21 
# @FileName: Live.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import requests
import time
from App.Parameter import get_parameter, get_value, save_config
from App.Stream import streaming

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
COOKIES = get_parameter("user_info", "cookies")
ROOM_ID = get_parameter("user_info", "room_id")
CSRF = get_value("bili_jct")
AREA = get_parameter("user_info", "area")


def start_live():
    """开始直播"""
    url = 'https://api.live.bilibili.com/room/v1/Room/startLive'
    headers = {'User-Agent': USER_AGENT, 'Cookie': COOKIES}
    params = {'room_id': ROOM_ID, 'area_v2': AREA, 'platform': "pc", 'csrf': CSRF}
    response = requests.post(url, headers=headers, params=params)
    json_data = response.json()
    print(json_data)
    if json_data["code"] == 0:
        addr = json_data['data']['rtmp']['addr']
        code = json_data['data']['rtmp']['code']
        time.sleep(3)
        print("直播已开始")
        try:
            streaming(addr, code)
        except Exception as e:
            print(e)
    else:
        print("开播失败")


def stop_live():
    """结束直播"""
    url = 'https://api.live.bilibili.com/room/v1/Room/stopLive'
    headers = {'User-Agent': USER_AGENT, 'Cookie': COOKIES}
    params = {'room_id': ROOM_ID, 'csrf': CSRF}
    response = requests.post(url, headers=headers, params=params)
    json_data = response.json()
    print(json_data)
    if json_data["code"] == 0:
        print("停播成功")
    else:
        print("停播失败")


def get_room_id(mid):
    """获取room_id"""
    url = 'https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld'
    headers = {'User-Agent': USER_AGENT}
    params = {'mid': mid}
    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()
    print(json_data)
    if json_data["code"] == 0:
        room_id = json_data["data"]["roomid"]
        save_config(room_id, "room_id")
        return True
    else:
        return False
