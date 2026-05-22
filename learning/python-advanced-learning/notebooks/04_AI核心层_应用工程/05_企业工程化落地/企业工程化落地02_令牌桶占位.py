# 练习时可先遮住实现自行编写。
"""令牌桶：固定窗口占位（毫秒时间戳 buckets）。"""

def requests_allowed(timestamps_ms: list[int], *, window_ms: int, limit: int) -> bool:
    """极简占位：同一时间窗内计数不超过 limit（输入已按时间排序）。"""
    pass

def simple_bucket(now_ms: int, window_ms: int) -> int:
    pass
