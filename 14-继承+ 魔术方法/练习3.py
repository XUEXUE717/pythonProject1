'''定义一个 Animal 类，有个 speak 方法返回“发出声音”。
定义一个 Cat 类继承它，重写 speak 返回“喵喵喵”。
实例化一个 Cat 对象，打印它的叫声。'''
class Animal:
    def __init__(self,name):
        self.animal_name = name
    def speak(self):
        return f"发出声音"
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def speak(self):
        return f"喵喵喵"
    def __str__(self):
        return f"我是猫咪{self.animal_name}"
    def __repr__(self):
        return f"Cat（‘{self.animal_name}’）"
c = Cat('doudou')
print(c)
print(repr(c))