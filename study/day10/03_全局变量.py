# 定义全局变量
sum = 0

# 定义函数
def cal_sum(a, b):
    # 声明为全局变量
    global sum
    sum = a + b
    print("cal_sum, sum = {}".format(sum))


# 调用函数
cal_sum(33, 21)
print("sum = {}".format(sum))
