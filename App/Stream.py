# -*- coding: utf-8 -*-
# @Time: 2023/2/5 19:46
# @FileName: Stream.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import os
import time
import subprocess
from loguru import logger
from App.Parameter import get_parameter

DEPLOY = get_parameter("deploy")
TYPE = DEPLOY["type"]
VIDEO_PATH = DEPLOY["video_path"]
LIVE_TIME = DEPLOY["live_time"]


def streaming(live_addr, live_code):
    if TYPE == 1:
        for root, dirs, files in os.walk(VIDEO_PATH):
            if LIVE_TIME == 0:
                for file in files:
                    logger.info(f"即将直播: {file}")
                    ffmpeg_run(live_addr, live_code, os.path.join(root, file))
            elif LIVE_TIME == -1:
                while True:
                    for file in files:
                        logger.info(f"即将直播: {file}")
                        ffmpeg_run(live_addr, live_code, os.path.join(root, file))
            else:
                start_time = time.time()
                end_time = start_time + LIVE_TIME
                while time.time() < end_time:
                    for file in files:
                        logger.info(f"即将直播: {file}")
                        ffmpeg_run(live_addr, live_code, os.path.join(root, file))
                        if time.time() >= end_time:
                            break
    else:
        if LIVE_TIME != 0 and LIVE_TIME != -1:
            start_time = time.time()
            end_time = start_time + LIVE_TIME
            while time.time() < end_time:
                ffmpeg_run(live_addr, live_code, VIDEO_PATH)
        elif LIVE_TIME == 0:
            ffmpeg_run(live_addr, live_code, VIDEO_PATH)
        else:
            while True:
                ffmpeg_run(live_addr, live_code, VIDEO_PATH)


def ffmpeg_run(live_addr, live_code, video_path):
    cmd = f'ffmpeg -re -i {video_path} -c copy -f flv "{live_addr}{live_code}"'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    p.wait()
    output, error = p.communicate()
    logger.debug((output.decode()))
