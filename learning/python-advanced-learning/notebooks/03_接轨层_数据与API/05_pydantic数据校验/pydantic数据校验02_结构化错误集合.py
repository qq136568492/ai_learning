# 练习时可先遮住实现自行编写。
"""Pydantic：验证失败结构化错误。"""
from pydantic import BaseModel, Field, ValidationError

class Req(BaseModel):
    k: int = Field(ge=1, le=10)

def collect_errors(payload: dict) -> list:
    pass
if __name__ == '__main__':
    bad = collect_errors({'k': 0})
    assert bad, bad
    good = collect_errors({'k': 5})
    assert good == []
    print('ok')
