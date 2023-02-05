# -*- coding: utf-8 -*-
# @Time： 2023/2/5 19:32 
# @FileName: Parameter.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import json
import re


def get_parameter(parameter):
    with open('Config.json', 'r+', encoding='utf-8') as json_file:
        config = json.load(json_file)
    parameter = config[parameter]
    return parameter


def get_push_parameter(platform, value):
    with open('Config.json', 'r+', encoding='utf-8') as json_file:
        config = json.load(json_file)
    value = config["push"][platform][value]
    return value


def get_value(value, value_item='cookies'):
    value_list = get_parameter(value_item)
    value = re.search(r"{}=(\w+)".format(value), value_list).group(1)
    return value
