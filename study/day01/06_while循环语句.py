# 1.while循环语义
index = 1
while (index <= 10):
    print("循环打印第%d" % index)
    index += 1

# 2.break/continue
# break:终止循环，包括while，for
# continue:终止当前一次循环，还会执行下一次循环,包括（while,for）
index = 1
while index < 100:
    print("***打印第%d次" % index)
    if index == 50:
        print("index==%d,跳出循环" % index)
        break
    index += 1

index = 1
while index < 10:
    print("+++++打印第%d次++++" % index)
    if index == 6:
        print("index==%d,结束本次循环,继续下次循环..." % index)
        index += 1
        continue
    index += 1

# 3.while嵌套
# 99乘法表
print("\n***************99乘法表*************")
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}x{i}={i * j}", end="\t")
        j += 1
    i += 1
    print("")

# 4.while / else
# else里面的代码是在循环执行完毕之后在执行.
# 注意：如果是break终止循环是不会执行的

index = 1
while index <= 10:
    print("+++++打印第%d次++++" % index)
    index += 1
else:
    print("10此循环打印完成后执行的代码...")

index = 1
while index <= 10:
    print("ssssss打印第%d次++++" % index)
    if index == 5:
        print("index=5,结束循环...,不会到else语句...")
        break
    index += 1
else:
    print("10此循环打印完成后执行的代码...")
