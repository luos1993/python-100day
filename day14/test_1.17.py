#!-*-coding:utf-8 -*-
"""
    问题：字典中提取子集
"""
#字典推导式
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

#创建元组传给字典函数也可以实现
p1 = dict((key, value) for key, value in prices.items() if value > 200)
p2 = { key:prices[key] for key in prices.keys() & tech_names }

#几种方式主要在于运行时间的快慢，第一种相比更快