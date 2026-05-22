# 练习时可先遮住实现自行编写。
"""填补缺失：数值列均值填充。"""

def fill_na_mean(series: dict[str, float | None]) -> dict[str, float]:
    pass
if __name__ == '__main__':
    out = fill_na_mean({'a': 1.0, 'b': None, 'c': 3.0})
    assert abs(out['b'] - 2.0) < 1e-09
    print('ok')
