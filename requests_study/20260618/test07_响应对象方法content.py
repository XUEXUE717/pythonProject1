import requests
#百度logo
img_url = "https://www.baidu.com/img/flexible/logo/pc/result.png"


r = requests.get(img_url)

#文本显示乱码
#print(r.text)

#二进制显示
#print(r.content)
with open("baidu.png", "wb") as f:
    f.write(r.content)