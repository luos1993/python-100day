#!-*-coding:utf-8 -*-
"""
    问题：程序包含了大量无法直视的硬编码切片,并且你想清理一下代码
"""
# slice()创建一个切片对象, 减少硬编码，提高程序可读性
record = '....................100 .......513.25 ..........'
cost1 = int(record[20:23]) * float(record[31:37])
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost2 = int(record[SHARES]) * float(record[PRICE])
print(cost1)
print(cost2)
a = slice(20, 23)
a.start
a.stop
a.step
#a.indices(),映射到已知大小的序列上，返回一个三元组(start, stop, step)
b = slice(0)
b.indices(len(record))
print(b.indices(len(record)))