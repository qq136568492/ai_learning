---
type: concept
created: 2026-05-14
updated: 2026-05-14
tags: [fastapi, security, oauth2, jwt]
source_count: 1
---

# api-security

FastAPI 的 API 安全核心包括 OAuth2/JWT 鉴权、CORS、中间件防护、输入校验与错误处理策略。

## 关键要素
- OAuth2 Password Flow / Bearer Token
- JWT 令牌签发、校验、过期控制
- CORS 策略最小化授权
- TrustedHost / HTTPSRedirect 等中间件

## 工程建议
- 认证与授权分层（身份认证 vs 权限判断）
- 对高风险接口增加速率限制与审计日志
- 在网关与应用层双重执行安全策略

## 关联
- [[topics/fastapi-api-engineering]]
- [[entities/fastapi]]

## 来源
- [[sources/2026-05-14-fastapi-official-docs]]
