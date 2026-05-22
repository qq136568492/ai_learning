# Obsidian Bridge（Python 进阶）

## 1) 目标

将 `learning/python-advanced-learning`（原 README 口中的「python进阶」指同一子工程别名）与本机 Obsidian 知识库打通，形成：

- 问题先查本地知识库；
- 再进行学习内容生成；
- 最终把问答记录回写到 Obsidian。

## 2) 固定路径

- **主 Vault（本机）**：`D:/Obsidian/repository/Obsidian Vault`
- （若使用历史路径）顶层亦可能出现 `LLM_Learning/wiki/`：`index.md`、`log.md`、`qa-records.md` —— 请以本机 Vault 为准。
- **仓库回退（Portable）**：`obsidian-vault/LLM_Learning/wiki/`、`obsidian-vault/LLM_Learning/raw/`。

## 2.5) 本子工程 notebooks 分层

现行学习材料集中在：

`learning/python-advanced-learning/notebooks/` 下的四层目录（`_legacy_*` 为旧版快照）。Vault 条目路径在 `*_note.md` 中以「命中（生成前检索）」小节列出。

## 3) 问答记录模板（写入 Obsidian）

```markdown
## [HH:mm:ss] Q: <用户问题>
- Context: learning/python-advanced-learning
- Hits:
  - <命中文件路径1>
  - <命中文件路径2>
- Answer-Summary: <3~6 行摘要>
- References:
  - <Vault 文件路径或标题>
  - <外部 URL（如有）>
```

## 4) 执行顺序（学习会话）

1. 从 Vault 本地笔记检索答案主干；
2. 若不足再补充外部权威资料；
3. 生成/更新 `notebooks/` 学习材料；
4. 回写问答记录到 `qa-records.md` 与 `log.md`。
