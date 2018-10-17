#!-*-coding:utf-8 -*-
"""
    字符串操作--倒转字符串
"""
from io import StringIO

def reverse_str1(str):
    #切片，步长 -1
    return str[::-1]

def reverse_str2(str):
    #利用递归一个个读取
    if len(str) <= 1:
        return str
    return reverse_str2(str[1:]) + str[0:1]

def reverse_str3(str):
    l = list(str)
    for i, j in zip(range(len(l)//2), range(len(l)-1, len(l)//2, -1)):
        l[i], l[j] = l[j], l[i]
    return ''.join(l)

if __name__ == '__main__':
    str = 'I love python'
    print(reverse_str1(str))
    print(reverse_str2(str))
    print(reverse_str3(str))