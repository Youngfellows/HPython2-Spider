"""
一、Python3 列表
"""
# 1、定义列表
# 列表的数据项不需要具有相同的类型
company_list = ["百度", "谷歌", "微软", "华为", "腾讯"]
car_price = [28, 34.7, 54, 108]
print("***********定义列表*******************")
print(company_list)
print(car_price)

# 2.访问列表元素
print("第2个元素:", company_list[1])
print("第2个到第4个元素:", company_list[1:4])

# 3.更新列表元素
company_list[2] = "小米"  # 修改元素
print(company_list)

# 4.添加新元素
company_list.append("招商银行")
print(company_list)

# 5.删除元素,列表
del company_list[0]
print(company_list)
# del car_price
# print(car_price)

"""
二、Python列表脚本操作符
    列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
"""
# 1.列表长度
size = len(company_list)
print("列表长度: %d" % size)

# 2.列表相加
new_list = company_list + car_price
print("相加后的列表: %s" % new_list)

# 3.列表重复
car_list = ["奥迪", "奔驰", "宝马", "丰田", "长安", "东风"]
new_cars = car_list * 4
print(car_list)
print(new_cars)

# 4.是否在列表中
if ("奔驰" in car_list):
    print("奔驰在列表中...")

if ("特斯拉" not in car_list):
    print("特斯拉不在列表中...")

# 5.遍历列表
print("遍历列表:")
for car in car_list:
    print(car)

# 6.获取列表元素
print("列表第2个元素:%s" % car_list[1])
print("列表倒数第2个元素:%s" % car_list[-2])
print("从第二个元素开始后的所有元素:%s" % car_list[1:])
print("从第二个元素开始后的到倒数第2元素:%s" % car_list[1:-1])

# 7.嵌套列表
cars = ["奥迪", "奔驰", "宝马", "丰田", "长安", "东风"]
prices = [22, 35.7, 44, 8, 9]
new_list = [cars, prices]
print("嵌套后的列表:%s" % new_list)

"""
二、Python列表函数&方法
    函数
        len(list) 列表元素个数
        max(list) 返回列表元素最大值
        min(list) 返回列表元素最小值
        list(seq) 将元组转换为列表 
        list.append(obj) 在列表末尾添加新的对象
        list.count(obj) 统计某个元素在列表中出现的次数
        list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
        list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
        list.insert(index, obj) 将对象插入列表
        list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        list.remove(obj) 移除列表中某个值的第一个匹配项
        list.reverse() 反向列表中元素
        list.sort( key=None, reverse=False) 对原列表进行排序
        list.clear() 清空列表
        list.copy() 复制列表
"""
# 列表
flowers = ["月季花", "水仙花", "玫瑰花", "水仙花", "桃花", "茉莉花"]

# 元组
citys = ("深圳", "广州", "武汉", "大连")

# 列表大小
print("flowers列表的大小: %d" % len(flowers))
print("flowers列表的最大值: %s" % max(flowers))
print("flowers列表的最小值: %s" % min(flowers))

# 元组转换为列表
print("元组citys: ", citys)
print("将city元组转换为列表: ", list(citys))

# 添加列表元素
flowers.append("百合花")
print(flowers)
flowers.insert(2, "海棠花")
print(flowers)
flowers.extend(citys)
print(flowers)

# 元素出现次数
print("水仙花出现次数:", flowers.count("水仙花"))

# 获取元素的索引位置
index = flowers.index("玫瑰花")
print("玫瑰花的索引位置是:%d" % index)

# 移除最后一个元素
flower = flowers.pop()
print("移除最后一个元素:%s" % flower)
print(flowers)
flower2 = flowers.pop(1)
print("移除第2个元素:%s" % flower2)

print("*" * 30)
flowers.remove("桃花")  # 移除桃花
print(flowers)

# 反向列表中元素
flowers.reverse()
print(flowers)

# 对原列表进行排序
flowers.sort(reverse=True)
print("降序:", flowers)

flowers.sort(reverse=False)
print("升序:", flowers)

# 拷贝列表
coyp_cars = cars.copy()
print(coyp_cars)

# 清空列表
cars.clear()
print("清空列表cars后:", cars)
