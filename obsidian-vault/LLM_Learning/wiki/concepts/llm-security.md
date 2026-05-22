---
type: concept
created: 2026-05-19
updated: 2026-05-19
tags: [llm, security]
source_count: 1
---

# llm-security

LLM 安全除了传统软件安全，还包括 prompt injection、prompt/data leaking、jailbreaking、训练数据投毒、后门等模型特有风险。

## 主要风险
- Prompt Injection：用户输入劫持系统指令
- Data / Prompt Leaking：诱导模型泄露上下文或系统提示
- Jailbreaking：绕过安全策略
- Data Poisoning / Backdoors：污染训练或微调数据

## 防御思路
- 红队测试与安全评估（如 garak）
- 工具调用白名单、参数校验、权限隔离
- 生产观测：记录输入、输出、工具调用与异常行为
- 参考 OWASP LLM Top 10 建立基线

## 来源
- [[sources/2026-05-19-mlabonne-llm-course]]
