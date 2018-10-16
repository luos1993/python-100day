#!-*-coding:utf-8 -*-
"""
    抽象类 / 方法重写 / 多态
    实现一个工资结算系统 公司有三种类型的员工
	- 部门经理固定月薪12000元/月
	- 程序员按本月工作小时数每小时100元
	- 销售员1500元/月的底薪加上本月销售额5%的提成
    输入员工的信息 输出每位员工的月薪信息

"""
from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):

    def __init__(self, name):
        super(Manager, self).__init__(name)

    def get_salary(self):
        return 20000

class Programmer(Employee):

    def __init__(self, name):
        super(Programmer, self).__init__(name)

    def work_hour(self, work_hour):
        self._workhour = work_hour

    def get_salary(self):
        return 5000 + 50 * self._workhour

class Salesman(Employee):

    def __init__(self, name):
        super(Salesman, self).__init__(name)

    def get_salary(self):
        return 3000 + self._sales * 0.05

    def set_sales(self, sales):
        self._sales = sales
if __name__ == '__main__':
    emps = [Manager('武则天'), Programmer('狄仁杰'), Salesman('白元芳')]
    for emp in emps:
        if isinstance(emp, Programmer):
            work_hour = int(input('请输入%s本月工作时间: ' % emp.name))
            emp.work_hour(work_hour)
        elif isinstance(emp, Salesman):
            sales = float(input('请输入%s本月销售额: ' % emp.name))
            emp.set_sales(sales)
        print('%s本月月薪为: ￥%.2f元' % (emp.name, emp.get_salary()))