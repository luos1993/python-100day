#!-*-coding:utf-8 -*-
"""
    定义矩形类
"""
import math

class Rect(object):

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2*(self.width + self.height)

    def area(self):
        return self.width * self.height

    def __str__(self):
        return '矩形[%f, %f]' % (self.width, self.height)

    def __del__(self):
        print('销毁矩形对象')

if __name__ == '__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(4, 5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())