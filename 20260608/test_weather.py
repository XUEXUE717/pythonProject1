import requests

def get_weather():
    """获取重庆天气的普通函数"""
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params = {"key": "94b307c675364698e95bdabc2bf45280", "city": "渝北区", "extensions": "base"}
    response = requests.get(url, params=params)
    return response.json()

# Pytest 测试用例：函数名必须以 test_ 开头
def test_weather_success():
    result = get_weather()
    # 断言：验证返回的状态码是否为 1（高德接口成功返回1）
    print("接口返回的完整数据是：", result)  # 加上这一行，看看真实返回
    assert result["status"] == "1"
    assert result["lives"][0]["city"] == "重庆" # 验证城市名