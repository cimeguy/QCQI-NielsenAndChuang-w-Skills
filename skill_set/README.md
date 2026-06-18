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

## HTML 可视化浏览（离线）

除了作为 Agent Skill 加载，本仓库还提供一套**可离线浏览的 HTML 知识页面**，把每个 skill 的全部内容（SKILL.md + 各小节 + 术语表 + 技巧 + 速查表）渲染成单文件页面，并在页首附带该章的**手绘 SVG 可视化图示**（Bloch 球、量子线路图、QFT/Shor 流程、Grover 几何旋转、量子信道仿射变换、跨章思维导图等）。

```bash
python3 skill_set/build_html.py      # 纯标准库，无需安装依赖
```

生成物（已随仓库提交，可直接打开）：

- `skill_set/index.html` — **门户页**，卡片式导航到各章。
- `skill_set/<skill>/index.html` — 每个 skill 一页，含左侧小节导航、客户端搜索过滤、深/浅色切换、章节锚点、章首可视化面板。

双击任一 `index.html` 即可在浏览器查阅（`file://` 直接可用，无 CDN/网络依赖）。修改 `.md` 笔记后重跑脚本即可重新生成；可视化片段存放在 `skill_set/_viz/<skill>.html`，会被脚本注入对应页面。

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
