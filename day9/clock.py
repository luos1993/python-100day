#!-*-coding:utf-8 -*-

from time import time, localtime, sleep

class Clock(object):

    def __init__(self, hour=0, min=0, sec=0):
        self._hour = hour
        self._min = min
        self._sec = sec

    @classmethod
    def now(cls):
        """获取当前时间"""
        ctime = localtime(time())
        print(ctime)
        print(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._sec +=1
        if self._sec == 60:
            self._sec = 0
            self._min += 1
            if self._min == 60:
                self._min = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示"""
        return '%s:%s:%s' % (self._hour, self._min, self._sec)

def main():
    clock = Clock.now()
    print(clock.now())
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()