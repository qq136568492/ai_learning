# 练习时可先遮住实现自行编写。
"""对象身份与相等：区分 is 与 =="""

class Box:
    __slots__ = ('v',)

    def __init__(self, v: int) -> None:
        pass

    def __eq__(self, other: object) -> bool:
        pass
if __name__ == '__main__':
    a = Box(1)
    b = Box(1)
    assert a == b
    assert a is not b
    print('ok')
