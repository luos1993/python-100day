#!-*-coding:utf-8 -*-
"""
    读取json文件
"""
import json
import csv2

dict1 = '{"name": "元芳", "age": 22, "title": "叫兽"}'
result = json.loads(dict1)
print(result)

teacher = csv2.Teacher(**result)
print(teacher)
print(teacher.name)
print(teacher.age)