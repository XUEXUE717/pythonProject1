"""
    lambda 创建匿名函数
    lambda函数是一种小型的、匿名的、内联函数，可以具有任意数量的参数，只能有一个表达式
    无需def关键字定义
    lambda通常用于编写简单的 单行函数，通常在需要函数作为参数的情况下使用，例如在map（），filter（），reduce（）等函数中
    lambda函数是匿名的，没有函数名称，只能通过赋值给变量或者作为参数传递给其他函数使用，通常只包含一行代码

                补充：map（）内置高阶函数，核心作用：报一个函数依次作用到可迭代对象（列表，元组等）的面一个元素上返回一个迭代器
                        返回值是迭代器，必须用list（）、tuple（）等转换
                        惰性计算，只有循环时才会组个计算元素
                        长度不一致时，多个迭代对象长度不同，以最短的那个为准
                filter（）同高阶函数，根据指定的过滤条件，从可迭代对象中筛选符合条件元素，返回布尔值
                      filter(条件，变量)
                reduce（）高阶函数，持续累积计算，最终返回一个单一结果，
                    需要导入模块，必须接收两个参数，空迭代返回错误提示


    lambda 参数列表：表达式
        参数列表可以包含0个或多个参数，但必须在冒号前指定
        表达式用于计算并返回函数结果
"""
#无参数的lambda函数
f = lambda : "Hello world!"
print(f())

#有参数的匿名函数,多个参数用逗号隔开
y = lambda a : a + 10
print(y(5))

x = lambda a,b : a + b
print(x(2,6))

#与内置函数map()一起使用
numbers = [1,2,3,4,5]
squared = list(map(lambda x : x**2,numbers))
print(squared)

#与filter()一起使用，筛选偶数
numbers = [1,2,3,4,5,6,7,8]
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(even_numbers)

#与reduce()演示如何计算一个序列的累积乘积

from functools import  reduce
numbers = [1,2,3,4,5]
product = reduce(lambda x,y: x*y ,numbers)
#reduce()函数通过遍历numbers列表，并使用lambda函数累积的结果不断更新，最终1*2*3*4*5=120
print(product)

nums = [1,2,3,4,5,6,7,8]
even = filter(lambda x : x % 2 == 0,nums)
doubled = map(lambda x : x * 2, even)
sum = reduce(lambda x , y : x + y ,doubled)
print(sum)