# Q&A Records

## [2026-05-21 20:51:02] Q: 创建一个SKILL，当向大模型提问时 或者要求生成文档时，优先检索obsidian知识库。如果检索到相关内容，则参考obsidian知识库的内容，并且在输出时 显示输出参考了知识库的哪些内容。当提问时，让obsidian将问题吸收。
- Context: Codex skill creation / Obsidian knowledge bridge
- Hits:
  - D:\Python_WorkSpace\Learning_Project\AGENTS.md
  - D:\Python_WorkSpace\Learning_Project\learning\python-advanced-learning\obsidian_bridge.md
  - D:\Python_WorkSpace\Learning_Project\learning\python-advanced-learning\README_python_jinjie.md
- Answer-Summary: 创建了 Codex skill obsidian-knowledge-bridge。该技能要求在回答问题或生成文档前优先检索本地 Obsidian Markdown 知识库；若命中相关内容，输出中列出使用的本地知识库来源；回答后将问题、命中、摘要和引用追加到 Obsidian qa-records.md 与 log.md。技能包含 scripts/obsidian_bridge.py，用于本地检索和问答记录写回。
- References:
  - C:\Users\Lenovo\.codex\skills\obsidian-knowledge-bridge\SKILL.md
  - C:\Users\Lenovo\.codex\skills\obsidian-knowledge-bridge\scripts\obsidian_bridge.py

## [2026-05-22 12:00:00] Q: 根据mcp server的网址 把mcp添加到cursor中（Web Fetching / Fetch）
- Context: Learning_Project / Cursor MCP 配置
- Hits:
  - D:\Python_WorkSpace\Learning_Project\.cursor\mcp.json
  - D:\Python_WorkSpace\Learning_Project\.cursor\skills\fetch-url-bundle-docs\SKILL.md
- Answer-Summary: 根据 cursormcp.dev Web Fetching 标签页，为项目添加 Anthropic 官方 Fetch MCP（mcp-server-fetch）。本机已 pip 安装该包，故在 .cursor/mcp.json 中使用 python -m mcp_server_fetch，并设置 Windows 推荐的 PYTHONIOENCODING=utf-8。配置完成后需重载 Cursor 窗口使 MCP 生效。
- References:
  - https://cursormcp.dev/tag/web-fetching
  - https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
  - D:\Python_WorkSpace\Learning_Project\.cursor\mcp.json
