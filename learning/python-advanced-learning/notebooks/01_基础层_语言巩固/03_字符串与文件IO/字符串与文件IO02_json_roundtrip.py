# 练习时可先遮住实现自行编写。
"""文件与 JSON：安全写入再读回。"""
import json
from pathlib import Path

def roundtrip_config(tmp: Path, obj: dict) -> dict:
    pass
if __name__ == '__main__':
    p = Path(__file__).resolve().parent / '_tmp_json'
    p.mkdir(exist_ok=True)
    data = {'a': 1, '嵌套': {'b': [2, 3]}}
    assert roundtrip_config(p, data) == data
    print('ok')
