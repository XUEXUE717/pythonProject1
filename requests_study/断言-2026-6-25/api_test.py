#1.状态码断言
#用于验证Http请求是否成功
import requests
import json

url = " https://restapi.amap.com/v3/weather/weatherInfo"
parmas = {'key': '94b307c675364698e95bdabc2bf45280',
              'city': '重庆'}
r = requests.get(url=url, params=parmas, timeout=5)
assert r.status_code == 200,f"Expected stasus code 200.but got{r.status_code}"


#响应数据（json）断言
#验证接口返回的具体业务数据是否符合预期，包含特定字段点值，字段是否存在
data = r.json()

print(data)
#断言特定字段的值,等号后面是正确内容，若发生错误，输出后面点提示
assert data['lives'] != '',f"expected name to be '',but got {data['lives']}"
#assert "token" in data ,"登录成功但未返回token"


##响应数据结构断言
data = r.json()
#判断某字段的数据类型是否为整数
assert isinstance(data['status'],str),f"当前字段点数据类型不为整数，格式为{type(data['status'])}"

##结合测试框架（unittest）进行断言
import unittest
class TeatAPI(unittest.TestCase):
    def test_status_code(self):

        response = requests.get(url,params=parmas)

        #检查预期是否与实际值相等
        self.assertEqual(response.status_code,200,f"Expected status code 200, but got {response.status_code}")
    def test_response_data(self):
        response = requests.get(url,params=parmas)
        data = response.json()
        self.assertIn("title",data)
##封装统一断言工具
def assert_response_contains(resp:requests.Response,key:str,value):
    '''断言响应体包含指定键值对'''
    assert key in resp.json(),f"响应体中不存在键{key}"
    assert  resp.json()[key]==value,f"键值错误，预期{value}，实际{resp.json()[key]}"
##调用封装好点断言方法
assert_response_contains(r,'info',0)