"""
一、列表
    Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能。

    以下是 Python 中列表的方法：
    方法	描述
    list.append(x)	    把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
    list.extend(L)	    通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
    list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
    list.remove(x)	    删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
    list.pop([i])	    从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
    list.clear()	    移除列表中的所有项，等于del a[:]。
    list.index(x)	    返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
    list.count(x)	    返回 x 在列表中出现的次数。
    list.sort()	        对列表中的元素进行排序。
    list.reverse()	    倒排列表中的元素。
    list.copy()	        返回列表的浅复制，等于a[:]。
"""

# 1.将列表当做堆栈使用
stack = [1, 2, 3, 4, 5, 6]

# 弹栈
# print(stack.pop())
# print(stack)

print(stack)
while len(stack) != 0:
    print("弹出: ", stack.pop())
    print(stack)

print("*" * 30)

"""
二、将列表当作队列使用
    也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；
    但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，
    然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
"""
print("***********将列表当作队列使用****************")
from collections import deque

citys = ["北京", "成都", "武汉", "大连"]
queue = deque(citys)
print(type(queue))
print(queue)

# 添加队列元素
queue.append("深圳")
queue.appendleft("广州")
print(queue)

# 取出队列元素
print("取出队列左边元素:%s" % queue.popleft())
print("取出队列左边元素:%s" % queue.popleft())
print("取出队列左边元素:%s" % queue.popleft())
print(queue)
print("取出队列右边元素:%s" % queue.pop())
print(queue)

"""
三、列表推导式
    每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。
    返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。
    如果希望表达式推导出一个元组，就必须使用括号。
"""
print("*************列表推导式***************")
test_list1 = [2, 4, 6, 8]
result_list1 = [3 * x for x in test_list1]
print(result_list1)

result_list2 = [[x, x * 2] for x in test_list1]
print(result_list2)

# 对序列里每一个元素逐个调用某方法
fruits = ["apple        ", "             banana", "  orange   ", "       pear  "]
new_fruits = [fruit.strip() for fruit in fruits]
print(fruits)
print(new_fruits)

# 用 if 子句作为过滤器
test_list2 = [1, 21, 5, 7, 9, 11, 22, 6, 12, 4, 35, 49]
result_list3 = [x * 2 for x in test_list2 if x > 10]
print(result_list3)
