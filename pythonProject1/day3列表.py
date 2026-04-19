#!/usr/bin/python3

list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]

# 读取第二位
print ("list[1]: ", list[1])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print ("list[1:-2]: ", list[1:-2])

print("列表元素个数：",len(list))
#列表的方法
list.append('append')
print(list)
print('taobao',list.count('taobao'))
list.extend(range(0,5))
print(list)

print(list.index(0))
list.insert(3,'index')
print(list)

list.reverse()
print(list)

#查看列表元素
lst = [10,20,30,40]
print(lst[0])
print(lst[-1])
print(lst[1:3])#切片

#删
lst.remove(30)
print(lst)
del lst[0]
print(lst)
lst.pop()
print(lst)


#练习1
names = ["小明","小红","小刚","小李"]
print(names[1])
names[2] = "小强"
print(names)

#练习2
names.append("小张")
names.insert(0,"小王")
print(names)

#练习3
scores = [90,85,77,92,68]
del scores[2]
scores.pop()
print(scores)

#练习4
fruits = ["苹果","香蕉","橙子","栗子"]
print(fruits[0])
fruits[1] = '葡萄'
fruits.append("西瓜")
del fruits[0]
print(fruits)

#综合切片
lst = [10,20,30,40,50,60,70]
print(lst[:3])
print(lst[2:5])
print(lst[-2:])
print(lst[::-1])

#遍历与统计
nums = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in nums:
    if(i%2==0):
        print(i)
    sum+=i
print(sum)

#查找与判断
names = ["Alice","Bob","Charlie","Bob","David"]
c = names.count("Bob")
print("Bob" in names)
if(c==0):
    print("不存在")
else:
    print("出现次数：",c)
print(names.index("Bob"))

#列表去重（不用集合）
lst = [2,3,2,5,4,7,2,3]
y=[]
for i in lst:
    if i not in y:
        y.append(i)
print(y)

#增删改综合
scores = [88,76,92,55,99]
for i in range(len(scores)):
    if(scores[i]<60):
        scores[i]=60
x = min(scores)
del scores[scores.index(x)]
x = max(scores)
scores.insert(scores.index(x)+1,100)
print(scores)

#嵌套列表操作
students = [["小明",85],["小红",92],["小刚",78]]
print(students[1][1])
students[2][1] = 80
for i in students:
    print(i)

#列表推导式  `[对每个元素做什么  for 元素 in 旧列表 if 条件]`
nums = [1,2,3,4,5,6,7,8,9,10]
"""for i in nums:
    if(i*i>5):
        print(i*i)"""
result = [i**2 for i in nums if i**2 >5]
print(result)

#筛选+修改
words = ["hello","world","python",""]
y = []
for i in words:
    if i != "":
        y.append(i)
print(y)

#排序与反转
lst = [5,2,9,1,5,6]
y = []
for i in range(len(lst)):
    x=min(lst)
    y.append(x)
    del lst[lst.index(x)]
print(y)
print(y[::-1])

#综合小项目——模拟购物车
cart = ["苹果","香蕉","橙子"]
cart.append("西瓜")
for i in cart:
    if i == "香蕉":
        del i
for i in cart:
    if i == "橙子":
        i="橘子"
print(len(cart))
print(cart)
