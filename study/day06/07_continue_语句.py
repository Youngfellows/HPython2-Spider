# break
print("**********1 break***********")
i = 0
while i < 10:
    print("i = %d" % i)
    if i == 5:
        print("结束while循环...")
        break
    i += 1

print("**********2 continue ***********")
i = 0
while i < 10:
    if i == 5:
        print("结束当前循环...")
        i += 1
        continue
    i += 1
    print("i = %d" % i)
