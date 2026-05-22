# 练习时可先遮住实现自行编写。
"""习题（继承）：`Shape` → `Rect` → `Square`。

- `Rect(w, h)`：保存宽高，`area()` 返回 `w * h`。
- `Square(side)`：用 `super().__init__(side, side)` 交给 `Rect`，不写自己的 `area` 亦可。
- `Shape.area()`：占位即可，可用 `raise NotImplementedError`。

通过：运行脚本，`Rect(2,5).area()==10`，`Square(3).area()==9`，并完成下方 `assert`。"""
from __future__ import annotations


class Shape:
    """平面图形基类：`area()` 由子类实现。"""

    def area(self) -> float:
        raise NotImplementedError("请在子类中实现 area")


class Rect(Shape):
    """长方形：宽 × 高。"""

    def __init__(self, w: float, h: float) -> None:
        self.width = w
        self.height = h

    def area(self) -> float:
        return self.width * self.height

class Square(Rect):
    """正方形：等价于 Rect(side, side)。"""

    def __init__(self, side: float) -> None:
        super().__init__(side, side)

if __name__ == "__main__":
    assert Rect(2.0, 5.0).area() == 10.0
    assert Square(3.0).area() == 9.0
    assert isinstance(Square(3.0), Rect)
    assert isinstance(Square(3.0), Shape)
    print("ok")
