
import json
import time

# 模拟原始数据（包含脏数据）
raw_data = [
    {"id": 101, "name": "Alice", "email": "alice@example.com", "reg_time": 1678888888},
    {"id": 102, "name": "Bob", "email": "bob-at-mail.com", "reg_time": 1678999999}, # 邮箱格式错误
    {"id": 103, "name": "Charlie", "email": "charlie@test.org", "reg_time": None}, # 时间缺失
    {"id": 104, "name": "David", "email": "david@demo.net", "reg_time": 1679111111},
    {"id": 105, "name": "Eve", "email": "eve@example.com", "reg_time": 1679222222}
]

# 生成文件
with open('raw_users.json', 'w', encoding='utf-8') as f:
    json.dump(raw_data, f, ensure_ascii=False, indent=2)

print("✅ 测试数据 raw_users.json 已生成")