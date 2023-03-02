# coding=utf-8
import requests
from bs4 import BeautifulSoup
import xlwt
import random
import traceback
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def request_douban(url):
    try:
        ua_list = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36'
        ]
        user_agent = random.choice(ua_list)
        headers = {'User-Agent': user_agent,
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
                   }
        response = requests.get(url=url, headers=headers, verify=False)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print e
        traceback.print_exc()
        return None


book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '图片')
sheet.write(0, 2, '排名')
sheet.write(0, 3, '评分')
sheet.write(0, 4, '作者')
sheet.write(0, 5, '简介')

n = 1


def save_to_excel(soup):
    list = soup.find(class_='grid_view').find_all('li')

    for item in list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        if (item.find(class_='inq') != None):
            item_intr = item.find(class_='inq').string

        # print('爬取电影：' + item_index + ' | ' + item_name +' | ' + item_img +' | ' + item_score +' | ' + item_author +' | ' + item_intr )
        print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)

        global n

        sheet.write(n, 0, item_name)
        sheet.write(n, 1, item_img)
        sheet.write(n, 2, item_index)
        sheet.write(n, 3, item_score)
        sheet.write(n, 4, item_author)
        sheet.write(n, 5, item_intr)

        n = n + 1


def main(page):
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    print("url = {}".format(url))
    html = request_douban(url)

    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings()  # 去除警告
    for i in range(0, 10):
        main(i)
        print("\n************************************************************************")
book.save(u'豆瓣最受欢迎的250部电影.xlsx')
