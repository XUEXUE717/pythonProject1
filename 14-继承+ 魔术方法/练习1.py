'''定义一个 Vehicle (交通工具) 类，有 move() 方法打印“正在移动”。
定义 Car 类继承 Vehicle，重写 move() 打印“正在公路上跑”，并添加 honk() 方法打印“滴滴”。'''
class Vehicle():
    def __init__(self,name):
        #初始化父类，给当前类别命名
        self.vehivle_name = name

    def move(self):
        print("正在移动")
class Car(Vehicle):
    def __init__(self,name):
        super().__init__(name)
    def move(self):
        print("正在公路上跑")
    def honk(self):
        print("滴滴")

c = Car("公交车717路")
print(c.vehivle_name)
c.move()
c.honk()
