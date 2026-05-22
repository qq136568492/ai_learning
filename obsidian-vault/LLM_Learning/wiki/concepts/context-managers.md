---
type: concept
created: 2026-05-14
updated: 2026-05-14
tags: [python, advanced, context-manager]
source_count: 1
---

# context-managers

上下文管理器用于安全管理资源生命周期（获取→使用→释放），避免异常时资源泄漏。

## 核心要点
- 协议：`__enter__` / `__exit__`
- 语法：`with ... as ...:`
- 函数式写法：`contextlib.contextmanager`
- 异步版本：`async with` + `@asynccontextmanager`

## 常见场景
- 文件/网络连接/数据库会话自动关闭
- 临时上下文（切换目录、锁、事务）
- FastAPI `yield` 依赖中的资源清理

## 关联
- [[concepts/file-io]]
- [[concepts/dependency-injection]]
- [[topics/python-advanced-to-ai-roadmap]]

## 来源
- [[sources/2026-05-14-python-advanced-to-ai-roadmap]]
