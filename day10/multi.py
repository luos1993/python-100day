#!-*-coding:utf-8 -*-
"""
    多重继承
"""
class Father(object):
    def __init__(self, name):
        self._name = name

    def gamble(self):
        print('%s在打麻将' % self._name)

    def eat(self):
        print('%s在胡吃海喝。' % self._name)

class Mank(object):
    def __index__(self, name):
        self._name = name

    def eat(self):
        print('%s在吃斋。' % self._name)

    def chant(self):
        print('%s在念经。' % self._name)

class Musican(object):
    def __init__(self, name):
        self._name = name

    def eat(self):
        print('%s在细嚼慢咽。' % self._name)

    def play_piano(self):
        print('%s在弹钢琴。' % self._name)

class Son(Father, Mank, Musican):
    def __init__(self, name):
        super(Son, self).__init__(name)

son = Son('王大锤')
son.gamble()
# 调用继承自Father的eat方法
son.eat()
son.chant()
son.play_piano()
