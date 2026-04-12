'''方法重写
父类方法的功能不能满足需求，可在子类重写父类的方法
'''
class Parent:
    def myMethod(self):
        print("调用父类方法")
class Child(Parent):
    def myMethod(self):
        print("调用子类方法")

c = Child()
c.myMethod()
super(Child,c).myMethod()