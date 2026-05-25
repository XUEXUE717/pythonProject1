#put请求修改/覆盖已有资源
import requests
#1.请求地址
url = "https://postman-echo.com/delete"

#2.需要更新的完整资源数据
delete_data = {
    "dep_id":"TT702"
}
#3.发送put请求，json参数自动序列化+请求头
resp = requests.put(url = url,json = delete_data)

#4.打印调试信息
print("状态码：",resp.status_code)
print("原始响应文本：\n",resp.text)

#安全解析json，捕捉错误
try:
    resp_json = resp.json()
    print("\n解析后的JSON对象：\n",resp_json)
except Exception as e:
    print("解析失败：",e)