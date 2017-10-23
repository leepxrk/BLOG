import re
import urllib2
url=raw_input("冒号后输入视频地址：")

#处理PC视频
if urllist[7:10]==['w','w','w']:
    urllist[7:10]=['m']
    url="".join(urllist)
#处理手游地址
if  urllist[7:14]==['s', 'h', 'o', 'u', 'y', 'o', 'u']:
    urllist[7:14]=['m']
    url="".join(urllist)

content=urllib2.urlopen(url).read()
m=re.mp4(r'\bhttp\b.*\bmp4\b',content)
m=re.jpg(r'\bhttp\b.*\bjpg\b',content)
ywj=m.group(0)
slt=m.group(0)
print ywj
print slt

