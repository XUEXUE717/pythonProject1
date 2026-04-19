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
            menu(now_user)

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
            del_stu = int(input("请输入需要删除的学号").strip())#根据学号删除，可以设置选项根据姓名，班级，删除
            for num in range(len(students)):
                if del_stu == students[num][0]:
                    students.remove(students[num])
            print('更新后的学生信息：',students)
            menu(now_user)
#更新修改数据
def up_data(now_user):
    global Amessage,students
    match now_user:
        case '1':
            print("账号信息：\n")  # 输出账号信息可以归纳与一个查询函数
            for key in Amessage:
                print(key)
            upuser = input("请输入需要修改密码的账号:\n").strip()  # 输入需要修改的账号（具有唯一性），根据账号修改密码
            while True:
                if upuser in Amessage.keys():
                    up_pw1= input("请输入更改的密码:\n")
                    up_pw2 = input("请再次输入密码：\n")
                    if up_pw1 != up_pw2:
                        print("两次密码不一致重新输入！")
                        continue
                    else:
                        Amessage[upuser] = up_pw1
                        print(f"修改成功{Amessage}")
                        menu(now_user)
                else:
                    print("输入错误！请重新输入\n")

        case '2':
            while True:
                upuser = int(input("请输入需要修改信息的学号:\n").strip())  # 输入需要修改的学号（具有唯一性），根据学号修改信息
                i_num = -1
                for x in range(len(students)):
                    if students[i_num][0] == int(upuser):
                        i_num = x
                        break
                if i_num == -1:
                    print("输入错误 重新输入！\n")
                    continue
                print("需要修改数据的学号相关信息：\n",students[i_num])
                change = input("请选择的需要修改的字段：A姓名，B性别,C班级,D返回菜单栏")#一次性多次修改——后续改进
                match change:
                    case 'A':
                        updata = input("请输入修改的新姓名：\n").strip()#后续还需要添加检测是否输入正确
                        students[i_num][1] = updata
                        print(f"更新后的学生信息为：{students[i_num]}")
                        menu(now_user)
                    case 'B':
                        updata = input("请输入修改的新内容（性别：F女 M男）：\n").strip()
                        students[i_num][2] = updata
                        print(f"更新后的学生信息为：{students[i_num]}")
                        menu(now_user)
                    case 'C':
                        updata = input("请输入班级：\n").strip()
                        students[i_num][3] = updata
                        print(f"更新后的学生信息为：{students[i_num]}")
                        menu(now_user)
                    case 'D':
                        menu(now_user)
#显示查询数据
def find_data(now_user):
    match now_user:
        case '1':
            while True:
                user = input("请输入需要查询密码的账号")
                if user in Amessage:
                    print(f"密码：{Amessage[user]}")
                    menu(now_user)
                else:
                    print("账号不存在，重新输入\n")
        case '2':
            while True:
                f_data = input("请选择查询方式:A学号 B姓名 C性别 D班级 E返回到菜单").strip()
                match f_data:
                    case 'A':
                        user = int(input("请输入需要查询的学号").strip())
                        estimate = -1
                        for x in students:
                            if x[0] == user:
                                print(x)
                                estimate = 0
                        if estimate == -1:
                            print("学号不存在，请重新输入")
                    case 'B':
                        user = input("请输入需要查询的姓名").strip()
                        estimate = -1
                        for x in students:
                            if x[1] == user:
                                print(x)
                                estimate = 0
                        if estimate == -1:
                            print("姓名不存在，请重新输入")
                    case 'C':
                        user = input("请输入需要查询的性别F M").strip()
                        estimate = -1
                        for x in students:
                            if x[2] == user:
                                print(x)
                                estimate = 0
                        if estimate == -1:
                            print("输入错误，请重新输入")
                    case 'D':
                        user = input("请输入需要查询的班级信息").strip()
                        estimate = -1
                        for x in students:
                            if x[3] == user:
                                print(x)
                                estimate = 0
                        if estimate == -1:
                            print("班级不存在，请重新输入")
                    case 'E':
                        menu(now_user)

#退出登陆
def quit_data():
    sign()


#菜单栏
def menu(now_user):
    input_num = input("请选择功能：\nA.增加数据\nB.删除数据\nC，更新数据\nD.删除数据\nE.查找数据\nF.退出登陆")
    match input_num:
        case 'A':
            add(now_user)
        case 'B':
            dele(now_user)
        case 'C':
            up_data(now_user)
        case 'D':
            dele(now_user)
        case 'E':
            find_data(now_user)
        case 'F':
            quit_data()

def sign():#登陆
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

sign()