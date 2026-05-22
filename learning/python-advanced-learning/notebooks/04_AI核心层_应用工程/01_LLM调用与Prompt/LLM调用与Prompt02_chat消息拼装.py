# 练习时可先遮住实现自行编写。
"""Chat messages 组装顺序：system 在前。"""

def build_messages(system: str, user: str) -> list[dict[str, str]]:
    pass
if __name__ == '__main__':
    m = build_messages('You are helpful.', 'Hi')
    assert m[0]['role'] == 'system'
    print('ok')
