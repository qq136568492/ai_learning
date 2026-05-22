# 练习时可先遮住实现自行编写。
"""Pandas：groupby 求均值。"""

def avg_by_city(rows: list[tuple[str, int]]) -> dict[str, float]:
    pass
if __name__ == '__main__':
    data = [('bj', 10), ('sh', 5), ('bj', 14)]
    m = avg_by_city(data)
    assert abs(m['bj'] - 12.0) < 1e-09 and m['sh'] == 5.0
    print('ok')
