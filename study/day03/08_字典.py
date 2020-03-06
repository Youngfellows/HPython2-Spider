'''
Dictionary（字典）
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
'''

# 0.定义字典
# 构造函数 dict() 可以直接从键值对序列中构建字典
sourse = {}
sourse["one"] = "语文"
sourse[1] = "英语"

student_info = {"name": "小明", "age": 33, "address": "南京"}
market_info = dict([("fruit", "apple"), ("age", 33), ("price", 23.4)])
score = dict(name="李寻欢", subject="语文", score=88.5)

# 1.打印字典元素
print(sourse)
print(student_info)
print(market_info)
print(score)

# 2.获取字典元素
print(sourse["one"])
print(sourse[1])

# 3.输出所有键
print(student_info.keys())

# 4.输出所有值
print(student_info.values())

print(type(student_info.keys()))
