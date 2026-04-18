import requests
import time

URL = "https://api.tangdouz.com/a/60/?return="

while True:
    try:
        res = requests.get(URL, timeout=10)
        img_url = res.text.strip()
        
        # 直接打印图片链接，这就是你能看到的效果
        print("当前图片链接：", img_url)

    except Exception as e:
        print("获取失败", e)

    time.sleep(60)
