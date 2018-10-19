#!-*-coding:utf-8 -*-
"""
    问题：怎样在字典中执行一些运算，如排序，求最值
"""
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
print(prices.values())
print(prices.keys())
min_prices = min(zip(prices.values(), prices.keys()))
print(min_prices)