# -*- coding: utf-8 -*-
# @Time： 2023/5/27 21:32 
# @FileName: test.py.py
# @Software： PyCharm
# @GitHub: KimmyXYC
from App.Push import Pusher
from Utils.Base import read_yaml_file


def main():
    config = read_yaml_file()
    pusher = Pusher(push_config=config["push"])
    pusher.push("推送测试消息")


if __name__ == '__main__':
    main()
