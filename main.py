# -*- coding: utf-8 -*-
# @Time： 2023/2/5 16:44 
# @FileName: main.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import time
from App.Live import startlive, stoplive
from App.Parameter import get_push_parameter
import App.Push


def main():
    startlive()
    time.sleep(15)
    stoplive()


if __name__ == '__main__':
    if get_push_parameter("telegram", "enable"):
        App.Push.telegram("直播已开始")
    start_time = time.time()
    main()
    duration = time.time() - start_time
    info = f'直播完成，共耗时 {int(duration)} 秒'
    print(info)
    if get_push_parameter("telegram", "enable"):
        App.Push.telegram(info)
