import requests_demo
import json

def get_location(address, api_key):
    """
    高德地理编码：地址转经纬度
    """
    url = "https://restapi.amap.com/v3/geocode/geo"
    params = {
        "address": address,
        "key": api_key
    }

    try:
        # 1. 发送请求
        response = requests.get(url, params=params, timeout=10)

        # 2. 检查HTTP状态码 (双重校验第一步)
        if response.status_code != 200:
            print(f" HTTP请求失败，状态码: {response.status_code}")
            return None

        data = response.json()

        # 3. 检查高德业务状态码 (双重校验第二步)
        if data.get("status") != "1":
            print(f" 高德API业务错误: {data.get('info', '未知错误')}")
            return None

        # 4. 安全提取数据 (使用 .get() 防止KeyError)
        # 注意：地理编码的结果在 'geocodes' 列表里，不是 'lives'
        geocodes = data.get("geocodes", [])
        if not geocodes:
            print(" 未查询到该地址的地理信息")
            return None

        # 取第一个匹配结果
        first_result = geocodes[0]

        return {
            "地址": address,
            "经纬度": first_result.get("location"),  # 格式是 "经度,纬度"
            "城市": first_result.get("city"),
            "行政区划编码": first_result.get("adcode")
        }

    except requests.exceptions.Timeout:
        print(" 请求超时，请检查网络或稍后重试。")
    except requests.exceptions.RequestException as e:
        print(f" 网络请求发生错误：{e}")
    except Exception as e:
        print(f" 数据解析发生未知错误：{e}")

    return None

# --- 测试代码 ---
if __name__ == "__main__":
    # 请替换为你的实际Key
    API_KEY = "94b307c675364698e95bdabc2bf45280"

    result = get_location("重庆市渝北区", API_KEY)
    if result:
        print(" 查询成功！")
        print(json.dumps(result, ensure_ascii=False, indent=2))