'''1.单继承
    语法：class Chilid(Parent)'''
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "发出某种声音"
#Dog 继承 Animal
class Dog(Animal):
    #1.重写__init__(如果需要初始化子类特有属性)
    def __init__(self,name,breed):
        #调用父类初始化，处理name
        super().__init__(name)#super等同于super（Dog，self）
        self.breed = breed#子类特有属性
#新添__str__魔术方法
    def __str__(self):
        return f"我是{self.name},品种是{self.breed}"
#__repr__
    def __repr__(self):
        return f"Dog({self.name},{self.breed})"
    #重写speak方法
    def speak(self):
        return "汪汪汪！"   #这里完全替代父类行为
    #扩展父类行为
    def speak_with_super(self):
        original_sound = super().speak()#获取原始父类的声音方法
        return f"{original_sound}"
d = Dog("旺财","柯基")
print(d)
print(repr(d))

