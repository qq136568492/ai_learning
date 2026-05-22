# -*- coding: utf-8 -*-
"""Inject teaching scaffold into learning/python-advanced-learning/notebooks/*_note.md.

Run from repo root: python tools/inject_python_advanced_note_scaffold.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_ROOT = ROOT / "learning" / "python-advanced-learning" / "notebooks"

MARK_H = "<!-- teaching-scaffold-head:v1 -->"
MARK_T = "<!-- teaching-scaffold-tail:v1 -->"

ANCHOR = "## 一、核心定义（What）"

# map_section → learning map bullet; bridge/motivation/analogy/questions unique per lesson
DATA: dict[str, dict[str, str]] = {}

# --- Layer 01 ---------------------------------------------------------------
DATA["数据类型与可变性_note.md"] = dict(
    map_section="Python 基础层 **A1 数据类型**（可变/不可变、可哈希）。",
    bridge="""- （路径起点小结）你已能写字面量、`list/dict`，并知道 **`a = b` 不是复印**这句口号，但还容易在具体代码里踩坑。
- **但是，我们遇到了一个新的问题：** 为什么有的地方「改副本却影响到原件」？为什么列表不能塞进 `set`？
- **因此本章需要：**把 **身份 / 类型 / 可变与不可变 / 赋值与拷贝**说清楚，后面的函数默认值、容器用法才有稳固地基。""",
    motivation="写程序像管理「箱子里的东西」：**名字是标签**，多个标签可以指向同一只箱子；可变类型是「开箱改内容」，不可变是「换新箱」。搞不清楚就会写出「静默串改数据的 bug」，调试极耗时间。",
    analogy="**快递单号与人名：**不可变更像「一单到底的条码」（换掉就是新单据）；可变像「库房货位」（单号不变，里面东西可随时盘点）。别把「贴第二张同样的货位条码」误以为「复制了新库房」。",
    basic_ex="解释 `a=[1]; b=a; b.append(2)` 后 `a` 为何变化；口述「浅拷贝 vs 深拷贝」各解决什么。",
    adv_ex="用 `collections.namedtuple` 或 `frozenset` 设计一枚「可当 dict 键」的组合键；写一段对比 `copy.copy`/`deepcopy`。",
    open_ex="查文档说明：为什么在并发场景更倾向不可变数据结构或加锁可变共享状态？写 5 行读书笔记。",
    q1="用一句话说明「赋值」「浅拷贝」「深拷贝」三者的直觉差异分别是什么？",
    q2="为什么「可变默认值」（如 `def f(x, L=[])`）会坑？底层发生几次「求值」？",
    q3="「容器里装的东西可哈希」和「把整个容器放进去当键」为什么规则不同？",
)

DATA["控制流与match_note.md"] = dict(
    map_section="Python 基础层 **A2 控制流**（分支/循环/early exit / `match`）。",
    bridge="""- （上一章你应带走）你已知道数据如何存进容器，并开始写小段逻辑。
- **但是，我们遇到了一个新的问题：** 分支和循环一长串就难以阅读，`for` 背后到底发生什么也不清楚。
- **因此本章需要：**掌握 **结构化分支 / 遍历 / 安全的循环修改**，并了解 **`match`** 在多形态数据上的可读写法（3.10+）。""",
    motivation="业务代码里大量「如果这个则…否则…」，以及遍历集合。**控制流不清晰**就会把 bug 埋在角落（例如遍历中删元素、误解循环 `else`）。",
    analogy="交通灯：**if** 是某一路口红绿灯；**while** 是「一直等到雨停」这种条件驱动；**for** 像「按计划表依次办事」，`match` 像「对不同形状零件走不同分拣口」。",
    basic_ex="用 `for` + `enumerate` 打印索引与字符；写一个 `match` 把二元组分出坐标轴特例。",
    adv_ex="实现 `find`：找到返回下标且在 `break` 后解释循环 `else` 何时触发。",
    open_ex="把一段 5 层 `if-elif` 改成 `match` 或映射表 handler，注明可读性利弊。",
    q1="用口语解释：**为什么** `for` 不是单纯「计数」，而是迭代？",
    q2="「循环带 `else`」和「`if-else`」直觉差在哪里？各举一个正确使用场景。",
    q3="什么时候 **不该**用 `match`（仍用朴素 `if` 更清晰）？",
)

DATA["字符串与文件IO_note.md"] = dict(
    map_section="基础层 **A3/A4**：字符串格式化 + 文本文件与 JSON（学习地图中与 `file-io`、`string-formatting` 对应）。",
    bridge="""- （上一章你应带走）你能写分支循环，并开始处理小段文本列表。
