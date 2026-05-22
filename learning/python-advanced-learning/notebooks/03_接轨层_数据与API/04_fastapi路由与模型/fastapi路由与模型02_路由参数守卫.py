# 练习时可先遮住实现自行编写。
"""FastAPI：路径参数校验。"""
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

def build_app() -> FastAPI:
    pass

    @app.get('/square/{x}')
    async def square(x: int) -> dict[str, int]:
        pass
    pass
if __name__ == '__main__':
    c = TestClient(build_app())
    assert c.get('/square/3').json()['v'] == 9
    assert c.get('/square/-2').status_code == 400
    print('ok')
