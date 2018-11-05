#!-*-coding:utf-8 -*-
"""
问题：出现非常规文本”pýtĥöñ”，如何将这些字符清理掉
解决：文本清理问题会涉及到包括文本解析与数据处理等一系列问题。 在非常简单的情形下，你可能会选择使用字符串函数(比如 str.upper() 和 str.lower() )
将文本转为标准格式。 使用 str.replace() 或者 re.sub() 的简单替换操作能删除或者改变指定的字符序列。 你同样还可以使用2.9小节的 unicodedata.normalize()
函数将unicode文本标准化。

然后，有时候你可能还想在清理操作上更进一步。比如，你可能想消除整个区间上的字符或者去除变音符。 为了这样做，你可以使用经常会被忽视的 str.translate() 方法
"""
import unicodedata
import sys

s = 'pýtĥöñ\fis\tawesome\r\n'

#清理空白符,
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
a = s.translate(remap)
print(a)

#删除和音符, dict.fromkeys() 方法构造一个字典，每个Unicode和音符作为键，对应的值全部为 None
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(type(b))
c = b.translate(cmb_chrs)
print(c)
