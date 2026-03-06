#原始数据
scores = [90,85,90,78,85,95,78,78]
#1.转换为集合去重
unique_scores_set = set(scores)
print("去重后的集合:",unique_scores_set)

#2.转换回列表
unique_scores_list = list(unique_scores_set)
print("转换回列表：",unique_scores_list)

#3.保存顺序的去重方法
ordered_unique = list(dict.fromkeys(scores))
print("保持原顺序去重后的集合:",ordered_unique)

'''复杂数据去重
    集合可以处理不可变的复杂类型，常用于清理数据库查询结果
'''
#原数据：学生打卡记录
attendance = [
    ("Alice","2026-03-01"),
    ("Bob","2026-03-01"),
    ("Alice","2026-03-01"),
    ("Charlie","2026-03-02")
]
#直接转换为集合去重
unique_set = set(attendance)
print("清洗后的打卡记录",unique_set)

"""
集合运算去重（交集、并集）
对比两组数据，找出共同项或合并项
"""
class_a = {"张三","李四","王五"}
class_b = {"王五","赵六","孙七"}

#1.去重，合并两个班级（基于哈希算法）
#等价于 class_a.union(class_b)
print("合并班级",class_a | class_b)

#交集-ab中均包含
#等价于class_a.intersection(class_b)
print("重复报名的学生：",class_a & class_b)

"""
基础题——清洗一个包含重复字符串的列表，并按结果字母排序sorted()
"""
words = ["apple","banana","apple","orange","banana","grape"]
unique_words_set = set(words)
ordered_unique_list = list(sorted(unique_words_set))
print("清洗后的字符串列表",ordered_unique_list)

"""
进阶题目——模拟用户注册的“查重”功能
"""
registered_users = ["user1001","user1002","user1003"]
new_signups = ["user1003","user1004","user1005","user1002"]

no_signups = set(registered_users) & set(new_signups)
yes_signups = set(new_signups) - set(registered_users)
print("重复注册：",no_signups)
print("注册成功：",yes_signups)


"""练习1
接口返回数据去重
给定一个接口返回的用户ID列表，保持第一次出现的顺序
用set/dict.fromkeys
"""
user_ids = [101,102,103,101,104,102,105]
unique_user_ids_set = sorted(set(user_ids))
unique_set = set(dict.fromkeys(user_ids))
print(unique_user_ids_set,"\n",unique_set)

'''
练习2
判断两个用例集的差异
有两组测试ID
1.有两组都有的用例（交集）
2.只在A，不在B
3.只在B，不在A
'''
case_a = {1,2,3,4,5}
case_b = {4,5,6,7,8}
one_case = case_a | case_b
tow_case = case_a - case_b
three_case = case_b - case_a
print("1:",one_case,"\n2:",tow_case,"\n3:",three_case)

"""练习3
统计日志中出现最多的接口
统计每个接口出现次数，并找出出现次数最多的接口
"""
api_log = [
    "/api/login","/api/user","/api/login",
    "/api/order","/api/user","/api/user","/api/login"
]
dict_api_log = {}

for i in api_log:
    if i in dict_api_log:
        dict_api_log[i]+=1
    else:
        dict_api_log[i] = 1
max_num = max(dict_api_log)
print(max_num,dict_api_log[max_num])

"""
练习4
从配置列表中过滤无效用例
给定测试用例列表，只保留“pass”“fail”
"""
cases = [
    {"id":"1","status":"pass"},
    {"id":"2","status":"skip"},
    {"id":"3","status":"fail"},
    {"id":"4","status":"pass"},
    {"id":"5","status":"skip"}
]
new_cases = []
for i in cases:
    if "skip" not in i["status"]:
        print(i["status"])
        new_cases.append(i)
print(new_cases)


"""
第五题
接口参数合法性检查
"""
def check_params(user):
    if ("username" not in user) or ("password" not in user):
        return False
    username = user["username"]
    password = user["password"]
    if len(username) >= 6 and len(password) >= 8:
        return True
    else:
        return  False
p1 = {"username":"zhangsan","password":"12345678"}
p2 = {"username":"lisi","password":"123456"}
p3 = {"username":"wangwu"}

print("p1",check_params(p1))
print("p2",check_params(p2))
print("p3",check_params(p3))