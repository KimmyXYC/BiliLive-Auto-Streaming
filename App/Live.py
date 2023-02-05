# -*- coding: utf-8 -*-
# @Time： 2023/2/5 19:21 
# @FileName: Live.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import requests
import time
from App.Parameter import get_parameter, get_value
from App.Stream import streaming

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
COOKIES = get_parameter("cookies")
ROOM_ID = get_parameter("room_id")
CSRF = get_value("bili_jct")


def startlive():
    # room_id = get_room_id(get_value("DedeUserID"))
    url = 'https://api.live.bilibili.com/room/v1/Room/startLive'
    headers = {'User-Agent': USER_AGENT, 'Cookie': COOKIES}
    params = {'room_id': ROOM_ID, 'area_v2': 192, 'platform': "pc", 'csrf': CSRF}
    response = requests.post(url, headers=headers, params=params)
    json_data = response.json()
    print(json_data)
    addr = json_data['data']['rtmp']['addr']
    code = json_data['data']['rtmp']['code']
    time.sleep(10)
    streaming(addr, code)


def stoplive():
    # room_id = get_room_id(get_value("DedeUserID"))
    url = 'https://api.live.bilibili.com/room/v1/Room/stopLive'
    headers = {'User-Agent': USER_AGENT, 'Cookie': COOKIES}
    params = {'room_id': ROOM_ID, 'csrf': CSRF}
    response = requests.post(url, headers=headers, params=params)
    json_data = response.json()
    print(json_data)


# def get_room_id(mid):
#     url = 'https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld'
#     headers = {'User-Agent': USER_AGENT}
#     params = {'mid': mid}
#     response = requests.get(url, headers=headers, params=params)
#     json_data = response.json()
#     print(json_data)
#     room_id = json_data["push"]["data"]["roomid"]
#     return room_id
