import requests_demo

session = requests.Session()
session.headers.update({"x-api-key": "94b307c675364698e95bdabc2bf45280"})
amap_key = "你申请的高德Web服务Key"
url = f"https://restapi.amap.com/v3/geocode/geo?address=北京市朝阳区&key={amap_key}"
login_url = "https://reqres.in/api/login"
login_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

try:
    # 1. 发送登录请求
    login_resp = session.post(login_url, json=login_data)

    # 2. 第一重校验：检查 HTTP 状态码是否为 200
    assert login_resp.status_code == 200,f"状态码错误：{login_resp.text}"

    resp_json = login_resp.json()
    assert "token" in resp_json,f"缺少Token字段:{resp_json}"

    token = resp_json["token"]
    assert token is not None,"Token值为空"


    if not token:
        print("❌ 登录失败！虽然状态码是200，但响应体中未找到 Token 字段。")
        print(f"实际返回内容: {login_resp.json()}")
    else:
        print("✅ 登录成功！双重校验通过。")
        print(f"获取到的 Token: {token}")

        # 校验通过后，才将 Token 注入到 Session 中
        session.headers.update({"Authorization": f"Bearer {token}"})

except requests.exceptions.JSONDecodeError:
    # 4. 防御性编程：防止服务器返回的不是 JSON 格式（比如返回了 HTML 报错页面）
    print("❌ 解析失败！服务器返回的不是有效的 JSON 数据。")
    print(f"原始响应内容: {login_resp.text}")

except requests.exceptions.RequestException as e:
    # 5. 网络异常处理：防止断网或服务器宕机导致脚本崩溃
    print(f"❌ 网络请求异常: {e}")