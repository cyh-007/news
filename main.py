import requests
from datetime import datetime, timedelta

# 获取 前一天 的日期
yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y年%m月%d日")

try:
    # 获取图片
    url = "https://api.tangdouz.com/a/60/?return="
    res = requests.get(url, timeout=10)
    img_url = res.text.strip()

    # 输出 前一天日报
    print("=====================================")
    print(f"📅 {yesterday} 日报")
    print("=====================================")
    print(f"🖼️ 图片链接：{img_url}")
    print("✅ 日报生成完成！")

except Exception as e:
    print("❌ 运行出错：", e)
