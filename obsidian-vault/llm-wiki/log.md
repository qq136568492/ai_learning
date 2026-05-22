# LLM Wiki Log
- [2026-05-21 20:51:02] Codex skill creation / Obsidian knowledge bridge: 创建一个SKILL，当向大模型提问时 或者要求生成文档时，优先检索obsidian知识库。如果检索到相关内容，则参考obsidian知识库的内容，并且在输出时 显示输出参考了知识库的哪些内容。当提问时，让obsidian将问题吸收。 -> 创建了 Codex skill obsidian-knowledge-bridge。该技能要求在回答问题或生成文档前优先检索本地 Obsidian Markdown 知识库；若命中相关内容，输出中列出使用的本地知识库来源；回答后将问题、命中、摘要和引用追加到 Obsidian qa-records.md 与 log.md。技能包含 scripts/obsidian_bridge.py，用于本地检索和问答记录写回。
- [2026-05-22 12:00:00] Cursor MCP / Fetch: 根据 cursormcp.dev Web Fetching 标签，为 Learning_Project 配置官方 Fetch MCP（python -m mcp_server_fetch + PYTHONIOENCODING）。
