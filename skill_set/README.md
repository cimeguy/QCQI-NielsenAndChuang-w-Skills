# QCQI Skill Set · 《量子计算与量子信息》Agent 技能集

把 Nielsen & Chuang《Quantum Computation and Quantum Information》(QCQI) 的中文学习笔记 (Mathematica `.nb`) 转换成的一组 **Agent Skills**，可被 Claude Code / GitHub Copilot CLI / Amp 等支持 Skill 标准的智能体加载，用于学习、复习、查询 QCQI 各章知识。

## 包含的 skill

| Skill | 覆盖章节 | 主题 |
|---|---|---|
| `qcqi-ch01-intro` | 第一章 | 量子计算简介：qubit、Bloch、量子门、量子线路、隐形传态、Deutsch、量子并行 |
| `qcqi-ch02-linalg-qm` | 第二章 | 线性代数与量子力学：四公理、SVD、密度矩阵、PVM/POVM、偏迹、Schmidt 分解、纯化、Bell 不等式、态区分、超密编码 |
| `qcqi-ch04-circuits` | 第四章 | 量子线路与模拟：单比特门=旋转、z-y-z 分解、受控门、测量原理、通用门 {H,T,CNOT}、量子计算机要素、其他计算模型、Trotter/BCH 量子模拟 |
| `qcqi-ch05-qft` | 第五章 | QFT 与 Shor：量子并行、量子傅里叶变换、相位估计、Shor 大数分解/求阶、隐藏子群问题 |
| `qcqi-ch06-search` | 第六章 | 量子搜索：搜索问题、布尔/相位翻转预言机、Grover 迭代、几何意义、成功概率、启发式推导 |
| `qcqi-ch08-quantum-channels` | 第八章补充 | 量子信道：信道/Kraus 算符/蔡氏矩阵 (Choi) 三种描述与相互转换、典型信道、Bloch 仿射变换、扰动量子纠错验证 |
| `qcqi-key-points` | 第 2/4/5 章 | 各章关键知识点汇总——跨章复习与导航索引 |

## 每个 skill 的结构

遵循 Agent Skill 标准：

```
qcqi-chNN-xxx/
├── SKILL.md          # 入口：frontmatter(name/description) + 核心框架 + 小节索引 + 主题索引
├── chapters/         # 各小节详解（核心思想 / 框架 / 关键要点 / 关联）
│   └── secN.M-*.md
├── glossary.md       # 术语表（中英对照）
├── patterns.md       # 技巧与构件（何时用 / 怎么做 / 权衡）
└── cheatsheet.md     # 速查表与决策表
```

`SKILL.md` 的 `description` 字段决定智能体何时自动加载该 skill；`chapters/` 下的文件按需加载，避免一次性占用上下文。

## 在线浏览（GitHub Pages）

已部署到 GitHub Pages，可直接在线访问（公式渲染、深浅色、搜索均可用）：

**<https://cimeguy.github.io/QCQI-NielsenAndChuang-w-Skills/>**

三套门户互相链接：公式精简版 `index.html` · 🗣️ 人话版 `explained.html` · 🎓 大学生版 `student.html`。
推送到 `main` 且改动 `skill_set/**` 时由 GitHub Actions 自动重新部署，发布的人工操作步骤见仓库根目录 [`部署网站.md`](../部署网站.md)。

## HTML 可视化浏览（离线）

除了作为 Agent Skill 加载，本仓库还提供一套**可离线浏览的 HTML 知识页面**，把每个 skill 的全部内容（SKILL.md + 各小节 + 术语表 + 技巧 + 速查表）渲染成单文件页面，并在页首附带该章的**手绘 SVG 可视化图示**（Bloch 球、量子线路图、QFT/Shor 流程、Grover 几何旋转、量子信道仿射变换、跨章思维导图等）。

本仓库提供三套面向不同读者的页面版本，由三个脚本分别生成（均为纯标准库、离线可用）：

```bash
python3 skill_set/build_html.py        # 公式精简版 index.html（忠实原书）
python3 skill_set/build_explained.py   # 🗣️ 人话版 explained.html（程序员友好）
python3 skill_set/build_student.py     # 🎓 大学生版 student.html（从零补线代/概率）
```

