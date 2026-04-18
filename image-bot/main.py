import requests
import time

# 你的图片接口
URL = "https://api.tangdouz.com/a/60/?return="

def get_and_save():
    try:
        # 获取图片链接
        res = requests.get(URL, timeout=8)
        img_url = res.text.strip()
        
        if not img_url.startswith("http"):
            print("❌ 没有获取到有效图片")
            return

        # 下载图片
        img = requests.get(img_url, timeout=8)
        with open("tangdou_image.png", "wb") as f:
            f.write(img.content)
            
        print("✅ 成功：" + img_url)

    except Exception as e:
        print("⚠️ 异常，继续运行：", str(e))

# 主程序
if __name__ == "__main__":
    print("🚀 服务已启动")
    while True:
        get_and_save()
        time.sleep(60)
