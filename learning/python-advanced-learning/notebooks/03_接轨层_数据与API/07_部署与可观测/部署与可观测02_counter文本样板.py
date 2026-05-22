# 练习时可先遮住实现自行编写。
"""Prometheus text 格式的 Counter 单行（手写字符串）。"""

def fmt_counter(name: str, labels: dict[str, str], value: float) -> str:
    pass
if __name__ == '__main__':
    s = fmt_counter('http_requests_total', {'route': '/v1/chat'}, 3.0)
    assert 'route="/v1/chat"' in s and s.endswith(' 3.0')
    print('ok')
