# -*- coding: utf-8 -*-
# @Time: 2023/2/5 19:46
# @FileName: Stream.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import os
import time
import subprocess
from loguru import logger


def streaming(live_addr, live_code, config):
    stream_type = config["type"]
    video_path = config["video_path"]
    live_time = config["live_time"]
    if stream_type == 1:
        for root, dirs, files in os.walk(video_path):
            if live_time == 0:
                for file in files:
                    logger.info(f"即将直播: {file}")
                    ffmpeg_run(live_addr, live_code, os.path.join(root, file))
            elif live_time == -1:
                while True:
                    for file in files:
                        logger.info(f"即将直播: {file}")
                        ffmpeg_run(live_addr, live_code, os.path.join(root, file))
            else:
                start_time = time.time()
                end_time = start_time + live_time
                while time.time() < end_time:
                    for file in files:
                        logger.info(f"即将直播: {file}")
                        ffmpeg_run(live_addr, live_code, os.path.join(root, file))
                        if time.time() >= end_time:
                            break
    else:
        if live_time != 0 and live_time != -1:
            start_time = time.time()
            end_time = start_time + live_time
            while time.time() < end_time:
                ffmpeg_run(live_addr, live_code, video_path)
        elif live_time == 0:
            ffmpeg_run(live_addr, live_code, video_path)
        else:
            while True:
                ffmpeg_run(live_addr, live_code, video_path)


def ffmpeg_run(live_addr, live_code, video_path):
    cmd = f'ffmpeg -re -i {video_path} -c copy -f flv "{live_addr}{live_code}" -flvflags no_duration_filesize'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    p.wait()
    output, error = p.communicate()
    logger.debug((output.decode()))
