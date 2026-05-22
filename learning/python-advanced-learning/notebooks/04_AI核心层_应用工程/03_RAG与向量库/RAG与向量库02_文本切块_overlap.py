# 练习时可先遮住实现自行编写。
"""RAG：切块 + overlap 占位实现。"""

def chunks(text: str, size: int, overlap: int) -> list[str]:
    pass
if __name__ == '__main__':
    s = 'abcdefghij'
    out = chunks(s, size=4, overlap=1)
    assert out[0] == 'abcd'
    print('ok')
