from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import os

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

f = open("text.txt", "r")
words = f.readlines()
f.close()


def isPresented(classname):
    try:
        element = driver.find_element_by_class_name(classname)
    except NoSuchElementException as e:
        return False
    else:
        return True

driver = webdriver.Chrome('D:\Anaconda3\Scripts\driver\chromedriver',chrome_options=chrome_options)
driver.maximize_window()
driver.get("http://www.12309.gov.cn/guestweb/s?siteCode=N000007720&searchWord=1")
time.sleep(8)

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
    elem = driver.find_element_by_id("allSearchWord")
    elem.clear()
    elem.send_keys(word)
    elem.send_keys(Keys.RETURN)
    for i in range(1, 6):
        print(word,"正在截图……")
        time.sleep(7)
        scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(scroll_width, scroll_height)
    #    长截屏代码引自https://www.cnblogs.com/MasterMonkInTemple/p/9970512.html，张缤分
        if i == 1:
            url = driver.save_screenshot('.\\' + word + '\\' + word + '_人民检察院案件信息公开网' + '.png')
        else:
            try:
                url = driver.save_screenshot('.\\' + word + '\\' + word + '_人民检察院案件信息公开网' + str(i) + '.png')
                print("%s ：截图成功！" % url)
            except BaseException as pic_msg:
                print("截图失败：%s" % pic_msg)
        if isPresented("next disabled") == False:
            try:
                driver.find_element_by_class_name("next").click()
            except BaseException:
                break
        else:
            break
        time.sleep(2)

driver.close()
