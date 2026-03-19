import using_sys

#导入模块
import support
support.print_func("Runoob")

import fibo
fibo.fib(1000)  #等价于fib3 = fibo.fib  fib3(1000)

print(fibo.fib2(100))

from fibo import  fib, fib2 #导入fibo中的fib函数，并不会把整个fibo模块导入命名空间内