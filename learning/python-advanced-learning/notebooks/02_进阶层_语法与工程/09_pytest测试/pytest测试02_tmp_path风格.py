# 练习时可先遮住实现自行编写。
"""临时目录 + 断言文件存在（轻量集成）。"""
from pathlib import Path

def write_echo(tmp: Path, name: str, text: str) -> Path:
    pass
if __name__ == '__main__':
    d = Path(__file__).resolve().parent / '_pytest_tmp'
    d.mkdir(exist_ok=True)
    f = write_echo(d, 'echo.txt', 'hi')
    assert f.read_text(encoding='utf-8') == 'hi'
    print('ok')