- **但是，我们遇到了一个新的问题：** 如何把数据稳定写进磁盘、又怎么避免 Windows 编码坑？
- **因此本章需要：**掌握 **f-string / 模板**，以及 **`open` + encoding + JSON** 的工程习惯。""",
    motivation="几乎每个项目都要落盘配置、读写日志上下文、拼装用户可见文案。**不写 encoding、`read()` 大文件**，线上与本地都可能炸。",
    analogy="格式化像「填空题试卷」：**f-string** 是临场手写答案；**`Template`** 像统一印制的工资条模板，填充区固定。磁盘文件则是「保险箱里的纸质档案」，**进出都要同一套语种（编码）**。",
    basic_ex="用 `encoding=\"utf-8\"` 读入再写出一个 JSON；用 f-string 做两位小数格式化。",
    adv_ex="用 `string.Template` 生成一封短信模板；用 `pathlib.Path` 拼路径读写。",
    open_ex="实现逐行读完大文件的生成器接口（不写一次性 `read()`），并说明你如何测内存占用直觉。",
    q1="为什么「文本模式打开文件」要特别关心 `encoding`？",
    q2="`with open(...)` 相比手动 `close` 多解决了哪类事故？",
    q3="JSON 不能直接序列化的类型，你如何设计扩展策略（钩子/转换字典）？",
)

DATA["函数与作用域_note.md"] = dict(
    map_section="基础层 **A5 函数**：参数、`lambda`、LEGB 作用域。",
    bridge="""- （上一章你应带走）你能安全读写文本与配置文件。
- **但是，我们遇到了一个新的问题：** 一写函数就出现「外层变量改了没」「默认参数作怪」两类谜题。
- **因此本章需要：**掌握 **签名、\*args/\*\*kwargs、闭包、LEGB**。""",
    motivation="函数是复用逻辑的抓手；**不明确作用域边界**会像「房间里的开关不知道控制哪盏灯」，调试全凭猜。",
    analogy="函数像**带说明书的工具插槽**：`/ *` 限定位孔宽严；`**kwargs` 像「附带配件筐」。闭包像一个**记忆上次设定的小扳手**——但要小心循环里捕获的是「变量的最新值」。",
    basic_ex="写 ` greet(name, *, polite=True)`：体会仅限关键字参数。",
    adv_ex="复现闭包延迟绑定问题并用「默认参数绑定当前值」修复。",
    open_ex="读 `inspect.signature`，反思团队 API 如何避免「一切皆 kwargs」。",
    q1="用一句话说明 LEGB 的查找顺序在现实中对应什么心智模型？",
    q2="为什么 `funcs = [lambda: i for i in range(3)]` 会输出「全是最后一个 i」？",
    q3="什么时候该用 `nonlocal`，什么时候该把状态改成显式参数或小型类？",
)

DATA["异常处理_note.md"] = dict(
    map_section="基础层 **A6 异常**：`try`/`raise`/`from`/`ExceptionGroup`（3.11+）。",
    bridge="""- （上一章你应带走）函数帮你拆分了可复用逻辑。
- **但是，我们遇到了一个新的问题：** 错误如果只靠返回码层层判断，主干代码会被 `if not ok` 淹没。
- **因此本章需要：**学会 **EAFP**：用异常表达「走错路」，并保留 **可追溯因果链**。""",
    motivation="异常把「异常情况」拉平到少数处理点——**等价于在正常剧情里少打岔**。不会用 `from`/自定义异常会把线上排障拖成玄学。",
    analogy="异常的传播像「火警铃沿楼层往上响」：**try** 是「本楼层先尝试救火」；`**from**` 是「报告时注明最初起火点」，方便事后复盘。",
    basic_ex="把 `str → int` 转换包成捕获 `ValueError` 并带上文 `raise ... from`。",
    adv_ex="写最小 `batch_validate`，收集后 `raise ExceptionGroup`（或口述何时不用）。",
    open_ex="对比「Go 风格 `(ok,val)`」与 Python EAFP：各写同等逻辑伪代码一页纸。",
    q1="`else`/`finally` 各自承诺的执行时机是什么（含中途 `return` 直觉理解）？",
    q2="裸 `except:` 为什么在工程里一般要禁止？你希望捕获到什么粒度？",
    q3="什么时候该自定义异常层级，而不是到处抛 `RuntimeError`？",
)

DATA["数据模型与对象_note.md"] = dict(
    map_section="基础层 **B 数据模型**：对象三要素、`is`/`==`、协议的「人话入门」。",
    bridge="""- （上一章你应带走）你会用异常把错误通路整理清楚。
- **但是，我们遇到了一个新的问题：** 为什么说 Python「一切皆对象」？`len(x)`、`x[i]`背后怎样挂钩？
- **因此本章需要：**建立 **协议直觉**（用少量特殊方法就能把类型接入语法糖），分清身份与相等。""",
    motivation="不写类也会遇到「为什么这个能迭代、那个不能哈希」。数据模型是一张**插口规格表**。",
    analogy="对象是带**多功能插座**的机器：装好某几个孔（协议），电风扇就能插在同一个排插上（语法统一）。不等于你要一次买齐所有孔的转接头。",
    basic_ex="手写 `Point`：`__repr__`/`__eq__`/`__hash__`。",
    adv_ex="用 `Sequence`/`__getitem__` 实现「伪列表」可被 `list()` 转换。",
    open_ex="读 `dataclasses.Field`：`frozen=True` 对 `__hash__`/`__eq__` 的工程含义写下来。",
    q1="`is` 和 `==` 分别承诺比较什么？",
    q2="「实现 `__iter__`/`__next__`」与「只实现老式 `__getitem__`」在体验上有什么不同？（本章只口述现象）",
    q3="为什么可变对象一般不应当可哈希？",
)

DATA["模块包与虚拟环境_note.md"] = dict(
    map_section="基础层 **C 模块与环境**：`import`、`sys.path`、venv、条目入口。",
    bridge="""- （上一章你应带走）你理解对象是程序里「打包状态+行为」的单元。
