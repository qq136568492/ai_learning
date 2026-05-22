# 练习时可先遮住实现自行编写。
"""类上下文管理器：记录进入/退出。"""

class Recorder:

    def __init__(self) -> None:
        pass

    def __enter__(self) -> 'Recorder':
        pass

    def __exit__(self, exc_type, exc, tb) -> None:
        pass
if __name__ == '__main__':
    r = Recorder()
    with r:
        assert r.events[-1] == 'enter'
    assert r.events[-1] == 'exit:None'
    try:
        with Recorder() as rr:
            raise ValueError('x')
    except ValueError:
        pass
    print('ok')
