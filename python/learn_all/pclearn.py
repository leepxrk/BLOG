#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb,re,urllib2

url=raw_input("冒号后输入视频地址：")
content = urllib2.urlopen(url).read()

mp4ss = r'\bhttp\b.*\bmp4\b'
mp4 = re.search(mp4ss,content)
ywj = mp4.group()

jpg = re.search(r'\bhttp\b.*\bjpg\b',content)
slt = jpg.group()

#var pop_nickname  = 'Yuki酱丶';

vnamess = r'\var pop_nickname  = [*]\';'
vname = re.findall(vnamess,content)

glurl = re.findall(r'\http://www.aipai.com/c30\b.*\html\b',content)

s = r'\d{8}'
pzh = re.search(s,content)
bid = pzh.group()



print ywj
print slt
str_glurl = '\n'.join(glurl)
print str_glurl
print bid
print vname


#conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="19900807",db="python_pc")
#with conn:

#    cursor = conn.cursor()

#    cursor.execute ("insert into video_msg(id,video_url,mp4_url) values ('url+url','30018655','打酱油路过','1','2015-11-19')")
# cursor.execute(sql)

#row=cursor.fetchone()

#print row

#cursor.close()
#conn.close()
