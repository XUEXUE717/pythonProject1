'''题目三：简单的API模拟与日志记录
背景：模拟一个简单的API请求过程。程序接收一个用户ID，模拟从“服务器”获取数据（以JSON字符串形式模拟），解析数据，并将其保存到文本日志文件中。
要求：
获取JSON：编写一个函数 fetch_data(user_id)，返回一个模拟的JSON字符串（例如 {"status": "success", "data": {"id": 1, "value": "test"}}）。
传参与解析：编写主函数，接收用户ID，调用上述函数获取JSON字符串，并使用 json.loads() 将其解析为字典。
文件读写：将解析后的数据（格式化为可读的字符串）追加写入到 api_log.txt 文件中。
异常处理：
如果解析JSON失败（例如返回了无效的JSON格式），捕获 json.JSONDecodeError。
如果写入文件失败，捕获相应的IO异常。'''