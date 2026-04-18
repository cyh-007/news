import requests
import time
import os

# 确保运行目录可写
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 你的接口
url = "https://api.tangdouz.com/a/60/?return="

def download_image():
    try:
        # 1. 请求接口获取图片地址
        resp = requests.get(url, timeout=10)
        resp.encoding = "utf-8"
        img_url = resp.text.strip()

        print("✅ 获取图片地址成功：")
        print(img_url)

        # 2. 下载图片
        print("\n⬇️ 正在下载图片...")
        img_resp = requests.get(img_url, timeout=10)
        
        # 保存
        with open("tangdou_image.png", "wb") as f:
            f.write(img_resp.content)

        print("✅ 图片下载完成！文件名：tangdou_image.png\n")
        
    except Exception as e:
        print("❌ 出错：", e)

# 云端持续运行
if __name__ == "__main__":
    print("🚀 云端程序已启动，自动循环下载图片")
    while True:
        download_image()
        time.sleep(60)  # 60秒下载一次，可修改