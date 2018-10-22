#!-*-coding:utf-8 -*-
"""
    问题：通过指定文本模式检查str的开头或结尾
    解决：str.startswith(), str.endswith()
"""
import os
filenames = os.listdir('.')
print(filenames)
n = [name for name in filenames if name.endswith('.py')]        #多个匹配项放入元组传入endswith()
print(n)

