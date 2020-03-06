# 定义类
class Persion:
    # 定义类属性
    name = ""
    age = 0

    # 定义私有属性
    __sex__ = ""
    __weight__ = 0

    # 构造函数
    def __init__(self, name, age, sex, weight):
        self.name = name
        self.age = age
        self.__sex__ = sex
        self.__weight__ = weight

    # 定义方法
    def speak(self):
        print("{0}说,我今年{1}岁,我的性别是{2},我的体重是{3}斤".format(self.name, self.age, self.__sex__, self.__weight__))


# 测试代码
if __name__ == "__main__":
    # 实例化类-创建对象
    laowang = Persion("老王", 35, "男", 128)
    laowang.speak()
