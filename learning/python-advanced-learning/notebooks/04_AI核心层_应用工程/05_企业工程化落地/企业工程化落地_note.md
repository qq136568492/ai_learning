# 企业级 AI 工程化落地｜讲义笔记（阶段精读）

<参考资料>

- `obsidian-vault/LLM_Learning/wiki/concepts/api-security.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/deployment-strategy.md`
- `obsidian-vault/LLM_Learning/wiki/topics/enterprise-llm-engineering-roadmap.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **N**

CI/CD、密钥：**GitHub Actions**、Vault、云 KMS——均为外部系统，本节只给 **对齐清单**，不替代各云厂商操作手册。

</参考资料>

---

## 本地知识库命中（与本节对齐）

- 同 `<参考资料>` 所列路径（api-security、deployment-strategy、enterprise-llm-engineering-roadmap、学习地图 **N**）。

---

## 上一章核心收获回顾（衔接「微调 / 推理」）

你已能拆开 **微调成本** 与 **在线推理 SLA** 两笔账。

你已理解：**吞吐、延迟与量化取舍**连在一起谈才有意义。

你已知道：**adapter / LoRA** 常是专有领域的折中打法。

你已准备：**把整条 LLM 子系统**，放进 **SOC2 风格可追溯**的工程约束——而不只是 Jupyter 能用。

---

## 但是，我们遇到了一个新的问题……

模型仅占系统一隅：**密钥、漂移、成本控制、法务、回放、人在回路**。**因此本章需要：**对齐 **密钥轮换、Prompt/配置版本化、RBAC、harness 评测、gitleaks、PII、配额与账本**。 

---

## 动机：**可追责、能睡觉**——出事知道谁改了什么配置、钱花在哪、样本有没有越权出境。

---

## 类比（非编程）

餐饮店：**大厨（模型）**再强，也需 **出纳、门禁、供货商合同、卫生台账**齐备。 

---

## 精讲（MECE 清单口吻）

| 域 | 你应落地的最小条目 |
|---|---------------------|
| 密钥 | 环境挂载、Vault/KMS、禁止写仓库与镜像 |
| CI | **`pytest`、`ruff`/lint、镜像扫描、gitleaks** |
| 数据 | **PII 标注、红线出境、采样脱敏日志**|
| 成本 | tokens/$ 面板、租户配额、告警 |
| 漂移 | golden 题库周期跑、离线对比线上抽样 |
| 人在回路 | 高危写操作二次确认、审批留痕 |

---

## 陷阱（≥2）：成因 → 改法

1. **只靠 prompt 实现 RBAC**。**改：**网关、策略引擎、最小权限凭据。  
2. **无成本监控**直至账单爆雷。**改：**配额、预算告警、缓存与批处理。  

---

## 适用范围 · 延伸

与 **部署与可观测**、**LLM 调用**、**RAG 索引治理**三节交叉——企业章是横切收口。

---

## 双重示例

### A. **Secrets：三选一方式表**

各写一行心智：**Vault / 云 KMS / SealedSecrets**适用的团队成熟阶段。

### B. **CI 伪 jobs**

示意：`pytest` → `docker build` → `helm template` lint（任选一条链写伪 YAML）。

---

## 练习

- **基础**：自拟 **PII + 出境** checklist ≥5 条。  

- **开放**：**Red‑team**：假设提示词注入成功案例，三道防线各是谁？  

---

## 费曼反问

1. 可观测三类信号你如何分工给 **LLM 平台**各组件？  
2. **哪一种动作**必须坚持人在回路？  
3. Prompt 版本化最接近传统工程的哪条实践（分支/发布/配置中心）？

---

> **闭环**：口述 **四类「非模型本身」却必须写进运维手册的风险**。 
