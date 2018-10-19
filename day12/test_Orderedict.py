#!-*-coding:utf-8 -*-
"""
    问题：创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序
    OrderedDict:插入新元素时，会放在链表尾部。对于已从在的 key 重新赋值将不会改变 key 的顺序。
"""
from collections import OrderedDict

d = OrderedDict()
d['apple'] = 1
d['banda'] = 2
d['peach'] = 3
print(d)
print(len(d))
for key in d:
    print((key, d[key]), end='\t')
d['apple'] = 4                      #改变已从在 key 的值
print()
print(d.items())