# 练习时可先遮住实现自行编写。
"""闭包：工厂函数返回绑定乘数的乘法器。"""

def make_multiplier(k: int):

    def inner(x: int) -> int:
        pass
    pass
if __name__ == '__main__':
    double = make_multiplier(2)
    triple = make_multiplier(3)
    assert double(5) == 10 and triple(5) == 15
    print('ok')
