'''super是什么？
super是一个class
super（）是创建一个实例
'''
#单继承
class A:
    def __init__(self):
        self.n = 2
    def add(self,m):
        print('self is {} @A.add'.format(self))
        self.n += m
class B(A):
    def __init__(self):
        self.n = 3
    def add(self,m):
        print('self is {} @B.add'.format(self))
        super.add(m)
        self.n += m
b = B()  #调用B类的__init__方法，将实例b的属性n初始值化为3
b.add(2)
print(b.n)