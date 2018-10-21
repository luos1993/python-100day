#!-*-coding:utf-8 -*-
"""
    问题：将多个字典从逻辑上合并为一个单一的映射后执行某些操作， 比如查找值或者检查某些键是否存在
    解决:collections中的ChainMap(),这个类不改变原有的字典
"""

from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

#ChainMap 类只是在内部创建了一个容纳这些字典的列表, 并重新定义了一些常见的 字典操作 来遍历这个列表。大部分字典操作都是可以正常使用的
c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['y'])
print(c['z'])  #出现相同的key时， 将返回靠前的字典中的值，比如此处z的值来自a字典

#还可以这样搞
values = ChainMap()
values['x'] = 1
#添加一个新mapping
values = values.new_child()
values['y'] = 2
print(values)