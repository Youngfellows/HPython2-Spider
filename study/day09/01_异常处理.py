# 1.捕获异常

while True:
    try:
        number = int(input("请输入一个数字:"))
        print("你输入的是:%d" % number)
    except ValueError:
        print("您输入的不是数字,请从新输入!")
    else:
        print("没有发生异常执行的代码")
        break
    finally:
        print("有没有发生异常都会执行...")
