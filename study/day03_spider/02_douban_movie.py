# coding=utf-8
import time
# selenium 的版本是 2.48.0
# 导入webdriver API对象，可以调用浏览器和操作页面
from selenium import webdriver
# 导入Keys，可以使用操作键盘、标签、鼠标
from selenium.webdriver.common.keys import Keys

# 豆瓣电影分类排行榜 - 剧情片
url = "https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action="

# 查un关键PhantomJS浏览器对象
# driver = webdriver.PhantomJS(executable_path=r"H:\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver = webdriver.PhantomJS(
    executable_path=r"/mnt/samba/share/Selenium_PhantomJS_Driver/phantomjs_Driver/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
# driver = webdriver.PhantomJS()
driver.get(url)

# 休眠3秒
time.sleep(3)

# 向下滚动10000像素
js = "document.body.scrollTop=10000"
# js="var q=document.documentElement.scrollTop=10000"

# 查看页面快照
driver.save_screenshot("./screenshot/douban.png")

# 执行JS语句
driver.execute_script(js)
time.sleep(10)

# 查看页面快照
driver.save_screenshot("./screenshot/newdouban.png")

# 退出
driver.quit()
