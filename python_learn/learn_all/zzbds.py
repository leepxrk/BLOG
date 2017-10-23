#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

s = r'abc'
a = re.findall(s,'abcaaabc')
print a

ss = 'rap,rop,rpp,rwp,rep'
rss = r'r[^aw]p'
b = re.findall(rss,ss)
print b

sss = '1874678593887363'
rsss = r'[0-9]'
c = re.findall(rsss,sss)
print c

ssss = [010-12345678,010-27487645]

rssss = r'^010-\d\d\d\d\d\d\d\d'
d = re.findall(rssss,ssss)
print d
