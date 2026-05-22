# 模块包与虚拟环境｜讲义笔记

<参考资料>

- https://docs.python.org/3/tutorial/modules.html
- https://docs.python.org/3/library/venv.html
- https://packaging.python.org/en/latest/tutorials/installing-packages/

</参考资料>

## 本地知识库命中（与本节对齐）

- `obsidian-vault/LLM_Learning/wiki/topics/python-module-system.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/modules-and-packages.md`
- `obsidian-vault/LLM_Learning/wiki/concepts/virtual-environment.md`
- `obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — **基础层 C**

---

## 上一章核心收获回顾（衔接「数据模型」）

你已知道 **对象是属性 + 方法 +（可选）协议钩子**的合集。

你已建立 **`import`把一个 `.py` 文件当命名空间读进来**的早期印象——虽然还不系统。

你已理解 **`__init__`、`__repr__`、`__eq__/__hash__`**在「自编类型」里最常用。

你已能想象 **团队协作**时需要「互不踩依赖版本」的工程手段。

你已准备收口：**包布局 / 入口脚本 /site-packages**。 

---

## 但是，我们遇到了一个新的问题……

- **「我这儿能跑」**换机器：`ModuleNotFoundError`。  
- 同名模块 **shadow**。  
- 不知道 **`__name__=="__main__"`**、`sys.path`。  
**因此本章需要：**掌握 **`venv`、`pip`、`import`语义、包的目录约定**——让项目 **可重现**。

---

## 动机：`pip install` 装进「全家桶」全局 site-packages ⇒ 团队协作灾难。

---

## 类比（非编程）

模块像 **单行本漫画**独立剧情；包像 **单行本凑系列 + 书目清单**挂在出版社目录下。`venv`像给项目一套 **私家书架 + 独享调味料架**——不会把邻桌项目的辣酱拿错。

---

## 精讲

### 导入执行一次缓存

首批 `import m`：**执行顶层代码** ⇒ 以后再取 `sys.modules['m']`。

### 包 & `__init__.py`

可暴露子模块 API：`from .foo import Bar`。**Namespace 包**（PEP 420）可无 `__init__.py`。

### **`if __name__ == "__main__":`** 

既当模块可被 import，又可 `python -m pkg.cli`直达。

### venv Quickstart（Windows PowerShell）

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pydantic fastapi    # example
pip freeze > requirements.txt
```

---

## 辨析

| | **模块** | **包** |
|--|----------|--------|
| 形态 | `.py` 单文件 | 目录（常含多个 `.py`) |

---

## 陷阱（≥2）

1. **相对导入在非包上下文直跑脚本**报错 — **成因**：脚本不在包搜索图。**改法**：`-m`/调整 `PYTHONPATH`。  
2. **忘记锁依赖** — **成因**：漂移。**改法**：`requirements`、`uv.lock`/`poetry.lock` 或等价锁文件。  
3. **同名文件挡标准库**（shadow）。

---

## 适用范围 · 延伸

`pyproject.toml`/`uv`/`poetry`：**宣言式锁定**演进；进阶阅读 Packaging User Guide。

---

## 双重示例

### A. 极简｜双模块互引

```
pkg/
   __init__.py   # optional
   a.py -> def ping(): return "a"
   b.py -> import pkg.a ; assert pkg.a.ping()=="a"
```

### B. 工程切片｜CLI 守卫

```python
# hello_cli.py

def main():
    print("hi")


if __name__ == "__main__":
    main()
```

PowerShell：**`python -m`** 运行时注意 **包根在 `PYTHONPATH`。

---

## 练习

- **基础**：建新 venv，`pip freeze`前后对比差异。  
- **进阶**：用 `src` 布局写一个 `pip install -e .` 可编辑装（任选工具）。  
- **开放**：读 **PEP 420**一页笔记。

---

## 费曼反问

1. 「首次导入执行顶层」会怎样影响 **全局可变单例？**  
2. 为什么团队协作需要 **锁依赖**胜过口头约定？  
3. **相对导入失败的典型场景**复述一则。

---

> **闭环**：口述 **`sys.path`** 三件事如何影响导入。
