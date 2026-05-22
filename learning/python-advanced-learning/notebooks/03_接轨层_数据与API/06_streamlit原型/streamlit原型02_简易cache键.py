# 练习时可先遮住实现自行编写。
"""TTL 近似缓存键：把时间桶化。"""

def bucket_key(prompt: str, minute_bucket: int) -> str:
    pass
if __name__ == '__main__':
    assert bucket_key('  Hi ', 12) == '12:hi'
    print('ok')
