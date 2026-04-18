import requests
import time

def main():
    try:
        r = requests.get("https://api.tangdouz.com/a/60/?return=")
        print("✅ 图片链接：", r.text.strip())
    except:
        print("❌ 失败")

if __name__ == "__main__":
    print("🚀 程序启动")
    while True:
        main()
        time.sleep(60)
