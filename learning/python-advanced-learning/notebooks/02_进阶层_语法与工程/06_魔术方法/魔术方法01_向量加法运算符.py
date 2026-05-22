# 练习时可先遮住实现自行编写。
"""向量加法：__add__ 与 repr。"""
from __future__ import annotations

class Vec:

    def __init__(self, x: int, y: int) -> None:
        pass

    def __add__(self, other: Vec) -> Vec:
        pass

    def __repr__(self) -> str:
        pass
if __name__ == '__main__':
    assert repr(Vec(1, 2) + Vec(3, 4)) == 'Vec(4,6)'
    print('ok')
