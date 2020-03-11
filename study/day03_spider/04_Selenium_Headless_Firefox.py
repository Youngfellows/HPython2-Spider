# encoding=utf-8

"""
使用无界面浏览器
Selenium+Headless Firefox
Selenium+Headless Firefox和Selenium+Firefox，区别就是实例option的时候设置-headless参数。

前提条件：
- 本地安装Firefox浏览器
- 本地需要geckodriver驱动器文件，如果不配置环境变量的话，需要手动指定executable_path参数。

示例代码：
"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def main():
    options = Options()
    options.add_argument('-headless')
    driver = Firefox(
        executable_path='/mnt/samba/share/Selenium_PhantomJS_Driver/Firefox_geckodriver/geckodriver/geckodriver',
        firefox_options=options)
    driver.get("https://www.qiushibaike.com/8hr/page/1/")
    print(driver.page_source)
    driver.close()

    # 退出
    driver.quit()


if __name__ == '__main__':
    main()
