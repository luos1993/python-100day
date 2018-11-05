#!-*-coding:utf-8 -*-
"""
    问题：处理Unicode字符串，需要确保所有字符串在底层有相同的表示
    解决：unicodedata模块
"""
import unicodedata

s1 = 'Spicy Jalape\u00f1o'      #整体字符
s2 = 'Spicy Jalapen\u0303o'     #组合字符

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t1 == t2)
print(t3 == t4)

#NFC表示字符应该是整体组成(比如可能的话就使用单一编码)，而NFD表示字符应该分解为多个组合字符表示