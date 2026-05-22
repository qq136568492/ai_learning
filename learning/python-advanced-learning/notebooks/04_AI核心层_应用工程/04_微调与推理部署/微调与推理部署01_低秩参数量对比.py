# 练习时可先遮住实现自行编写。
"""LoRA 概念：低秩分解参数计数对比（玩具）。"""

def full_params(in_dim: int, out_dim: int) -> int:
    pass

def lora_params(in_dim: int, out_dim: int, r: int) -> int:
    pass
if __name__ == '__main__':
    assert full_params(1024, 1024) > lora_params(1024, 1024, r=8)
    print('ok')
