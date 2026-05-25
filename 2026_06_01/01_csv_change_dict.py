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

    #打印查看第一条数据
    print(records[0])
    # 预期输出类似: {'station_id': 'ST001', 'user_id': 'USER88', 'power': 7.0}

#将字典直接接入requests发起请求
#根据实际调用点接口是GET还是POST,选择传参方式
#场景A：如果是GET请求，参数拼接在URL后面

url = "https://httpbin.org/get"

for record in records:
    #直接将字典传给params参数，request会自动将其编码到URL上
    response = requests.get(url,params=record)
    print(f"正在查询站点{record['station_id']}...")
    print("返回状态码",response.status_code)
    print("响应内容",response.json())
    print("*"*40)

#场景B：post请求，参数放在请求体body中
url = "https://httpbin.org/post"
for record in records:
    #直接将字典传给json参数，requests会自动处理为json格式并设置Header
    responsee = requests.post(url,json = record)

    print("创建订单结果",response.json())
