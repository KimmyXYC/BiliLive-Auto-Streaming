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


def get_parameter(*parameters):
    try:
        value = get_config_file()
        for parameter in parameters:
            value = value.get(parameter)
        return value
    except Exception as e:
        logger.error(f"获取指定参数失败: {e}")
        return None


def get_value(value, values):
    try:
        value = re.search(r"{}=(\w+)".format(value), values).group(1)
        return value
    except Exception as e:
        logger.error(f"获取指定值失败: {e}")
        return None


def get_config_file():
    try:
        with open('Config.json', 'r+', encoding='utf-8') as json_file:
            data = json.load(json_file)
            json_file.close()
        return data
    except Exception as e:
        logger.error(f"获取配置文件失败: {e}")
        return None


def save_config(value, parameter):
    try:
        with open('Config.json', 'r+', encoding='utf-8') as json_file:
            data = json.load(json_file)
            data["user_info"][parameter] = value
            json_file.seek(0)
            json.dump(data, json_file, ensure_ascii=False, indent=2)
            json_file.truncate()
            json_file.close()
    except Exception as e:
        logger.error(f"保存配置文件失败: {e}")


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
