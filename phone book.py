book = {'h1uhu':"1234"}

def input_message():
    print("请输入姓名:")
    name = input()
    print("请输入电话（换行结束）：")
    phone = input()
    book[name] = phone
    print("保存成功")

def fine_name(name):
    for i in book:
        if i == name:
            print(book[i])
            break
    else:
        print("该电话不存在")
def all_in():
    for i in book:
        print("姓名：",i)
        print("电话:",book[i])

def del_name(name):
    if name in book:
        del book[name]
        print("删除成功")
    else:
        print("删除失败，该电话不存在")
def menu():
    print("菜单栏\n 添加A 查找F 显示全部B 删除D 退出E ")





#input_message()

#fine_name("huhu")

#all_in()
#del_name("na")


while True:
    menu()
    choice = input()
    match choice:
        case "A":
            input_message()
        case "F":
            print("请输入需要查找的电话姓名")
            name = input()
            fine_name(name)
        case "B":
            all_in()
        case "D":
            print("请输入需要删除的电话姓名")
            name = input()
            del_name(name)
        case "E":
            break