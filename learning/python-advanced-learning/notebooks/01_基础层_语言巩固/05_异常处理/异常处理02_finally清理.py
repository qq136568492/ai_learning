# 练习时可先遮住实现自行编写。
"""try/finally：即使 return 也执行清理。"""

def guarded_compute(flag: bool) -> int:
    pass
if __name__ == '__main__':
    assert guarded_compute(True) == 1
    try:
        guarded_compute(False)
    except RuntimeError:
        pass
    print('ok')
