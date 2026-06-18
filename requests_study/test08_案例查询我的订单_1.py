'''
目标：登录TPshop查询我的订单
案例数据：
    获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
    登录接口：http://localhost/index.php?m=Home&c=User&a=do_login
    订单：http://localhost/Home/Order/order_list.html
    登录数据：
        data = ｛
            “username”:13800138006
            "password":123456
            "verify_code":2zjx
    ｝
'''

#1.导包
import requests

#请求验证码
url_verify_code = "http://localhost/index.php?m=Home&c=User&a=verify"
r_v = requests.get(url_verify_code)
#获取cookies

r_cookie = r_v.cookies
print("获取点cookie为：",r_cookie)

#设置cookies信息
cookies = {"PHPSESSID":r_cookie['PHPSESSID']}


#

#2.调用post
url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"
data = {
    "username":"13800138006",
    "password":"123456",
    "verify_code":"2zjx"
}
r = requests.post(url = url_login,data = data,cookies=cookies)
#3.验证是否登录成功
print(r.json())
#4.查询我的订单

url_order = "http://localhost/Home/Order/order_list.html"
res_order = requests.get(url_order,cookies=cookies)
print("我的订单页面响应：",res_order.text)
