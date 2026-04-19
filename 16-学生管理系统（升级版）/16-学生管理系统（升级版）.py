#学生管理系统
#请选择功能：\nA.增加数据\nB.删除数据\nC，更新数据\nD.删除数据\nE.查找数据\nF.退出登陆
import csv
import os


class Prante():
    def __init__(self,user_id,name,class_id):
        self.name = name
        self.user_id = user_id
        self.class_id = class_id


class Student(Prante):
    def __init__(self,user_id,name,age,grade,class_id):
        super().__init__(user_id,name,class_id)
        self.age = age
        self.grade = grade


class Teachers(Prante):
    def __init__(self,user_id,name,class_id,):
        super().__init__(user_id,name,class_id)

new_row = {'id':'1002','name': "张三",'class':701, 'age': 22, 'grade': [99,88,77]}
new_row2 = {'id':'1001','name': "王五",'class':701, 'age': 12, 'grade': [69,78,87]}
'''你的数据中包含一个列表 grade。csv 模块会默认将其转换为字符串 "[99, 88, 77]" 写入。
这在 CSV 中是合法的，但当你再次读取时，它会是一个字符串，而不是列表。
如果需要以列表形式读回，后续需要自己用 eval() 或 json.loads() 等方法进行转换。
'''
#创建写入CSV文件（判断文件是否存在，若存在则录入内容，不存在新建一个）
file_path = 'student.csv'
fieldname = ['id', 'name', 'class', 'age', 'grade']

if not os.path.exists(file_path):#判断路径是否存在（文件或者目录）
    '''方法二：专门判断是否为常规文件 #if os.path.isfile(file_path):'''
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()  # 写入表头
        writer.writerow(new_row)#写入第一行数据
    print(f"文件{file_path}已创建，并写入首行数据。")
else:
    # 文件存在，则在后面追加内容
    with open(file_path, 'a', encoding='utf-8', newline='') as f:
        #使用DictWriter，并传入相同的fieldnames
        writer = csv.DictWriter(f, fieldnames=fieldname)
        # 追加数据
        writer.writerow(new_row2)
    print("数据已成功追到 student.csv")