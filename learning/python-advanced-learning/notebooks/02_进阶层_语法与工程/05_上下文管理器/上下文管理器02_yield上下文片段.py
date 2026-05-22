# 练习时可先遮住实现自行编写。
"""@contextmanager：临时切换前缀。"""
from contextlib import contextmanager

@contextmanager
def with_prefix(lines: list[str], p: str):
    yield from ()
if __name__ == '__main__':
    out: list[str] = []
    with with_prefix(out, 'A:'):
        out.append('work')
    assert out == ['A:begin', 'work', 'A:end']
    print('ok')
