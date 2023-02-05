# -*- coding: utf-8 -*-
# @Time： 2023/2/5 19:46 
# @FileName: Stream.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import os


def streaming(live_addr, live_code):
    os.system('ffmpeg -re -i video.flv -c copy -f flv "{}{}"'.format(live_addr, live_code))
