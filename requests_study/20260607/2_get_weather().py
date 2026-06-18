import requests
import json


def get_weather(city, api_key):
    url = "https://restapi.amap.com/v3/weather/weatherInfo"
    params = {
        "city": city,
        "key": api_key,
        "extensions": "base"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code != 200:
            print(f"❌ HTTP请求失败，状态码: {response.status_code}")
            return None

        data = response.json()
        if data.get("status") != "1":
            print(f"❌ 高德API业务错误: {data.get('info', '未知错误')}")
            return None

        # 👇 关键修正：安全获取列表，并取出列表中的第一个字典
        lives = data.get("lives", [])
        if not lives:
            print("❌ 未查询到该城市的天气信息")
            return None

        # 取出列表的第一个元素（它才是真正的字典）
        weather_info = lives[0]

        # 现在可以安全地使用 .get() 了
        return {
            "城市": weather_info.get("city"),
            "天气": weather_info.get("weather"),
            "温度": weather_info.get("temperature") + "℃",
            "风向": weather_info.get("winddirection") + "风",
            "风力": weather_info.get("windpower") + "级",
            "湿度": weather_info.get("humidity") + "%",
            "更新时间": weather_info.get("reporttime")
        }

    except requests.exceptions.Timeout:
        print("❌ 请求超时，请检查网络或稍后重试。")
    except requests.exceptions.RequestException as e:
        print(f"❌ 网络请求发生错误：{e}")
    except Exception as e:
        print(f"❌ 数据解析发生未知错误：{e}")

    return None

# --- 运行测试 ---
if __name__ == "__main__":
    # 替换为你自己的高德 Web服务 Key
    API_KEY = "94b307c675364698e95bdabc2bf45280"

    # 高德天气接口支持直接传中文城市名，也支持传城市编码（如 110000 代表北京）
    result = get_weather("沙坪坝", API_KEY)

    if result:
        print("✅ 天气查询成功！")
        print(json.dumps(result, ensure_ascii=False, indent=2))