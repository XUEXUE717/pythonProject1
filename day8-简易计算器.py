def input_num():
    num = 0
    while True:
        num1 = input("请输入数字,输入ok结束：")
        if num1 == 'ok':
            return num
        if num1 <= '0' and num1 >='9':
            print("输入错误，请重新输入")
            continue

        num = num * 10 + int(num1)

def con_str():
    while True:
        str = input("请选择需要做的运算 加+  减-  乘*  除/:")
        if str not in ['+','-','*','/']:
            print("输入错误，请重新输入")
            continue
        match str:
            case '+':
                print(num1, "+", num2, '=', num1 + num2)
            case '-':
                print(num1, "-", num2, '=', num1 - num2)
            case '*':
                print(num1, "*", num2, '=', num1 * num2)
            case '/':
                if num2 != 0:
                    print(num1, "/", num2, '=', num1 + num2)
                else:
                    print("除数不能为0")





while True:
    num1 = input_num()
    num2 = input_num()
    con_str()