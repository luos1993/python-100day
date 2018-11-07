#!-*-coding:utf-8 -*-
"""
问题：有一些长字符串，想以指定的列宽将它们重新格式化
解决：textwrap模块
"""

import os
import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
s1 = textwrap.fill(s, 70)
s2 = textwrap.fill(s, 40, initial_indent='    ')

#a = os.get_terminal_size()
#s3 = textwrap.fill(s, a)
print(s1)
print(s2)