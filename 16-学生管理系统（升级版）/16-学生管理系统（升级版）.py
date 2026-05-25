#学生管理系统
#请选择功能：\nA.增加数据\nB.删除数据\nC，更新数据\nD.删除数据\nE.查找数据\nF.退出登陆
import csv
import os

file_path = 'student.csv'


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
    def add_student(self):#追加学生信息
        new_row = {'id': self.user_id, 'name': self.name, 'class': self.class_id, 'age': self.age, 'grade': self.grade}
        '''你的数据中包含一个列表 grade。csv 模块会默认将其转换为字符串 "[99, 88, 77]" 写入。
        这在 CSV 中是合法的，但当你再次读取时，它会是一个字符串，而不是列表。
        如果需要以列表形式读回，后续需要自己用 eval() 或 json.loads() 等方法进行转换。
        '''
        # 创建写入CSV文件（判断文件是否存在，若存在则录入内容，不存在新建一个）

        fieldname = ['id', 'name', 'class', 'age', 'grade']
        if not os.path.exists(file_path):  # 判断路径是否存在（文件或者目录）
            '''方法二：专门判断是否为常规文件 #if os.path.isfile(file_path):'''
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldname)
                writer.writeheader()  # 写入表头
                writer.writerow(new_row)  # 写入第一行数据
            print(f"文件{file_path}已创建，并写入首行数据。")
        else:
            # 文件存在，则在后面追加内容
            with open(file_path, 'a', encoding='utf-8', newline='') as f:
                # 使用DictWriter，并传入相同的fieldnames
                writer = csv.DictWriter(f, fieldnames=fieldname)
                # 追加数据
                writer.writerow(new_row)
            print("数据已成功追到 student.csv")

    def find_student(self):
        #查找功能
        '''查找学生：通过学号或姓名搜索特定学生。
显示所有：列出系统中所有学生的信息。
筛选：例如“显示所有 701 班的学生”或“显示所有年龄大于 18 岁的学生”。'''
        mess = input('请选择查找方式 X学号\n N姓名\n B班级\n  S筛选\n A显示全部 \n E返回上一级')
        if mess in ['X','x','n','N','B','b','S','s','A','a','E','e']:
            match mess:
                case 'X','x': #学号查找
                    find_id = input("请输入需要查找的【学号】：\n")
                    # 适合数据比较多，或者需要明确知道哪一列是哪个数据
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # 自动把第一行当做键值
                        reader = csv.DictReader(f)
                        for row in reader:
                            if find_id in row['id']:
                                print(f'查找到学号{find_id}的信息\n{row}')

                case 'n','N': # 姓名查找
                    find_name = input("请输入需要查找的【姓名】：\n")
                    # 适合数据比较多，或者需要明确知道哪一列是哪个数据
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # 自动把第一行当做键值
                        reader = csv.DictReader(f)
                        for row in reader:
                            if find_name in row['name']:
                                print(f'查找到姓名{find_name}的信息\n{row}')

                case 'B','b': # 班级查找
                    find_class = input("请输入需要查找的【姓名】：\n")
                    # 适合数据比较多，或者需要明确知道哪一列是哪个数据
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # 自动把第一行当做键值
                        reader = csv.DictReader(f)
                        for row in reader:
                            if find_class in row['class']:
                                print(f'查找到姓名{find_class}的信息\n{row}')

                case 'S','s': # 条件筛选：年龄
                    try:
                        reg1 = int(input('请输入需要查找的年龄范围下限(数值)：\n').strip())
                        reg2 = int(input('请输入需要查找的年龄范围上限（数值）：\n').strip())
                        if reg1 >reg2:#保证上下限没输错
                            ch = reg1
                            reg1 = reg2
                            reg2 = ch
                        if reg1 == reg2:#上下限相同即为恒等于
                            with open(file_path, 'r', encoding='utf-8') as f:
                                reader = csv.DictReader(f)
                                for row in reader:
                                    if row['age'] == reg1 :
                                        print(row)

                        with open(file_path,'r',encoding='utf-8') as f:
                            reader = csv.DictReader(f)
                            for row in reader:
                                if row['age'] >= reg1 and row['age'] <= reg2 :
                                    print(row)
                    except:
                        print("输入错误，请重新输入！")

                case 'A','a':  # 显示全部学生信息
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # 自动把第一行当做键值
                        reader = csv.DictReader(f)
                        for row in reader:
                            print(f'所有学生信息：\n {row}')

                case 'E','e':  # 返回上一级
                    return
    def change(self):
        #信息更新：学生转班、修改年龄或联系方式时，更新对应数据。
        """修改学生信息"""
        student_id = input("请输入要修改的学号: ").strip()

        for stu in self.students:
            if stu.student_id == student_id:
                try:
                    print(f"当前信息: {stu}")
                    stu.name = input("请输入新姓名: ").strip()
                    stu.age = int(input("请输入新年龄: "))
                    stu.score = float(input("请输入新成绩: "))
                    print("修改成功！")
                except ValueError:
                    print("输入错误：年龄和成绩必须是数字！")
                return
        print("未找到该学号的学生。")

    def del_student(self):
        #删除学生：学生毕业或退学后，将其信息从系统中移除。
        pass

class Teachers(Prante):
    def __init__(self,user_id,name,class_id,):
        super().__init__(user_id,name,class_id)

