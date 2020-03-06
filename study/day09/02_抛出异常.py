# 抛出异常
number = int(input("请输入一个数字:"))
if number > 7:
    raise Exception("number不能大于7,number是{0}".format(number))

print("你输入的数字是:{0}".format(number))


