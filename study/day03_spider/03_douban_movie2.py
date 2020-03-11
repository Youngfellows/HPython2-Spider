# coding=utf-8
import time
# selenium 高版本版本是
# 导入webdriver API对象，可以调用浏览器和操作页面
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

# 豆瓣电影分类排行榜 - 剧情片
url = "https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action="

# 使用无界面浏览器 Selenium+Headless,本地安装Firefox
options = Options()
options.add_argument('-headless')
driver = Firefox(
    executable_path='/mnt/samba/share/Selenium_PhantomJS_Driver/Firefox_geckodriver/geckodriver/geckodriver',
    firefox_options=options)
driver.get(url)
html = driver.page_source

print(html)

# 休眠3秒
time.sleep(3)
# 向下滚动10000像素
js = "document.body.scrollTop=10000"
# js="var q=document.documentElement.scrollTop=10000"

# 查看页面快照
driver.save_screenshot("./screenshot/firefox_douban.png")

# 执行JS语句
driver.execute_script(js)
time.sleep(10)

# 查看页面快照
driver.save_screenshot("./screenshot/firefox_newdouban.png")

# 退出
driver.quit()
