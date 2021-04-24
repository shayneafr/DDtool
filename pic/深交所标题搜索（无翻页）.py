from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

f = open("text1.txt", "r")
words = f.readlines()
f.close()

driver = webdriver.Chrome('D:\Anaconda3\Scripts\driver\chromedriver', chrome_options=chrome_options)
driver.maximize_window()
driver.get("http://www.szse.cn/application/search/index.html?keyword=")
time.sleep(2)
scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(scroll_width, scroll_height)
# 长截屏代码引自https://www.cnblogs.com/MasterMonkInTemple/p/9970512.html，张缤分
for word in words:
    word = word.strip('\n')
    try:
        File_Path = os.getcwd() + '\\' + word
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
            print("目录新建成功：%s" % File_Path)
        else:
            print("目录已存在")
    except BaseException as msg:
        print("新建目录失败：%s" % msg)
    # 新建目录代码引自https://www.cnblogs.com/hong-fithing/p/9656221.html
#    driver.switch_to.frame("DataList")
    elem = driver.find_element_by_xpath("//*[@id='search_form']/div/div[1]/div[2]/input")
    elem.clear()
    elem.send_keys(word)
    print(word,"正在截图……")
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    driver.set_window_size(scroll_width, scroll_height)
    try:
        url = driver.save_screenshot('.\\' + word + '\\' + word + '_深圳证券交易所标题搜索' + '.png')
        print("%s ：截图成功！" % url)
    except BaseException as pic_msg:
        print("截图失败：%s" % pic_msg)
driver.close()
