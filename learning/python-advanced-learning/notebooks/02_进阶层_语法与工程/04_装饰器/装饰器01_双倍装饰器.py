# 练习时可先遮住实现自行编写。
"""无参装饰器：把返回值乘 2。"""
from collections.abc import Callable
from functools import wraps

def double_out(fn: Callable[..., int]):

    @wraps(fn)
    def inner(*args, **kwargs) -> int:
        return fn(*args, **kwargs) * 2
    
    return inner

if __name__ == '__main__':

    @double_out
    def f(x: int) -> int:
        return x
    assert f(3) == 6
    print('ok')