### 依赖与环境

| 用途 | 依赖 | 说明 |
|---|---|---|
| 生成 HTML | **Python ≥ 3.8** | 仅用标准库（`html`、`re`、`pathlib`），**无需 `pip install` 任何包**。 |
| 公式渲染 | **MathJax** | 国内 CDN（npmmirror/bootcdn）优先，失败回退仓库自带的 `skill_set/vendor/tex-svg.js`（约 2.1 MB）；联网时秒开，离线/CDN 不可用时仍可渲染。 |
| 浏览页面 | 任意现代浏览器 | 双击 `index.html`，`file://` 直接打开即可，无需本地服务器。 |

> 不依赖 Node.js、npm、`markdown`/`jinja2` 等第三方库；Markdown→HTML 由 `build_html.py` 内置的精简转换器完成。升级公式引擎只需替换 `vendor/tex-svg.js`。

生成物（已随仓库提交，可直接打开）：

- `skill_set/index.html` — **门户页**，卡片式导航到各章。
- `skill_set/<skill>/index.html` — 每个 skill 一页，含左侧小节导航、客户端搜索过滤、深/浅色切换、章节锚点、章首可视化面板。

双击任一 `index.html` 即可在浏览器查阅（`file://` 直接可用，无 CDN/网络依赖）。修改 `.md` 笔记后重跑脚本即可重新生成；可视化片段存放在 `skill_set/_viz/<skill>.html`，会被脚本注入对应页面。

### 人话版（程序员友好的通俗讲解）

除了上面忠实于原书的「公式版」，仓库还提供一套**「人话版」**页面：面向有计算机背景、但没有物理基础的读者，把晦涩的量子数学翻译成程序员能秒懂的大白话——每条公式都配直觉解释、编程类比与避坑提示。

```bash
python3 skill_set/build_explained.py     # 同样纯标准库，离线可用
```

生成物：

- `skill_set/explained.html` — **人话版门户**（暖色主题），与公式版门户 `index.html` 相互链接。
- `skill_set/<skill>/explained.html` — 每章一页，含四类彩色提示框：
  - 💡 **人话**：这条公式到底在说什么；
  - 🧠 **类比**：用代码 / 数据结构 / 复杂度等 CS 概念打比方；
  - ⚠️ **坑**：容易误解的地方；
  - 🔑 **记住**：一句话带走的结论。

内容源文件为各 skill 目录下的 `explained.md`，公式约定与公式版一致（LaTeX + 内置 MathJax 离线渲染、数学中不使用裸 `|`、改用 `\ket{}` 等宏）。

### 大学生版（从零补数学基础）

第三套**「大学生版」**面向刚学过矩阵 / 概率 / 线性代数但基础还不太牢的同学：每个量子概念都先把用到的数学基础**从头讲一遍**，再一步步代数字演算，并标出最容易踩的坑。

```bash
python3 skill_set/build_student.py        # 同样纯标准库，离线可用
```

生成物：

- `skill_set/student.html` — **大学生版门户**（冷色主题），与公式版、人话版门户相互链接。
- `skill_set/<skill>/student.html` — 每章一页，含七类彩色提示框：🎯 用来干嘛 / ⚛️ 物理上是啥 / 📖 补基础 / 🧮 一步步算 / 💭 直觉 / ⚠️ 常见错误 / ✅ 小结。

此外还支持两种可折叠 `<details>` 块：

- `:::expand 标题 … :::` → ⚛️ 物理科普盒（讲清量子概念背后的物理意义）；
- `:::qa 标题 … :::` → 蓝色「答疑」盒，收录不同背景读者（数学基础薄弱的学生、计算机/数学从业者等）最常问的问题与解答。

内容源文件为各 skill 目录下的 `student.md`，公式约定与上面两版一致。

### 公式渲染（LaTeX / MathJax，离线）

