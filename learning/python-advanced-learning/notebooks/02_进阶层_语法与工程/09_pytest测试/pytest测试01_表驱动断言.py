# 练习时可先遮住实现自行编写。
"""手写 mini 测试表驱动：无需 pytest 运行器即可自测。"""

def add(a: int, b: int) -> int:
    pass
if __name__ == '__main__':
    cases = [((1, 2), 3), ((-1, 1), 0)]
    for args, exp in cases:
        assert add(*args) == exp, (args, exp)
    print('ok')
