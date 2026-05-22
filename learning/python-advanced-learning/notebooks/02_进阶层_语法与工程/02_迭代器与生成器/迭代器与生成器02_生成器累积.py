# 练习时可先遮住实现自行编写。
"""生成器函数：前缀累加。"""

def cumsum(vals: list[int]):
    total = 0
    for val in vals:
        total += val
        yield total
        
if __name__ == '__main__':
    assert list(cumsum([1, 2, 3])) == [1, 3, 6]
    print('ok')
