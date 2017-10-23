#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

# 随机插入一些整数至序列内，并从大到小排列
hardExam = [45,72,36,654,63,653]
newRandom = random.randint(0,9999)
countLenHardExam = len(hardExam)

while countLenHardExam < 10:
    hardExam.insert(0,newRandom)
    countLenHardExam = len(hardExam)

# hardExam.sort()
print hardExam


# 从列表内计算出某个值是那两个数值的积




n = hardExam
m = hardExam

x = 0
y = 1



while n[x] * 654 == 23544:
    x = x+1
    del n[0]
    print n[0]
    print x


#    if len(n) < len(hardExam):
#        n.append(x)
#        x = x + 1
#        print n








#print hardExam[answerA]
#print hardExam[answerB]

#print hardExam[0]
#print hardExam



>

