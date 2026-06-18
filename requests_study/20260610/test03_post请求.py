'''
目标：requests库post方法使用
案例：新增学院
参数：
    1.json：传入json字符串
    2.headers传入请求信息头内容
响应：
    响应对象.json（）
'''

#1.导包
import requests
import json
#2.调用psot
#请求url
url = "Https://httpbin.org/post"
#请求headers
headers = {"Content-Type":"application/json"} #固定值

#请求json
#格式为后台固定格式
data = {
    "data":[
        {
            "dep_id":"T01",
            "dep_name":"Test学院",
            "master_name":"Test-Master",
            "slogan":"Here is Slogan"
        }
    ]
}
r = requests.post(url = url,json = data,headers = headers)
#3.获取响应对象

print(r.json())
#4.获取响应状态码
print(r.status_code)