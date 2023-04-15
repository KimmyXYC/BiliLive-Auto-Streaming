# -*- coding: utf-8 -*-
# @Time： 2023/2/5 20:17 
# @FileName: Push.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import requests
from loguru import logger
from App.Parameter import get_parameter

push_config = get_parameter("push")


def message_push(message):
    try:
        if push_config["telegram"]["enable"]:
            telegram(message)
        if push_config["pushplus"]["enable"]:
            pushplus(message)
        if push_config["server"]["enable"]:
            server(message)
        if push_config["ijingniu"]["enable"]:
            ijingniu(message)
    except Exception as e:
        logger.error(f"推送发生错误: {e}")


def telegram(message):
    bot_token = push_config["telegram"]["bot_token"]
    group_id = push_config["telegram"]["group_id"]
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={group_id}&text={message}"
    if push_config["telegram"]["proxy"]:
        proxies = {
            'http': push_config["telegram"]["proxy"],
            'https': push_config["telegram"]["proxy"]
        }
        response = requests.get(url, proxies=proxies)
    else:
        response = requests.get(url)
    if response.status_code == 200:
        logger.success("【Telegram推送】成功")
    else:
        logger.warning("【Telegram推送】失败")


def pushplus(message):
    token = push_config["pushplus"]["token"]
    url = f"http://www.pushplus.plus/send/{token}?title=【BiliLive】&text={message}"
    response = requests.get(url)
    if response.status_code == 200:
        logger.success("【PushPlus推送】成功")
    else:
        logger.warning("【PushPlus推送】失败")


def server(message):
    sendkey = push_config["server"]["sendkey"]
    url = f"f'https://sctapi.ftqq.com/{sendkey}.send?title=【BiliLive】&desp={message}"
    response = requests.post(url)
    if response.status_code == 200:
        logger.success("【Server酱推送】成功")
    else:
        logger.warning("【Server酱推送】失败")


def ijingniu(message):
    channelkey = push_config["ijingniu"]["channelkey"]
    url = f"f'http://push.ijingniu.cn/send?key={channelkey}&head=【BiliLive】&body={message}"
    response = requests.get(url)
    if response.status_code == 200:
        logger.success("【及时达推送】成功")
    else:
        logger.warning("【及时达推送】失败")
