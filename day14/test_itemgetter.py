#!-*-coding:utf-8 -*-
"""
    问题：对一个字典列表，根据某个关键字排序
    解决：利用operator模块， 的itemgetter函数
"""

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_lname = sorted(rows, key=itemgetter('lname'))
print(rows_by_fname)
print(rows_by_lname)

#itemgetter函数也支持多个keys
row_by_flname = sorted(rows, key=itemgetter('lname', 'fname'))
print(row_by_flname)

#itemgetter也可以换成lambda，但运行稍慢一些
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
print(rows_by_fname)

#itemgetter也适用于min,max函数
m = min(rows, key=itemgetter('uid'))
print(m)