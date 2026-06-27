'''
题目一：用户信息管理系统
背景：你需要编写一个程序来管理用户信息。程序需要从JSON文件中读取现有数据，
允许用户通过命令行输入更新信息（涉及传参），并将更新后的数据写回文件。同时，必须处理可能发生的文件不存在或数据格式错误的异常。
要求：
函数传参：编写一个函数 update_user_info(user_id, **kwargs)，接收用户ID和任意数量的关键字参数（如 name="张三", age=25）来更新信息。
JSON处理：读取名为 users.json 的文件，更新对应ID的用户数据，并将结果写回该文件。
异常处理：处理文件不存在（FileNotFoundError）以及JSON解码错误（json.JSONDecodeError）的情况，并给出友好的提示。
文件读写：确保写入时使用UTF-8编码。
示例数据 (users.json)：
json
编辑
[
    {"id": 1, "name": "Alice", "age": 22},
    {"id": 2, "name": "Bob", "age": 30}
]
'''
###json文件为字典，先用r读取数据，用updata更新后，用w写入
import json
path = "users.json"
def updata_user_info(user_id,**kwargs):

    try:
        with open(path,'r',encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        data = []

    #更新数据

    user_found = False
    for user in data:
        if user.get("id") == user_id:
            user.update(kwargs)
            user_found = True
            break
    if not user_found:
        print(f"未找到ID为{user_id}的用户，正在新增...")
        new_user = {"id":user_id}
        new_user.update(kwargs)
        data.append(new_user)
    with open(path,'w',encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=4)

updata_user_info(1,name = '爱丽丝',age=23)
updata_user_info(2,age=31)
updata_user_info(3, name="Charlie", age=28)

""" 
    new_data = {"id":3,"name": "cling", "age": 21}
    data.append(new_data)
    print(data)
    with open(path,'w',encoding="utf-8") as f :
        json.dump(data,f,ensure_ascii=False,indent=4)
        ##data需要保存的内容，f表示需要存储的文件，ensure_ascii=false,中文字符原样输出，保证文件内容可读，indent缩进4
    #遍历列表，查找并指定ID的用户"""