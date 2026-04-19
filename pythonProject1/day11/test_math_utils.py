from math_utils import *
#测试平均值
print(f"平均值：{calculate_mean([1,2,3,4,5,6])}")
print(f"平均值：{calculate_mean([1])}")

#测试质数
print(f"17是质数吗？{id_prime(17)}")
print(f"18是质数吗？{id_prime(18)}")

#测试距离
point_a = (0,0)
point_b = (3,4)
print(f"距离：{edclidean_distance(point_a,point_b)}")


#测试阶乘
print(f"5的阶乘：{factorial(5)}")

#测试限制数值
print(f"限制数值：{clamp(150,0,100)}")
print(f"限制数值：{clamp(-10,0,100)}")