各 `.md` 笔记中的公式以 LaTeX 书写（行内 `$...$`、行间 `$$...$$`），HTML 页面用 **MathJax**（`tex-svg`，SVG 输出、自带字形）渲染。加载策略为**国内 CDN 优先 + 本地兜底**：先从 npmmirror（阿里）/ bootcdn 拉取 `tex-svg.js`，失败再回退到仓库自带的 `skill_set/vendor/tex-svg.js`，因此国内访问秒开、离线或 CDN 不可用时仍能正常显示公式。

约定与注意：

- 预定义了量子记号宏：`\ket{}`、`\bra{}`、`\braket{}{}`、`\ketbra{}{}`、`\Tr`，在 `build_html.py` 的 MathJax 配置里注入。
- 数学式中**不使用裸 `|`**（会与 Markdown 表格列分隔符冲突），一律用 `\ket{}` / `\lvert` / `\mid` 等宏——这样表格内也能安全写 ket。
- 生成器会在 Markdown→HTML 前把 `$...$` / `$$...$$` 整体"保护"起来，避免被 `**`、表格、转义破坏，渲染后再还原（仅对 `<`、`>`、`&` 做安全转义，矩阵 `&` 对齐可正常工作）。
- 章首的 SVG 可视化面板带 `viz` 类，MathJax 通过 `ignoreHtmlClass` 跳过，不会误渲染图示中的文字。
- 升级/替换引擎：重新下载 `tex-svg.js` 到 `vendor/` 即可（页面以相对路径 `../vendor/tex-svg.js` 引用）。

## 如何使用

### Claude Code
把某个 skill 目录（或整个 `skill_set/`）放到 skill 根目录下，例如：

```bash
cp -r skill_set/qcqi-ch05-qft ~/.claude/skills/
```

之后在对话中提到相关主题（如"讲讲 Shor 算法的求阶"），Claude 会自动加载并参考该 skill；也可显式用 `/qcqi-ch05-qft` 调用。

### GitHub Copilot CLI / Amp
放到对应的 skill 根目录即可（如 `~/.copilot/skills/`、`~/.agents/skills/`、`~/.config/agents/skills/`）。

### 典型用法
- **不带参数**：加载该章核心概念框架。
- **带主题**：问 `Schmidt 分解`、`Grover`、`蔡氏矩阵` 等，智能体读对应小节再回答。
- **带小节号**：问 `5.4` / `sec5.4`，加载该小节。
- **复习**：用 `qcqi-key-points` 做跨章串讲与"必背清单"。

## 这些 skill 是怎么生成的

源文件是中文 **Mathematica 笔记** (`.nb`)，文本以 `\:xxxx` Unicode 转义、`\[Alpha]` 等数学符号、以及 base64 栅格图像数据存储，标准工具难以直接读取。本仓库用一个自写的 `.nb → markdown` 提取器（纯 Python 标准库）处理：

1. **解码**：还原 `\:xxxx` Unicode 转义与 `\[Name]` 数学符号。
2. **按单元对齐**：以 Cell 的 style（Title/Section/Subsection/Text/Item 等）为锚点切分，保持层级。
3. **降噪过滤**：丢弃 Input/Output 代码单元、UUID、导航元数据、base64 图像 blob（>120 字符且不含中文的串、含 `RasterBox`/`GraphicsData` 等关键字的串）。
4. **保留散文**：抽取引号内的中文/英文说明文字。

提取出的 markdown 作为"源"，再依据 Agent Skill 标准提炼成上面的 SKILL.md + chapters + glossary + patterns + cheatsheet 结构。

> 说明：第 9/10/11 章是 Goodnotes 手写 PDF（无文本层，需 OCR），暂未转换；第 8 章主章为手写 PDF，仅"第八章补充"`.nb` 已转换。

## 范围与限制

- 公式以纯文本 / Unicode 近似表示，精确推导、矩阵数值、线路图、绘图请参阅原书与原始 `.nb`。
- 内容源于一份个人中文学习笔记（部分章节作者：魏文杰），可能与原书章节编号、措辞不完全一致。
- 第八章补充笔记较"骨架化"（多为公式单元与代码），相应 skill 在忠实转录结构的基础上结合量子信道标准知识补全脉络，已在该 skill 的"范围与限制"中注明。

## 原书

M. A. Nielsen & I. L. Chuang, *Quantum Computation and Quantum Information*, Cambridge University Press.
