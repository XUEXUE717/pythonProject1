'''
派生类(子类)会继承基类（父类）的属性和方法
两者需要定义在一个作用域内
还可用作表达式
'''
class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说：我 %d 岁。"%(self.name,self.age))
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade = g
    #覆盖父类的方法
    def speak(self):
        print("%s 说：我 %d 岁,我在读 %d 年级" % (self.name, self.age,self.grade))
s = student('ten',10,60,3)
s.speak()

'''多继承

'''