---
type: concept
created: 2026-05-14
updated: 2026-05-14
tags: [python, advanced, decorators]
source_count: 1
---

# decorators

装饰器用于在不修改原函数源码的前提下，为函数/方法增加横切能力（日志、计时、鉴权、缓存等）。

## 核心要点
- 本质：高阶函数（函数接收函数并返回函数）
- 语法糖：`@decorator` 等价于 `func = decorator(func)`
- 带参装饰器：多一层工厂函数
- 元数据保留：使用 `functools.wraps`

## 常见场景
- 接口计时与性能统计
- 统一日志与审计埋点
- 权限校验、重试、缓存

## 关联
- [[concepts/functions]]
- [[topics/python-advanced-to-ai-roadmap]]

## 来源
- [[sources/2026-05-14-python-advanced-to-ai-roadmap]]
