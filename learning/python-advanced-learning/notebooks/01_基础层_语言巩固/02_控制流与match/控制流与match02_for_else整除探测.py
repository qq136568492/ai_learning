# 练习时可先遮住实现自行编写。
"""for-else：循环正常结束触发 else。"""
from __future__ import annotations

def first_divisor(n: int, candidates: list[int]) -> int | None:
    """返回 candidates 中第一个能整除 n 的数；若不存在则返回 None。"""
    pass
if __name__ == '__main__':
    assert first_divisor(15, [2, 4, 9]) is None
    assert first_divisor(15, [2, 3, 5]) == 3
    print('ok')
