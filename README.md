 DDTool
 PDF就是截取PDF的，截图就是截图的，整合就是可以整体调用的，其中的main.exe是可以不安装python直接用的，但是就是不能调整具体参数了，且容易报错
写这个代码的目的:做券商律师的尽调太累了TUT老眼昏花，一个项目接一个项目忙不过来，于是花了两天从头学了如何写代码，结合网上热心网友的分享憋出了一个代码续了狗命。但！只是方便截图，还是得一个个看才叫尽职调查呀……
功能:
1.自动归档：根据网站特性包括text.txt(搜索词）、number.txt（可能的代码比如身份证号、社会信用代码），根据text内容，按照搜索词逐一生成文件夹，根据选择自动截图或者截取pdf并按照设置格式重命名保存到对应文件夹，如XXX-百度搜索截图-1.jpg
2.截取保存：根据需要选择截图或者截取pdf，代码是分开的。截图可以后台静默操作，而截取pdf只能前台操作。
3.自定义设置:可以自行调整比如百度搜索的每页搜索结果、截取页数等。

简单说明代码的逻辑，方便大家根据实际情况调整内容。具体如百度等因为网站本身有特点，所以也有相应适配的代码，就不一一列举了，在这分享一些我踩过的坑。由于我也是野鸡学习法，所以懂代码的求轻喷...反正这个截图本身太快也容易报错，所以没把心思放在优化代码上。附件也有封装好的命令行的代码，但是日常会有bug，所以大家还是懂点代码吧~使用前请看以下代码注释，不然一定会有哪里报错，比如chromedriver的版本问题！
当时没觉得会分享，有很多代码用的网上分享的，如有侵权联系我吧QAQ
