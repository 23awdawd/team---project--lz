def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "除数不能为 0"
    return a / b

while True:
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 退出")
    choice = input("请输入你的选择（1 - 5）：")
    if choice == '5':
        break
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    if choice == '1':
        result = add(num1, num2)
        print(f"结果：{result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"结果：{result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"结果：{result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"结果：{result}")
    else:
        print("无效的选择，请重新输入")