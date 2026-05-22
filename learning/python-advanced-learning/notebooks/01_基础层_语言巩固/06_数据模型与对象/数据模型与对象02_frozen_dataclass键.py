# 练习时可先遮住实现自行编写。
"""可哈希冻结小对象：用作 dict 键。"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
if __name__ == '__main__':
    m = {Point(0, 0): 'origin'}
    assert m[Point(0, 0)] == 'origin'
    print('ok')
