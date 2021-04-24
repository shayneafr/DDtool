# DDTool
# PDF就是截取PDF的，截图就是截图的，整合就是可以整体调用的，其中的main.exe是可以不安装python直接用的，但是就是不能调整具体参数了，且容易报错
 写这个代码的目的:做券商律师的尽调太累了TUT老眼昏花，一个项目接一个项目忙不过来，于是花了两天从头学了如何写代码，结合网上热心网友的分享憋出了一个代码续了狗命。但！只是方便截图，还是得一个个看才叫尽职调查呀……
# 功能:
1.自动归档：根据网站特性包括text.txt(搜索词）、number.txt（可能的代码比如身份证号、社会信用代码），根据text内容，按照搜索词逐一生成文件夹，根据选择自动截图或者截取pdf并按照设置格式重命名保存到对应文件夹，如XXX-百度搜索截图-1.jpg
2.截取保存：根据需要选择截图或者截取pdf，代码是分开的。截图可以后台静默操作，而截取pdf只能前台操作。
3.自定义设置:可以自行调整比如百度搜索的每页搜索结果、截取页数等。

# 简单说明代码的逻辑，方便大家根据实际情况调整内容。
具体如百度等因为网站本身有特点，所以也有相应适配的代码，就不一一列举了，在这分享一些我踩过的坑。由于我也是野鸡学习法，所以懂代码的求轻喷...反正这个截图本身太快也容易报错，所以没把心思放在优化代码上。附件也有封装好的命令行的代码，但是日常会有bug，所以大家还是懂点代码吧~使用前请看以下代码注释，不然一定会有哪里报错，比如chromedriver的版本问题！
当时没觉得会分享，有很多代码用的网上分享的，如有侵权联系我吧QAQ
 ```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os  # 引入相应的库，不同网站可能不一样，比如有的需要有识别和截取验证码的库，有的比如百度需要有相应点选搜索设置模拟鼠标的库，要根据实际情况下载，用pip install

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')  # 这三行的作用是让chrome后台运行，实现后台截图，同时给老板打两份工~PDF的话不可以这样，因为PDF打印根据尽调要求是需要有日期的，所以现有的生成PDF的插件基本都不能用，我是模拟的鼠标逐一保存，所以只能前台。

f = open("text.txt", "r") # 读取text.txt的内容
words = f.readlines() # 逐行读取，所以txt得一行一个名字
f.close()
for word in words:
    word = word.strip('\n') #这 里是用上面的人名或者公司名逐一创建文件夹，有的券商这方面要求挺高的，比如十几个人名，十几个检索地址，那按照人名归档会方便一点。
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
    driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options) # 务必注意！chromedriver这个程序需要下载，和路径一致，比如这里就是放在这个执行的.py边上。不同chrome的对应程序版本不一样，一定要网上找对应的不然会报错。
    driver.maximize_window() # 后台放最大，好截图
    driver.get("http://www.csrc.gov.cn/pub/newsite/") # 具体访问的网址
    time.sleep(2) # 在此停顿两秒！政府机关的网站容易卡，数字可以自己改 
    elem = driver.find_element_by_id("schword") # 根据页面属性找到对应的搜索框啥的，其实更推荐用xpath路径，可以网上了解下，就是在F12调出控制台，用左上角的鼠标找到你想找的搜索框，然后看看控制台显示在哪里，右键可以复制xpath路径，把这里改成find_element_by_xpath，括号放你复制出来的路径。这样避免找不到这个所谓的id。id怎么找和xpath一样。
    elem.clear() # 清空搜索框的内容
    elem.send_keys(word) # 输入读取的txt文件中每行的人名、公司名
    print(os.getcwd()) #我忘了，好像是康康现在的路径，这样运行的时候好观察，可能是这个代码我调整了发现不需要删除了，有的复杂点的留着。可能没闪干净。
    elem.send_keys(Keys.RETURN) # 按下回车
    time.sleep(2)
    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth') # 读取网页宽度方便截全咯
    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight') # 读取网页长度方便截全咯
    driver.set_window_size(scroll_width, scroll_height) #根据读取到的长宽来设置屏幕大小好截图
    # 长截屏代码引自https://www.cnblogs.com/MasterMonkInTemple/p/9970512.html，张缤分
    try:
        url = driver.save_screenshot('.\\' + word + '\\' + word + '_证监会搜索界面' + '.png') # 调用截图功能截图，这里的意思是在这个py文件的边上对应的人名文件夹里截图命名，第一个\\是同一文件夹的意思，第一个word和\\是人名文件夹，第二个word和后面的文字是命名方式，意思是比如小明_证监会搜索界面.png的意思，可以自己改
        print("%s ：截图成功！！！" % url) # 反馈截图结果
    except BaseException as pic_msg:
        print("截图失败：%s" % pic_msg) # 反馈截图结果
    driver.close() # 关闭这个浏览器，如果放在这个位置就是每个人名关闭一次，因为实际如果不关闭我老是遇到各种bug还不如查一次关一次。如果要提高效率，这行顶格写。
 ```
