# -*- coding:utf-8 -*-
"""
案例_(单线程)使用xpath爬取糗事百科
步骤如下:
    首先通过xpath插件找出我们要爬取的信息的匹配规则
    url = "https://www.qiushibaike.com/8hr/page/1/"
    xpath插件的模糊查询:contains(),第一个参数是要匹配的标签,第二个参数是这个标签的部分内容
    1.//div[contains(@id,"qiushi_tag_")] 匹配出所有段子包括评论,点赞数  以此作为根节点
    2.用户名://div[contains(@id,"qiushi_tag_")]/div[@class="author clearfix"]//h2
    3.内容://div[contains(@id,"qiushi_tag_")]//div[@class="content"]/span
    4.点赞数://div[contains(@id,"qiushi_tag_")]//span[@class="stats-vote"]/i
    5.评论数://div[contains(@id,"qiushi_tag_")]//span[@class="stats-comments"]//i
    6.图片链接://div[contains(@id,"qiushi_tag_")]//div[@class="thumb"]//@src
"""

# from urllib.request import *
import urllib2
import time
from lxml import etree


class Spider(object):
    def __init__(self):
        # 定义一个空列表装所有信息
        self.__info = []

        # 定义一个字典保存每条段子的信息
        self.__item = {}

        # 用户输入开始页面和结束页面
        self.__start_page = int(input("请输入开始爬取的页面:"))
        self.__end_page = int(input("请输入结束爬取的页面:"))

        self.__header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36"}

    def __load_page(self, url):
        """构建request请求,并发起请求"""
        request = urllib2.Request(url, headers=self.__header)

        # 发送请求获取html源码
        # response 为<class 'http.client.HTTPResponse'>对象
        # response.read()  为<class 'bytes'>对象
        # response.read().decode() 为字符串对象
        response = urllib2.urlopen(request)
        # html = response.read().decode()
        html = response.read()

        # 调用方法使用xpath获取信息
        return html

    def __xpath_get_info(self, html):
        """将HTML字符串解析为HTML DOM格式,并获取相关信息"""
        selector = etree.HTML(html)

        # 返回所有段子的节点位置,contant()模糊查询方法,第一个参数是要匹配的标签,第二个参数是这个标签的部分内容
        # 每个节点包括一条完整的段子(用户名,段子内容,点赞,评论等)
        node_list = selector.xpath('//div[contains(@id,"qiushi_tag_")]')

        for node in node_list:
            # 爬取所有用户名信息
            # 取出标签里的内容,使用.text方法
            user_name = node.xpath('./div[@class="author clearfix"]//h2')[0].text

            # 爬取段子内容,匹配规则必须加点  不然还是会从整个页面开始匹配
            # 注意:如果span标签中有br 在插件中没问题,在代码中会把br也弄进来
            duanzi_info = node.xpath('.//div[@class="content"]/span')[0].text.strip()

            # 爬取段子的点赞数
            vote_num = node.xpath('.//span[@class="stats-vote"]/i')[0].text

            # 爬取评论数
            comment_num = node.xpath('.//span[@class="stats-comments"]//i')[0].text

            # 爬取图片链接
            # 属性src的值,所以不需要.text
            img_url = node.xpath('.//div[@class="thumb"]//@src')
            if len(img_url) > 0:
                img_url = img_url[0]
            else:
                img_url = "无图片"

            self.__save_info(user_name, duanzi_info, vote_num, comment_num, img_url)

    def __save_info(self, user_name, duanzi_info, vote_num, comment_num, img_url):
        """把每条段子的相关信息写进字典"""
        item = {
            "username": user_name,
            "content": duanzi_info,
            "zan": vote_num,
            "comment": comment_num,
            "image_url": img_url
        }
        self.__info.append(item)

    def show_result(self):
        """展示爬取的结果"""
        for info in self.__info:
            print(info)

    def run(self):
        """启动爬虫程序"""
        for page in range(self.__start_page, self.__end_page + 1):
            url = "https://www.qiushibaike.com/8hr/page/" + str(page)
            html = self.__load_page(url)

            # 爬取一页休眠一秒,应对反爬策略
            # time.sleep(1)
            self.__xpath_get_info(html)


if __name__ == '__main__':
    qiushi_spider = Spider()
    qiushi_spider.run()
    qiushi_spider.show_result()
