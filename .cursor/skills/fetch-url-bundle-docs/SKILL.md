---
name: fetch-url-bundle-docs
description: >-
  Fetches a docs index URL plus all Sphinx tutorial-style sibling `.html`
  chapters discovered under the same path prefix (e.g. Python tutorial index →
  interpreter.html, controlflow.html, …) and merges them into one Markdown
  output under the workspace. Uses project MCP Fetch server for optional
  preflight/quick single-page grabs; prefers the bundled CLI
  tools/python_doc_to_md/bundle_python_docs.py for full multi-page aggregation.
  Use when the user says 「爬取url」「爬取 URL」「抓取文档聚合」`/fetch`, or `/fetch `
  followed by an http(s) URL, or asks to MCP-fetch and merge docs sub-pages
  into one .md file.
disable-model-invocation: false
---

# MCP + 文档章节聚合抓取（`/fetch` /「爬取url」）

本 Skill 对齐 `Learning_Project/.cursor/mcp.json`：**`mcp-fetch`**（HTTP）与 **`mcp-filesystem`**（可读工作区）。

> **用户单次提示禁写 Obsidian：** 不向 Vault 追加 `qa-records` / `log`。

---

## 何时启用

在用户出现以下任一意图时载入并执行全流程：

- 「**爬取url**」「爬取文档」「抓取官方文档」「用 MCP 拉文档」；
- 「**`/fetch`**」或 「`/fetch https://…`」（斜杠指令按普通自然语言口令处理）；
- 给出 **Python tutorial / Sphinx 同级目录书籍式结构**的种子 URL，并要求 **单文件 Markdown 汇总子页面**。

---

## 判定目标类型

| 场景 | 行为 |
|------|------|
| **多页 Sphinx 索引**（`/tutorial/index.html` 等有完整章节目录） | 走 **聚合脚本**（见下）——与对同一 URL **反复调用 MCP Fetch**等价，但更省回合与令牌。 |
| **单页**/只要正文一节 | **只调 MCP Fetch**一次（`mcp-fetch`），必要时再用现有「单页」脚本 `fetch_python_doc.py`。 |
| 非 Sphinx / 小众站点 DOM | 先 MCP Fetch **种子页**判断是否可解析；无法再建议用户收窄 scope。 |

---

## 操作顺序（必读）

### 1) 与工作区 MCP 对齐

- **`mcp-fetch`**：用于按需拉取任一 http(s)；多页大批量时等价于脚本内的 `urllib` 请求（勿重复赘述「未用 MCP」，HTTP 语义一致）。
- **`mcp-filesystem`**：可对输出 Markdown 路径做复核（可读工作区）。
- CLI 生成的文件一般用 Cursor **Write / 编辑器**写入用户指定路径（与 MCP 文件服务器作用域同为 `${workspaceFolder}`）。

### 2) 聚合（推荐阅读 python.org 教程全量）

在满足依赖 `pip install -r tools/python_doc_to_md/requirements.txt` 后执行：

```bash
python tools/python_doc_to_md/bundle_python_docs.py \
  --seed "<用户粘贴的索引 URL>" \
  -o "<工作区内输出路径>.md" \
  --delay 1.0
```

可选：

- **`--recurse`**：对每个已发现子页再在 **主正文区**递归收集同前缀链接（更慢）。
- **`--max-pages`**：防爆（默认 `80`）。

脚本行为摘要：

1. **种子页**抓取后，仅在 **`role=main`（及同类）主正文**中用 `urllib.parse.urljoin` 收集 **同源 + 同级路径前缀下的 `.html`**，按 DOM 遍历顺序 **去重**；
2. 种子 **`index.html`** 会 **剔除 `.toctree-wrapper`**等整书目录块，以免与子页正文重复堆砌；
3. 每页经 `html2text` → 以一个 `##` 标题并入 **单一 Markdown**；frontmatter 中列出 **`urls` 清单**；
4. **请求间隔**：`--delay` 默认为礼貌爬虫；不要随意并发狂刷 docs.python.org。

示例（与用户给定一致）：种子 `https://docs.python.org/zh-cn/3.11/tutorial/index.html` 会拉出 `tutorial/interpreter.html`、`tutorial/controlflow.html` … 等与索引同目录的官方教程页并入一个 `.md`。官方教程入口可参考：[Python 3.11 中文教程索引](https://docs.python.org/zh-cn/3.11/tutorial/index.html)。

### 3) 可选预检（MCP Fetch）

在跑长任务前（非必须）：对 `--seed` 调一次 **`mcp-fetch`**，确认 200 / 可读；若 MCP 不可用则直接脚本同样可验证。

### 4) 结果交付

- 输出 Markdown 保存在用户给定或你提议的 **`Learning_Project/...`** 路径；
- **简短说明你合并了多少页、`--delay`/`--max-pages` 选型**；
- **不**触碰 Obsidian / `qa-records`（本次用户要求）。

---

## 纯 MCP「手工链式」备选（少用）

仅在 **页数 ≤ 3～5**且用户明示「不要脚本」时使用：

1. MCP Fetch **种子**，手抄主内容区中出现的 **tutorial/*.html（或等价）**；
2. 对每个 URL MCP Fetch；
3. 自行拼 `##`/横线分段并 **Write** 单文件；

此路径更易漏链或超令牌——默认仍 **优先脚本**。

---

## 常见问题

**Q：为何不全用 MCP 工具一条条拉？**

A：**可以**，但当教程有十几～几十个子页时会消耗大量 MCP/模型回合；脚本与 MCP Fetch **同为 HTTP GET**，只是把解析与拼装自动化。

**Q：会不会爬到 docs 站外？**

A：脚本把链接限制在 **种子 URL 所在目录前缀**；仍应尊重 [docs.python.org robots.txt](https://docs.python.org/robots.txt) 与版权说明。

**Q：单页要带 `#锚点` 的小节**

A：用 `fetch_python_doc.py`，不是本聚合脚本主业。
