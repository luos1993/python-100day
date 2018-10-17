#!-*-coding:utf-8 -*-
"""
    写入json文件
"""
import json

teacher_dict = {"name": "u元芳", "age": 25, "title": "砖家"}
result = json.dumps(teacher_dict)
print(result)