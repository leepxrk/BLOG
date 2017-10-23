#!/usr/bin/python
# -*- coding: UTF-8 -*-

#判断成员资格
#判断输入的用户名或者密码是否在数据库中/列表
#用户判断用户登录名与密码是否正确
#可以作为通用方法进行判断
#列表内容可以从数据库中获取
permissions = 'rw'
print 'w' in permissions
print 'a' in permissions

users = ['aaa','bbb','ccc']
print raw_input('enter your name:') in users

databases = [['aaa','bbb'],['aa','bb'],['a','b'],['aaaa','bbbb']]
user_name = raw_input('user name :')
pin = raw_input('pin code:')

if [user_name,pin] in databases:
    print 'access granted'

【TME平台】您的校验码为：746732，工作人员不会向您索取，请勿泄露。

【TME平台】您的校验码为：746732，请勿泄露。如非本人操作请忽略此短信。