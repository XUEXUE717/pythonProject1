"""异常：
1. 基础结构：try-except-else-finally"""

try:
    #1.试着打开文件（可能文件不存在）
    with open('test1.txt','r',encoding='utf-8') as f:
        content = f.read()
        #模拟一个数学错误
        result = 10 / 0
except FileNotFoundError:
    #2.文件如果找不到执行这里
    print("错误！文件不存在，请检查路径")
except ZeroDivisionError:
    #3.如果除以0执行
    print("错误：不能除以0")
else:
    #4.如果上面没有报错
    print(f"文件读取成功，内容长度：{len(content)}")
finally:
    #5.无论是否报错，最后都会执行
    print("end操作结束")