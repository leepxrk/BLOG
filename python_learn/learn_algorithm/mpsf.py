#!/usr/bin/python
# -*- coding: UTF-8 -*-
#比较相邻的元素。如果第一个比第二个大，就交换他们两个。
#对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
#针对所有的元素重复以上的步骤，除了最后一个。
#持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

def bubble(l):
    flag = True
    for i in range(len(l)-1, 0, -1):
        if flag:
            flag = False
            for j in range(i):
                if l[j] > l[j + 1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    flag = True
        else:
            break
    print l

li = [44,1,45,33,4,3,67,32,56,78,12,23,34,26,27]
bubble(li)
