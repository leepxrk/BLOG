#!/usr/bin/python
# -*- coding: UTF-8 -*-


#列表函数
st = [1,2,1,1]
sst = [2,2,3,3,56,4,6]

#append 函数
st.append(68)  #在列表最后增加新的元素，一次仅能添加一个元素
print 'append 方法:',st


#insert 函数
st.insert(2,68)   #insert方法有两个参数，第一个参数是代表函数插入的索引位，第二个参数代表插入的元素
print 'insert 方法:',st


#extend：在列表末尾一次性追加另一个序列中的多个值
st.extend(sst)
print 'extend 方法:',st
#extend 操作和连接操作最大的不同是，连接操作是新建了一个列表，而extend操作是拓展了第一个列表


#count：统计某个元素在列表中出现的次数
print 'count 方法:',st.count(2)

#index 函数
print 'index 方法:',st.index(56)
# 用于查找列表中某个值的第一个匹配项的索引位置


#pop 函数
print 'pop 方法:',st.pop()   ##pop方法会移除函列表中的一个元素，默认是最后一个元素，并返回该函数的值
print st
#pop函数是唯一一个即能修改列表又返回元素值的函数


#remove 函数
print 'remove 方法:',st.remove(56)  #移除列表中某个值的第一个匹配值
print st
#remove 是修改了列表且没有返回值，与pop方法相反

#reverse 函数
st.reverse()   #讲列表中的元素反向存放
print 'reverse 方法:',st


#sort 函数
st.sort()   #在原位置对列表进行排序
print 'sort 方法:',st
#sort 有两个可选参数，key 和 reverse
#key 是为每个元素建立一个键，根据键值来进行排序，例如
#reverse 是根据布尔值来判断是否需要进行反向排序

