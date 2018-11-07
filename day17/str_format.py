#!-*-coding:utf-8 -*-
"""
    问题：创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉
    解决：strde format方法
"""
s = '{name} has {n} message'
s1 = s.format(name='John', n=5)
print(s1)

#替换的变量能在变量域中找到， 那么你可以结合使用 format_map() 和 vars()
name = 'John'
n = 3
s2 = s.format_map(vars())
print(s2)

#vars也适用于对象实例
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('John', 3)
s3 = s.format_map(vars(a))
print(s3)