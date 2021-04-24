from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import win32api
import win32con
import os

# torexe = os.popen(r'D:\Program Files\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
# PROXY = "socks5://localhost:9050" # IP:PORT or HOST:PORT

chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
# chrome_options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

f = open("text1.txt", "r")
words = f.readlines()
f.close()

driver = webdriver.Chrome(executable_path='D:\Anaconda3\Scripts\driver\chromedriver.exe',chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://www.qichacha.com/")
time.sleep(1)
driver.find_element_by_xpath("/html/body/header/div/ul/li[14]/a/span").click()
time.sleep(10)
# # driver.find_element_by_xpath("//*[@id='normalLogin']").click()
# lname = driver.find_element_by_id("nameNormal")
# lname.clear()
# lname.send_keys('13601098964')
# lpass = driver.find_element_by_id("pwdNormal")
# lname.clear()
# lpass.send_keys('haiwen20')
# source=driver.find_element_by_xpath("//*[@id='nc_5_n1z']")#需要滑动的元素
# action = ActionChains(driver)
# action.click_and_hold(source).perform()
# action.move_by_offset(308,0)#需要滑动的坐标
# action.release().perform() #释放鼠标
# driver.find_element_by_xpath("//*[@id='user_login_normal']/button").click()

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
    driver.get("https://www.qichacha.com/")
    time.sleep(1)
    elem = driver.find_element_by_id("searchkey")
    elem.clear()
    elem.send_keys(word)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
#    driver.switch_to_window(driver.window_handles[-1])
    driver.find_element_by_xpath("//*[@id='search-result']/tr[1]/td[3]/a").click()
    time.sleep(1)
#    driver.switch_to_window(driver.window_handles[-1])
    driver.find_element_by_xpath("//*[@id='company-top]/div[3]/div[2]/a[3]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='reportModal']/div/div/div[2]/div/div/section[1]/div[4]/a").click()
    time.sleep(1)
    elem3 = driver.find_element_by_id("reportEmail")
    elem3.clear()
    elem3.send_keys('shayneafr@foxmail.com')
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[7]/a").click()
    time.sleep(1)
#    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
#    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
#    driver.set_window_size(scroll_width, scroll_height)
    # 长截屏代码引自https://www.cnblogs.com/MasterMonkInTemple/p/9970512.html，张缤分
    print("{}下载请求已提交！".format(word))
driver.close()
