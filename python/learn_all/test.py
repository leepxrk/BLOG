import re                                         #导入正则表达式模块
import urllib2                                    #导入URL模块，可提供获得源码
url=raw_input("冒号后输入视频地址：")       #输入网址数据
urllist=list(url)

#处理PC视频
if urllist[7:10]==['w','w','w']:
    urllist[7:10]=['m']
    url="".join(urllist)
#处理手游地址
if  urllist[7:14]==['s', 'h', 'o', 'u', 'y', 'o', 'u']:
    urllist[7:14]=['m']
    url="".join(urllist)

content=urllib2.urlopen(url).read()               #获得网站源码
m=re.search(r'\bhttp\b.*\bmp4\b',content)         #在源码中寻找视频地址
a=m.group(0)                                      #调用方法获得符合条件的字符串
print a                                           #打印该视频地址

