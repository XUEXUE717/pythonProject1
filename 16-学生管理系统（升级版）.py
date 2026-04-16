#学生管理系统
#请选择功能：\nA.增加数据\nB.删除数据\nC，更新数据\nD.删除数据\nE.查找数据\nF.退出登陆
import csv


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



#第一次创建写入CSV文件
try:
    with open('student.csv','w',encoding='utf-8',newline='') as f:
        fieldname = ['id','name','class','age','grade']
        writer = csv.DictWriter(f,fieldnames=fieldname)
        writer.writeheader()#写入表头
        writer.