# 部署与可观测｜讲义笔记

<参考资料>

- https://docs.python.org/3/library/logging.html
- Docker：`https://docs.docker.com/`（**外部**）
- `obsidian-vault/LLM_Learning/wiki/concepts/deployment-strategy.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/api-security.md`

```bash
pip install prometheus-client opentelemetry-api   # 可选进阶
```

生产 **HTTPS** 往往在 **`nginx`/云 LB** 终止，本节只要求建立心智。

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/deployment-strategy.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/api-security.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **I**

---

## 上一章核心收获回顾（衔接「Streamlit 原型 → 要扛生产 SLA」）

你能 **五分钟出原型**，并已接触 **pandas / HTTP 占位对接**。

你已写过 **结构化日志**初稿：**`logging.getLogger`** 层次与级别。

你已理解：**venv / 依赖 / 配置文件**要上服务器，不能只靠 **`--reload` 开发者模式**糊弄。

你已准备：**容器边界、进程模型、探活、最基本的指标/trace 心智**接轨运维同事的语言。

你已知道：**密钥不进仓库**应与 **十二要素 / K8s Secret**对齐。

---

## 但是，我们遇到了一个新的问题……

笔记本里 **`uvicorn --reload`** 绝不等于 **SLA**。**因此本章需要：** Dockerfile 多阶段、非 root、`PYTHONUNBUFFERED`、workers 大致与 CPU、`readiness/liveness`、`/healthz`、结构化日志、`metrics`/trace ID 延伸阅读。

---

## 动机：**要能值班**：半夜报警时你敢不敢重启、知不知道是否「依赖挂了却还在瞎接流量」？

---

## 类比（非编程）

从家里 Wi‑Fi 玩具路由搬到写字楼：**物业、UPS、门禁、监控**各司其职。

---

## 精讲（由浅入深）

- **镜像**：拷贝依赖、`COPY` 应用、`CMD` **显式监听 `0.0.0.0`**。  
- **进程**：Uvicorn / Gunicorn workers 选型 —— CPU 绑定与同步/异步语义请读部署 wiki。  
- **探活**：**readiness**（依赖齐备才接流量）与 **liveness**（进程不健康则重启）。  
- **可观测**：**日志（事件） / 指标（速率、直方） / 链路追踪**三位一体入门。

---

## 辨析（探活）

| 概念 | **readiness（就绪）** | **liveness（存活）** |
|------|------------------------|---------------------|
| 问什么 | 依赖齐了吗？能接流量吗？ | 还在喘气吗？ |
| 典型 | DB 不可用 ⇒ 摘掉 Service | 死锁 ⇒ 杀 Pod |

---

## 陷阱（≥2）：成因 → 改法

1. **stdout 非结构化**。 — JSON 字段 + **`request_id`**。  
2. **SECRET bake 进镜像层**。**改：**挂载卷 / KMS / CI 注入。

---

## 双重示例

### A. **一行 JSON 日志（标准库）**

```python
import json
import time

line = {"ts": time.time(), "level": "INFO", "event": "ready", "service": "demo"}
print(json.dumps(line, ensure_ascii=False))
```

### B. **最小 Dockerfile + `/healthz`**

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app ./app
ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
def health():
    return {"ok": True}
```

验证：**`curl -sf http://127.0.0.1:8000/healthz`**（镜像内未装 **`curl`** 时常改由编排发起 HTTP GET）。

---

## 适用范围 · 延伸

容器编排、`stdout` 聚合。**Prometheus**/ **OpenTelemetry**：地图 **I** 后续精读。

---

## 练习

- **基础**：本机 **`docker build` + `docker run -p 8000:8000`。  

- **进阶**：ASCII 拓扑 **TLS 终结 → 反向代理 → app workers**。  

- **开放**：一页 **Threat model**：密钥 / 日志脱敏 / PII。

---

## 费曼反问

1. readiness 与 liveness 各举一个 **真实事故**语义。  
2. 为何生产环境禁用 **`--reload`**？  
3. 三类 **可观测信号**各管什么？

---

> **闭环**：复述 **五条「最小能上生产」checklist**。 
