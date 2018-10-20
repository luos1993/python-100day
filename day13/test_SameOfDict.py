#!-*-coding:utf-8 -*-
"""
    问题：查找两个字典的相同之处
"""
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(b.keys() - a.keys())
print(a.items() & b.items())
print(a.items() - b.items())

#构造字典不包含指定的键
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)