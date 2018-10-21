#!-*-coding:utf-8 -*-
"""
    问题：对一个字典或者实例序列，根据特定字段 分组 进行迭代访问
    解决：利用itertools.groupby(): 先根据 字段 排序， 再调用groupby()， groupby检查连续的元素，要先排序
"""
from itertools import groupby
from operator import  itemgetter
from collections import defaultdict

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
rows.sort(key=itemgetter('date'))     #排序

#Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)
print('*************************************************************************')

#只是想根据 date 字段将数据分组到一个大的数据结构中去，并且允许随机访问，可以利用defaultdict()
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)
print('*************************************************************************')
for r in rows_by_date['07/01/2012']:
    print(r)                             #相比groupby()不用排序，更占内存