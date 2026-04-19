'''使用 os.path 模块
这是最常用的方法之一。os.path.exists() 可以判断路径（文件或目录）是否存在，
而 os.path.isfile() 则专门用于判断路径是否存在且是一个常规文件。'''
import os

file_path = 'example.txt'

# 方法一：判断路径是否存在（文件或目录）
if os.path.exists(file_path):
    print(f"路径 {file_path} 存在")

# 方法二：专门判断是否为常规文件
if os.path.isfile(file_path):
    print(f"文件 {file_path} 存在")

'''使用 pathlib 模块 (Python 3.4+)
pathlib 提供了面向对象的文件系统路径操作接口，更加现代化。'''
from pathlib import Path

file_path = Path('example.txt')

# 判断路径是否存在
if file_path.exists():
    print(f"路径 {file_path} 存在")

# 专门判断是否为常规文件
if file_path.is_file():
    print(f"文件 {file_path} 存在")

    '''使用 try-except 语句
通过尝试打开文件来捕获 FileNotFoundError 异常。
这种方法适合在判断存在后需要立即对文件进行操作的场景。'''
file_path = 'example.txt'
try:
    with open(file_path, 'r') as file:
        print(f"文件 {file_path} 存在并已打开")
except FileNotFoundError:
    print(f"文件 {file_path} 不存在")