'''
任务：编写一个 Python 脚本，使用 requests.get() 方法，传入你的 key 和一个城市编码（如北京的 110000），调用高德天气 API。
提示：API 的完整 URL 格式是 https://restapi.amap.com/v3/weather/weatherInfo?key=你的KEY&city=城市编码。
产出：打印出 API 返回的原始 JSON 字符串。
'''
#导包
import requests
import json
#获取信息
url = " https://restapi.amap.com/v3/weather/weatherInfo"
parmas = {'key':'94b307c675364698e95bdabc2bf45280',
        'city':'500240'}

r = requests.get(url=url,params=parmas)
print(r.json())

'''任务：使用 response.json() 方法将上一步返回的字符串解析为 Python 字典。
然后，尝试从中提取并打印出 status（状态码）和 info（返回状态说明）字段。
提示：status 为 "1" 代表请求成功。
产出：在控制台清晰地打印出“请求状态：成功”或“请求状态：失败，原因：...”。'''
status = r.json()["status"]
info = r.json()["info"]
if status=='1':
        print("请求成功！")
else:
        print(f"请求失败,原因{info}")