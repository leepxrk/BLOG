#!/usr/bin/python
# -*- coding: UTF-8 -*-

#字典中，前面的字符串称为键，后面的字符串称为值，一项对应一个键与一个值
#键是唯一的，值可以不唯一

#dict 函数  建立字典
itemt = [('name','gumby'),('age','42'),('k','123'),('kk','456')]
d = dict(itemt)
print d
print d['kk']


#基本字典操作
a = d
print len(a)
print a['k']
a['k']=222
print a
del a['k']
print a
print len(a)
print 'kk' in a


#字典了列表的不同
#键类型
#自动添加
#成员资格
