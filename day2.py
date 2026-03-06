'''1'''
var1 = 'hello world!'
var2 = "Runoob"
print("var1[0]:",var1[0])
print("var2[1,5]:",var2[1:5])

#2python字符串更新
var1 = 'Hello World!'
print("已更新字符串：",var1[:6] + 'Runoob！')

'''转义字符'''

#使用\r实现百分比进度
import time
for i in range(101):
    bar = '[' + '=' * (i//2) +' ' * (50 - i // 2) + ']'
    #f代表格式化字符串，即f-字符串格式化，允许在字符串中直接嵌入表达式，这些表达式在运行时会被其值所替换
    #\r回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
    #flushflush=True 表示强制立即刷新输出缓冲区，确保内容立即被写入到目标设备（通常是控制台），而不是等待缓冲区满或者程序结束时才输出
    print(f"\r{bar}{i:3}%",end='',flush=True)
    time.sleep(0.05)
print()

#转义字符演示
print('\'Hello world!\'')
print("Hello World!\nHow are you?")

#ASCII码互换
decimal_number = 42
binary_number = bin(decimal_number) #十  → 2
octal_number = oct(decimal_number) #八
hexadecimal_number = hex(decimal_number) #十六
print('转换为二进制：',binary_number)
print('转换为八进制：',octal_number)
print('转换为十六进制：',hexadecimal_number)
print('转换为二进制：%s \n转换为八进制：%s \n转换为十六进制：%s \n'%(binary_number,octal_number,hexadecimal_number))

#f-string  以f开头，后面跟着字符串，字符串中的表达式用大括号｛｝包起来，它会将变量或表达式计算后的值替换进去，不用判断数据类型
name = 'Runoob'
print(f'Hello {name}') #替换变量