- **但是，我们遇到了一个新的问题：** 如何把 `.py` 文件组织进可维护工程，并让依赖互不踩脚？
- **因此本章需要：**掌握 **模块/包语义** 与 **`venv + pip`/锁文件**。""",
    motivation="没有虚拟环境会像「全屋共用一个调味料罐」：**甜咸串味**。弄清 `import` 才能拆库、写测试。",
    analogy="模块是**章回体小说的单章**，包是有目录的「卷」；`if __name__ == \"__main__\":` 像「本篇是否独立成书」的检验戳。`venv` 是给项目单独买一套**厨具与调料架**。",
    basic_ex="创建 `.venv`，安装一个第三方包，`pip freeze` 导出依赖。",
    adv_ex="画 `src` 布局 + `python -m` 启动的差异说明。",
    open_ex="读 PEP 517/621 引言：对比 `requirements.txt` 与「`pyproject` 宣言式」的工程取舍。",
    q1="为什么模块「首次 import 执行一次」会影响全局单例写法？",
    q2="相对导入在什么场景报错（如脚本直跑），如何避免？",
    q3="`sys.path` 里你最希望控制哪几项以保证 CI 一致性？",
)

# --- Layer 02 ---------------------------------------------------------------
DATA["推导式_note.md"] = dict(
    map_section="进阶层 **D1 推导式**（与生成器表达式区分）。",
    bridge="""- （上一章你应带走）你已会把代码拆模块并隔离依赖。
- **但是，我们遇到了一个新的问题：** 手写 `append`/`for` 过滤映射冗长缓慢，读起来像说明书。
- **因此本章需要：**用 **推导式声明「结果长什么样」**，并知道退回普通循环的时机。""",
    motivation="推导式让你在单屏内表达「对每个元素做一次变换/筛选」。滥用嵌套四层以上则适得其反。",
    analogy="像在超市清单上直接写：**只要苹果、并且要削皮版**——不是逐步口述采购动作。生成器表达式像**排队领号**，一次只出产一个果子省袋子。",
    basic_ex="把双重 `append` 改写成单层列表推导式与字典推导式各一题。",
    adv_ex="`sum(x*x for x in nums)` vs `sum([x*x ...])` 解释惰性优势。",
    open_ex="用 `dis`/`timeit` 粗测推导式与小循环（了解即可）。",
    q1="「列表推导」与「生成器表达式」在 **内存与时间**心智上差什么？",
    q2="为什么「副作用很强的逻辑」一般要退回普通 `for`？",
    q3="嵌套推导什么时候该拆成有名中间变量或小函数？",
)

DATA["迭代器与生成器_note.md"] = dict(
    map_section="进阶层 **D2 迭代器/生成器**（惰性、读大文件/分页语义）。",
    bridge="""- （上一章你应带走）你能用推导式声明式聚合数据。
- **但是，我们遇到了一个新的问题：** 不是所有序列都能预先放进内存，也不是所有流程都适合 eager list。
- **因此本章需要：**理解 **`iter`/`next`/`StopIteration`** 驱动的遍历，并用 **`yield` 流水线化**。""",
    motivation="惰性迭代是性能和架构的分水岭：**边读边算**才能支撑大文件和网络流。", 
    analogy="DVD 快进逐帧 vs Youtube 流媒体缓冲：`list`像是「整部下载完再看」，`generator`像是**边缓冲边播放**，播完即止，`StopIteration` 像「本片终」。", 
    basic_ex="用手写类实现计数到 `n`，或生成平方序列。",
    adv_ex="用生成器拆解 `read_chunks`/分页 API 伪代码。",
    open_ex="把树遍历改成迭代器接口（可先DFS栈草图）。",
    q1="`for x in obj` 在背后最少经历哪三步心智模型？", 
    q2="「生成器函数」和「普通函数立刻 return」在栈与状态上有什么不同（口语层面）？", 
    q3="为什么在组合多个处理阶段时用生成器链路比巨型 list 更合适？", 
)

DATA["类与面向对象_note.md"] = dict(
    map_section="进阶层 **D3 面向对象**：实例/类命名空间、继承组合、`super`。",
    bridge="""- （上一章你应带走）你能用迭代惰性处理数据序列。
- **但是，我们遇到了一个新的问题：** 业务里「状态 + 行为 + 演进」混在一起，单靠函数散落全局越来越难维护。
- **因此本章需要：**用 **类建模状态边界**，理清 **实例属性 vs 类属性**，并审慎使用继承。""",
    motivation="合适的类是一份**权责清单**：把不变式收口到构造函数和少量方法。", 
    analogy="实例像**具体员工卡片**（上面有姓名工时），类像**考勤制度模板**。类变量是公司公告栏上的「默认值」：`self.x`更像个人工牌字段。", 
    basic_ex="用 `@dataclass` 建只读坐标点并放进 `set`。",
    adv_ex="画一张「类属性可变共享」的事故现场并修复。", 
    open_ex="用组合而非继承改写一个「支付适配器」，写 10 行设计说明。", 
    q1="**类变量**和**写在 `self` 上的属性**在多实例场景各承担什么默认角色？", 
    q2="（术语闸门）什么叫 **「方法绑定」**？举一个 `obj.method()` 等价展开（不必背公式）。", 
    q3="（术语闸门若出现）一句话解释 **继承查找顺序**：为什么 `super()` 不是「只管爸爸」？", 
)

DATA["装饰器_note.md"] = dict(
    map_section="进阶层 **D4 装饰器**（计时/缓存/日志横切关注点）。",
    bridge="""- （上一章你应带走）你会把状态和职责收到类与方法里。
