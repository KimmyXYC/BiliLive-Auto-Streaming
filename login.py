# -*- coding: utf-8 -*-
# @Time: 2023/2/10 19:58
# @FileName: login.py
# @Software: PyCharm
# @GitHub: KimmyXYC
import requests
import time
import qrcode
import io
from Utils.Parameter import process_cookies
from Utils.Json import save_config
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"


def get_qrcode():
    url = "https://passport.bilibili.com/x/passport-login/web/qrcode/generate"
    headers = {'User-Agent': USER_AGENT}
    response = requests.get(url, headers=headers)
    return response.json()["data"]


def qr_login(qrcode_key):
    url = "https://passport.bilibili.com/x/passport-login/web/qrcode/poll"
    headers = {'User-Agent': USER_AGENT}
    params = {'qrcode_key': qrcode_key}
    response = requests.get(url, headers=headers, params=params)
    return response


def login():
    data = get_qrcode()
    qrcode_url = data["url"]
    qrcode_key = data["qrcode_key"]

    print("请扫描二维码或将下面的链接复制到哔哩哔哩内打开")
    print(qrcode_url)
    qr = qrcode.QRCode()
    qr.add_data(qrcode_url)
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())

    cookies = ""
    while cookies == "":
        try:
            login_requests = qr_login(qrcode_key)
            login_data = login_requests.json()
        except Exception as e:
            print(e)
        code = login_data["data"]["code"]
        message = login_data["data"]["message"]
        print(f"Code:{code} Status:{message}")
        if login_data["data"]["code"] == 0:
            cookies = login_requests.cookies.get_dict()
            break
        time.sleep(1.5)

    print(f"Cookies: {cookies}")
    save_config(process_cookies(cookies), "cookies")
    print("Cookies储存完成")


if __name__ == '__main__':
    login()
