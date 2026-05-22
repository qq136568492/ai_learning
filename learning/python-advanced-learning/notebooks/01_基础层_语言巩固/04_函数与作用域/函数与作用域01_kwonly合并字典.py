# 练习时可先遮住实现自行编写。
"""函数：仅限关键字参数 / 解包。"""

def merge_payload(*, base: dict, extra: dict) -> dict:
    pass
if __name__ == '__main__':
    b = {'x': 1}
    e = {'y': 2}
    assert merge_payload(base=b, extra=e) == {'x': 1, 'y': 2}
    print('ok')
