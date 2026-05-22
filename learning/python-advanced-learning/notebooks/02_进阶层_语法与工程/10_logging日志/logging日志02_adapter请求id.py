# 练习时可先遮住实现自行编写。
"""LoggerAdapter 注入 request_id。"""
import logging

def build_logger() -> tuple[logging.LoggerAdapter, list[str]]:
    pass
    pass
    pass

    class ListHandler(logging.Handler):

        def emit(self, record: logging.LogRecord) -> None:
            pass
    pass
    pass
    pass
    pass
    pass
    pass
if __name__ == '__main__':
    log, buf = build_logger()
    log.info('hello')
    assert any(('hello' in s for s in buf))
    print('ok')
