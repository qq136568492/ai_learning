# 练习时可先遮住实现自行编写。
"""占位：永远不要硬编码 API Key；仅从环境读取。"""
import os

def resolve_api_key() -> str | None:
    pass
if __name__ == '__main__':
    os.environ.setdefault('PYTHON_JINJIE_OPENAI_API_KEY', 'stub')
    assert isinstance(resolve_api_key(), str)
    print('ok')
