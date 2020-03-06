print("数字猜谜游戏!")
number = 7
while True:
    guess = int(input("请输入你猜的数字:"))
    if guess == number:
        print("恭喜你猜中了...")
        break
    elif guess > number:
        print("大了...")
    else:
        print("小了...")