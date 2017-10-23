#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb,re,urllib2,string

#格式化字符串
formal = 'hello.%s. %s enough for ya'
values = ('world','hot')
print formal % values

#字符串常量
print string.digits   #包含数字1～9的字符串
