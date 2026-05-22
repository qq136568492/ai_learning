# 练习时可先遮住实现自行编写。
"""数据类型与可变默认：用 None 哨兵避免跨调用共享可变状态。"""

def append_tail(x: int, acc: list[int] | None=None) -> list[int]:
    """将 x 追加到 acc 末尾并返回 acc；acc 为 None 时创建新列表。"""
    pass
if __name__ == '__main__':
    a = append_tail(1)
    b = append_tail(2)
    assert a == [1] and b == [2]
    shared: list[int] = []
    c = append_tail(3, shared)
    d = append_tail(4, shared)
    assert c is d is shared == [3, 4]
    print('ok')
