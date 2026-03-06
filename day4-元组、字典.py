t = (1,2,3,4,5)
print(t[1])
print(type(t))

#判断是否为元组（三种写法）
t = (10,)
if type(t)==tuple:
    print("yes")
print(type(t)==tuple)
print(isinstance(t,tuple))

#交换元组值(是否还有其他方法？元组交换是反转吗)
t = (3,5)
t1 = t[::-1]
print(t1)

#统计2出现几次
t = (1,2,2,2,23,3,4,2)
x=0
for i in t:
    if i==2:
        x+=1
print("2在元组中出现次数：",x)

#元组列表互换
t = (1,2,3)
l = list(t)
l[1] = 99
t = tuple(l)
print("转化后的元组：",t)

#拆分元组
t = (10,20,30,40)
a,b,c,d=t
print(a,b,c,d)

#拆分2
t = (1,2,3,4,5)
t1 = t[0::2]
print(t1)

#找最大、最小、总和
t = (5,1,8,3,9)
s = 0
print(max(t))
print(min(t))
for i in t:
    s = s + i
print(s)

#判断是否在元组中
t = (1,2,3,4,5)
print(6 in t)

#连接俩元组
t1 = (1,2)
t2 = (3,4)
t3 = t1 + t2
print(t3)

#创建字典
dict1 = {'name':'小红','age':18,'city':'上海'}
print(dict1['age'])
dict1["city"] = "北京"
dict1["score"] = 90
del dict1['age']
print(dict1.keys())
#打印键值三种方法1️⃣keys() 2️⃣迭代 3️⃣ 转化为列表

for value in dict1:
    print(value)
    print(dict1[value])
for value in dict1:
    print(value + " :" + str(dict1[value]))
#安全获得“hright”，没有就返回0（安全获取：拿字典里的值，不存在也不会报错）
print(dict1.get('height',0))

#合并俩字典
d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}
d3 = d1 | d2
print(d3)

message = {"姓名":"小刚","性别":"女","成绩":(89,90,95)}
sum = 0
for i in message["成绩"]:
    print(i)
    sum+=i
message["总分"] = sum
print(message)

list1 = [["小花",18,90],["豆豆",17,88],["小楷",19,99]]
max = 0
for i in list1:
    if i[2] > max:
        max = i[2]
        name = i[0]
print(name,max)