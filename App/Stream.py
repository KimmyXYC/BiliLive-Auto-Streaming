# -*- coding: utf-8 -*-
# @Time： 2023/2/5 19:46 
# @FileName: Stream.py
# @Software： PyCharm
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
        for root, dirs, files in os.walk(TYPE):
            logger.info(f"当前目录: {root}")
            logger.info(f"当前目录下的文件: {files}")
            logger.info(f"当前直播时间: {LIVE_TIME}")
            if LIVE_TIME == 0:
                for file in files:
                    logger.info(f"即将直播: {file}")
                    ffmpeg_run(live_addr, live_code, os.path.join(root, file))
                    time.sleep(3)
            elif LIVE_TIME == -1:
                while True:
                    for file in files:
                        logger.info(f"即将直播: {file}")
                        ffmpeg_run(live_addr, live_code, os.path.join(root, file))
                        time.sleep(3)
            else:
                start_time = time.time()
                end_time = start_time + LIVE_TIME
                while time.time() < end_time:
                    for file in files:
                        logger.info(f"即将直播: {file}")
                        ffmpeg_run(live_addr, live_code, os.path.join(root, file))
                        time.sleep(3)
                        if time.time() >= end_time:
                            break
    else:
        logger.info(f"当前直播时间: {LIVE_TIME}")
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
                time.sleep(3)


def get_video_length():
    try:
        command = f'ffprobe -i {VIDEO_PATH} -show_entries format=duration -v quiet -of csv="p=0"'
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        video_length = float(result.stdout.readlines()[0])
        logger.debug(f"视频时长: {video_length}")
        return video_length
    except Exception as e:
        logger.error(f"发生错误: {e}")
        return None


def ffmpeg_run(live_addr, live_code, video_path):
    logger.debug(f"当前时间: {LIVE_TIME}")
    cmd = f'ffmpeg -re -i {video_path} -c copy -f flv "{live_addr}{live_code}"'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    p.wait()
    output, error = p.communicate()
    logger.debug((output.decode()))
