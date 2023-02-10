# 哔哩哔哩自动直播
### 使用方法
- 安装 `Python3.7` 或更高的版本
- 终端执行 `pip install -r requirements.txt` 安装依赖
- 运行 `python3 login.py` 扫码登录
- 填写 `config.json` 文件
```config
{
    "user_info": {
        "cookies": "", //登录信息，可使用 login.py 自动获取
        "room_id": 0, //自己的哔哩哔哩直播房间号
        "area": 192 //直播分区ID
    },
    "deploy": {
        "video_path": "video.flv", //视频文件路径（支持相对路径和绝对路径）
        "live_time": 15 //目标直播时长（单位：秒）
    },
    "push": { //推送配置
        "telegram": {
            "enable": false, //是否启用
            "group_id": "",
            "bot_token": ""
        }
    }
}
```
- 安装并配置 `ffmpeg`
- 运行 `python3 main.py`

### 注意事项
- 请保证程序完整运行，否则会导致哔哩哔哩直播未关闭（欢迎会解决这个问题的大佬前来PR）
- 若使用云服务器，请保证服务器位于中国大陆，否则会因为哔哩哔哩的限制导致无法开播