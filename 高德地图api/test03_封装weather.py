#导包
import requests
import json
#获取信息



'''任务：将获取天气的逻辑封装成一个函数，例如 get_weather(city_code)。
这个函数接收城市编码作为参数，并返回解析后的天气数据（一个字典）。
产出：一个可以被重复调用的 get_weather 函数。

提取核心天气信息
提取出 province (省份), city (城市), weather (天气现象，如“晴”), temperature (气温), winddirection (风向) 和 windpower (风力)
'''

def get_weather(city_code)->dict:
        url = " https://restapi.amap.com/v3/weather/weatherInfo"
        parmas = {'key': '94b307c675364698e95bdabc2bf45280',
                  'city': city_code}

        r = requests.get(url=url, params=parmas)
        status = r.json()["status"]
        info = r.json()["info"]
        if status == '1':
                return {
                        "province":r.json()["lives"][0]["province"],
                        "city": r.json()["lives"][0]["city"],
                        "weather": r.json()["lives"][0]["weather"],
                        "temperature": r.json()["lives"][0]["temperature"],
                        "winddirection": r.json()["lives"][0]["winddirection"],
                        "windpower": r.json()["lives"][0]["windpower"]
                }
        else:
                return {"请求失败,原因":info}




def print_weather_report(weather_data): #输出天气信息
        print(f"【{weather_data["city"]}】天气实况")
        print("-"*20)
        print(f"天气：{weather_data["weather"]}")
        print(f"温度：{weather_data["temperature"]}")
        print(f"风力：{weather_data["winddirection"]}")
        print(f"风向：{weather_data["windpower"]}")

weather_data = get_weather("500240")
if len(weather_data)!=1:
        print_weather_report(weather_data)
else:
        print(weather_data)
