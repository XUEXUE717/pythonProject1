'''
任务：编写一个 Python 脚本，使用 requests.get() 方法，传入你的 key 和一个城市编码（如北京的 110000），调用高德天气 API。
提示：API 的完整 URL 格式是 https://restapi.amap.com/v3/weather/weatherInfo?key=你的KEY&city=城市编码。
产出：打印出 API 返回的原始 JSON 字符串。
'''
#导包
import requests
#获取信息
url = " https://restapi.amap.com/v3/weather/weatherInfo"
parmas = {'key':'94b307c675364698e95bdabc2bf45280',
        'city':'重庆'}

r = requests.get(url=url,params=parmas)
print(r.json())