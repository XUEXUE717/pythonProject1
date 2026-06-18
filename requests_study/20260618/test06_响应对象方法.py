'''目标:响应对象常用的方法
1.encoding
    获取请求编码
    设置响应编码
2.headers
    获取响应信息头像
案例：http://www.baidu.com
'''
#1.导包
import requests

#调用get方法
url = "http://www.baidu.com"
r = requests.get(url)

#查看默认请求编码 ISO-8859-1
print(r.encoding)

#设置响应代码
r.encoding = "utf-8"

#查看响应内容 text形式
print(r.text)