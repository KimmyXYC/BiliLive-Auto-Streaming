# -*- coding: utf-8 -*-
# @Time： 2023/2/5 20:17 
# @FileName: Push.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import requests
from App.Parameter import get_parameter


def message_push(message):
    if get_parameter("push", "telegram", "enable"):
        telegram(message)


def telegram(message):
    bot_token = get_parameter("push", "telegram", "bot_token")
    group_id = get_parameter("push", "telegram", "group_id")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={group_id}&text={message}"
    response = requests.get(url)
    if response.status_code == 200:
        print("【Telegram推送】成功")
    else:
        print("【Telegram推送】失败")
