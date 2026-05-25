import requests_demo
import time
from functools import wraps

def retry(max_retries=2,delay=1):
    '''
    papram max_retries:最大次数
    :param delay: 时间间隔
    :return:
    '''
    def decorator(func):# func 就是被包起来的汉堡（safe_request）
        @wraps(func)
        def wrapper(*args,**kwargs):#真正干活点替身
            for attempt in range(max_retries+1):
                try:
                    return func(*args,**kwargs)#执行真正的请求
                except requests.exceptions.RequestException as e:
                    print(f"第{attempt+1}次请求失败：{e}")
                    if attempt<max_retries:
                        time.sleep(delay)
                    else:
                        raise #3次都失败，彻底放弃，把错误抛出去
        return wrapper
    return decorator

@retry(max_retries=2,delay=2)
def safe_request(url):
    response = requests.get(url,timeout = 5)
    response.raise_for_status()
    return response.json()