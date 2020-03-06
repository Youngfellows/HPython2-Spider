'''
Set（集合）
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：
parame = {value01,value02,...}
或者
set(value)
'''

students = {"老吴", "小李", "张三", "八哥", "小李"}

# 1.输出集合，重复的元素被自动去掉
print(students)
print("set size is: %d" % len(students))

# 2.成员测试
if "老吴" in students:
    print("老吴在集合中")
else:
    pass

# 成员测试
if "小彭" in students:
    print("小彭在集合中")
else:
    print("小鹏不在集合中...")

# 3. set可以进行集合运算
print("*" * 30)
stu_class1 = {"老吴", "小李", "张三", "八哥", "思雨"}
stu_class2 = {"乔峰", "杨过", "小李", "九妹", "小鱼儿"}

print(stu_class1)
print(stu_class2)
# a 和 b 的差集
print(stu_class1 - stu_class2)

# a 和 b 的并集
print(stu_class1 | stu_class2)

# a 和 b 的交集
print(stu_class1 & stu_class2)

# a 和 b 中不同时存在的元素
print(stu_class1 ^ stu_class2)
