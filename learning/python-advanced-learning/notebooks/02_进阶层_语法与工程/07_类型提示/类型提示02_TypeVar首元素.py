# 练习时可先遮住实现自行编写。
"""TypeVar 泛型函数 first。"""
from typing import TypeVar
T = TypeVar('T')

def first_or_default(items: list[T], default: T) -> T:
    pass
if __name__ == '__main__':
    assert first_or_default([], 0) == 0
    assert first_or_default([3, 4], 0) == 3
    print('ok')
