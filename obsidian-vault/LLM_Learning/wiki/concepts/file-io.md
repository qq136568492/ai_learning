---
type: concept
created: 2026-05-13
updated: 2026-05-13
tags: [python, io, file]
source_count: 1
---

# 文件 I/O

Python 的文件读写操作。

## 打开文件

```python
f = open('file.txt', 'r', encoding='utf-8')
```

### 模式

| 模式 | 含义 |
|------|------|
| `'r'` | 只读（默认） |
| `'w'` | 写入（覆盖） |
| `'a'` | 追加 |
| `'x'` | 排他创建（文件已存在则失败） |
| `'b'` | 二进制模式（与上述组合，如 `'rb'`） |
| `'+'` | 读写（与上述组合，如 `'r+'`） |

## with 语句（推荐）

```python
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# 离开 with 块后文件自动关闭
```

- 即使发生异常也能正确关闭文件
- 不需要手动调用 `f.close()`

## 读取方法

```python
f.read()          # 读取全部内容为字符串
f.read(size)      # 读取 size 个字符/字节
f.readline()      # 读取一行（含换行符）
f.readlines()     # 读取所有行为列表

# 逐行迭代（内存高效）
for line in f:
    process(line)
```

## 写入方法

```python
f.write(string)       # 写入字符串，返回写入字符数
f.writelines(lines)   # 写入字符串列表（不自动加换行）
```

- `write()` 不自动添加换行符
- 非字符串值需先转换：`f.write(str(value))`

## 文件位置

```python
f.tell()          # 返回当前位置
f.seek(offset)    # 移动到指定位置
f.seek(0)         # 回到文件开头
```

## JSON 序列化

```python
import json

# 写入
json.dump(data, f)
json_string = json.dumps(data)

# 读取
data = json.load(f)
data = json.loads(json_string)
```

## 编码注意事项

- 始终显式指定 `encoding='utf-8'`（平台默认编码可能不同）
- 二进制文件用 `'rb'`/`'wb'` 模式，不指定 encoding

## 来源

- [[sources/2026-05-13-python311-tutorial]]
