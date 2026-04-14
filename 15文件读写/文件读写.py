#open()方法
'''用于打开一个文件，并返回文件对象
若文件无法打开，会抛出OSError，使用完之后一定要调用close()关闭文件
语法： open(file,mode= 'r')
'''
"""t = open('test1.txt',mode = 'r+',encoding='utf-8')
print("文件名为：",t.name)

#readline() 方法用于从文件读取整行，包括 "\n" 字符。
#如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
line = t.readline()#文件指针刚开始在开头处
print("读取第一行：",line)
#执行完上面readline后指针往后移动
line = t.readline(11)
print("读取字符串为：",line)
t.close()"""
#flush()刷新文件内部缓冲区

#fileno()返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作
t = open('test1.txt',mode = 'wb')
fid = t.fileno()
print("文件描述为：",fid)
#关闭文件
t.close()




with open('test1.txt','r',encoding='utf-8') as f:
    content = f.read()
    #文件自动关闭，无需close()
