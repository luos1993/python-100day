#!-*-coding:utf-8 -*-
"""
    问题：字符串的合并
"""
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
s1 = ' '.join(parts)        #用空格链接
s2 = ''.join(parts)
s3 = ','.join(parts)
print(s1)
print(s2)
print(s3)

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(parts)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ' '.join(parts)

#组合文件操作
with open('test.txt', 'w') as f:
    for part in combine(sample(), 16):
        f.write(part)
    print(f)