#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入 g3模块
import G3

G3.isdn()


import sys

print '命令行参数如下'
for i in sys.argv:
    print i

print '/n/nthe pythonpath is',sys.path,'/n'