- **但是，我们遇到了一个新的问题：** 想在许多函数外挂「前后缀逻辑」又不想复制粘贴样板代码。
- **因此本章需要：**理解 **函数是一等公民** 与装饰器如何把「外包装」重用起来。""",
    motivation="装饰器=Dry 切面：权限、度量、缓存。理解闭包、`functools.wraps` 才能把元数据留对。", 
    analogy="像给每个房间统一装门禁读卡：**卡套（装饰器）不动房间布局，但每次进出都先刷卡**。", 
    basic_ex="写 `@timer` 打印耗时（用 `wraps`）。",
    adv_ex="写一个带参数的 `@retry(times=3)` 草图。", 
    open_ex="讨论类装饰器 vs 函数装饰器各自适用。", 
    q1="装饰器本质是「高阶函数」，这句话对你意味着哪两种对象在来回传递？", 
    q2="没有 `wraps` 会失去哪些排障友好的信息？", 
    q3="哪类逻辑 **不该**塞进装饰器（以免隐藏控制流）？", 
)

DATA["上下文管理器_note.md"] = dict(
    map_section="进阶层 **上下文管理**：`with`/`__enter__`/`__exit__`/`contextlib`。",
    bridge="""- （上一章你应带走）你能用装饰器复用环绕逻辑。
- **但是，我们遇到了一个新的问题：** 有成对操作（开锁/关锁）怕中间异常漏清理。
- **因此本章需要：**用 **上下文管理器协议**描述「进入一个作用域前要准备、离开时要收拾」。""",
    motivation="数据库连接、锁、临时目录都符合「先拿后放」：**异常安全**比「记得 finally」更值得交给协议。", 
    analogy="舞台剧换景：大幕升降算 `__enter__`/`__exit__`，中途演员忘词砸场也得保证幕落下来（finally 语义）。", 
    basic_ex="手写了最小 `Timer`：`__enter__` 记起点 `__exit__` 打印间隔。", 
    adv_ex="用 `@contextmanager` + yield 写一个临时切换工作目录。", 
    open_ex="对比 `suppress`/`ExitStack` 的使用场景写一个清单。", 
    q1="`__exit__` 收到异常信息时，`return True`/`False` 分别代表什么决策？", 
    q2="`with` 和单纯 `try/finally` 在表达「资源是一对」的问题上谁更可读？", 
    q3="异步上下文（可先标记「进阶」）在现实中解决什么问题？", 
)

DATA["魔术方法_note.md"] = dict(
    map_section="进阶层 **运算符/容器魔力方法**（算术、比较、`__getitem__`、`__contains__` 等）。",
    bridge="""- （上一章你应带走）你能用上下文管理资源边界。
- **但是，我们遇到了一个新的问题：** 希望自己的类型更像内置类型一样自然参与运算与被容器语法驱动。
- **因此本章需要：**挑选性实现 **运算符与容器钩子**，避开坑（尤其是可变哈希）。""",
    motivation="「Python 风格」有时是「让它用起来像 builtin」：**但别实现全套**，只拣领域需要的运算符。", 
    analogy="像在自定义遥控玩具车：你不想复刻真车所有踏板，只留下 **左转/鸣笛** 两三个常用键 ——运算符重载是加物理键，但不要加到驾驶舱过载。", 
    basic_ex="为简单向量实现 `__add__`/`__repr__`。",
    adv_ex="实现只读映射视图（可先仅 `keys`/`__getitem__`）。", 
    open_ex="读「可变对象不要乱 `__hash__`」，写一页决策表。", 
    q1="实现 `__eq__` 后默认 `__hash__` 可能变 `None`，这对外部使用者意味着什么？", 
    q2="`__contains__` 缺省时 Python 会如何兜底（口语）？", 
    q3="哪类运算符重载在团队规范里常常被禁止，为什么？", 
)

DATA["类型提示_note.md"] = dict(
    map_section="进阶层 **E1 类型提示**，对接 `Protocol`/`TypedDict` 等演进点。",
    bridge="""- （上一章你应带走）你能改写对象行为钩子。
