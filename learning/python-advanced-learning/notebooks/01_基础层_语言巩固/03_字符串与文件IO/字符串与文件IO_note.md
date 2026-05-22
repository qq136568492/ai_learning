# 字符串与文件 I/O｜讲义笔记

<参考资料>

- https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- https://docs.python.org/3/library/pathlib.html — 面向对象的跨平台路径
- https://docs.python.org/3/library/json.html
- PEP 498 — f-string（3.6+，`=` 调试后缀 3.8+）

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/concepts/string-formatting.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/file-io.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **A3 / A4**

---

## 上一章核心收获回顾（衔接「控制流」）

你能用 **`if/for/while`** 组织逻辑，并开始理解 **遍历中不要原地乱改容器**的运行时后果。

你已能拆开 JSON / CSV 等小数据集的 **逐条处理**，知道「读一行处理一行」有时是性能必需。

你已具备 **格式化输出**的早期印象（哪怕是简单拼接），并意识到 **`print`** 只适合临时查看。

你已了解 **布尔短路**可帮助避免非法索引或除零前先判断。

你已准备把视角从「内存里的小变量」切换到 **磁盘上的持久字节流**——这要求你认真面对 **编码**。

---

## 但是，我们遇到了一个新的问题……

- Windows 不写 **`encoding`** 时出现 **乱码**，因为文本模式走的是 **locale 默认编码**。  
- 把整份 **`read()`进内存**，大日志 / 巨型 JSON 会直接 **OOM**。  
- **`f-string`/日志模板**无意间把密钥或 token **插进控制台**泄漏。

**因此本章需要：**建立 **文本模式读写 + 显式 `utf-8` + `with` 资源释放 + JSON dump/load ** 的工程习惯。

---

## 动机：运维「在我机器明明是中文」的悲剧

团队协作 / CI / Docker 环境里 **不写 `encoding="utf-8"`** ⇒ `UnicodeDecodeError` 或与真实文件编码错配 ⇒ **silent 替换字符**更难查。

---

## 类比（非编程）

磁盘文件像在两国邮局间寄明信片：**信封外写邮编（字节）**，读信人心里要有 **同一种字典（encoding）**。`with`像 **借阅卡到期自动盖章归还**，避免阅览室丢书 (`fd leak`)。

---

## 精讲

### f-string vs `format` vs `Template`

| 写法 | **人话何时用** |
|------|------------------|
| **`f"...{expr}..."`** | 局部插值可读性最高 |
| **`"{:.2f}".format(x)`** | 模板与数据分离或可复用时 |
| **`string.Template`** | 占位符形如 `$who`（见官方 `string` 一章）|

### **`open` 必背四件事**

```python
from pathlib import Path

p = Path("cfg.json")
text = p.read_text(encoding="utf-8")   # pathlib 也需显式
p.write_text(text, encoding="utf-8")
```

### JSON 读写

```python
import json
from pathlib import Path

cfg = {"a": 1}
Path("cfg.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")
roundtrip = json.loads(Path("cfg.json").read_text(encoding="utf-8"))
```

术语「上下文管理 **`__exit__`** 释放资源」：**`上下文管理器_note.md`**。

---

## 辨析

| | **`read()`** | **逐行 `for line in f`** |
|--|---------------|---------------------------|
| 心智 | 「一口吞」 | **流式**：内存友好 |

| | **`str`** | **`bytes`** |
|--|-------|--------------|
| 文本模式 | ✅ | ❌（走 `'rb'`） |

---

## 陷阱（≥2）

1. **`open("x.txt")`** 未写 encoding — **成因**：locale。**改法**：**永远显式**。UTF-8 模式辅助：`PYTHONUTF8=1`，仍建议源代码写死编码。详见历史 QA。  
2. **大文件 `read()`** — **成因**：内存。**改法**：分块/`for line`。  
3. **JSON 不能直接 dump `datetime`/自定义类** — **成因**：encoder 不知如何拆。**改法**：`default=`钩子或预处理。

---

## 适用范围 · 延伸

配置文件、爬虫落盘批处理、离线特征缓存；二进制协议走 **`bytes`** + struct（后续）。

---

## 双重示例

### A. 极简｜规范化姓名 + Template

```python
from pathlib import Path
from string import Template

who = " ".join("  Ada\tLovelace ".split())
letter = Template("Hello, $who.").substitute(who=who)
Path("hello.txt").write_text(letter, encoding="utf-8")
```

### B. 工程切片｜流式计数行数

```python
from pathlib import Path

def line_count(path: Path) -> int:
    n = 0
    with path.open(encoding="utf-8") as f:
        for _ in f:
            n += 1
    return n
```

**运行**：PowerShell：`python .\your.py`，确保工作目录有可写权限。

---

## 练习

- **基础**：显式读写 JSON；用 f-string `{pi=:.3f}` 调试后缀。  
- **进阶**：`Path`/`os.path`任选其一比对跨平台可读性。  
- **开放**：检索 **UTF-8 Mode** (`-X utf8`) 的官方约束。

---

## 费曼反问

1. 文本和二进制打开的 **本质差别**？
2. 为什么团队规范常写 **`encoding=utf-8` 字面量**，而不是全凭环境？
3. 何时应采用 **生成器**式读而不是 `readlines()`？

---

> **闭环**：默写 **`with Path(...).open(... ) as f`** 的三条收益。
