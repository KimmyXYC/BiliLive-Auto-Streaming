# -*- coding: utf-8 -*-
# @Time： 2023/2/5 19:46 
# @FileName: Stream.py
# @Software： PyCharm
# @GitHub: KimmyXYC
import os
import time
import subprocess
from App.Parameter import get_parameter

TYPE = get_parameter("deploy", "type")
VIDEO_PATH = get_parameter("deploy", "video_path")
LIVE_TIME = get_parameter("deploy", "live_time")


def streaming(live_addr, live_code):
    if TYPE == 1:
        for root, dirs, files in os.walk(TYPE):
            if LIVE_TIME == 0:
                for file in files:
                    ffmpeg_run(live_addr, live_code, os.path.join(root, file))
            elif LIVE_TIME == -1:
                while True:
                    for file in files:
                        ffmpeg_run(live_addr, live_code, os.path.join(root, file))
            else:
                start_time = time.time()
                end_time = start_time + LIVE_TIME
                while time.time() < end_time:
                    for file in files:
                        ffmpeg_run(live_addr, live_code, os.path.join(root, file))
                        if time.time() >= end_time:
                            break
    else:
        if LIVE_TIME != 0 and LIVE_TIME != -1:
            start_time = time.time()
            video_length = get_video_length()
            end_time = start_time + LIVE_TIME
            while time.time() + video_length < end_time:
                ffmpeg_run(live_addr, live_code, VIDEO_PATH)
                time.sleep(3)

            time_left = end_time - time.time()
            if time_left > 0:
                cmd = f'ffmpeg -re -i {VIDEO_PATH} -c copy -f flv "{live_addr}{live_code}"'
                subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
                time.sleep(time_left)
            else:
                pass
        elif LIVE_TIME == 0:
            ffmpeg_run(live_addr, live_code, VIDEO_PATH)
        else:
            while True:
                ffmpeg_run(live_addr, live_code, VIDEO_PATH)


def get_video_length():
    """获取视频长度"""
    command = f'ffprobe -i {VIDEO_PATH} -show_entries format=duration -v quiet -of csv="p=0"'
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    video_length = float(result.stdout.readlines()[0])
    return video_length


def ffmpeg_run(live_addr, live_code, video_path):
    """推送直播流"""
    os.system(f'ffmpeg -re -i {video_path} -c copy -f flv "{live_addr}{live_code}"')
