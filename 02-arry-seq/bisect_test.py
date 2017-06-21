#coding=utf8
import bisect
grades = 'FEDCBA'
breakpoints = [3, 20, 34, 43, 45, 54]


def grade(totle):
    """
    breakpoints是原数据，totle是要查询的数据
    bisect.bisect(breakpoints, totle) 返回的是列表的索引值
    :param totle:
    :return:
    """
    print(grades[bisect.bisect(breakpoints, totle)])
grade(45)

