# 练习时可先遮住实现自行编写。
"""Protocol：结构化子类型计数。"""
from typing import Protocol

class SizedBox(Protocol):

    def __len__(self) -> int:
        pass

def describe(x: SizedBox) -> str:
    pass
if __name__ == '__main__':

    class Bag:

        def __len__(self) -> int:
            pass
    assert describe(Bag()) == 'n=5'
    print('ok')
