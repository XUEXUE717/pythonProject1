'''
目标：requests库post方法 参数（data和json区别）
案例：新增学院
将字典对象转换为json字符串
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
#使用json方式新增学院成功
#r = requests.post(url,json = data,headers = headers)

#使用data方式新增学院，（这里成功，视频博主失败，可能是我这个url）
#python字典和json虽然长得一样，但是数据序列格式化还是有一定的区别
#r = requests.post(url,data = data,headers = headers)
r = requests.post(url,data = json.dumps(data),headers = headers)
#3.获取响应对象

print(r.json())
#4.获取响应状态码
print(r.status_code)