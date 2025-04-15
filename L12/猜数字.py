import random

target = random.randint(1, 100)
count = 0

while True:
    try:
        guess = int(input("请猜一个1-100之间的数字："))
        count += 1
        if guess > target:
            print("太大了，请重新输入")
        elif guess < target:
            print("太小了，请重新输入")
        else:
            print(f"恭喜你，猜中了！共猜了{count}次")
            break
    except ValueError:
        print("请输入有效的数字！")
