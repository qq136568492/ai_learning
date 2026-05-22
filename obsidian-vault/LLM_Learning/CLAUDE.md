# LLM_Learning — Schema

这是一个**AI 学习知识库**，采用 Karpathy 的 LLM Wiki 模式构建。LLM 负责维护 wiki，人类负责采集 source、提问、决定学习方向。

核心理念：LLM 每接收一个新 source 就把它整合进现有 wiki，知识持续累积而非每次查询时重新检索。wiki 是一个持续演化的、结构化的 markdown 集合，坐在用户和原始资料之间。

---

## 三层架构

```
LLM_Learning/
├── CLAUDE.md              # 本文件（schema，LLM 的工作手册）
├── raw/                   # 第一层：原始素材（只读）
│   ├── assets/            # 图片、附件
│   └── *.md / *.pdf       # 文章、教程、论文、网页快照
└── wiki/                  # 第二层：LLM 生成与维护的知识页面
    ├── index.md           # 全部页面目录，按类别组织
    ├── log.md             # 时间倒序记录 ingest / query / lint
    ├── overview.md        # 当前学习主题的综合叙述（随 ingest 演化）
    ├── sources/           # 每条 raw 对应一页：摘要 + 要点 + 链接
    ├── concepts/          # 概念、术语、方法
    ├── entities/          # 具体实体：人物、组织、论文、产品、工具
    ├── topics/            # 跨 source 的主题综述
    └── questions/         # 用户提问 + LLM 回答，回填为页面
```

**第三层是本文件（schema）**：告诉 LLM wiki 的结构、约定和工作流。

**`raw/` 只读**。LLM 从 raw 读取信息，但绝不修改或删除其中的文件。
**`wiki/` 由 LLM 完全拥有**：创建、更新、重组、删除都允许。

---

## 命名约定

- 小写 kebab-case：`retrieval-augmented-generation.md`
- ISO 日期：`2026-05-13`
- source 页建议前缀日期：`wiki/sources/2026-05-13-paper-title.md`
- 中文页面也用拼音/英文文件名，标题里再写中文

---

## Frontmatter（每个 wiki 页面顶部必须有）

```yaml
---
type: source | concept | entity | topic | question | overview
created: 2026-05-13
updated: 2026-05-13
tags: []
source_count: 0           # concepts/entities/topics 页用：引用了多少 source
source_url:                # sources 页用：原文 URL
source_path:               # sources 页用：raw/ 内路径
---
```

---

## Wikilinks

- 页面内互链一律用 `[[page-name]]`
- 第一次提到 entity/concept 必须链接
- 不要链接到不存在的页面。如果需要引用但还没写，先创建 stub（3 行占位 + `type` + `tags: [stub]`），再链接

---

## 工作流

### Ingest（处理新 source）

触发：用户说「处理/消化/ingest 这个文件/链接」，或把东西放进 `raw/`。

1. 读取 `raw/` 里的文件或 URL（URL 优先用 `defuddle` skill 抽正文）
2. 和用户讨论 1-3 个要点（不自作主张）
3. 在 `wiki/sources/` 新建摘要页：
   - 标题 + 元信息
   - 核心论点（3-5 条）
   - 关键证据 / 数据
   - 和现有 wiki 的连接（哪些 concept/entity 出现了）
4. 提取涉及的 concepts / entities，更新或新建对应页面
5. 更新相关 `wiki/topics/` 综述
6. 如果这条 source 改变了主线叙述，更新 `wiki/overview.md`
7. 更新 `wiki/index.md`
8. 在 `wiki/log.md` 最顶部追加：`## [YYYY-MM-DD] ingest | 标题`

一条 source 通常触及 5-15 个页面。慢一点没关系，宁可多更新也不要漏。

### Query（回答问题）

1. 先读 `wiki/index.md` 定位相关页面
2. 读这些页面（必要时追读 source 原文）
3. 回答问题，引用页面名：`参考 [[concepts/xxx]]`
4. **判断答案是否有沉淀价值**：如果这个回答综合了多个 source、揭示了新连接、或用户明确说「保存下来」——写入 `wiki/questions/YYYY-MM-DD-问题简述.md` 或更新相应 topic
5. 在 `wiki/log.md` 追加：`## [YYYY-MM-DD] query | 简短描述`

### Lint（健康检查）

用户说「lint / 体检 / 检查 wiki」时触发。逐项输出结果：

- **矛盾**：跨页面是否有冲突的事实
- **过时**：新 source 是否推翻了旧 claim
- **孤儿**：没有入链的页面
- **缺失**：高频被提及但没有独立页面的概念
- **死链**：指向不存在页面的 wikilink
- **gap**：值得搜新 source 的学习方向

不自动改，先报告给用户确认。

---

## 页面风格

- **主张要有出处**：关键事实标注来源 `([[sources/xxx]])`
- **矛盾不删除**，用 callout 标记：
  ```
  > [!warning] 冲突
  > [[sources/a]] 认为 X，[[sources/b]] 认为 Y。
  ```
- 存疑用 `> [!question] 待查证`
- 页面 > 500 行考虑拆分
- `source_count` 字段在每次关联新 source 时 +1

---

## index.md 的结构

按 type 分节组织，每页一行：

```
## overview
- [[overview]] — 主题的当前综述

## topics
- [[topics/xxx]] — 一句话摘要

## concepts
- [[concepts/xxx]] — 一句话摘要
...
```

每次 ingest 结束必须更新 index.md。

---

## log.md 的结构

append-only，最新在顶部。每条开头一致：

```
## [2026-05-13] ingest | Python 3.11 官方教程
- 新增 [[sources/2026-05-13-python311-tutorial]]
- 更新 [[concepts/list]]、[[entities/python]]
- overview 小修

## [2026-05-13] query | 列表推导式和生成器的区别
- 综合 2 个 source，写入 [[questions/2026-05-13-list-comp-vs-generator]]
```

格式统一便于 `grep "^## \[" wiki/log.md | head -20` 快速看最近动作。

---

## 和用户的分工

| 职责 | 谁 |
|-----|-----|
| 采集 source（放进 raw/） | 用户 |
| 决定学习方向、提问 | 用户 |
| 读 source、写 wiki、维护链接、写日志 | LLM |
| 审阅 wiki、纠偏、调整 schema | 用户 + LLM |

**LLM 不要替用户决定学习主题或观点倾向**。有歧义先问。

---

## 元规则

这份 schema 本身会演化。当你（LLM）发现现有约定不够用（比如新类型的 source、新的页面种类），和用户商量后修改这个文件。每次改 CLAUDE.md，都在 log.md 记一笔 `## [date] schema | 改了什么`。
