#!-*-coding:utf-8 -*-
"""
    问题：排序不支持原生排序操作的类实例
    解决：
"""
from operator import attrgetter

class User(object):
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=lambda u: u.user_id))

#还可以利用atttrgetter, 同样适用于min, max函数
print(sorted(users, key=attrgetter('user_id')))
print(min(users, key=attrgetter('user_id')))