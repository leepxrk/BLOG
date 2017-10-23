#!/usr/bin/python
# -*- coding: UTF-8 -*-

#面向对象
#属性相近的分类：在该分类下，定义了bird,并定义了两个变量 have_faether 和 way_of_reperoduction
#动作分类：在该分类下，定义了一些行为的方法进行区分，即move

class bird(object):
    have_faether = True
    way_of_reperoduction = 'egg'
    def move(self,dx,dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position
        
summer = bird()
print summer.way_of_reperoduction
print 'after move' , summer.move(5,8)


#大分类下会定义一个子类
#引如继承的概念

class chicken(bird):
    way_of_move = 'walk'
    possile_in_kfc = True
    
class oriole(bird):
    way_of_move = 'fly'
    possile_in_kfc = False
    
summer = chicken()
print summer.have_faether
print summer.move(5,8)

#将东西根据属性归类 ( 将object归为class )
#方法是一种属性，表示动作
#用继承来说明父类-子类关系。子类自动具有父类的所有属性。
#self代表了根据类定义而创建的对象。
#建立对一个对象： 对象名 = 类名()
#引用对象的属性： object.attribute



#定义方法，必须要有self参数，用于表示某个对象，以及对象拥有的的性质，可以通过self，调用类属性
class human(object):
    laugh = 'hahaha'
    def show_laugh(self):
        print self.laugh
    def laugh_100th(self):
        for i in range(100):
            self.show_laugh()


lilei = human()
print lilei.laugh_100th()


#_init_()  是一个特殊方法，python会特殊对待，在类中定义了该方法，创建对象时，python会自动调用这个方法进行初始化

class happybird(bird):
    def __init__(self,more_words):
        print 'we are happybirds',more_words
summer = happybird('happy,happy')







微信登录获取个人信息，之前产品上限制昵称不允许重复，解决方案
1、微信名 + 5sign用户ID
2、特殊情况处理
    1）特殊字符
    2）超长
    3）符号

第二个时间会比较长一点，单独我比较偏向第二个方案



我梳理一下，绩效管理那个界面要有这些功能
1. 数据筛选
    1）搜索姓名
    2）部门/组 筛选
    3）考核等级选择
    4）考核周期控制
        - 单期
        - 某个时间周期
    5）流程状态选择
        - 全部
        - 未提交
        - 员工自评
        - 考核人考核
        - 一级审批人
        - 二级审批人
        - 三级审批人
        - HR复核
        - 待员工确认
        - 申诉中
        - 退回
        - 完成

2. 明细数据（根据数据筛选结果展示）
3. 报表（统计图 + 表格）
4. 