- **但是，我们遇到了一个新的问题：** 人一多、模块一多，只靠「跑动才知道类型错在哪里」太累。
- **因此本章需要：**用 **注解 + 工具链**提早发现签名错误。""",
    motivation="类型提示≠运行变慢：它是静态协作契约，尤其对 API 与中台数据结构极划算。", 
    analogy="在建筑图纸上标清门洞尺寸 vs 装修时才发现冰箱进不去。", 
    basic_ex="给三个函数补上 `list[str]`、`dict[str,int]`。", 
    adv_ex="写一个 `Protocol` 描述「有 `read()`」的文件类对象。", 
    open_ex="跑 `pyright`/ `mypy` 任一，对报错分类「真 bug」vs 「工具局限」。", 
    q1="`Optional[X]`/`X | None` 想提醒调用方什么事情？", 
    q2="`Protocol` vs 继承 ABC 在什么场景更合适？", 
    q3="`from __future__ import annotations` 解决的主要痛点？", 
)

DATA["asyncio异步_note.md"] = dict(
    map_section="进阶层 **E2 asyncio**：`async`/`await`、事件循环、`gather`。",
    bridge="""- （上一章你应带走）你能用静态类型收窄接口歧义。
- **但是，我们遇到了一个新的问题：** I/O 等待时线程开太多上下文重，需要协作式调度。
- **因此本章需要：**懂 **异步任务粒度**（它不是万能加速器）。""",
    motivation="asyncio 强项是海量 **等待型 I/O**：HTTP、WebSocket、流式推理；CPU 密集型计算请优先考虑多进程等方案。",
    analogy="奶茶店高峰：异步像**单人轮询多张单等杯盖到位**再继续；多线程像**人手一杯同时等**——杯盖机只有一个时不见得更快。", 
    basic_ex="用 `asyncio.sleep`/`gather`写并发三个假请求。", 
    adv_ex="用 `wait_for` 做超时。", 
    open_ex="读 `asyncio.to_thread`，举「blocking 库里函数」迁入线程例子。", 
    q1="`await`点前后代码分别运行在什么样的调度语义下（口语）？", 
    q2="为什么 CPU 密集型循环通常不适合靠 async 提速？", 
    q3="一个 async 上下文里混入阻塞 `time.sleep`/同步 HTTP 会发生什么级别的问题？", 
)

DATA["pytest测试_note.md"] = dict(
    map_section="进阶层 **F1 pytest**：断言、fixture、参数化。",
    bridge="""- （上一章你应带走）你已建立异步与高并发范式的心智模型。
- **但是，我们遇到了一个新的问题：** 没有自动回归时，重构就像在悬崖边拆桥。
- **因此本章需要：**写 **可读、隔离、可参数化** 的单测。""",
    motivation="fixture 是把「重复的测试 Setup」抽到声明式钩子；pytest 的失败信息比手写 assert 链路更友好。", 
    analogy="单元测试像**工厂的质检夹具**：fixture 是可换夹具底板；参数化是一套模具压多种厚度。", 
    basic_ex="为纯函数写 3 case `parametrize`。",
    adv_ex="`pytest.raises`+`match=` 断言异常。", 
    open_ex="给异步 handler 写一个最小 async 测试（若环境允许）。",
    q1="fixture 与普通函数测试相比，复用边界在哪里？", 
    q2="什么时候该用 monkeypatch/mock，何时应当避免？", 
    q3="如何组织 `tests/` 与实际包镜像结构？", 
)

DATA["logging日志_note.md"] = dict(
    map_section="进阶层 **观测基础**：logging 模块化与结构化扩展口子。",
    bridge="""- （上一章你应带走）你会用 pytest 守门回归。
- **但是，我们遇到了一个新的问题：** `print` 难分级、难分流，也难对齐生产的采集链路。
- **因此本章需要：**用 **`logging` 层级 / Handler / Formatter** 建模输出。""",
    motivation="结构化日志是未来可观测链路（ELK/Otel）最便宜的上游。", 
    analogy="像在音响系统：**Logger**决定节目单，Handler 决定扬声器房间，Formatter 混音EQ。", 
    basic_ex="配置 root logger 打到文件+控制台不同级别。", 
    adv_ex="用 `logging.LoggerAdapter` 注入 `request_id` 字段草图。", 
    open_ex="对比 stdlib logging 与 `structlog/opentelemetry`选型笔记。", 
    q1="`DEBUG/INFO/WARN` 的工程分工是什么？", 
    q2="为什么库代码里常用 `logging.getLogger(__name__)`？", 
    q3="在异常路径如何确保堆栈进到日志而不泄露敏感上下文？", 
)

# --- Layer 03 ---------------------------------------------------------------

DATA["numpy向量化与广播_note.md"] = dict(
    map_section="接轨层 **G1 NumPy**：向量化、`dtype`、广播、视图。",
    bridge="""- （上一章你应带走）语言与 pytest / logging 等工程习惯已就位。
- **但是，我们遇到了一个新的问题：** Python 双层循环做大矩阵既慢又长。
- **因此本章需要：**用 **ndarray 的形状与 dtype 语义** 思考数值问题。""",
    motivation="向量化和广播是几乎所有数值/特征入口；搞错 view/copy 会像「误以为复印件可涂改原件」。",
    analogy=" ndarray像「带固定格子尺寸的 Excel 单表」，广播像**智能拖拽填充**：尺寸对不上会先商量扩行还是扩列。", 
    basic_ex="用向量化表达式替代手写平方累加。", 
    adv_ex="写一个触发广播错误再修正轴例子。", 
    open_ex="读 wiki `view-vs-copy` 概念页并总结一条团队规范。", 
    q1="向量化直觉上替换了哪一种 Python 低效模式？", 
    q2="「形状」和「dtype」出错各带来哪类 silent bug？", 
    q3="什么时候必须显式 `.copy()`？", 
)

DATA["pandas清洗与聚合_note.md"] = dict(
    map_section="接轨层 **G2 Pandas**：ETL、对齐、`groupby`。",
    bridge="""- （上一章你应带走）你理解 ndarray 块状数值与张量语义。
