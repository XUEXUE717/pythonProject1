'''读取：使用 with open 和 json.load 读取 raw_users.json。
清洗与验证（核心逻辑）：
检查邮箱：邮箱必须包含 @ 符号。
检查时间：reg_time 不能是 None。
数据转换：使用 time.strftime 将时间戳（如 1678888888）转换为字符串（如 '2023-03-15'）。
异常处理：如果在读取文件或转换时间时出错，程序不能崩溃，要打印错误信息。
写入：将清洗后的有效数据写入 valid_users.csv。
CSV 格式应为：ID,姓名,邮箱,注册日期
统计：最后打印：“共处理 X 条数据，成功清洗 Y 条，丢弃 Z 条”。'''
import json
import csv
import time


def process_user_data():
    valid_users = []
    total_count = 0
    discarded_count = 0

    # 1. 读取文件 (包裹在 try-except 中防止文件不存在)
    try:
        with open('raw_users.json', 'r', encoding='utf-8') as f:
            users = json.load(f)
    except FileNotFoundError:
        print("❌ 错误：找不到 raw_users.json 文件！")
        return
    except json.JSONDecodeError:
        print("❌ 错误：JSON 文件格式错误！")
        return

    # 2. 遍历与清洗
    for user in users:
        total_count += 1
        is_valid = True

        # 规则 A: 检查邮箱是否包含 @
        if '@' not in user.get('email', ''):
            print(f"⚠️ 丢弃用户 {user['name']}: 邮箱格式错误")
            is_valid = False

        # 规则 B: 检查时间是否存在
        if user.get('reg_time') is None:
            print(f"⚠️ 丢弃用户 {user['name']}: 注册时间缺失")
            is_valid = False

        if is_valid:
            try:
                # 规则 C: 转换时间戳 -> 日期字符串
                # %Y-%m-%d 代表 年-月-日
                date_str = time.strftime("%Y-%m-%d", time.localtime(user['reg_time']))

                # 构建清洗后的数据结构
                clean_user = {
                    "id": user['id'],
                    "name": user['name'],
                    "email": user['email'],
                    "date": date_str
                }
                valid_users.append(clean_user)

            except Exception as e:
                print(f"❌ 处理用户 {user['name']} 时发生未知错误: {e}")
                discarded_count += 1

    # 3. 写入 CSV 文件
    if valid_users:
        try:
            # 使用 'w', newline='' 是写入 CSV 的标准写法，防止出现空行
            with open('valid_users.csv', 'w', encoding='utf-8-sig', newline='') as f:
                # 定义 CSV 的列头
                fieldnames = ['id', 'name', 'email', 'date']
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writeheader()  # 写入表头
                writer.writerows(valid_users)  # 写入多行数据

            print("-" * 30)
            print(f"✅ 处理完成！")
            print(f"📊 统计结果：")
            print(f"   - 总数据量: {total_count}")
            print(f"   - 有效数据: {len(valid_users)}")
            print(f"   - 丢弃数据: {total_count - len(valid_users)}")
            print(f"💾 结果已保存至 valid_users.csv")

        except Exception as e:
            print(f"❌ 写入 CSV 文件失败: {e}")
    else:
        print("⚠️ 没有有效数据可写入。")


# 运行程序
if __name__ == "__main__":
    process_user_data()