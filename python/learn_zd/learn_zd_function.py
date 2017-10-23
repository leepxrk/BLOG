#!/usr/bin/python
# -*- coding: UTF-8 -*-

import copy

#clear 清除字典所有的项，该方法为原地操作，不返回值。。
#d = {}
#d['name'] = 'gumby'
#d['age'] = '42'
#print d

#copy 返回一个具有相同兼职的新字典（浅复制）;在副本替换值的时候，原始字典不受影响
x = {'user':'admin','machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print y
print x

#深复制 使用copy模块的deepcopy 进行复制
from copy import deepcopy
d = {}
d['names'] = ['Alfred','bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('clive')
print c
print dc


#fromkeys 使用给定的键建立新的字典，每个键都对应一个默认值none
#aa = {}.formkeys(['name','age'])
#print aa

#get 访问字典项的方法
