#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string

title = '         WHIT A MOO-MOO here here. and a moo-moo there         '
seq = [1,2,3,4,5]
sep = '+'
ssq = '1+2+3+4+5+6+7'
ssqq = '/use/usb/usa/uss'
ssqqq = 'user   the  default  '

#find 方法在一个较长的字符串中查找子字符串，返回子字符串最左侧的索引，无则返回-1
print title.find(here)

#join 字符串中非常重要的方法，是split方法的逆方法，用于连接序列中的元素
print seq.join(sep)

#lower  返回字符串的小写字母版
print title.lower()

#replace  返回某字符串的所有匹配项军备替换之后得到的字符串
print title.replace('moo','mee')

#split  join的逆方法，用于将字符串分割成序列
print ssq.split('+')
print ssqq.split('/')
print ssqqq.split()

#strip  返回去除两侧空格的字符串
print title.split()


#translate  该方法与replace方法类似，都是替换字符串中的某些部分
#translate仅仅替换单个字符，但是可以多处同时替换



#
