#!-*-coding:utf-8 -*-
"""
    问题：过滤元素，提取需要的值或者缩短序列
"""

from itertools import compress

#最简单用列表推到式, 缺点：如果输入很大将占用大量内存
mylist = [1, 2, 4, -4, -6, -8, -10, 18]
lst = [n for n in mylist if n > 0]
print(lst)

#上述该用生成器迭代表达
pos = (n for n in mylist if n > 0)
print(type(pos))
for r in pos:
    print(r, end='\t')
print()

#过滤规则比较复杂，无法用上述方式表达，可以把规则写进函数中， 然后农户使用fiter()
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))  #filter创建了一个迭代器，想得到list就如左边这样转换
print(ivals)

#过滤器itertools.compress(), compress于两个参数(data, selectors,关键在于如何构建这个selecors, compress返回的也是一个迭代器
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n for n in counts if n >5]
result = list(compress(addresses, more5))     #关键在于
print(result)