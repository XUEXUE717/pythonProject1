'''
一、类对象
类对象支持两种操作:属性应用和实例化
标准语法：obj.name
类对象创建后，类命名空间中饭所有的命名都是有效属性名
'''

class MyClass:
    """一个简单的类实例"""

    i = 12345
    def f(self):   #属性名用变量表示，称为实例变量，用self修饰???
        return 'hello world'
#实例化
x = MyClass()

#访问类的属性和方法
print("MyClass 类的属性 i 为 ：",x.i)
print("MyClass类的方法 f 输出为：",x.f())

#构造方法————__int__()，该方法在类实例化时会自动调用
def __int__(self):
    self.data = []
#__int__（）方法可以有参数，通过__int__()传递到类的实例化操作上
class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0,-4.5)
print(x.r,x.i)
