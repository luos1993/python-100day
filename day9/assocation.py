#!-*-coding:utf-8 -*-
"""
    对象之间的关联
"""
from math import sqrt

class Point(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move_to(self, x, y):
        self._x = x
        self._y = y

    def move_by(self, dx, dy):
        self._x += dx
        self._y += dy

    def distance(self, other):
        dx = other._x - self._x
        dy = other._y - self._y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return 'point(%s, %s)' % (self._x, self._y)

class Line(object):

    def __init__(self, start=Point(0,0), end=Point(0,0)):
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        self._end = end

    def length(self):
        return self.start.distance(self._end)

if __name__ == '__main__':
    p1 = Point(3, 5)
    print(p1)
    p2 = Point(4, 6)
    line = Line(p1, p2)
    print(line.length())
    line.start.move_to(6, 6)
    print(line)
    print(line.length())
