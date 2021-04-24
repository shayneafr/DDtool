from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

f = open("text.txt", "r")
words = f.readlines()
f.close()

driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://www.baidu.com/")
time.sleep(2)
# ActionChains(driver).move_to_element(driver.find_element_by_link_text(u'设置')).perform()
# time.sleep(1)
# driver.find_element_by_class_name('setpref').click()
# time.sleep(2)
# Select(driver.find_element_by_name('NR')).select_by_value('20')
# driver.find_element_by_class_name('prefpanelgo').click()
# driver.switch_to.alert.accept()
# ActionChains(driver).send_keys(Keys.ENTER).perform()

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
    elem = driver.find_element_by_id("kw")
    elem.clear()
    elem.send_keys(word)
    driver.find_element_by_id('su').click()
    time.sleep(2)
    for i in range(1, 4):
        print(word, "正在截图……")
#    elem.send_keys(Keys.RETURN)
#    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#    driver.set_window_size(scroll_width, scroll_height)
        scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(scroll_width, scroll_height)
        try:
            url = driver.save_screenshot('.\\' + word + '\\' + word + '_百度' + str(i) + '.png')
            print("%s ：截图成功！" % url)
        except BaseException as pic_msg:
            print("截图失败：%s" % pic_msg)
        try:
            driver.find_elements_by_class_name('n').pop(-1).click()
        except BaseException:
            break
        time.sleep(2)

driver.close()
