#!-*-coding:utf-8 -*-
"""
    问题：用shell中的通配符（比如*.py)匹配字符串
    解决:fnmatch模块--> fnmatch(), fnmatchcase(),匹配能力介于简单的字符串方法和强大的正则表达式之间
"""
from fnmatch import fnmatch, fnmatchcase

b = fnmatch('foo.txt', '*.txt')
print(b)
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

#有过滤的功效
addr_ST = [addr for addr in addresses if fnmatch(addr, '*ST')]
print(addr_ST)