# -*- coding: utf-8 -*-
# @Time: 2023/7/29 20:44 
# @FileName: Tool.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import requests
from loguru import logger
from Utils.Json import save_config


def get_room_id(mid):
    url = 'https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld'
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/96.0.4664.110 Safari/537.36"}
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
