---
type: concept
created: 2026-05-14
updated: 2026-05-14
tags: [python, async, asyncio]
source_count: 1
---

# asyncio-in-practice

`asyncio` 是 Python 异步 I/O 的核心框架，适用于高并发网络/文件等待场景。

## 核心要点
- `async def` / `await` / 事件循环
- 并发编排：`create_task`、`gather`、`wait_for`
- 异步资源：`async with`、`async for`
- 与同步桥接：`asyncio.to_thread`

## 实战建议
- I/O 密集用异步；CPU 密集改多进程或外部任务系统
- 任务设置超时、取消与重试策略
- 在 FastAPI 中优先使用异步客户端与驱动

## 关联
- [[topics/fastapi-api-engineering]]
- [[topics/python-advanced-to-ai-roadmap]]

## 来源
- [[sources/2026-05-14-python-advanced-to-ai-roadmap]]
