# -*- coding: utf-8 -*-
# @Time: 2023/7/29 21:14 
# @FileName: Base.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import yaml
from loguru import logger


def read_yaml_file():
    with open("Config/config.yaml", 'r', encoding='utf-8') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as exc:
            logger.error(f"Error while reading YAML file: {exc}")
            return None


def write_yaml_file(value, parameter):
    with open("Config/config.yaml", 'r', encoding='utf-8') as file:
        try:
            data = yaml.safe_load(file)
            data["user_info"][parameter] = value
        except yaml.YAMLError as exc:
            logger.error(f"Error while loading YAML file: {exc}")
            return

    with open("Config/config.yaml", 'w', encoding='utf-8') as file:
        try:
            yaml.dump(data, file, allow_unicode=True)
        except yaml.YAMLError as exc:
            logger.error(f"Error while writing YAML file: {exc}")
