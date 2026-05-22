# 练习时可先遮住实现自行编写。
"""工具描述：name/docstring → OpenAI tools JSON 草案（离线）。"""
from __future__ import annotations
from typing import Any

def tool_schema_stub(name: str, description: str) -> dict[str, Any]:
    pass
if __name__ == '__main__':
    schema = tool_schema_stub('weather', 'get weather by city')
    assert schema['function']['name'] == 'weather'
    print('ok')
