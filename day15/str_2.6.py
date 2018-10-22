#!-*-coding:utf-8 -*-
"""
    问题：以忽略大小写的方式搜索与替换文本字符串
"""
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
t1 = re.findall('python', text, flags=re.IGNORECASE)
t2 = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(t1)
print(t2)       #结果看出替换字符串并未大小写一致

#添加一辅助函数
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

t3 = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(t3)