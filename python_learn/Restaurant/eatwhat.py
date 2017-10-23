#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

# 餐厅列表
Restaurant_list = ["M记","KFC","TGF","BFJZG"];

#Chioce_Change = Y  #input("选择是否需要修改列表[Y/N]")

#if Chioce_Change == 'y':
#    Restaurant_1 = input("INPUT:")
#    Restaurant_list.append(Restaurant_1);
#else if Chioce_Change == Y and Chioce_Change == ‘N':
#    Chioce_Change = input("请选择是否修改列表[Y/N]")
#else:
#break:


# 定义随机选择餐厅区间
EatWhat_random = random.randint(0,len(Restaurant_list)-1)

# 输出选择结果
print Restaurant_list[EatWhat_random]




