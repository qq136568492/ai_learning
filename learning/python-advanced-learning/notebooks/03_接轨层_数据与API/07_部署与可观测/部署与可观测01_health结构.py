# 练习时可先遮住实现自行编写。
"""健康检查数据结构：就绪需模型已加载标记。"""

def build_status(model_loaded: bool, db_ok: bool) -> dict[str, bool]:
    pass
if __name__ == '__main__':
    assert build_status(True, False)['ready'] is False
    assert build_status(True, True)['ready'] is True
    print('ok')