- **但是，我们遇到了一个新的问题：** 真实业务多半是带索引、缺失值的表格。
- **因此本章需要：**用 **DataFrame / Series** 做清洗与聚合。""",
    motivation="pandas 把「对齐」做到默认：**merge/join 隐式对齐**要学会有意识地检查。", 
    analogy="像在 Excel里但所有 sheet 都有一张「隐形对齐尺」：**不小心就会按错尺剪尺寸**。", 
    basic_ex="读 csv → `dropna` → `describe`。", 
    adv_ex="`groupby().agg` 多指标。", 
    open_ex="将一份宽表 reshape 成长期表并解释意义。", 
    q1="`SettingWithCopyWarning` 想提醒你什么？", 
    q2="`merge` vs `join`/`concat`如何选择？", 
    q3="时间索引 `resample` 解决什么问题？", 
)

DATA["matplotlib与seaborn可视化_note.md"] = dict(
    map_section="接轨层 **可视化**：matplotlib 轴对象 + seaborn 统计图层。",
    bridge="""- （上一章你应带走）你能对表格做分组与对齐。
- **但是，我们遇到了一个新的问题：** 光看数字难看出分布漂移与长尾。
- **因此本章需要：**会画 **EDA 级别** 的诊断图。""",
    motivation="可视化是「与人类视觉带宽对齐」的接口；matplotlib 要学清 **figure/axes**。",
    analogy="matplotlib像**画布+画架层次**；seaborn像买一送一的**统计配色主题套餐**。", 
    basic_ex="画直方图+散点两子图。", 
    adv_ex="用 seaborn facet 分拆类别。", 
    open_ex="做一张随时间漂移对比图配文说明。", 
    q1="`pyplot` 接口与「显式 axes」心智差？", 
    q2="什么图不适合默认美化（可能误导）？", 
    q3="如何把图导出矢量格式给报告？", 
)

DATA["fastapi路由与模型_note.md"] = dict(
    map_section="接轨层 **H FastAPI+Pydantic 模型绑定**。",
    bridge="""- （上一章你应带走）你能用可视化理解离线数据视图。
- **但是，我们遇到了一个新的问题：** 如何把类型态契约通过网络暴露给他人调用？
- **因此本章需要：**理解 **路由、依赖钩子、自动生成 OpenAPI** 三件事如何串起来。""",
    motivation="FastAPI 把 pydantic validate 前移：更早失败更接近调用方。", 
    analogy="像机场值机：**请求体验证是第一道安检闸门**，进去了才卸行李（handler 执行业务）。", 
    basic_ex="写两个路径返回 JSON schema。", 
    adv_ex="用 `Depends` 抽JWT用户伪依赖。", 
    open_ex="读 OpenAPI yaml 一页，标注安全定义缺口。", 
    q1="为什么 path/query/body 参数应分区清晰？", 
    q2="依赖注入比普通函数导入强在哪里？", 
    q3="自动文档信任边界是什么？", 
)

DATA["pydantic数据校验_note.md"] = dict(
    map_section="接轨层请求体验证：**`BaseModel`** 语义（常与 FastAPI 联用）。",
    bridge="""- （上一章你应带走）你能挂路由并让框架帮你生成文档草稿。
- **但是，我们遇到了一个新的问题：** JSON 进来仍是「散装 dict」，错在深层才爆炸。
- **因此本章需要：**用 **`BaseModel`** 收口字段类型、默认值与别名。""",
    motivation="模型的 value_error 可把 bug 转成 422 靠近边缘。", 
    analogy="表单印刷带复写框：**缺框、写超出格**当场退还，不靠办事员口述规则。", 
    basic_ex="写模型含可选字段/默认值。", 
    adv_ex="自定义 validator（v2.field_validator）清洗字符串。", 
    open_ex="设计嵌套响应模型+D引用共享子模型。", 
    q1="`model_validate` vs 手工 dict 拆装差在哪？", 
    q2="什么时候该 `model_config strict`？", 
    q3="如何平衡「模型层」 vs 「领域层校验」？", 
)

DATA["streamlit原型_note.md"] = dict(
    map_section="接轨层 **原型工具 Streamlit**：快速可视化交互。",
    bridge="""- （上一章你应带走）你能用 Pydantic 把数据结构讲清楚。
- **但是，我们遇到了一个新的问题：** 业务只想半小时看到可点的 demo，而不是一上来就写完 API 套件。
- **因此本章需要：**理解 **自上而下重跑的脚本模型**如何做原型。""",
    motivation="Streamlit 强项是 DEMO，不是巨型状态管理。", 
    analogy="像一个**幻灯片播放器**：每次改动重新放映整套 slide，而不是传统 GUI 的信号槽细粒度。", 
    basic_ex="上传 csv 显示 head。", 
    adv_ex="`st.cache_data`/`cache_resource`分界实验。", 
    open_ex="把 FastAPI+pandas 草稿接进 Streamlit。", 
    q1="为什么默认「自上而下整脚本重跑」？", 
    q2="`session_state` 解决什么痛点？", 
    q3="它不适合的场景列举两条。", 
)

DATA["部署与可观测_note.md"] = dict(
    map_section="接轨层 **I 部署与安全基线**：反代、`uvicorn` / 容器、HTTPS、观测。",
    bridge="""- （上一章你应带走）你能堆出可演示的原型或服务雏形。
