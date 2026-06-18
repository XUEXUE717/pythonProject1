'''
1.Get请求案例
请求：
    请求方法GET
响应：
    响应对象.url #获取请求url
    响应对象。status_code #获取响应状态码
    响应对象.text #以文本形式显示响应内容
'''
#导包
import requests
#调用get
url = "http://www.baidu.com"
reponse = requests.get(url)
#获取请求urL
print(f"请求地址{reponse.url}")
#获取响应码
print(f"响应状态码{reponse.status_code}")
#获取文本形式显示内容
print(f"{reponse.text}")