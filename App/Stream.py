# -*- coding: utf-8 -*-
# @Time： 2023/2/5 19:46 
# @FileName: Stream.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import os
import time
import subprocess
from App.Parameter import get_parameter

VIDEO_PATH = get_parameter("deploy", "video_path")
LIVE_TIME = get_parameter("deploy", "live_time")


def streaming(live_addr, live_code):
    start_time = time.time()
    video_length = get_video_length()
    end_time = start_time + LIVE_TIME
    while time.time() + video_length < end_time:
        ffmpeg_run(live_addr, live_code)
        time.sleep(3)

    time_left = end_time - time.time()
    if time_left > 0:
        cmd = f'ffmpeg -re -i {VIDEO_PATH} -c copy -f flv "{live_addr}{live_code}"'
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        time.sleep(time_left)
    else:
        pass


def get_video_length():
    """获取视频长度"""
    command = f'ffprobe -i {VIDEO_PATH} -show_entries format=duration -v quiet -of csv="p=0"'
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    video_length = float(result.stdout.readlines()[0])
    return video_length


def ffmpeg_run(live_addr, live_code):
    """推送直播流"""
    os.system(f'ffmpeg -re -i {VIDEO_PATH} -c copy -f flv "{live_addr}{live_code}"')
