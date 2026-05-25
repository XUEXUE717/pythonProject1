import time
import requests
from functools import wraps

# ==========================================
# 第一步：必须有这个“图纸”（定义装饰器）
# ==========================================
def retry(max_retries=2, delay=1):
    """重试装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    print(f"⚠️ 第 {attempt + 1} 次请求失败: {e}")
                    if attempt < max_retries:
                        print(f"⏳ {delay}秒后进行第 {attempt + 2} 次重试...")
                        time.sleep(delay)
                    else:
                        print("❌ 达到最大重试次数，请求彻底失败！")
                        raise
        return wrapper
    return decorator

# ==========================================
# 第二步：然后才能“使用”它（调用装饰器）
# ==========================================
@retry(max_retries=2, delay=2)
def safe_request(url):
    """一个普通的请求函数"""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

# ==========================================
# 第三步：运行测试
# ==========================================
if __name__ == "__main__":
    # 故意传一个错误的网址，看看重试效果
    result = safe_request("https://www.abc12345-not-exist.com")
    print(result)