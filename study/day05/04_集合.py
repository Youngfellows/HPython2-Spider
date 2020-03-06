"""
Python3 集合
    集合（set）是一个无序的不重复元素序列。
    可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
# 1.创建集合
fruits = {"apple", "orange", "banana", "pear"}
company = set(("Google", "Baidu", "Tencent", "Facebook", "apple"))
print(fruits)
print(company)

# 2.集合运算
# 集合a中包含而集合b中不包含的元素
print(fruits - company)

# 集合a或b中包含的所有元素
print(fruits | company)

# 集合a和b中都包含了的元素
print(fruits & company)

# 不同时包含于a和b的元素
print(fruits ^ company)

# 3.添加元素
company.add("Microsoft")
print(company)

# 参数可以是列表，元组，字典等
china_company = ("招商银行", "vivi", "oppo", "美团")
price_list = [3, 4, 2.5, 8]
persion = {"name": "老王", "age": 45, "sex": "男"}  # 只添加key到集合
company.update(china_company)
company.update(price_list, persion)
print(company)

# 4.移除元素
car = {"奥迪", "奔驰", "宝马", "特斯拉", "东风"}
print(car)
car.remove("奔驰")
print(car)
try:
    car.remove("本田")
except KeyError:
    print("元素不存在...")

# 如果元素不存在，不会发生错误
car.discard("宝马")
car.discard("红旗")
print(car)

# 5.集合大小
print("集合大小: size = %d" % len(car))

# 6.清空集合
# car.clear()
# print("car size is ", len(car))

# 7.判断元素是否在集合中存在
if "奥迪" in car:
    print("奥迪存在集合中...")
else:
    print("奥迪不在集合中...")

if "奔驰" not in car:
    print("奔驰不在集合中...")
else:
    print("奔驰存在集合中...")

"""
二、集合内置方法完整列表
"""
# 1.	为集合添加元素
car.add("大众")
print(car)

# 2.清空集合
# car.clear()
# print("car size is ", len(car))


# 3.拷贝一个集合
new_car = car.copy()
print(new_car)

# 4.返回集合的差集
heros = {"杨过", "小龙女", "郭靖", "黄蓉"}
citys = {"东京", "北京", "上海", "小龙女"}
print(heros.difference(citys))

# 返回集合的交集
print(heros.intersection(citys))

# intersection_update() 方法用于获取两个或更多集合中都重叠的元素，即计算交集。
# intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，而 intersection_update() 方法是在原始的集合上移除不重叠的元素。
print("*******1***************")
# heros.intersection_update(citys)

# 返回两个集合中不重复的元素集合
print(heros.symmetric_difference(citys))

# 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
heros.symmetric_difference_update(citys)

# 返回两个集合的并集
heros.union(citys)

# 5.移除两个集合中都存在的元素
print(heros)
print(citys)
heros.difference_update(citys)
print(heros)
print(citys)
print("*" * 30)

# 6.删除集合中指定的元素
citys.discard("上海")
print(citys)
print(heros)

# 7.判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
print(heros.isdisjoint(citys))

# 8.指定集合是否为该方法参数集合的子集
print(heros.issubset(citys))
print(heros.issuperset(citys))

# 9.随机移除元素
heros.pop()
print(heros)

# 10.移除指定元素
citys.remove("东京")
print(citys)

# 11.给集合添加元素
set1 = {1, 2, 3, 4}
set2 = {"apple", "orange", "banana"}
set1.update(set2)
print(set1)
print(set2)
