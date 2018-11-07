#!-*-coding:utf-8 -*-
"""
问题：将HTML或者XML实体如 &entity; 或 &#code; 替换为对应的文本。 再者，你需要转换文本中特定的字符(比如<, >, 或 &)。
        编码, 解码
"""
import html
from html.parser import HTMLParser

s = 'Elements are written as "<tag>text</tag>".'
#编码
s1 = html.escape(s)
print(s1)

a = 'Spicy &quot;Jalape&#241;o&quot.'
p = HTMLParser()
#解码
print(p.unescape(a))
