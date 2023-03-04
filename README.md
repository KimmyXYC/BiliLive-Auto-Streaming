# 哔哩哔哩自动直播
### 使用方法
- 安装 `Python3.7` 或更高的版本
- 执行 `pip install -r requirements.txt` 安装依赖
- 执行 `python3 login.py` 扫码登录哔哩哔哩账号
    * 或从 `https://api.bilibili.com/x/web-interface/nav` 请求中获取 Cookies 填入
- 填写 `Config.json` 文件
```config
{
    "user_info": {
        "cookies": "", //登录信息，可使用 login.py 自动获取
        "room_id": 0, //自己的哔哩哔哩直播房间号
        "area": 192 //直播分区ID
    },
    "deploy": {
        "type": 0, //路径类型，0 表示单个视频文件路径（或视频直链），1表示文件夹路径
        "video_path": "video.flv", //视频文件路径（支持相对路径和绝对路径以及视频直链）
        "live_time": 2100 //目标直播时长（单位：秒）
                          //0 表示播完当前视频后停止；-1 表示 24h 持续直播
    },
    "push": { //推送配置
        "telegram": {
            "enable": false, //是否启用
            "group_id": "",
            "bot_token": "",
            "proxy": "" //代理地址，支持 socks5 和 http 留空为禁用
        }
        --snip--
    }
}
```
- 安装并配置 `ffmpeg`
- 运行 `python3 main.py`

### 注意事项
- 程序运行过程中强制停止可能会导致 ffmpeg 未停止运行，请留意
- 若使用云服务器，请保证服务器位于中国大陆，否则会因为哔哩哔哩的限制导致无法开播
