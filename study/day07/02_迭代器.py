"""
迭代器
    迭代是Python最强大的功能之一，是访问集合元素的一种方式。
    迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
    迭代器有两个基本的方法：iter() 和 next()。
    字符串，列表或元组对象都可用于创建迭代器：
"""
students = ["杨过", "郭靖", "乔峰", "李寻欢"]
# 创建迭代器对象
iter_stu = iter(students)
try:
    # 输出迭代器的下一个元素
    print(next(iter_stu))
    print(next(iter_stu))
    print(next(iter_stu))
    print(next(iter_stu))
    print(next(iter_stu))
except StopIteration:
    print("迭代元素异常...")

# 迭代器对象可以使用常规for语句进行遍历
print("*" * 30)
citys = ("上海", "深圳", "北京", "成都")
iter_citys = iter(citys)
for city in iter_citys:
    print(city)

# next() 函数遍历列表
print("*" * 30)
fruits = ["apple", "orange", "banana", "pear"]
iter_fruits = iter(fruits)

while True:
    try:
        print(next(iter_fruits))
    except StopIteration:
        break

print("*" * 30)
