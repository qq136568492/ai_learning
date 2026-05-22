# 练习时可先遮住实现自行编写。
"""浅共享 vs 拷贝：区分赋值绑定与列表拷贝。"""
from copy import deepcopy

def snapshot_matrix(m: list[list[int]]) -> list[list[int]]:
    """返回矩阵的深层拷贝（内层列表也需独立）。"""
    pass
if __name__ == '__main__':
    src = [[1, 2], [3]]
    cp = snapshot_matrix(src)
    cp[0][0] = 99
    assert src[0][0] == 1
    assert cp[0][0] == 99
    print('ok')
