'''封装自动刷新（推荐掌握）
创建AuthClient类，实现：
自动登录获取Token。
请求时自动注入Token。
检测401错误时自动刷新Token（关键！）'''

#后续将其改为手动注入，自动注入有问题

import requests_demo
class AuthClient:
    #初始化（构造函数）
    def __init__(self,base_url,username,password):
        self.session = requests.Session()
        self.base_url = base_url
        self.username = username
        self.password = password
        self.token = None
    def login(self):
        '''登录并更新Token'''
        resp = self.session.post(f"{self.base_url}/login",json={"username":self.username,"password":self.password})
        self.token = resp.json()["token"]
        self.session.headers["Authorization"] = f"Bearer {self.token}"

    def request(self,method,endpoint,**kwargs):
        '''自动处理Token过期点请求方法'''
        if not self.token:
            self.login()
        response = self.session.request(method,f"{self.base_url}{endpoint}",**kwargs)
        #检测tokne过期的请求方法401错误
        if response.status_code == 401:
            self.login()#重新登录
            response = self.session.request(method,f"{self.base_url}{endpoint}",**kwargs)
        return response

client = AuthClient("https://reqres.in/api/login", "test", "123456")
profile = client.request("GET", "/profile")  # 自动处理登录和Token过期