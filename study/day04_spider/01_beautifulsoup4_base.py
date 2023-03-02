# coding=utf-8
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf8')

html_doc = """

<html><head><title>学习python的正确姿势</title></head>
<body>
<p class="title"><b>小帅b的故事</b></p>

<p class="story">有一天，小帅b想给大家讲两个笑话
<a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
<a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
他问大家，想听长的还是短的？</p>

<p class="story">...</p>

"""


def main():
    soup = BeautifulSoup(html_doc, "lxml")
    # 获取标题的内容
    title = soup.title.string
    print title

    # 获取p标签里面的内容
    p_content = soup.p.string
    print p_content

    # 获取 title 的父级标签
    parent_title = soup.title.parent.name
    print parent_title

    print("*" * 60)

    # 获取第一个a标签的超链接和内容
    a_href = soup.a['href']
    a_content = str(soup.a.string)
    print("a_href: {}".format(a_href))
    print("type(a_content) = {}".format(type(a_content)))
    print("a_content: {}".format(a_content))

    # 获取所有超链接
    a_list = soup.find_all('a')
    # print("a_list = {}".format(a_list))
    for a in a_list:
        href = a['href']
        content = a.string
        print("href: {},content: {}".format(href, content))

    print("*" * 60)
    # 获取所有p标签
    p_list = soup.find_all('p')
    # print("p_list = {}".format(p_list))
    for p in p_list:
        print p

    print("********************* 获取所有p标签的子节点 *******************************")
    # 获取第一个p标签的b子节点,返回是一个列表
    p_contents = soup.p.contents
    print p_contents[0].string
    p_contents = soup.p.children
    for content in p_contents:
        print content.string

    print("********************** 获取属性class=story的p标签 *************************")
    # 获取属性class=story的p标签
    p_ele_2 = soup.find(name="p", attrs={"class": "story"})
    print(p_ele_2)
    print(p_ele_2.get_text())

    print("********************** 获取属性class=story的p标签的全部字节点 *************************")
    p_ele_2 = soup.find(name="p", attrs={"class": "story"})
    p2 = soup.find(name="p", class_="story")  # 找出p标签
    print(type(p2))
    print p2
    print p2.get_text()

    # 获取子节点
    # a_ele_list = p2.find_all(name="a")
    a_ele_list = p2.find_all(name="a", class_="sister")
    # a_ele_list = p2.find_all(name="a", attrs={"class": "sister"})

    print(a_ele_list)
    for a in a_ele_list:
        # print a.string + ":" + a["href"]
        print("{} : {}".format(a.string, a["href"]))

    # 获取 id 为 link2 的超链接
    # link2_href = soup.find(id='link2')
    # print link2_href

    # 获取网页中所有的内容
    # all_text = soup.get_text()
    # print all_text

    # 使用 select 方法
    # print(soup.select("title"))
    # print(soup.select("body a"))
    # print(soup.select("p > #link1"))


if __name__ == "__main__":
    main()
