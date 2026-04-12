'''
类的方法
在类的内部，使用 def 关键字来定义一个方法，
与一般函数定义不同，类方法必须包含参数 self,
且为第一个参数，self 代表的是类的实例。
'''

#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说：我 %d 岁。" %(self.name,self.age))

#实例化类
p = people('runoob',10,30)
p.speak()

#__init__：初始化方法（构造函数），用来在对象创建时设置初始状态
class Student:
    #初始化方法：在创建对象时自动调用，用来定义属性
    def __init__(self,name,student_id):
        self.name = name#实例属性：名字
        self.student_id = student_id#实例属性：学号
        self.scores = [] #实例属性：成绩列表，默认为空
    #自定义方法study
    #功能模拟学习行为，打印信息
    def study(self,subject):
        print(f"{self.name}正在努力学习{subject}...")

    #自定义方法：do_homework(self,homework_name),模拟完成作业打印信息
    def do_homework(self,homework_name):
        print(f"{self.name}正在完成{homework_name}")


    #自定义方法：check_score
    #功能：检查成绩，根据分数返回评价
    def check_score(self,score):
        self.scores.append(score)#将分数增加到列表中
        if score >= 90:
            print(f"当前共有{len(self.scores)}次成就记录")
            return  '优秀'
        elif score >= 60:
            print(f"当前共有{len(self.scores)}次成就记录")
            return '及格'
        else:
            print(f"当前共有{len(self.scores)}次成就记录")
            return "不及格"
#1.实例化对象（创建具体的学生），这里自动触发__init__方法
student_a = Student("张三",'1001')
student_b = Student("李四",'1002')

#2.调用stydy方法。这里的student_a就是self
student_a.study('Python编程')
#3.调用check_score方法并接受返回值
result = student_a.check_score(95)
print(f"{student_a.name}的成绩评价{result}")
#4.不同对象互不干扰
student_b.check_score(50)



###实例——
'''
创建一个名为 Calculator 的类。
定义一个 __init__ 方法，初始化一个名为 history 的空列表。
定义一个 add 方法，接收两个数字，将它们相加，并将结果存入 history 列表，同时打印结果。
定义一个 show_history 方法，打印所有的计算历史。
实例化两个计算器对象 calc1 和 calc2。
分别用它们进行几次加法运算，并查看各自的历史记录（验证它们是否独立）。'''

class Calculator:
    def __init__(self):
        self.history = []
    def add(self,a,b):
        sum = a + b
        self.history.append(sum)
        print(f"{a}+{b}={sum}")
    def show_history(self):
        print(f"历史记录：{self.history}")
calc1 = Calculator()
calc1.add(3,5)
calc1.add(57,8,)
calc2 = Calculator()
calc2.add(23,5)
calc2.add(7,8,)
calc1.show_history()
calc2.show_history()