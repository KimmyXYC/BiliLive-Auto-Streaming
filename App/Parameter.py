# -*- coding: utf-8 -*-
# @Time： 2023/2/5 19:32 
# @FileName: Parameter.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import json
import re


def get_parameter(*parameters):
    """从配置文件中读取指定参数"""
    value = get_config_file()
    for parameter in parameters:
        value = value.get(parameter)
    return value


def get_value(value, value_item='cookies'):
    """从指定内容中正则匹配获取指定值"""
    value_list = get_parameter("user_info", value_item)
    value = re.search(r"{}=(\w+)".format(value), value_list).group(1)
    return value


def get_config_file():
    """获取config文件"""
    with open('Config.json', 'r+', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def save_config(value, parameter):
    """保存数据到config文件"""
    with open('Config.json', 'r+', encoding='utf-8') as json_file:
        data = json.load(json_file)
        data["user_info"][parameter] = value
        json_file.seek(0)
        json.dump(data, json_file, ensure_ascii=False, indent=4)
        json_file.truncate()


def process_cookies(cookies):
    """将cookies从字典格式转换为字符串格式"""
    cookies_str = ""
    for key, value in cookies.items():
        cookies_str += f"{key}={value}; "
    return cookies_str[:-2]
