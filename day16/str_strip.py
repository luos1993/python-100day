#!-*-coding:utf-8 -*-
"""
    问题：删除字符串中多余的字符，如前面、中间、结尾的空格
"""

import os
import re

#str.strip()删除开头结尾的空格，也可以删除其他字符
str = '   hello    world   '
s1 = str.strip()
s2 = str.lstrip()
s3 = str.rstrip()

str1 = '-------hello world++++++'
s4 = str1.strip('-, +')
print([s1, s2, s3, s4], end='\n')

#中间的空格可以用replace()替换或者正则表达式替换
s5 = str.replace(' ', '')
s6 = re.sub('\s+', ' ', str)
print([s5, s6])

filename = 'test.txt'
with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)