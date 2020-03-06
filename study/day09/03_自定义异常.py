# 自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        # 自定义异常打印
        return repr(self.value)


if __name__ == "__main__":
    try:
        raise MyError(2 * 3)
    except MyError as e:
        print("异常信息是:{}".format(e.value))
