---
type: concept
created: 2026-05-13
updated: 2026-05-13
tags: [python, stdlib]
source_count: 1
---

# 标准库精选

Python 自带的常用标准库模块概览。

## 操作系统接口 — os

```python
import os
os.getcwd()              # 当前工作目录
os.chdir('/path')        # 切换目录
os.listdir('.')          # 列出目录内容
os.mkdir('new_dir')      # 创建目录
os.environ['HOME']       # 环境变量
```

> [!tip] 推荐用 `shutil` 做高级文件操作（复制、移动、删除目录树）

## 文件通配符 — glob

```python
import glob
glob.glob('*.py')        # 当前目录所有 .py 文件
glob.glob('**/*.md', recursive=True)  # 递归搜索
```

## 正则表达式 — re

```python
import re
re.findall(r'\d+', text)         # 找所有数字
re.sub(r'\s+', ' ', text)        # 替换空白
match = re.match(r'(\w+)', text) # 匹配开头
```

- 简单操作优先用字符串方法（`str.replace`、`str.split`）

## 数学 — math / random

```python
import math
math.sqrt(16)       # 4.0
math.pi             # 3.14159...
math.log(e)         # 自然对数

import random
random.choice(['a', 'b', 'c'])
random.randint(1, 100)
random.shuffle(list)
```

## 日期时间 — datetime

```python
from datetime import date, timedelta
today = date.today()
birthday = date(1990, 5, 13)
age = today - birthday  # timedelta 对象
```

## 数据压缩 — zlib

```python
import zlib
compressed = zlib.compress(b'data')
original = zlib.decompress(compressed)
```

其他：`gzip`、`bz2`、`zipfile`、`tarfile`

## 性能测量 — timeit

```python
from timeit import Timer
Timer('a, b = b, a+b', 'a=1; b=1').timeit()
```

## 质量控制 — doctest / unittest

```python
# doctest: 在 docstring 中嵌入测试
def average(values):
    """
    >>> average([20, 30, 70])
    40.0
    """
    return sum(values) / len(values)

# unittest: 独立测试文件
import unittest
class TestAvg(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
```

## 日志 — logging

```python
import logging
logging.warning('Watch out!')
logging.info('Informational message')
```

- 比 print 更灵活：级别过滤、输出到文件、格式化

## 多线程 — threading

```python
import threading

def worker():
    print('working')

t = threading.Thread(target=worker)
t.start()
```

- GIL 限制：CPU 密集型任务用 `multiprocessing`
- I/O 密集型任务适合多线程

## 集合工具 — collections

- `deque`：双端队列（高效两端操作）
- `Counter`：计数器
- `defaultdict`：带默认值的字典
- `namedtuple`：具名元组

## 来源

- [[sources/2026-05-13-python311-tutorial]]
