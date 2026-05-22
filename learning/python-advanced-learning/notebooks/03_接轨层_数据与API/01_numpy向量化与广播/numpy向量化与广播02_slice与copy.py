# 练习时可先遮住实现自行编写。
"""视图 vs 拷贝：切片写入不污染原版。"""

def doubled_copy(original):
    pass
if __name__ == '__main__':
    arr, part = doubled_copy([[1], [2], [3]])
    assert arr.ravel().tolist() == [1, 2, 3]
    assert part.ravel().tolist() == [20, 30]
    print('ok')
