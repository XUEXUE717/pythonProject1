'''
一、类对象
类对象支持两种操作:属性应用和实例化
标准语法：obj.name
类对象创建后，类命名空间中饭所有的命名都是有效属性名
'''

class MyClass1:
    """一个简单的类实例"""

    i = 12345
    def f(self):   #属性名用变量表示，称为实例变量，用self修饰???
        return 'hello world'
#实例化
x = MyClass1()

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

#self代表类的实例而非类，类的方法与普通函数只有一个区别：它们必须有一个额外的第一个参数名称，按照惯例它的名称是self
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()
t.prt()

#定义一个类，并在类中定义方法，第一个参数通常被命名为self（可以使用其他的），为保持代码一致性和可读性，强烈使用self
class MyClass2:
    def __int__(self,value):
        self.value = value

    def display_value(self):
        print(self.value)
#创建一个实例
obj = MyClass2(42)
#调用实例的方法
obj.display_value()