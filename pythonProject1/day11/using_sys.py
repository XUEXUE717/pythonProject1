import sys
print('命令行参数如下：')
for i in sys.argv:
    #sys.argv把命令行输入的东西都存起来
    print(i)
print('\n\nPython 路径为：',sys.path,'\n')

'''
import sys 引入python标准库中的sys.py模块，这是引入某一模块的方法
sys.argv是一个包含命令行参数的列表
sys.path包含了python解释器自动查找所需模块的路径的列表
'''

if __name__ == '__main__':
    print('程序本身在运行')
else:
    print("我来自其他模块")