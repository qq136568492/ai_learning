# 练习时可先遮住实现自行编写。
"""NumPy：广播与一个标量缩放二维数组。"""

def scaled_rows():
    pass
if __name__ == '__main__':
    out = scaled_rows()
    assert out.shape == (3, 4)
    assert abs(out[0, 0] - 0.0) < 1e-09
    assert abs(out[1, 0] - 4.0) < 1e-09
    assert abs(out[2, 0] - 16.0) < 1e-09
    print('ok')
