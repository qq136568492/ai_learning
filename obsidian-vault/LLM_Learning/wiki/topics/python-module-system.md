---
type: topic
created: 2026-05-13
updated: 2026-05-13
tags: [python, modules, packages, import]
source_count: 1
---

# Python 模块系统

Python 代码组织、分发和复用的完整体系。

## 层级结构

```
脚本 (.py)
  └── 模块 (一个 .py 文件)
        └── 包 (含 __init__.py 的目录)
              └── 子包 (嵌套目录)
```

## 导入机制

### 导入发生了什么

1. 在 `sys.path` 中搜索模块
2. 找到后执行模块代码（仅首次）
3. 创建模块对象，绑定到导入者的命名空间

### sys.path 搜索顺序

1. 脚本所在目录
2. `PYTHONPATH` 环境变量
3. 标准库目录
4. site-packages（第三方包）

### 缓存

- 编译为 `__pycache__/*.cpython-311.pyc`
- 按源文件修改时间判断是否过期
- 只加快加载速度，不加快运行速度

## 包的组织

### 常规包

```
mypackage/
    __init__.py      # 必须存在
    module_a.py
    subpackage/
        __init__.py
        module_b.py
```

### `__init__.py` 的作用

- 标记目录为包
- 包被导入时执行
- 可定义 `__all__` 控制 `from package import *`
- 可做包级初始化

### 相对导入 vs 绝对导入

```python
# 绝对导入（推荐）
from mypackage.subpackage import module_b

# 相对导入（包内部使用）
from . import sibling_module
from .. import parent_module
from ..other_sub import something
```

## `__name__` 与入口点

```python
if __name__ == "__main__":
    main()
```

- 直接运行：`__name__` = `"__main__"`
- 被导入：`__name__` = 模块名
- 这个模式让文件既能当脚本又能当模块

## 命名空间隔离

- 每个模块有独立的全局命名空间
- 模块内的名称不会与其他模块冲突
- 通过 `module.name` 访问其他模块的名称

## 依赖管理

| 工具 | 用途 |
|------|------|
| pip | 安装/卸载包 |
| venv | 创建隔离环境 |
| requirements.txt | 锁定依赖版本 |
| PyPI | 包仓库 |

详见 [[concepts/virtual-environment]]。

## 相关页面

- [[concepts/modules-and-packages]] — 语法细节
- [[concepts/virtual-environment]] — 环境隔离

## 来源

- [[sources/2026-05-13-python311-tutorial]]
