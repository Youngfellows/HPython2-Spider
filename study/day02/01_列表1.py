'''
List列表
这个是python里面用的最多最常用的数据类型，可以通过下标来访问，可以理解为java或者c里面的数组.
但是功能比数组强大n倍,list可以放任意数量的python对象，可以是字符串，字符，整数，浮点等等都可以，
而且创建，添加，删除也很方便.
'''

# 1)创建list //list内部的对象可以是字符串，字符，数字，支持混搭
aList = ["apple", 100, 3.1415926, "banana", 'A', "B", "深圳", False, "orange"]
print(aList)

# 2)访问list //直接通过下标去访问
print("aList[3] = %s" % aList[3])

# 3)列表的切片 //通过切片来取列表中的一部分
print("aList[4:6] = %s" % aList[2:6])
print(type("type is %s" % aList[2:6]))

# 4)列表的嵌套 //列表支持嵌套，就是列表里面可以套列表，甚至套字典，元组等
bList = [100, 3.14, ["aaa", "apple", "banana"]]
print(bList)
print("siez = %d" % len(bList))
print("bList[0] = %d" % bList[0])
print("bList[2] = %s" % bList[2])

# 5)列表的插入//内置函数append,insert
print("*" * 30)
aList[2] = "小明"
aList.append("广州")
aList.insert(1, "google")
print(aList)

# 6)列表的删除//内置remove,pop函数
print("***********删除列表元素*********")
del aList[0]
print(aList)
aList.remove("banana")
print(aList)
aList.pop()
print(aList)
aList.pop(2)
print(aList)

# 7)列表支持*，+
print("*" * 30)
list1 = [1, 2, 3]
list2 = ["北京", "广州", "深圳"]
list3 = list1 + list2
print(list3)

list4 = ["a", "bbb", 100]
list5 = list4 * 3
print(list5)

# 8)列表的排序//内置了sort函数非常方便,通过传入reverse为True或者False来升序或者降序排列
print("************列表的排序*************")
list6 = [33, 22, 45, -1, 0, 250, -78, 3.15, -22, 70]
list6.sort()
list6.sort(reverse=False)  # 升序
print(list6)
list6.sort(reverse=True)  # 降序
print(list6)

# 9)计算列表的长度 //利用内置函数len()
size = len(list6)
print("size = %d" % size)

# 10)计算列表里面的最大值，最小值
list7 = [3.15, -7, 2, 0, 23, 2]
print(min(list6))
print(max(list6))

# 11)列表的扩展 //用内置extend函数，看起来和+差不多，其实区别在于+是返回一个新的列表，而extend是直接修改了列表
list8 = ["广州", "南京", "济南"]
list7.extend(list8)
print(list7)
print(list8)

# 12)查找列表中某一个元素的索引//内置函数index
list9 = ['This', 'is', 'a', "very", "google", "idea"]
print(list9.index("very"))

# 13)统计某个元组在列表里面的次数,内置函数count
aList = ['to', 'do', 'or', 'not', 'to', 'do']
print(aList.count("to"))