- **但是，我们遇到了一个新的问题：** 本子能跑 ≠ 线上可持续值班。
- **因此本章需要：**建立 **最少生产 checklist**（部署、密钥、观测的一页纸）。""",
    motivation="对齐 wiki `deployment-strategy` + `api-security`。", 
    analogy="把应用从家里 Wi-Fi 搬进「有物业、门禁、 CCTV」写字楼。", 
    basic_ex="用 `docker run`拉起最小镜像。", 
    adv_ex="草图：`nginx tls` termination → `uvicorn` workers。", 
    open_ex="列可观测三件事：metrics/logs/traces。", 
    q1="为什么生产少直接用 `reload=True`？", 
    q2="CORS misconfig 会如何误伤？", 
    q3="健康检查endpoint放什么信息量合适？", 
)

# --- Layer 04 AI -------------------------------------------------------------

DATA["LLM调用与Prompt_note.md"] = dict(
    map_section="核心层 **J LLM + Prompt**。",
    bridge="""- （上一章你应带走）你理解最少化的部署与安全外沿。
- **但是，我们遇到了一个新的问题：** 如何把「自然语言控制能力」变成可回放、可版本化的工程面？
- **因此本章需要：**理解 **`messages` 结构化**、温度等采样参数、流式响应与工具调用边界。""",
    motivation="prompt 与 schema 是同一张合同的两页：文本指令 + structured output。", 
    analogy="像在餐厅下单：**system=厨房纪律**，**user=客户口述**，few-shot像贴墙上的样例配菜图。", 
    basic_ex="写消息列表模板函数。", 
    adv_ex="设计 JSON-mode + pydantic校验伪代码。", 
    open_ex="读 rate limit backoff 一页笔记。", 
    q1="为什么 system 与用户输入要分身？", 
    q2="流式 SSE 带来什么产品体验？", 
    q3="工具调用如何避免「模型越权写入」？", 
)

DATA["LangChain与Agent_note.md"] = dict(
    map_section="核心层 **K 编排 / Agent**（链路、工具与记忆）。",
    bridge="""- （上一章你应带走）你会直连模型并拼 prompt。
- **但是，我们遇到了一个新的问题：** 真实应用需要多步、工具、状态，而散写 `if`/`for` 会迅速失控。
- **因此本章需要：**把链路想成 **有向步骤图 + 路由器 + memory 槽位**。""",
    motivation="编排框架价值在「合流工具链」≠神秘黑箱。", 
    analogy="像在旅行社拼团：**Agent=导游**，工具=景点班车，memory=客人偏好便签。", 
    basic_ex="画三步 LCEL/chain 手写草图。", 
    adv_ex="列举工具列表+伪 JSON 路由。", 
    open_ex="比较「纯 prompt 路由器」vs 显式 finite state。", 
    q1="链路与图（graph）选型边界？", 
    q2="memory 污染源有哪些？", 
    q3="如何单测一个不稳定的 LLM 步骤？", 
)

DATA["RAG与向量库_note.md"] = dict(
    map_section="核心层 **L RAG + 向量检索**（离线索引、在线检索）。",
    bridge="""- （上一章你应带走）你会搭多步应用骨架。
- **但是，我们遇到了一个新的问题：** 仅靠模型参数记忆挡不住专有知识与频繁变更。
- **因此本章需要：**理解 **离线 chunk → 向量索引 → Top‑k 检索 → prompt 拼装**。""",
    motivation="RAG 把检索当「可控外挂海马体」。", 
    analogy="开卷考：**向量库像索引贴**，模型像考生，Retriever 选对页码。", 
    basic_ex="写 chunk pipeline 口述。", 
    adv_ex="列 hybrid search 思路。", 
    open_ex="写评估：hit@k/context precision 草表。", 
    q1="embedding 选择与领域 mismatch 会发生什么？", 
    q2="chunk overlap 带来什么 trade-off？", 
    q3="如何缓解「检索胡拼」 hallucination？", 
)

DATA["微调与推理部署_note.md"] = dict(
    map_section="核心层 **M 微调 / 推理服务**（LoRA、批量推理与本地部署的概念槽）。",
    bridge="""- （上一章你应带走）你会用检索把事实挂进上下文。
