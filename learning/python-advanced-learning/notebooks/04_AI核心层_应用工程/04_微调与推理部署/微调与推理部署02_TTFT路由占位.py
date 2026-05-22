# 练习时可先遮住实现自行编写。
"""TTFT 预算：若首包延迟超限则降级走小模型占位。"""

def route_model(latency_budget_ms: float, est_ttft_large_ms: float) -> str:
    pass
if __name__ == '__main__':
    assert route_model(200.0, 150.0) == 'large'
    assert route_model(200.0, 999.0) == 'small'
    print('ok')
