#!-*-coding:utf-8 -*-
"""
    问题：找出一个序列中出现最多的元素
    解决：collections.Counter可以解决这类问题，
    Counter对象接受hashable的序列, 还可以进行数学运算操作
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
morewords = ['why','are','you','not','looking','in','my','eyes']

word_count = Counter(words)    #Counter给出每个词的出现次数
top_three = Counter(words).most_common(3)    #频率最高的三个词
print(word_count)
print(top_three)
print(word_count['look'])

for word in morewords:
    word_count[word] += 1
print(word_count)
print(word_count['eyes'])