# -*- coding: utf-8 -*-
# @Time: 2023/7/29 20:38 
# @FileName: Json.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import json
from loguru import logger


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
