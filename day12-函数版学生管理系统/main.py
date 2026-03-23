students = [[1,'ANAN','F','4'],[]]
taechers = [[1,'doudou','4']]
Amessage = { "root":"root","doudou":"doudou"}
num_num = 1




#增加数据
def add(now_user):
    global  Amessage
    match now_user:
        case '1':#1表示管理员添加教师账号
            user =  input("输入账号：")
            password =  input("输入密码")
            mess = {user:password}
            Amessage = Amessage | mess
            print(Amessage)

#菜单栏
def menu(now_user):
    input_num = input("1.增加数据\n2.删除数据\n3，更新数据\n4.删除数据\n5.显示全部数据\n6.退出登陆")
    match input_num:
        case '1':
            add(now_user)


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
