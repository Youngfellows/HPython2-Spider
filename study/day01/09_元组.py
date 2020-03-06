# 元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，以逗号隔开，也是可以存储不同类型的数据，但是尽量存储同类型数据,列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

# 一、元组
languages = ("java", "c++", "shell", "lua", "java")

# 1.index() 查找数据对应的下标
index = languages.index("shell")
print("index = %d" % index)

# 2.count() 统计元素出现的次数
count = languages.count("java")
print("count = %d" % count)

# 3.len() 统计元组的长度
size = len(languages)
print("size = %d" % size)

# 4.元组连接
names = ("小明", "丽丽", "小伟", "希希")
newTuple = languages + names
print(newTuple)
print(type(newTuple))

# 二、元组 与 列表相互转换
# 1.将列表转换为元组
fruits = ["apple", "banana", "orange"]
fruits_tuple = tuple(fruits)
print(fruits_tuple)
print("list type: %s" % type(fruits))
print("new_tuple type: %s" % type(fruits_tuple))

# 将元组转换为列表
print("*" * 30)
citys = ("深圳", "南京", "北京", "上海")
list_citys = list(citys)
print(list_citys)

print("citys type: %s" % type(citys))
print("list_citys type: %s" % type(list_citys))