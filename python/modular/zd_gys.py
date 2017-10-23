#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random,MySQLdb,sys

# 定义一个函数
def zd_gys(x, y):
   """该函数返回两个数的最大公约数"""

   # 获取最小值
   if x > y:
       smaller = x
   else:
       smaller = y

   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           zd_gys = i

   return zd_gys


# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print zd_gys(num1, num2)
