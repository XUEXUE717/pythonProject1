import csv

path = "scores.csv"
output_path = "averages.csv"

def calculate_averages(data_list) -> dict:
    """
    接收包含所有行数据的列表，返回一个字典，键为学生姓名，值为平均分。
    """
    student_scores = {}

    for row in data_list:
        try:
            name = row[0]
            score = float(row[2])  # 捕获非数字字符引发的 ValueError

            if name not in student_scores:##如果姓名不在成绩表student_score中
                student_scores[name] = []##创建该姓名对应的成绩列表
            student_scores[name].append(score)##吧这个成绩列表追加到这个姓名后面


        except (ValueError, IndexError) as e:
            print(f"⚠️ 数据转换错误：跳过无效行 {row}，原因: {e}")
            continue  # 遇到坏数据跳过，不影响整体计算

    # 计算每个学生的平均分
    averages = {}
    for name, scores in student_scores.items():
        averages[name] = sum(scores) / len(scores)

    return averages

def write_averages_to_csv(avg_data):
    """将平均分写入新的 CSV 文件"""
    # 题目明确要求输出格式为 name,average_score
    fieldnames = ['name', 'average_score']

    # 将字典转换为 DictWriter 需要的字典列表格式
    rows_to_write = []
    for name, avg_score in avg_data.items():
        rows_to_write.append({
            'name': name,
            'average_score': round(avg_score, 2)  # 保留两位小数
        })

    try:
        with open(output_path, "w", encoding="utf-8-sig", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows_to_write)
        print(f"✅ 结果已成功写入 {output_path}")
    except IOError as e:
        print(f"❌ 文件写入失败：{e}")

# ================= 主程序执行流程 =================

# 1. 读取 CSV 文件并捕获 IO 错误
data_list = []
try:
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # 跳过表头
        for row in reader:
            data_list.append(row)
except IOError as e:
    print(f"❌ 文件读取失败：{e}")
    exit()  # 如果读不到文件，直接退出

# 2. 计算平均分
if data_list:
    avg_data = calculate_averages(data_list)
    print("📊 计算结果：", avg_data)

    # 3. 写入新 CSV
    write_averages_to_csv(avg_data)
else:
    print("⚠️ 未读取到任何有效数据！")