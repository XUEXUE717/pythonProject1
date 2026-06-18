import requests
import ddddocr

session = requests.Session()
ocr = ddddocr.DdddOcr(show_ad=False)


#验证码地址
url_verify_code = "http://localhost/index.php?m=Home&c=User&a=verify"
#发送get请求获取验证码图片+cookie
res_verify = session.get(url_verify_code)

code_text = ocr.classification(res_verify.content).strip() #直接拿回接口返回点图片二进制识别
print("本次识别点动态验证码：",code_text)

##携带cookie+账号密码+识别出来的验证码，执行登录
url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username":"13800138006",
    "password":"123456",
    "verify_code":code_text
}

#登录请求带上cookie，保持会话
res_login = session.post(url = url_login,data = login_data)
print("登录返回：",res_login.json())

###登录成功后用同cookie查询我的订单
url_order = "http://localhost/Home/Order/order_list.html"
res_order = session.get(url_order)
print("我的订单页面响应：",res_order.text)
