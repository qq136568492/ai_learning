# 练习时可先遮住实现自行编写。
"""最小状态图：节点函数 + dict 路由。"""
from typing import Callable
State = dict[str, str]

def run_graph(nodes: dict[str, Callable[[State], tuple[str | None, State]]], start: str, init: State) -> State:
    pass
if __name__ == '__main__':

    def plan(_: State) -> tuple[str | None, State]:
        pass

    def act(state: State) -> tuple[str | None, State]:
        pass
    out = run_graph({'plan': plan, 'act': act}, start='plan', init={})
    assert out['done'] == 'yes'
    print('ok')
