# -*- coding: utf-8 -*-
# @Time: 2023/2/5 19:32
# @FileName: Parameter.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import json
import re
import urllib
import hashlib
from loguru import logger


def get_value(value, values):
    try:
        value = re.search(r"{}=(\w+)".format(value), values).group(1)
        return value
    except Exception as e:
        logger.error(f"获取指定值失败: {e}")
        return None


def process_cookies(cookies):
    try:
        cookies_str = ""
        for key, value in cookies.items():
            cookies_str += f"{key}={value}; "
        return cookies_str[:-2]
    except Exception as e:
        logger.error(f"处理 Cookies 失败: {e}")
        return None


def appsign(params, appkey, appsec):
    params.update({'appkey': appkey})
    params = dict(sorted(params.items()))
    query = urllib.parse.urlencode(params)
    sign = hashlib.md5((query + appsec).encode()).hexdigest()
    params.update({'sign': sign})
    return params
