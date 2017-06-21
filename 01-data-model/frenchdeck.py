#coding=utf8

from collections import namedtuple

"""
namedtuple可以创建简单的对象，并直接调用其中的属性
如下：x， y是其中的属性
point = Tpoint(1, 2,)是创建对象
使用point.x，或者point.y 调用其中的属性
"""
Tpoint = namedtuple('Tpoint', ['x', 'y'])
point = Tpoint(1, 2,)
# print(point.y)


Card = namedtuple('Card', ['rank', 'suit'])


class Frenchdeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        """
        使用列表解析
        """
        self._cards = [Card(rank, suit) for suit in self.suit for rank in self.ranks]

    def __len__(self):
        print(self._cards)
        print(self.suit)
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
f = Frenchdeck()


# 返回52， 使用len方法，调用的是自定义的__len__()
print(len(f))

