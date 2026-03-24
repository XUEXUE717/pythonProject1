students = [[1,'ANAN','F','4']]
taechers = [['doudou','4']]
Amessage = { "root":"root","doudou":"doudou"}
num_num = 1




#增加数据
def add(now_user):
    global  Amessage,students
    match now_user:
        case '1':#1表示管理员添加教师账号
            user =  input("输入账号：")
            password =  input("输入密码")
            mess = {user:password}
            Amessage = Amessage | mess
            print(Amessage)

        case '2': #添加学生信息
            while True:
                mess = input("请输入学生信息：学号，姓名，性别（男M女F），班级\n请用逗号分割\n退出请按'Q'").strip()
                if mess == 'Q':
                    menu(now_user)
                    break
                add_stu = mess.split(',')
                add_stu[0] = int(add_stu[0])
                students += [add_stu]
                print(f"添加后的学生信息：{students}")


#删除数据
def dele(now_user):
    global Amessage, students
    match now_user:
        case '1':#当前账号是管理员
            print("账号信息")
            i = 1
            for x in Amessage:
                print(f"{i,x}")
                i = i + 1
            dele_teca = input("请输入需要删除的账号").strip()
            Amessage.pop(dele_teca)
            print(Amessage)
            menu(now_user)
        case '2':
            print("学生信息[学号][姓名]")
            for stud in students:
                print(stud[0],stud[1])
            del_stu = int(input("请输入需要删除的学号").strip())
            for num in range(len(students)):
                if del_stu == students[num][0]:
                    students.remove(students[num])
            print('更新后的学生信息：',students)


#菜单栏
def menu(now_user):
    input_num = input("A.增加数据\nB.删除数据\nC，更新数据\nD.删除数据\nE.显示全部数据\nF.退出登陆")
    match input_num:
        case 'A':
            add(now_user)
        case 'B':
            dele(now_user)

while True :
    num = input("1，管理员  2.教师\n请选择账号登录：\n")
    if num != '1' and num != '2':
        raise ValueError("输入错误！")
    elif num == '1':
        user1 = input("请输入管理员账号")
        password1 = input("请输入管理员密码")
        is_all_in = all(key in Amessage and Amessage[key] == value for key,value in {user1:password1}.items())   #判断一个小字典的所有键值对，是否都存在与另一个大字典里
        if is_all_in:
            print("登陆成功！请选择功能")
            menu(num)
        else:
            raise ValueError("账号或者密码错误")
    else:
        user1 = input("请输入教师账号")
        password1 = input("请输入教师密码")
        is_all_in = all(key in Amessage and Amessage[key] == value for key, value in {user1: password1}.items())  # 判断一个小字典的所有键值对，是否都存在与另一个大字典里
        if is_all_in:
            print("登陆成功！请选择功能")
            menu(num)
        else:
            raise ValueError("账号或者密码错误")