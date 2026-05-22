---
type: concept
created: 2026-05-14
updated: 2026-05-14
tags: [fastapi, dependency-injection]
source_count: 1
---

# dependency-injection

FastAPI 使用 `Depends` 实现依赖注入，用于复用认证、数据库会话、配置加载、权限检查等横切逻辑。

## 作用
- 解耦路由与基础设施代码
- 提升可测试性（可 override 依赖）
- 支持分层组合（子依赖 / 全局依赖）

## 常见模式
- 请求级 DB Session 注入
- 当前用户注入（OAuth2/JWT）
- 配置对象注入（Settings）

## 关联
- [[topics/fastapi-api-engineering]]
- [[entities/fastapi]]

## 来源
- [[sources/2026-05-14-fastapi-official-docs]]
