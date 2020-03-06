# 1.for循环
str = "hello python"
for s in str:
    print(s)

# 2.while/else
# else里面的代码是在循环执行完毕之后在执行.
# 注意：如果是break终止循环是不会执行的
# for/else循环和while/else循环是一模一样的
for s in str:
    print(s)
else:
    print("for循环执行完成后的")
