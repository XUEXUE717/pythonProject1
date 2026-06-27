'''
使用 try...except 捕获 requests 可能抛出的网络异常（如 ConnectionError, Timeout）。
检查 API 返回的 status 字段，如果不是 "1"，则抛出一个自定义异常或打印错误信息。
产出：即使网络不通或 API Key 错误，程序也不会崩溃，而是会给出友好的错误提示。
'''


#导包
import requests
import json
#获取信息

#获取请求，返回字典类型
def get_weather(city_code)->dict:
        url = " https://restapi.amap.com/v3/weather/weatherInfo"
        parmas = {'key': '94b307c675364698e95bdabc2bf45280',
                  'city': city_code}
        try:
            r = requests.get(url=url, params=parmas,timeout=5)
        except requests.exceptions.Timeout:
            print("请求超时，请检查网络或稍后重试。")
        except requests.exceptions.RequestException as e:
            print(f"网络请求错误，{e}")
        except(KeyError,json.JSONDecodeError):
            print("天气数据解析失败")
        data = r.json()
        if data.get("status") == '1' and data.get("lives"):
            return {
                "province": data["lives"][0]["province"],
                "city": data["lives"][0]["city"],
                "weather": data["lives"][0]["weather"],
                "temperature": data["lives"][0]["temperature"],
                "winddirection": data["lives"][0]["winddirection"],
                "windpower": data["lives"][0]["windpower"]}
        return None



def print_weather_report(weather_data): #输出天气信息
        print("请求成功！")
        print(f"【{weather_data["city"]}】天气实况")
        print("-"*20)
        print(f"天气：{weather_data["weather"]}")
        print(f"温度：{weather_data["temperature"]}")
        print(f"风力：{weather_data["winddirection"]}")
        print(f"风向：{weather_data["windpower"]}")

weather_data = get_weather("500240")
if weather_data is None:
    print("请求错误，请检查'status'或者'lives'")
else:
    print_weather_report(weather_data)

