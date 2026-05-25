import requests
import json

import requests


def get_weather(city:str,api_key:str) ->dict|None:
    '''
    获取指定城市点当前天气信息
    :param city: 城市名称
    :param kry: API密钥
    :return: 包含天气信息的字典，失败返回None
    '''
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params = {"key":api_key,"city":city,"extensions":"base"}
    try:
        response = requests.get(url,params = params,timeout = 10)
        response.raise_for_status()#检查HTTP状态码
        data = response.json()

        #提取并组装结构化字典
        if data.get("status") =="1" and data.get("lives"):
            live_weather = data["lives"]
            return {
                "city":live_weather["city"],
                "temperature":live_weather["temperature"],
                "weather":live_weather["weather"]
            }
        return None
    except requests.exceptions.Timeout:
        print("请求超时，请检查网络或稍后重试。")
    except requests.exceptions.RequestException as e:
        print(f"网络请求发生错误：{e}")
    except(KeyError,json.JSONDecodeError):
        print("天气数据解析失败")
    return None


