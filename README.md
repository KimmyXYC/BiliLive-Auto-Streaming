# 哔哩哔哩自动直播
### 使用方法
- 安装 `Python3.7` 或更高的版本
- 安装依赖
```shell
pip install -r requirements.txt
```
- 执行 `python3 login.py` 扫码登录哔哩哔哩账号
    * 或从 `https://api.bilibili.com/x/web-interface/nav` 请求中获取 Cookies 填入
- 复制配置文件
```shell
cp Config/config.example.yaml Config/config.yaml
```
- 填写 `Config/config.yaml` 文件
- 安装并配置 `ffmpeg`
- 启动程序
```shell
python3 main.py
```

### 注意事项
- 程序运行过程中强制停止可能会导致 ffmpeg 未停止运行，请留意
- 若使用云服务器，请保证服务器位于中国大陆，否则会因为哔哩哔哩的限制导致无法开播
