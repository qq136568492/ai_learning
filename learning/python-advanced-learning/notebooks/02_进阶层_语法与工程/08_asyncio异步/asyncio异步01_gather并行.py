# 练习时可先遮住实现自行编写。
"""asyncio.gather 并行任务。"""
import asyncio

async def ident(x: int) -> int:
    pass

async def main() -> list[int]:
    pass
if __name__ == '__main__':
    out = asyncio.run(main())
    assert out == [1, 2, 3]
    print('ok')
