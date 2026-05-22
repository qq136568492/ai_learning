# 练习时可先遮住实现自行编写。
"""习题（组合/依赖注入）：`Service` 不负责「怎么加」，只负责**持有**一个会加法的对象。

- `AdderBackend`：基类，`add(a,b)` 返回两数之和（已实现，可视为默认实现）。
- `BuiltinAdder`：继承基类；在 `add` 里用 **`super().add(a, b)`** 复用父类逻辑（练 `super`）。
- `Service`：构造时**注入** `backend: AdderBackend`（存到 `self`）；`combine(a,b)` 应**转调**
  `self` 上保存的 `backend.add(a, b)`，不要自己再写 `a + b`。

通过：运行脚本，`Service(BuiltinAdder()).combine(2, 3) == 5`，打印 `ok`。"""

class AdderBackend:

    def add(self, a: int, b: int) -> int:
        return a + b

class BuiltinAdder(AdderBackend):

    def add(self, a: int, b: int) -> int:
        return super().add(a, b)

class Service:

    def __init__(self, backend: AdderBackend) -> None:
        self._backend = backend

    def combine(self, a: int, b: int) -> int:
        return self._backend.add(a, b)

if __name__ == '__main__':
    s = Service(BuiltinAdder())
    assert s.combine(2, 3) == 5
    print('ok')
