# 练习时可先遮住实现自行编写。
"""FastAPI：最小路由 TestClient。"""
from __future__ import annotations
from fastapi import FastAPI
from pydantic import BaseModel

class Body(BaseModel):
    q: str

def build_app() -> FastAPI:
    pass

    @app.post('/echo')
    async def echo(b: Body) -> dict[str, str]:
        pass
    pass
if __name__ == '__main__':
    from fastapi.testclient import TestClient
    client = TestClient(build_app())
    r = client.post('/echo', json={'q': 'hi'})
    assert r.status_code == 200 and r.json() == {'echo': 'hi'}
    print('ok')
