# 练习时可先遮住实现自行编写。
"""带参装饰器练习：`logged(prefix)` 在「原函数返回的字符串」前面拼接一段前缀。

等价链：`greet = logged('[svc] ')(greet_original)` —— 先绑定 prefix，再包住函数。

验收：`greet('ada') == '[svc] hi ada'`（前缀写在返回值里，不是单独一行 stderr）。"""
from collections.abc import Callable
from functools import wraps

def logged(prefix: str):

    def deco(fn: Callable[..., str]):

        @wraps(fn)
        def inner(*args, **kwargs) -> str:
            # prefix、fn 来自外层闭包；此处只做转发与拼接
            return f"{prefix}{fn(*args, **kwargs)}"
        return inner
    return deco


if __name__ == '__main__':

    @logged('[svc] ')
    def greet(name: str) -> str:
        return f'hi {name}'
    print(greet('ada'))
    assert greet('ada') == '[svc] hi ada'
    print('ok')
