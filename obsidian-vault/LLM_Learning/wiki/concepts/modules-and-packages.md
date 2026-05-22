---
type: concept
created: 2026-05-13
updated: 2026-05-13
tags: [python, modules, packages, import]
source_count: 1
---

# 模块与包

Python 的代码组织和复用机制。

## 模块

一个 `.py` 文件就是一个模块。模块名 = 文件名（去掉 `.py`）。

### 导入方式

```python
import fibo                    # 导入模块，用 fibo.fib() 访问
from fibo import fib, fib2     # 导入特定名称
from fibo import *             # 导入所有（不推荐）
import fibo as f               # 别名
from fibo import fib as fibonacci  # 名称别名
```

### 模块执行

- 模块代码在首次 import 时执行一次
- 每个模块有独立的全局命名空间
- `__name__`：被导入时为模块名，直接运行时为 `"__main__"`

```python
if __name__ == "__main__":
    # 仅在直接运行时执行
    main()
```

### 模块搜索路径（sys.path）

1. 脚本所在目录（或当前目录）
2. `PYTHONPATH` 环境变量
3. 安装默认路径（含 site-packages）

### 编译缓存

- 自动缓存为 `__pycache__/module.cpython-311.pyc`
- 按源文件修改时间判断是否过期
- `.pyc` 只加快加载速度，不加快运行速度

## 包

用目录层级组织模块的方式。

### 结构

```
sound/
    __init__.py          # 使目录成为包
    formats/
        __init__.py
        wavread.py
    effects/
        __init__.py
        echo.py
```

### `__init__.py`

- 使目录被识别为包（namespace package 除外）
- 可以为空，也可执行初始化代码
- 可定义 `__all__` 控制 `from package import *` 的行为

### 导入子模块

```python
import sound.effects.echo
from sound.effects import echo
from sound.effects.echo import echofilter
```

### 相对导入

```python
from . import echo           # 同级
from .. import formats       # 上级
from ..filters import equalizer  # 上级的子模块
```

- 基于当前模块的 `__name__`
- 主模块（`__main__`）不能使用相对导入

## dir() 函数

- `dir(module)`：列出模块定义的所有名称
- `dir()`：列出当前作用域的名称
- 不列出内置名称（在 `builtins` 模块中）

## 来源

- [[sources/2026-05-13-python311-tutorial]]
