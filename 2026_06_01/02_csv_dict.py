import csv
import requests

#使用dictreader读取数据并转换类型
#CSV读出来点默认全市字符串，而接口通常需要整数或者浮点数

def load_charging_data(file_path):
    data_list = []
    #使用with open可以自动管理文件点关闭，防止内存泄漏
    with open(file_path,mode='r',encoding='utf-8') as csvfile:
        #核心方法：dictreader会把第一行当做key
        reader = csv.DictReader(csvfile)

        for row in reader:
            #进行数据清洗和类型转换
            '''station_dict = {
                "station_id":str(row["station_id"]), # csv文件中点字段名
                "user_id":str(row["user_id"]),
                "power":float(row["power"])
            }'''
            #空值处理
            #1.station_id必须存在，如果空字符串就转为None
            station_id = row.get("station_id","").strip() or None
            user_id = row.get("user_id","").strip() or None
            raw_power = row.get("power","").strip()
            try:
                #只有当字符串非空时才转float
                power = float(raw_power) if raw_power else None
            except ValueError:
                #遇到“abc”这种非法字符，记录日志或者将其设置为None
                print(f"警告：站点（station_id）的功率'{raw_power}'不是有效数字，已跳过")
                power = None
            charge_type = row.get("charge_type","") or None
            location = row.get("location","") or None

            #组装字典
            station_dict = {
                "station_id":station_id,
                "user_id":user_id,
                "power":power,
                "charge_type":charge_type,
                "location":location
            }
            # 核心清洗：去掉所有 None 值，保持 JSON 干净
            clean_record = {k: v for k, v in station_dict.items() if v is not None}
            data_list.append(clean_record)
    return data_list

#调用接口前先打印看看格式对不对

if __name__ == "__main__":
    records = load_charging_data("charging_stations.csv")
    import json
    print(json.dumps(records,indent=2,ensure_ascii=False))
    #JSON格式化打印，dumps将python对象转换成标准的json字符串
    #indent设置缩进为两个空格
    #ensure_ascii = False默认情况 (True)：Python 默认会把非 ASCII 字符（比如中文“商圈”、“办公区”）全部转义成类似 \u5546\u5708 这样的乱码形式，以防止编码问题。
#设置为 False：告诉 Python “不要转义，直接显示中文字符”。这样你在控制台看到的就是正常的汉字，而不是让人头疼的 Unicode 编码。

