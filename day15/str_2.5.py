#!-*-coding:utf-8 -*-
"""
    问题：在字符串中搜索和匹配、替换指定的文本模式
"""

import re
from calendar import month_abbr

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

#简单字面模式，使用str.replace()
text1 = 'yeah, but no, but yeah, but no, but yeah'
t = text1.replace('yeah', 'yep')
print(t)
text2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
t2 = datepat.sub(r'\3-\1-\2', text2)
print(t2)

#更加复杂的替换，可以传递一个替换回调函数来代替
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(3), mon_name, m.group(2))
t3 = datepat.sub(change_date, text2)
print(t3)