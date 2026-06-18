import requests
import ddddocr
#验证码地址
url_verify_code = "http://localhost/index.php?m=Home&c=User&a=verify"
#发送get请求获取验证码图片+cookie
res_verify = requests.get(url_verify_code)
#提取响应里点cookie
cookie_all = res_verify.cookies
print("获取到的全部cookies：",cookie_all)
#单独把取出PHPSESSID,登录必须携带这个cookie，否则验证码不匹配
cookies = {"PHPSESSID":cookie_all['PHPSESSID']}

#识别动态变化图像验证码
ocr = ddddocr.DdddOcr()
code_text = ocr.classification(res_verify.content) #直接拿回接口返回点图片二进制识别
print("本次识别点动态验证码：",code_text)

##携带cookie+账号密码+识别出来的验证码，执行登录
url_login = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username":"13800138006",
    "password":"123456",
    "verify_code":code_text
}

#登录请求带上cookie，保持会话
res_login = requests.post(url = url_login,data = login_data, cookies=cookies)
print("登录返回：",res_login.json())

###登录成功后用同cookie查询我的订单
url_order = "http://localhost/Home/Order/order_list.html"
res_order = requests.get(url_order,cookies=cookies)
print("我的订单页面响应：",res_order.text)
