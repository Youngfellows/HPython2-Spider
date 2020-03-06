# 1.定义函数
def say():
    print("welcom to china ...")


# 调用函数
say()


# 2.函数返回值
def sum(a, b):
    return a + b


print("sum = %d" % sum(3, 4))

print("*" * 30)


# 3.不可变参数(类似传递值)
def changeInt(number):
    number = 3
    print("内部number: %d" % number)


number = 15
changeInt(15)
print("外面number: %d" % number)


# 4.可变参数(类似传递地址)
def changeme(mylist):
    mylist.append([1, 2, 3, 4, 5])
    print("函数内取值:", mylist)
    return


mylist = [33, 44, 55]
changeme(mylist)
print("函数外取值:", mylist)


def change_student(student):
    student["hobby"] = "上网"
    print("change_student: ", student)


student = {"name": "老王", "age": 45, "sex": "男"}
print("修改前:", student)
# 调用函数
change_student(student)
print("修改后:", student)


# 5.关键字参数
def print_info(name, age, sex):
    print("name:%s" % name)
    print("age:%s" % age)
    print("sex:%s" % sex)


print_info(age=18, name="老李", sex="女")


# 6.默认参数
def car_info(name, color="red"):
    print("car name is %s" % name)
    print("car color is %s" % color)


car_info("jeep")


# 7.不定长参数
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
def fruit_info(name, *var_tuple):
    print("name:%s" % name)
    print(var_tuple)


fruit_info("香蕉", "长", 3.8, 5)
fruit_info("苹果")


# 加了两个星号 ** 的参数会以字典的形式导入
def hero_info(name, **var_arg_dict):
    print("name:%s" % name)
    print(var_arg_dict)


hero_info("杨过", age=24, kongfu="玄铁剑法", friend="小龙女")

# 8.匿名函数
# python 使用 lambda 来创建匿名函数。
sum = lambda num1, num2: num1 + num2

# 调用匿名函数
print("sum = %d" % (sum(30, 5)))
print("sum = %d" % (sum(3, 8)))


# 9.return语句
# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。

def mult(a, b):
    return a * b


print("3*4 = %d" % mult(3, 4))


# 返回值为None
def hello():
    print("欢迎来深圳...")


print(hello())
