#!/usr/bin/python
# -*- coding: UTF-8 -*-


x = input("请输入年份：")

y = x % 4

if y == 0:
    print `x` + ("年是闰年")
else:
    print `x` + ("年不是闰年")
