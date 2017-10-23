#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys,string

people = {
    'alice':{
        'phone':'2345',
        'addr':'foo drive 23'
    },
    'beth':{
        'phone':'1357',
        'addr':'bar drive 42'
    },
    'cecil':{
        'phone':'2345',
        'addr':'foo drive 23'
    }
}
#针对电话号码的描述
laber = {
    'phone':'phone number',
    'addr':'address'
}
name = raw_input('请输入名字啊：')

#判断查找电话号码还是地址
request = raw_input('phone number(p) or address(a)?')

#使用正确的键
if request == 'p':
    key = 'phone'

if request == 'a':
    key = 'addr'


#如果名字在字典中则打印正确的信息
if name in people:
    print "%s's %s is %s," %(name,laber[key],people[name][key])
