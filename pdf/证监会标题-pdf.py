from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import win32api
import win32con
import os

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

f = open("text1.txt", "r")
words = f.readlines()
f.close()

driver = webdriver.Chrome(executable_path='D:\Anaconda3\Scripts\driver\chromedriver.exe',chrome_options=chrome_options)
driver.maximize_window()
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
    driver.get("http://www.csrc.gov.cn/pub/newsite/")
    time.sleep(1)
    elem = driver.find_element_by_id("schword")
    elem.clear()
    elem.send_keys(word)
#    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#    driver.set_window_size(scroll_width, scroll_height)
    # 长截屏代码引自https://www.cnblogs.com/MasterMonkInTemple/p/9970512.html，张缤分
    print(os.getcwd())
    try:
        currentpath = os.getcwd()
        asd = driver.find_element_by_xpath('/html/body/div/div/div[4]/div[1]/div[1]/div[1]')
        ActionChains(driver).context_click(asd).perform()
        time.sleep(1)
        win32api.keybd_event(80, 0, 0, 0)
        time.sleep(1)
        win32api.keybd_event(80, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)
        win32api.keybd_event(13, 0, 0, 0)
        time.sleep(1)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)
        #            url = driver.save_screenshot('.\\' + word + '\\' + word + '_百度' + str(i) + '.png')
        #          print("%s ：截图成功！" % url)
        file_path = "{}\{}\{}_{}.pdf".format(currentpath, word, word, "证监会标题搜索")
        os.system("{}\pdf.exe {}".format(currentpath, file_path))
        print("截取成功！")
    except BaseException as msg:
        print("截取失败：%s" % msg)
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
#    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#    driver.set_window_size(scroll_width, scroll_height)
    try:
        currentpath = os.getcwd()
        asd = driver.find_element_by_xpath('/html/body/div/div/div[4]/div[1]')
        ActionChains(driver).context_click(asd).perform()
        time.sleep(1)
        win32api.keybd_event(80, 0, 0, 0)
        time.sleep(1)
        win32api.keybd_event(80, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)
        win32api.keybd_event(13, 0, 0, 0)
        time.sleep(1)
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.5)
        #            url = driver.save_screenshot('.\\' + word + '\\' + word + '_百度' + str(i) + '.png')
        #          print("%s ：截图成功！" % url)
        file_path = "{}\{}\{}_{}.pdf".format(currentpath, word, word, "证监会搜索结果")
        os.system("{}\pdf.exe {}".format(currentpath, file_path))
        print("截取成功！")
    except BaseException as msg:
        print("截取失败：%s" % msg)
driver.close()
