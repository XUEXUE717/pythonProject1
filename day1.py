import string
'''def is_valid_identifier(name):
    try:
        exec(f"{name}=None")
        return True
    except:
        return False
print(is_valid_identifier("2var"))
print(is_valid_identifier("var2"))

"""等待用户输入"""
input("\n\n按下 enter 键退出")

'''
'''同一行显示多条语句

import sys; x = 'runoob';sys.stdout.write(x+ '\n')
'''
counter = 100
miles = 1000.0
name = "runoob"
print(counter)
print(miles)
print(name)
a = b = c =1
a, b, c = 1, 2, "runoob"
print(type(a))
print(type(b))
print(type(c))
print(type(counter))
print(type(miles))
print(type(name))

'''Tuple元组'''
tuple = ('abcd',675,2,23,'runoob',20.7)
tinytuple = (123,'runoob')
print(tuple)
print(tuple[0])
print(tuple[1:3])#第二个元素开始，连续三个
print(tuple[2:])
print(tinytuple * 2) #输出两次元组
print(tuple + tinytuple) #连接元组

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
print(dict['one'])

x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"
print("\a")