#导包
import requests

#获取session对象

session = requests.Session()

#请求验证码，让session对象记录cookies信息
##session自动附加cookies信息，获取一次用户对话，从客户端与服务器建立连接开始，到关闭为一个会话
url_verify = "http://localhost/index.php?m=Home&c=User&a=verify"
session.get(url_verify) #无需变量存储 ##确保本地服务器数据库已开启！！
#请求登录
url_login ="http://localhost/index.php?m=Home&c=User&a=do_login"
data = {
    "username":"13800138006",
    "password":"123456",
    "verify_code":"7skf"#已做修改，本地测试跳过验证码
}
r = session.post(url = url_login,data = data)
print("登录返回信心：",r.json())

#查询我的订单信息
url_order =  "http://localhost/Home/Order/order_list.html"
r_order = session.get(url_order)
print("获取到的订单信息：",r_order.text)
