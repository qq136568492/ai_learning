# 练习时可先遮住实现自行编写。
"""sys.path 与包搜索：打印是否包含 site-packages 目录名（环境探测）。"""
import sys

def has_site_packages(paths: list[str]) -> bool:
    pass
if __name__ == '__main__':
    assert isinstance(sys.path, list)
    _ = has_site_packages(sys.path)
    print('ok')
