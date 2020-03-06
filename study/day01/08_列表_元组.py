# 1.列表定义
course = ["java", "C++", "python", "shell", "android", "python", "ios"]

# 2.获取列表元素
print(course)
print(course[0])  # 取第一个元素
print(course[1])  # 取第一个元素
print(course[-2])  # 取倒数第2个元素

# 3.修改元素的值
course[1] = "web"
print(course[1])  # 取第一个元素

# 常用函数
# index() 返回指定数据所在的位置索引
# count() 统计指定的数据在当钱列表中出现的次数
# len() 访问列表长度，即为列表数据个数
# In:判断某个数据是否在序列中存在
# not:判断某个数据是否不在序列中
# append():在列表末尾添加新的对象
# extend():在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# insert(index, obj):将对象插入列表
# pop(): 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# remove(obj):移除列表中某个值的第一个匹配项
# clear() 清空列表
# reverse()反向列表中元素
# sort() 对原列表进行排序,默认升序排序，reverse=True为降序排序
# copy() 复制列表
# while循环 序列
# for循环序列
# 列表嵌套使用

# 4.获取列表长度
len1 = len(course)
print("len1 = %d" % len1)

# 5.获取指定元素的下标
print("python出现的索引: %d" % course.index("python"))

# 6.返回元素出现的次数
print("python出现的次数: %d" % course.count("python"))

# 7.In:判断某个数据是否在序列中存在
# not:判断某个数据是否不在序列中
isExitJava = "java" in course
print("java在列表中是否存在: %s" % isExitJava)

isExitJS = "javaScrcpy" not in course
print("javaScrcpy在列表中是否存在: %s" % isExitJS)

# 8.append():在列表末尾添加新的对象
course.append("ruby")
print(course)

# 9.extend():在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
newCourse = ["Objective-C", "swift", "kotlin"]
course.extend(newCourse)
print(course)

# 10.insert(index, obj):将对象插入列表
course.insert(3, "lua")
print(course)

# pop(): 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
course.pop()
print(course)

course.pop(3)  # 删除第4个元素
print(course)

# remove(obj):移除列表中某个值的第一个匹配项
course.remove("android")
print(course)

# clear() 清空列表
# course.clear()
# print(course)

# reverse()反向列表中元素
course.reverse()
print(course)

# sort() 对原列表进行排序,默认升序排序，reverse=True为降序排序
course.sort()
print(course)
course.sort(reverse=True)
print(course)

# copy() 复制列表
course2 = course.copy()
print(course2)
print("*" * 30)

# while循环 序列
index = 0
len2 = len(course)
print("len2 = %d" % len2)
print(type(index))
print(type(len2))
while index < len2:
    print(course[index])
    index += 1

print("*" * 30)
# for循环序列
for yy in course:
    print(yy)

# 11.列表嵌套使用
list1 = [["Java", "python", "C#", "php"], ["张三丰", "张无忌", "马永贞", "韦小宝"], [1, 2, 3, 4]]
for childList in list1:
    for child in childList:
        print(child)
    print("=" * 30)

# 12.删除序列元素
list1 = ["java", "python", "C#", "php"]
# del 删除序列也可以删除指定元素
del list1[0]
print(list1)

# 第一个元素已经被删掉了，第二个报错是将序列已经删除掉，所以找不到了
del list1
print(list1)
