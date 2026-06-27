'''任务：创建一个包含多个城市编码的列表，例如 ['110000', '310000', '440100'] (北京、上海、广州)。
使用一个循环，依次调用你的 get_weather 函数获取这些城市的天气，并调用 print_weather_report 打印出来。
产出：程序能一次性输出多个城市的天气报告。'''
'''
使用 try...except 捕获 requests 可能抛出的网络异常（如 ConnectionError, Timeout）。
检查 API 返回的 status 字段，如果不是 "1"，则抛出一个自定义异常或打印错误信息。
产出：即使网络不通或 API Key 错误，程序也不会崩溃，而是会给出友好的错误提示。
'''


#导包
import requests
import json
import csv
import os #用于检查文件是否存在
#获取信息

#获取请求，返回字典类型
def get_weather(city_code)->dict:
        url = " https://restapi.amap.com/v3/weather/weatherInfo"
        parmas = {'key': '94b307c675364698e95bdabc2bf45280',
                  'city': city_code}
        try:
            r = requests.get(url=url, params=parmas,timeout=5)
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

        except requests.exceptions.Timeout:
            print("请求超时，请检查网络或稍后重试。")
        except requests.exceptions.RequestException as e:
            print(f"网络请求错误，{e}")
        except(KeyError,json.JSONDecodeError):
            print("天气数据解析失败")
        return None #发生任何异常都返回None




def print_weather_report(weather_data): #输出天气信息
        print("请求成功！")
        print(f"【{weather_data["city"]}】天气实况")
        print("-"*20)
        print(f"天气：{weather_data["weather"]}")
        print(f"温度：{weather_data["temperature"]}")
        print(f"风力：{weather_data["winddirection"]}")
        print(f"风向：{weather_data["windpower"]}")
        #准备写入csv数据
        fieldnames = ['城市','天气','温度','风力','风向']
        ###检查文件是否已存在
        file_exists = os.path.exists("weather_report.csv")#
        with open("weather_report.csv","a",encoding='utf-8-sig',newline='',) as f:
            writer = csv.DictWriter(f,fieldnames = fieldnames)
            if not file_exists:
              #写入表头，文件不存在时
                writer.writeheader()
            #写入单行数据
            writer.writerow({'城市':weather_data["city"],
                             '天气':weather_data["weather"],
                             '温度':weather_data["temperature"],
                             '风力':weather_data["winddirection"],
                             '风向':weather_data["windpower"]})


weather_city = ['110000', '310000', '440100']
for city in weather_city:
    weather_data = get_weather(city)
    if weather_data is None:
        print(f"城市编码{city}请求错误，请检查'status'或者'lives'")
    else:
        print_weather_report(weather_data)
