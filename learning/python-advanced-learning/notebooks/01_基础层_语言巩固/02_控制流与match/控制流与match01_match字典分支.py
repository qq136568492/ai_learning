# 练习时可先遮住实现自行编写。
"""match：对简单数据结构做模式拆分。"""
from typing import Any

def describe_token(tok: dict[str, Any]) -> str:
    """已知 tok 形如 {"type":"num","value":int} 或 {"type":"sym","value":str}。"""
    pass
if __name__ == '__main__':
    assert describe_token({'type': 'num', 'value': 3}) == 'number:3'
    assert describe_token({'type': 'sym', 'value': 'pi'}) == 'symbol:pi'
    assert describe_token({'type': 'x'}) == 'unknown'
    print('ok')
