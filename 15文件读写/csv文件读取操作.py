'''读取 CSV 文件
方式一：按列表读取 (csv.reader)
适合：不需要关心列名，直接按顺序取数据。'''
import csv
with open('data.csv','r',encoding = 'utf-8') as f:
    #创建读取对象
    reader = csv.reader(f)
    #如果第一行是表头，单独先读取
    header = next(reader)
    print("表头：",header)
#遍历剩余行
for row in reader:
    #row是一个列表['',''...]
    print(f"姓名：{row},年龄：{row}")

#方式二：字典读取（csv.DictReader）
#适合数据比较多，或者需要明确知道哪一列是哪个数据
with open("data.csv",'r',encodeing='utf-8') as f:
    #自动把第一行当做键值
    reader = csv.DictReader(f)
    for row in reader:
        #row 是一个字典，
        print(f"姓名：{row['姓名']},年龄：{row['年龄']}")


''' 写入 CSV 文件
⚠️ 重要提示： 写入 CSV 时，open 函数必须加 newline=''，否则在 Windows 下每行数据之间会多出一个空行。
方式一：按列表写入 (csv.writer)
适合：手头数据本身就是列表或元组。'''
data = [
    ['姓名', '年龄'],  # 表头
    ['张三', 18],
    ['李四', 20]
]
#注意newline = ‘’
with open('output.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    # 写入多行
    writer.writerows(data)

"""方式二：按字典写入 (csv.DictWriter) —— 推荐
适合：手头数据是字典，或者需要严格对应列名。"""

#定义表头
fieldnames = ['姓名','年龄','城市']
with open('output_dict.csv','w',encoding='utf-8',newline='') as f:
    #创建写入对象，必须传入fielnames
    writer = csv.DictWriter(f,fieldnames = fieldnames)
    #1.写入表头
    writer.writeheader()

    #写入单行数据
    writer.writerow({'姓名':"王五", '年龄': 22, '城市': '北京'})

    # 3. 写入多行数据
    writer.writerows([
        {'姓名': '赵六', '年龄': 25, '城市': '上海'},
        {'姓名': '孙七', '年龄': 30, '城市': '广州'}
    ])