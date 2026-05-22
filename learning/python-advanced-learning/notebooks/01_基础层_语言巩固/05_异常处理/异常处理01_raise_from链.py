# 练习时可先遮住实现自行编写。
"""异常：链式 raise ... from ..."""

class ParseError(Exception):
    pass

def parse_int(s: str) -> int:
    pass
if __name__ == '__main__':
    try:
        parse_int('12a')
    except ParseError as e:
        assert isinstance(e.__cause__, ValueError)
    else:
        raise AssertionError
    print('ok')
