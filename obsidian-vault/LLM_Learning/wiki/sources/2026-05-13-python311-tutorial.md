---
type: source
created: 2026-05-13
updated: 2026-05-13
tags: [python, tutorial, official-docs]
source_url: https://docs.python.org/zh-cn/3.11/tutorial/index.html
source_path: raw/Python3.11_官方文档.md
---

# Python 3.11 官方教程（中文版）

17 页合并的完整教程，覆盖 Python 语言从入门到中级的核心知识。

## 元信息

- 来源：Python 官方文档中文翻译
- 版本：Python 3.11
- 页数：17 页合并
- 性质：语言教程（非 API 参考）

## 核心内容（按章节）

1. **语言定位**：解释型、动态类型、面向对象、高级数据结构、跨平台
2. **基础类型**：int、float、str（不可变）、list（可变）
3. **控制流**：if/elif/else、for（迭代序列）、while、match（模式匹配，3.10+）
4. **函数系统**：def、默认参数、关键字参数、*args/**kwargs、lambda、位置参数 `/`、仅关键字参数 `*`、docstring、类型注解
5. **数据结构**：list 方法、列表推导式、tuple、set、dict、deque
6. **模块与包**：import 机制、`__name__`、`sys.path`、`__init__.py`、相对导入
7. **I/O**：f-string、str.format()、文件读写（with 语句）
8. **异常处理**：try/except/else/finally、raise、自定义异常、ExceptionGroup
9. **类与 OOP**：命名空间与作用域、类定义、继承、多重继承、私有变量（name mangling）、迭代器协议（`__iter__`/`__next__`）、生成器（yield）、生成器表达式
10. **标准库精选**：os、glob、re、math、random、datetime、collections、logging、threading
11. **虚拟环境**：venv、pip install/freeze/uninstall

## 关键要点

- Python 的 for 循环是迭代器模式，不是 C 风格计数循环
- 默认参数只在函数定义时求值一次（可变默认值陷阱）
- 赋值不复制数据，变量是对象的引用（"对象引用调用"）
- 字符串不可变，列表可变——这是核心设计决策
- match 语句（3.10+）支持结构化模式匹配，远超 switch/case
- 生成器是创建迭代器的简洁方式，用 yield 惰性产出值
- `__init__.py` 使目录成为包（namespace package 除外）

## 涉及的 wiki 页面

- [[concepts/data-types]]
- [[concepts/control-flow]]
- [[concepts/functions]]
- [[concepts/list-comprehension]]
- [[concepts/modules-and-packages]]
- [[concepts/classes-and-oop]]
- [[concepts/exception-handling]]
- [[concepts/iterators-and-generators]]
- [[concepts/string-formatting]]
- [[concepts/virtual-environment]]
- [[entities/python]]
- [[topics/python-fundamentals]]
- [[topics/python-data-model]]
- [[topics/python-module-system]]
