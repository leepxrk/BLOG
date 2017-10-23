#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

# 餐厅列表
Restaurant_list = ["M记","KFC","TGF","BFJZG"];

# 确认餐厅列表
#Restaurant_1 = input("INPUT:")
#Restaurant_list.append(Restaurant_1);

#Restaurant_2 = input("INPUT:")
#Restaurant_list.append(Restaurant_2);

#Restaurant_3 = input("INPUT:")
#Restaurant_list.append(Restaurant_3);


# 定义随机选择餐厅区间

EatWhat_random = random.randint(0,len(Restaurant_list)-1)

# 输出选择结果
print Restaurant_list[EatWhat_random]




