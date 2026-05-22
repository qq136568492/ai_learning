# 练习时可先遮住实现自行编写。
"""手写余弦相似度（无向量库依赖）。"""
import math

def cosine(a: list[float], b: list[float]) -> float:
    pass
if __name__ == '__main__':
    assert abs(cosine([1, 0], [1, 0]) - 1.0) < 1e-09
    assert cosine([1, 0], [0, 1]) == 0.0
    print('ok')
