---
type: concept
created: 2026-05-13
updated: 2026-05-13
tags: [python, venv, pip, packages]
source_count: 1
---

# 虚拟环境

Python 的项目隔离和依赖管理机制。

## 为什么需要虚拟环境

- 不同项目可能依赖同一包的不同版本
- 系统 Python 不应被项目依赖污染
- 确保项目的可复现性

## 创建与使用

```bash
# 创建虚拟环境
python -m venv myenv

# 激活
# Windows:
myenv\Scripts\activate
# Unix/macOS:
source myenv/bin/activate

# 停用
deactivate
```

- 激活后，`python` 和 `pip` 指向虚拟环境内的版本
- 虚拟环境是一个目录，包含 Python 解释器副本和独立的 site-packages

## pip 包管理

```bash
pip install package_name          # 安装
pip install package==1.2.3        # 指定版本
pip install --upgrade package     # 升级
pip uninstall package             # 卸载
pip list                          # 列出已安装包
pip show package                  # 包详情
pip search keyword                # 搜索（PyPI）

# 依赖导出与复现
pip freeze > requirements.txt
pip install -r requirements.txt
```

## requirements.txt

- `pip freeze` 输出精确版本号，确保环境可复现
- 格式：每行一个 `package==version`
- 团队协作时提交到版本控制

## 最佳实践

- 每个项目一个虚拟环境
- 不要把虚拟环境目录提交到 git（加入 .gitignore）
- 用 requirements.txt 记录依赖

## 来源

- [[sources/2026-05-13-python311-tutorial]]
