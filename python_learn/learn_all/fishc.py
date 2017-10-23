#!/usr/bin/python
# -*- coding: UTF-8 -*-

#定义变量
import random;

answer = random.randint(1,10)
#以下为变量赋值
temp = input('输入猜测的数据：')
guess = int(temp)
while guess != answer:
    if guess > answer:
        print('太大了')
        temp = input('猜错了，qingcongxinshuru：')
        guess = int(temp)
    elif guess < answer:
        print('太小了')
        temp = input('猜错了，qingcongxinshuru：')
        guess = int(temp)
    else:
        print('caiduile') 

else:
    print('caiduile') 
print('然而你还是很有钱')


# for循环
# 语法  for 目标(变量) in 表达式(列表/元组):
#     循环体  

favourite = 'fishc'

for i in favourite:
    print(i)

munber = ['嘿嘿','嘻嘻','町町','芳泳','韦琦','敏仪姐姐']
for each in munber:
    print(each,len(munber))

munber = ['嘿嘿','嘻嘻','町町','芳泳','韦琦','敏仪姐姐']
for each in munber:
    print(each,len(each))


list(range(99))
    
