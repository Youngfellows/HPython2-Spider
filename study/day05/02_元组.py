"""
一、Python3 元组
    Python 的元组与列表类似，不同之处在于元组的元素不能修改。
    元组使用小括号，列表使用方括号。
    元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
"""
# 1、创建元组
citys = ("北京", "上海", "深圳", "武汉", "贵阳", "南京", "天津")
prices = (1.25, 3.4, 6, 9, 0, 3.1415)
fruits = ("apple", "banana", "orange")
empty_tupl = ()  # 空元组
country = ("韩国",)  # 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用

print("元组类型:%s" % type(citys))
print(citys)
print(prices)
print(empty_tupl)
print("type:%s --->>> %s" % (type(country), country))

# 2、访问元组
# 元组可以使用下标索引来访问元组中的值
print("元组第一个元素 citys[0]: ", citys[0])
print("citys[1:5]: ", citys[1:5])

# 元组索引，截取
# 因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素
print("元组倒数第2个元素 citys[-2]: ", citys[-2])
sub_citys = citys[2:]
print("截取第3个元素后的元组元素:", sub_citys)

# 3.修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
# citys[0] = "昆明"
new_tupl = citys + prices
print(new_tupl)

# 4.删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
# del citys[1]
# del citys
# print(citys)


# 5.元组运算符
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
# 元组的大小
print("元组的大小: size = %d" % len(citys))

# 6.元组连接
new_tupl2 = fruits + citys
print("连接后元组: ", new_tupl2)

# 7.元组复制
copy_tupl = fruits * 4
print("复制后元组: ", copy_tupl)

# 8.元素是否在元组中
if "上海" in citys:
    print("元素'上海'在元组citys中...")
else:
    print("元素'上海'不在元组citys中...")

if "乌鲁木齐" not in citys:
    print("元素'乌鲁木齐'不在元组citys中...")
else:
    print("元素'乌鲁木齐'在元组citys中...")

# 9遍历元组元素
for city in citys:
    print(city)

# 10.元组内置函数
# 元组元素个数
print("citys元组元素个数: %d" % len(citys))

# 元组中元素最大/小值
print("元组中元素最大值: %s" % max(fruits))
print("元组中元素最小值: %s" % min(fruits))

# 将列表转换为元组
students = ["杨过", "小龙女", "郭靖", "黄蓉"]
students_tupl = tuple(students)
print("type students is %s" % type(students))
print("type students_tupl is %s" % type(students_tupl))
print(students)
print(students_tupl)
