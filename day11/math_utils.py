import math
from typing import List,Union,Tuple
def calculate_mean(numbers:List[Union[int,float]])->float:
    #定义一个叫 calculate_mean 的功能，它必须接收一个由整数或小数构成的列表作为输入，并且计算结束后，必须返回一个小数。
    '''
    1.计算平均值——计算给指定数字列表的算术平均值
    参数解释：numbers表示传入参数的变量名
            : 冒号后面紧跟的时对该参数类型
            List[...]表示传入的参数必须是一个列表
            Union[int,float]表示列表里的元素可以是int或者float
            ->返回类型提示
            返回类型为float
    :param numbers:
    :return:
    '''
    if not numbers:
        raise ValueError("列表不能为空")#程序警报器
    return sum(numbers)/len(numbers)

def id_prime(n:int) -> bool:
    '''
    2.判断支数——检查一个整数是否为质数
    Args：
        n：待检查整数
    :return  如果是质数返回True，否则False

    :param n:
    :return:
    '''
    if n <= 1:
        return False
    if n<=3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    #检查从5到sqrt（n）因数，步长为6-优化算法
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True
def edclidean_distance(p1:Tuple[float,float],p2:Tuple[float,float]) ->float:
    '''
    3.计算欧几里得距离——计算二维平面上两点之间的距离

    :param p1:第一个点的坐标
    :param p2:第二个点的坐标
    :return:两点之间的距离（float）
    '''
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

def factorial(n:int)->int:
    '''
    计算阶乘（非负数）
    :param n:非负数整数n
    :return:int
    '''
    if n < 0:
        raise ValueError("阶乘不支持负数")
    if n==0 or n == 1:
        return 1
    result = 1
    for i in range(2,n+1):
        result *= i;
    return result

def clamp(value:Union[int,float],min_val:Union[int,float],max_val:Union[int,float])->Union[int,float]:
    '''
    5. 数值限制（Clamp）——将数值限制在指定的最小值和最大值之间，常用语游戏开发或者数据归一化
    :param value:原始数值
    :param min_val:最小边界
    :param max_val:最大边界
    :return:返回数值
    '''
    if min_val > max_val:
        raise ValueError("最小值不能大于最大值")
    return max(min_val,min(value,max_val))