'''父类 Person：姓名，年龄。方法：打招呼。
子类 Student：增加学号。重写打招呼（显示学号）。
子类 Teacher：增加科目。重写打招呼（显示科目）。'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
       return f"大家好，我是{self.name},今年{self.age}岁"
    def __str__(self):
        return f"Person({self.name})"
class Student(Person):
    def __init__(self,name,age,name_id):
        #调用父类初始化
        super().__init__(name,age)
        #初始化子类特有属性
        self.name_id = name_id
    #输出时调用
    def __str__(self):
        return f"学生你好！姓名：{self.name},学号：{self.name_id}"
    def say(self):
        #print(self)
        #重写方法，扩展父类功能
        base_say = super().say()
        return f"{base_say}我都学号是{self.name_id}"
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        # 输出时调用
#完全覆盖父类方法
    def say(self):
        return f"我是老师{self.name},教{self.subject}."
    def __repr__(self):
        return f"Teacher('{self.name}',{self.age},'{self.subject}')"

s = Student("nana",12,'1011')
t = Teacher("tutu",33,"语文")
p = Person("doudou",12)
print(p.say())
print(s.say())
print(t.say())
tt = Teacher("李老师",35,"数学")
print(repr(tt))
