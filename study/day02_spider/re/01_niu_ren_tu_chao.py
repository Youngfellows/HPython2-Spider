# coding=utf-8
import urllib2
import random
from lxml import etree


# 牛人吐槽段子
class Spider:

    # 构造函数
    def __init__(self):
        # 初始化起始页位置
        self.page = 1
        # 爬取开关，如果为True继续爬取
        self.switch = True
        # 保存爬取信息
        self.duanzi_list = []

    # 加载页面
    def loadPage(self):
        """
            作用：下载页面
        """
        print("正在下载数据...")
        url = "http://www.bullpeople.cn/"

        # 可以是User-Agent列表，也可以是代理列表
        ua_list = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        ]

        # 在User-Agent列表里随机选择一个User-Agent
        user_agent = random.choice(ua_list)

        # 构造一个请求
        request = urllib2.Request(url)

        # add_header()方法 添加/修改 一个HTTP报头
        request.add_header("User-Agent", user_agent)

        # 向指定的url地址发送请求，并返回服务器响应的类文件对象
        response = urllib2.urlopen(request)

        # 服务器返回的类文件对象支持Python文件对象的操作方法
        # read()方法就是读取文件里的全部内容，返回字符串
        html = response.read().decode("utf-8")
        # print(html)

        # 解析
        dom_tree = etree.HTML(html)

        # 取出帖子里段子的内容
        title_list = dom_tree.xpath('//div[@id="conbody"]//li/a[@class="tc"]/@title')  # title标题
        content_list = dom_tree.xpath('//div[@id="conbody"]//a[@class="tc"]')  # 内容
        comment_list = dom_tree.xpath('//div[@id="conbody"]//div[@class="clickSwiper pleft8"]/a')  # 评论
        start_list = dom_tree.xpath('//div[@id="conbody"]//span[@class="cursor"]/span')  # 赞

        # 标题列表
        for title in title_list:
            print ("title: %s" % title)

        # 内容列表
        for index in range(len(content_list)):
            # links[index]返回的是一个字典
            if (index % 2) == 0:
                # print(content_list[index].tag)
                # print(content_list[index].attrib)

                duanzi_item = {}  # 每一条段子
                content = content_list[index].text
                star = start_list[index].text
                duanzi_item["content"] = content
                duanzi_item["star"] = star
                self.duanzi_list.append(duanzi_item)  # 添加到列表

                print(content)
                print(star)

        # 评论列表
        # for index in range(len(comment_list)):
        #     if (index % 2) == 0:
        #         print(comment_list[index].tag)
        #         print(comment_list[index].attrib)
        #         print(comment_list[index].text)

        # 赞列表
        # for index in range(len(start_list)):
        #     # links[index]返回的是一个字典
        #     if (index % 2) == 0:
        #         # print(start_list[index].tag)
        #         # print(start_list[index].attrib)
        #         print(start_list[index].text)

    def dealPage(self, content_list):
        """
            处理每页的段子
            content_list : 每页的段子列表集合
        """

    def writePage(self):
        """
            把每条段子逐个写入文件里
            item: 处理后的每条段子
        """
        with open("./json/duanzi.txt", "wb") as f:
            f.write(str(self.duanzi_list))

    def startWork(self):
        """
             控制爬虫运行
        """
        # 循环执行，直到 self.switch == False
        while self.switch:
            # 用户确定爬取的次数
            self.loadPage()
            command = raw_input("如果继续爬取，请按回车（退出输入quit)")
            if command == "quit":
                # 如果停止爬取，则输入 quit
                self.switch = False
            # 每次循环，page页码自增1
            self.page += 1

        # 保存文件
        self.writePage()

        print("谢谢使用!")
        print("爬取结果: {}".format(self.duanzi_list))
        print("爬取结果: size = {}".format(len(self.duanzi_list)))


# 启动爬虫
if __name__ == "__main__":
    duanziSpider = Spider()
    duanziSpider.startWork()
