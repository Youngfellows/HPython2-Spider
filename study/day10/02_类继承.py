# 定义类
class Persion:
    # 定义公有属性
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


# 继承
class Doctor(Persion):
    # 定义特有属性
    hospital = ""

    # 重写构造
    def __init__(self, name, age, sex, weight, hospital):
        # 调用父类的构造
        Persion.__init__(self, name, age, sex, weight)
        self.hospital = hospital

    # 定义方法
    def job(self):
        print("我是{0},我是一名{1}医生,我来自{2},我的工作是救人....".format(self.name, self.__sex__, self.hospital))

        # 调用私有方法
        self.__hobby()

    # 重写父类的方法
    def speak(self):
        print("我是{0},是一名医生,我来自{1},大家赶快带上自己的口罩,不要被病毒感染了...".format(self.name, self.hospital))

    # 定义私有方法
    def __hobby(self):
        print("我是{}医生,我的爱好是看电影".format(self.name))


# 测试代码
if __name__ == "__main__":
    # 实例化类-创建对象
    wenliang = Doctor("文亮", 35, "男", 120, "武汉中心医院")
    wenliang.job()
    wenliang.speak()
