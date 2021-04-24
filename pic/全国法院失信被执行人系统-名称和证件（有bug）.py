from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

f = open("texta.txt", "r")
words = f.readlines()
f.close()
f1 = open("textb.txt", "r")
numbers = f1.readlines()
f1.close()

driver = webdriver.Chrome('D:\Anaconda3\Scripts\driver\chromedriver', chrome_options=chrome_options)
driver.maximize_window()
driver.get("http://zxgk.court.gov.cn/shixin/")
time.sleep(2)
scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(scroll_width, scroll_height)
# 长截屏代码引自https://www.cnblogs.com/MasterMonkInTemple/p/9970512.html，张缤分
for word, number in zip(words, numbers):
    word = word.strip('\n')
    number = number.strip('\n')
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
    elem = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("pName"))
    elem.clear()
    elem.send_keys(word)
    elem2 = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("pCardNum"))
    elem2.clear()
    elem2.send_keys(number)
    captcha_elem = driver.find_element_by_id("yzm")
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "yzm"))).click()
    captcha_element = driver.find_element_by_id('captchaImg')
    location = captcha_element.location
    size = captcha_element.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    pic = get_pic(driver)
    image = pic.crop((left, top, right, bottom))
    image.save('验证码.png')
    captcha_elem.clear()
    captcha_elem.send_keys(input("请输入验证码："))
    print(word,"正在截图……")
#    elem.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn-zxgk btn-block ']"))).click()
    time.sleep(2)
#    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#    driver.set_window_size(scroll_width, scroll_height)
    try:
        url = driver.save_screenshot('.\\' + word + '\\' + word + '_全国法院失信被执行人系统' + '.png')
        print("%s ：截图成功！" % url)
    except BaseException as pic_msg:
        print("截图失败：%s" % pic_msg)
driver.close()
