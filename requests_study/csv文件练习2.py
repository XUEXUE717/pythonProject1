'''题目二：学生成绩统计与CSV处理
背景：学校提供了一个CSV文件，记录了学生的姓名、科目和成绩。你需要编写脚本来读取这个文件，
计算每个学生的平均分（涉及列表/字典传参处理），并将结果输出到新的CSV文件中。
要求：
文件读写：读取 scores.csv，该文件包含表头 name,subject,score。
数据处理与传参：编写一个函数 calculate_averages(data_list)，接收包含所有行数据的列表，返回一个字典，键为学生姓名，值为平均分。
异常处理：
捕获文件读取时的IO错误。
捕获数据转换时的类型错误（例如成绩栏输入了非数字字符 ValueError）。
结果输出：将计算出的平均分写入 averages.csv，格式为 name,average_score。
示例数据 (scores.csv)：
name,subject,score
张三,Math,85
张三,English,90
李四,Math,78
李四,Science,88'''
import csv
path = "scores.csv"
data_list = []
def calculate_averages(data_list)->dict:#接收包含所有行数据的列表，返回一个字典，键为学生姓名，值为平均分。
    student_scores = {}
    for data in data_list:
        try:
            name = data[0]
            score = float(data[2])
            if name not in student_scores:
                student_scores[name]=[]
            student_scores[name].append(score)

        except(ValueError,IndexError) as e:
            print(f"数据转换错误：跳过无效行{data},原因{e}")
            continue #遇到坏数据跳过，不影响整体计算
    averages = {}
    for name,scores in student_scores.items():
        averages[name] = sum(scores)/len(scores)

    return averages

def write_averages_to_csv(avg_data, output_path="averages.csv"):
    fieldnames=['name','average_score']
    #将字典转换为Dictwriter需要的字典列表格式
    rows_to_write = []
    for name,avg_score in avg_data.items():
        rows_to_write.append({
            "name":name,
            "average_score":round(avg_score,2)
        })
    try:
        with open(output_path,"w",encoding="utf-8-sig",newline='') as f:
            writer = csv.DictWriter(f,fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(rows_to_write)
        print(f"已成功写入{output_path}")
    except IOError as e:
        print(f"文件写入失败：{e}")

try:
    with open(path,"r",encoding='utf-8') as f:
        """ reader = csv.DictReader(f)  # #字典读取，自动把第一行当做键值
        for row in reader:
            print(row)"""
        reader = csv.reader(f) #列表读取，第一行表头读取出来
        header = next(reader)#第一行
        for row in reader:
            data_list.append(row)
except IOError as e:
    print(f"文件读取失败{e}")
    exit()
if data_list:
    avg_data = calculate_averages(data_list)
    print("计算结果：",avg_data)
    write_averages_to_csv(avg_data)
else:
    print("未读取到任何有效数据！")