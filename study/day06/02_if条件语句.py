# if条件语句
age = int(input("请输入年龄:"))
if age > 60:
    print("%d岁是老年人" % age)
elif age > 18:
    print("%d岁是中年人" % age)
else:
    print("%d岁是年轻人" % age)

"""
以下为if中常用的操作运算符:
    操作符	描述
    <	    小于
    <=	    小于或等于
    >	    大于
    >=	    大于或等于
    ==	    等于，比较两个值是否相等
    !=	    不等于
"""

# 2.if 嵌套语句
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
