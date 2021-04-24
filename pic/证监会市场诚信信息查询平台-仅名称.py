from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import os

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

def get_pic(driver):  # 对目标网页进行截屏。这里截的是全屏
    driver.save_screenshot('pic.png')
    #  打开一个图片文件
    pic = Image.open('pic.png')
    #  返回图片对象
    return pic
# 引自https://github.com/cwsdrogo/Code_screenshot_by_Selenium

f = open("text.txt", "r")
words = f.readlines()
f.close()

driver = webdriver.Chrome('D:\Anaconda3\Scripts\driver\chromedriver', chrome_options=chrome_options)
driver.maximize_window()
driver.get("http://neris.csrc.gov.cn/shixinchaxun/")
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
    captcha_element = driver.find_element_by_id('captcha_img')
    location = captcha_element.location
    size = captcha_element.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    pic = get_pic(driver)
    image = pic.crop((left, top, right, bottom))
    image.save('验证码.png')
#    driver.switch_to.frame("DataList")
    elem = driver.find_element_by_id("objName")
    elem.clear()
    elem.send_keys(word)
    captcha_elem = driver.find_element_by_id("ycode")
    captcha_elem.clear()
    captcha_elem.send_keys(input("请输入验证码："))
    print(word,"正在截图……")
#    elem.send_keys(Keys.RETURN)
    driver.find_element_by_id('querybtn').click()
    time.sleep(2)
#    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#    driver.set_window_size(scroll_width, scroll_height)
    try:
        url = driver.save_screenshot('.\\' + word + '\\' + word + '_证监会市场诚信信息查询平台' + '.png')
        print("%s ：截图成功！" % url)
    except BaseException as pic_msg:
        print("截图失败：%s" % pic_msg)
driver.close()
