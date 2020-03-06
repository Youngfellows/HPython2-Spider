age = 17

# 1.条件控制if/else
if age > 18:
    print("年龄大于18岁...")
else:
    print("年龄不大于18岁...")

# 多重判断
height = 170
if age > 18:
    print("年龄大于18岁...")
elif height > 160:
    print("升高大于160")
else:
    pass

"""
如果年龄小于18表示为童工，不合法
如果18-60岁之间，为合法工作年龄
如果年龄大于60，为退休年龄
"""
age = int(input("请输入年龄:"))
if age < 18:
    print(f"年龄{age},为童工,不合法")
elif (age >= 18) and (age <= 60):
    print("如果18-60岁之间，为合法工作年龄")
else:
    print(f"年龄为{age},为退休年纪...")
    pass

