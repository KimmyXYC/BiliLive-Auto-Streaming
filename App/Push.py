# -*- coding: utf-8 -*-
# @Time： 2023/2/5 20:17 
# @FileName: Push.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import requests
from App.Parameter import get_push_parameter


def telegram(info):
    bot_token = get_push_parameter("telegram", "bot_token")
    group_id = get_push_parameter("telegram", "group_id")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={group_id}&text={info}"
    print(url)
    response = requests.get(url)
    print(response)
