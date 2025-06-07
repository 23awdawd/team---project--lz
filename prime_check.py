def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("请输入一个数字："))
if is_prime(num):
    print(f"{num} 是素数")
else:
    print(f"{num} 不是素数")