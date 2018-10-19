#!-*-coding:utf-8 -*-
"""
    怎样实现一个键对应多个值的字典：利用defaultdit很方便.
    defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值
"""
from collections import defaultdict

d = defaultdict(list)
print(d)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
for k, v in s:
    d[k].append(v)
print(d.items())
for item in d.items():
    print(item, end='\t')