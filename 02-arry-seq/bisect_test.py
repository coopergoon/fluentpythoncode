#coding=utf8
"""
bisect使用详情查看博客：https://walkmanchen.github.io/2017/06/21/bisect%E6%8E%92%E5%BA%8F%E6%A8%A1%E5%9D%97/
"""

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

