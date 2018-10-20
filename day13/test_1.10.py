#!-*-coding:utf-8 -*-
"""
    问题：怎样消除相同的值并保持序列不变
"""
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe1(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [1, 5, 2, 1, 9, 1, 5, 10]
b = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a)))
print(type(dedupe(a)))
print(b[0].__hash__())