- **但是，我们遇到了一个新的问题：** 仅靠 prompt+RAG 仍治不好「口吻、术语一致性、领域风格」时会想到改权重。
- **因此本章需要：**弄清 **微调成本** 与 **推理侧吞吐/延迟** 的基本张力。""",
    motivation="训练和推理是两条产线：**别混聊 latency 与 throughput**。", 
    analogy="微调像给企业制服加绣名字；推理部署像开店排班：**GPU 工时** versus **来客并发**。", 
    basic_ex="写一张「何时优先 prompt vs RAG vs finetune」checklist。", 
    adv_ex="比较 batching vs streaming 推理 SLA。", 
    open_ex="读 LoRA intuition 一页笔记。", 
    q1="full finetune vs adapter 的工程差异？", 
    q2="'量化'在什么情况下伤任务？", 
    q3="'本地 Ollama' vs 「托管 API」选型三维？", 
)

DATA["企业工程化落地_note.md"] = dict(
    map_section="核心层 **N 企业化**：CI/CD、密钥、红线、成本控制与观测。",
    bridge="""- （上一章你应带走）你能对比「训练侧」与「推理侧」的取舍。
- **但是，我们遇到了一个新的问题：** 模型只占系统一角，合规值班、成本控制与团队协作才是持久战。
- **因此本章需要：**把 **机密、门禁、漂移监测、人机协同**落成清单。""",
    motivation="把 map N 的工程清单落到「可值班」粒度。", 
    analogy="像在城里开连锁餐饮：**配方（模型）只占一角**，供应链/CCTV/出纳才是活得久的部分。", 
    basic_ex="列 secrets 管理方式三种。", 
    adv_ex="画 GitHub Actions 测试门禁草图。", 
    open_ex="写数据出境+PII checklist。", 
    q1="'可观测 AI'你定义哪三类信号？", 
    q2="'人在回路'在什么决策不可省略？", 
    q3="'提示词版本化'类比哪种传统工程实践？", 
)

# ---- helpers ----------------------------------------------------------------

def head_block(entry: dict[str, str]) -> str:
    body = (
        f"{MARK_H}\n\n"
        "## 本节在分层地图中的位置\n\n"
        f"- （总图）`obsidian-vault/LLM_Learning/raw/Python进阶到AI应用_完整学习地图.md` — {entry['map_section']}\n"
        "- （路线主题）`obsidian-vault/LLM_Learning/wiki/topics/python-advanced-to-ai-roadmap.md`\n"
        "- （概念索引）`obsidian-vault/LLM_Learning/wiki/index.md`\n\n"
        "## 衔接：上一章 · 新问题 · 本章\n\n"
        f"{entry['bridge']}\n\n"
        "## 动机（本章解决的真实痛点）\n\n"
        f"{entry['motivation']}\n\n"
        "## 类比（非编程对齐）\n\n"
        f"{entry['analogy']}\n\n"
        "## 如何阅读下方主干（对上述 Cursor 讲义结构）\n\n"
        "- 下文 **`## 一、` ~ `## 七、`** 依次承担 **定义（含辨析表）+ Why + 操作流程 + 边界 +（强化）陷阱 + 延伸阅读**。\n"
        "- 表中「与相关概念区别」即为 **辨析**；标为陷阱/误区处请对照抄写进你的错题本。\n\n"
    )
    return body


def tail_block(entry: dict[str, str]) -> str:
    return (
        f"{MARK_T}\n\n"
        "## 配套练习指引（自拟答案 / 或对目录内 `.py` 练习文件）\n\n"
        f"### 基础（必做）\n\n{entry['basic_ex']}\n\n"
        f"### 进阶（量力）\n\n{entry['adv_ex']}\n\n"
        f"### 开放（可多样解）\n\n{entry['open_ex']}\n\n"
        "## 费曼反问（只提问，不写标准长篇答案）\n\n"
        f"1. {entry['q1']}\n"
        f"2. {entry['q2']}\n"
        f"3. {entry['q3']}\n"
    )


CLOSER_RE = re.compile(r"\r?\n---\s*\r?\n\r?\n>\s*\*\*闭环")


def _is_unified_persona_note(text: str) -> bool:
    """Skip injection for notes already rewritten as full lecture (title + sections)."""
    lines = text.lstrip("\ufeff").splitlines()
    first = lines[0] if lines else ""
    return "｜讲义笔记" in first and "## 双重示例" in text


def inject_one(path: Path) -> str:
    name = path.name
    entry = DATA[name]
    raw = path.read_text(encoding="utf-8")

    if _is_unified_persona_note(raw):
        return raw

    core = raw
    if MARK_H not in raw:
        if ANCHOR not in raw:
            raise SystemExit(f"No anchor {ANCHOR!r} in {path}")
        core = raw.replace("\n" + ANCHOR, "\n" + head_block(entry) + ANCHOR, 1)

    if MARK_T not in core:
        tail_txt = tail_block(entry)
        m = CLOSER_RE.search(core)
        if m:
            core = core[: m.start()] + "\n\n" + tail_txt + "\n\n" + core[m.start() + 1 :]
        else:
            core = core.rstrip() + "\n\n" + tail_txt + "\n"

    return core


def main() -> None:
    missing: list[str] = []
    for md in sorted(NOTEBOOK_ROOT.rglob("*_note.md")):
        if md.name not in DATA:
            missing.append(str(md))
            continue
        new_text = inject_one(md)
        if new_text != md.read_text(encoding="utf-8"):
            md.write_text(new_text, encoding="utf-8")
            print("updated", md.relative_to(ROOT))
    if missing:
        raise SystemExit("Missing DATA entries for:\n  " + "\n  ".join(missing))


if __name__ == "__main__":
    main()
