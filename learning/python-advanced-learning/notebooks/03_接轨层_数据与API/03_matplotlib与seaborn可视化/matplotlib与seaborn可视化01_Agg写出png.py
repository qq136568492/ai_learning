# 练习时可先遮住实现自行编写。
"""Matplotlib：Agg 后端保存 PNG 到字节。"""
from io import BytesIO

def render_line_png_bytes(xs: list[int], ys: list[int]) -> bytes:
    pass
if __name__ == '__main__':
    b = render_line_png_bytes([0, 1, 2], [0, 1, 0])
    assert len(b) > 800
    assert b.startswith(b'\x89PNG')
    print('ok')
