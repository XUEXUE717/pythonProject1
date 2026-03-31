'''
类继承练习：
1.员工分为两类：全职与员工 FullTimeEmployee 兼职员工 PartTimeEmployee
2.全职和兼职都有姓名 name，工号 id 属性，都具备“打印信息 print_info”方法
3.全职月薪 monthly_salary,兼职日薪 daily_salary 属性、 每月工作天数 work_days
4.全职和兼职都要有计算月薪的方法，但计算过程不一样（calculate_monthly_pay）

'''
#父类——全职和兼职都有姓名 name，工号 id 属性，都具备“打印信息 print_info”方法
class Employee:
    def __init__(self,num,name):
        self.name = name
        self.id = num
    def print_info(self):
        print("姓名：%s  工号：%d"%(self.name,self.id))
#全职员工
class FullTimeEmployee(Employee):
    def __init__(self,num,name,ms,wd):
        Employee.__init__(self,num,name)
        self.monthly_salary = ms
        self.work_days = wd
    def calculate_monthly_pay(self):
        self.monthly_pay = self.monthly_salary  + 200
        Employee.print_info(self)
        print("月薪：", self.monthly_pay)
#兼职员工
class PartTimeEmployee(Employee):

    def __init__(self,id,name,ps,wd):
        Employee.__init__(self,id,name)
        self.daily_salary = ps
        self.work_days = wd

    def calculate_monthly_pay(self):
        self.monthly_pay = self.daily_salary * self.work_days
        Employee.print_info(self)
        print("月薪：",self.monthly_pay)
Full = FullTimeEmployee(123,"nana",5000,20)
Full.calculate_monthly_pay()
Part = PartTimeEmployee(345,'doudou',200,25)
Part.calculate_monthly_pay()