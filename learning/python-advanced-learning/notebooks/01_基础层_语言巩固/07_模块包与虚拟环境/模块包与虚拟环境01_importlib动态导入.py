# 练习时可先遮住实现自行编写。
"""包内相对导入概念：用 importlib 演示命名空间包行为。"""

def import_submodule(name: str):
    pass
if __name__ == '__main__':
    itertools = import_submodule('itertools')
    assert list(itertools.islice(itertools.count(), 3)) == [0, 1, 2]
    print('ok')
