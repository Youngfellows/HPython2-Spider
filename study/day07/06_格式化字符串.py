welcome = "welcome to \nchina ..."
print(str(welcome))

# 转义字符串中的特殊字符
print(repr(welcome))

print("公司名称:{},网站:{}".format("百度", "wwww.baidu.com"))
print("公司名称:{1},网站:{0}".format("百度", "wwww.baidu.com"))

print("**********指定字符串长度************")
import math

print("PI的近似值:{}".format(math.pi))
print("PI的近似值,保留3位小数:{0:.3f}".format(math.pi))
print("PI的近似值,保留3位小数:%.3f" % math.pi)

# 指定字符串长度
print("**********指定字符串长度************")
table = {"Google": 1, "Baidu": 2, "Tencent": 3, "Microsoft": 4}
for company, level in table.items():
    print("{0:10} ===> {1:10d}".format(company, level))
