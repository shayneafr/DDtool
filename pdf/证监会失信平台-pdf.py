from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
# import pytesseract
import time
# from PIL import Image
import win32api
import win32con
import os

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

f = open("text1.txt", "r")
words = f.readlines()
f.close()

f2 = open("text2.txt", "r")
numbers = f2.readlines()
f2.close()

# tesseract_cmd = 'tesseract.exe'

# def get_pic(driver):  # 对目标网页进行截屏。这里截的是全屏
#     driver.save_screenshot('pic.png')
#     #  打开一个图片文件
#     pic = Image.open('pic.png')
#     #  返回图片对象
#     return pic

driver = webdriver.Chrome(executable_path='D:\Anaconda3\Scripts\driver\chromedriver.exe',chrome_options=chrome_options)
# driver.maximize_window()
driver.get("http://neris.csrc.gov.cn/shixinchaxun/")
time.sleep(2)
for word,number in zip(words, numbers):
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
    # captcha_element = driver.find_element_by_xpath('//*[@id="captcha_img"]')
    # location = captcha_element.location
    # size = captcha_element.size
    # left = location['x']
    # top = location['y']
    # right = left + captcha_element.size['width']
    # bottom = top + captcha_element.size['height']
    # left, top, right, bottom = int(left), int(top), int(right), int(bottom)
    # pic = get_pic(driver)
    # image = pic.crop((left, top, right, bottom))
    # image.save('验证码.png')
    #    driver.switch_to.frame("DataList")
    elem = driver.find_element_by_id("objName")
    elem.clear()
    elem.send_keys(word)
    elem2 = driver.find_element_by_id("realCardNumber")
    elem2.clear()
    elem2.send_keys(number)
    captcha_elem = driver.find_element_by_id("ycode")
    captcha_elem.clear()
    # im = Image.open('验证码.png')
    # imgry = im.convert('L')
    # imgry.save('验证码.png')
    # threshold = 140
    # table = []
    # for j in range(256):
    #     if j < threshold:
    #         table.append(0)
    #     else:
    #         table.append(1)
    # out = imgry.point(table, '1')
    # out.save('验证码.png')
    # recog = ''
    # recog = pytesseract.image_to_string(im)
    # recog = re.sub("\W", "", recog)
    # print("识别为{}".format(recog))
    captcha_elem.send_keys(input("验证码："))
    print(word, "正在截取……")
    #    elem.send_keys(Keys.RETURN)
    driver.find_element_by_id('querybtn').click()
    time.sleep(2)
#    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#    driver.set_window_size(scroll_width, scroll_height)
    # 长截屏代码引自https://www.cnblogs.com/MasterMonkInTemple/p/9970512.html，张缤分
    print(os.getcwd())
    try:
        currentpath = os.getcwd()
        asd = driver.find_element_by_xpath('//*[@id="objList_form"]/table/tbody/tr[4]/td/div/table[1]/tbody/tr/td[2]')
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
        file_path = "{}\{}\{}_{}.pdf".format(currentpath, word, word, "证监会市场诚信信息查询平台")
        os.system("{}\pdf.exe {}".format(currentpath, file_path))
        print("截取成功！")
    except BaseException as msg:
        print("截取失败：%s" % msg)
    time.sleep(1)
#    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#    driver.set_window_size(scroll_width, scroll_height)
driver.close()
