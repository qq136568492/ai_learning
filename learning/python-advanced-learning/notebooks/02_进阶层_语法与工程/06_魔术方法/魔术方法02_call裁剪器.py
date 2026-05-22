# 练习时可先遮住实现自行编写。
"""可调用对象：__call__ 实现轻量策略。"""

class Clip:

    def __init__(self, lo: int, hi: int) -> None:
        pass

    def __call__(self, x: int) -> int:
        pass
if __name__ == '__main__':
    c = Clip(0, 10)
    assert c(15) == 10 and c(-3) == 0
    print('ok')
