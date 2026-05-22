# 练习时可先遮住实现自行编写。
"""logging：MemoryHandler 捕捉记录。"""
import logging
from logging.handlers import MemoryHandler

def capture_logs() -> list[str]:
    pass
if __name__ == '__main__':
    lines = capture_logs()
    assert lines[0].startswith('INFO:boot')
    assert lines[1].startswith('ERROR:fail')
    print('ok')
