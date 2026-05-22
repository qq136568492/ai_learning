---
type: topic
created: 2026-05-13
updated: 2026-05-13
tags: [python, fundamentals]
source_count: 1
---

# Python 基础语法总览

跨章节综述 Python 语言的基础语法体系，适合快速回顾或作为学习路线图。

## 语言特征

Python 是一门**解释型、动态类型、多范式**的语言。核心设计选择：

- 缩进定义代码块（不用花括号）
- 一切皆对象（函数、类、模块都是对象）
- 赋值是绑定引用，不是复制数据
- Duck typing：关注行为而非类型

## 学习路径

```
基础类型 → 控制流 → 函数 → 数据结构 → 模块 → 类 → 异常 → 标准库
```

### 第一阶段：能写脚本

| 知识点 | wiki 页面 |
|--------|-----------|
| 数字、字符串、列表 | [[concepts/data-types]] |
| if/for/while | [[concepts/control-flow]] |
| 函数定义与调用 | [[concepts/functions]] |
| 文件读写 | [[concepts/file-io]] |

### 第二阶段：能写模块

| 知识点 | wiki 页面 |
|--------|-----------|
| 列表推导式 | [[concepts/list-comprehension]] |
| 元组、集合、字典 | [[concepts/data-types]] |
| 模块与包 | [[concepts/modules-and-packages]] |
| 异常处理 | [[concepts/exception-handling]] |
| 字符串格式化 | [[concepts/string-formatting]] |

### 第三阶段：能写库

| 知识点 | wiki 页面 |
|--------|-----------|
| 类与 OOP | [[concepts/classes-and-oop]] |
| 迭代器与生成器 | [[concepts/iterators-and-generators]] |
| 标准库 | [[concepts/standard-library]] |
| 虚拟环境与包管理 | [[concepts/virtual-environment]] |

## 编码风格（PEP 8）

- 缩进：4 空格
- 行宽：≤ 79 字符
- 命名：类用 `UpperCamelCase`，函数/变量用 `snake_case`
- 空行：函数/类之间 2 行，方法之间 1 行
- 导入：每行一个，分组（标准库 / 第三方 / 本地）

## 来源

- [[sources/2026-05-13-python311-tutorial]]
