---
name: qcqi-ch01-intro
description: "《量子计算与量子信息》(Nielsen & Chuang) 第一章「量子计算简介」知识库。涵盖量子比特、Bloch 矢量、单/多比特量子门、量子线路、隐形传态、Deutsch 算法、量子并行、量子信息论等。当用户学习或引用 QCQI 第一章、需要量子计算入门概念、或讨论量子门/隐形传态/Deutsch 算法时使用。"
---

<!-- argument-hint: [主题、概念名 或 小节号 如 1.2 / sec1.2] -->

# 量子计算与量子信息 · 第一章 量子计算简介
**原著**: M. Nielsen & I. Chuang《Quantum Computation and Quantum Information》| **小节**: 1.1–1.6 | **来源**: 中文学习笔记 (.nb) | **生成**: 2026-06-19

## 如何使用本 skill

- **不带参数** — 加载第一章的核心概念框架
- **带主题** — 问 `隐形传态`、`Deutsch`、`Bloch`、`通用门` 等，我会读对应小节文件再回答
- **带小节号** — 问 `1.3` 或 `sec1.3`，加载该小节
- **浏览** — 问"有哪些小节？"查看完整索引

当你问的主题不在下面的核心框架里，我会先读相关小节文件再回答。

---

## 核心概念框架

**量子计算的定义**：利用量子系统及其特性（叠加、纠缠、测量的概率性、对环境敏感）完成信息处理任务。远期目标是实现实用的通用量子计算，在某些问题上超越任何经典计算机。

**量子比特 (qubit)**：状态 $\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$，$\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1$。区别于经典比特，可处于叠加态；测量塌缩为基态，概率为幅的模方。密度矩阵 $\rho$ 的迹为 1（概率归一）。

**Bloch 球表示**：单 qubit 纯态 = $\ket{\psi} = \cos(\theta/2)\ket{0} + e^{i\phi}\sin(\theta/2)\ket{1}$，对应单位球面上一点 $(\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$。任意态都可由某个 $U\in U(2)$ 作用 $\ket{0}$ 得到——几何上是绕某轴旋转。

**单比特门 = $U(2)$ 旋转**：核心门 = $R_x(\theta)$、$R_y(\theta)$、$R_z(\theta)$、Hadamard($H$，制备等权叠加)、相位门 $S$、$T$ 门。任意单比特门可做 **z-y-z 分解**（旋量空间欧拉角），$(SU(2)\ltimes U(1))/2 = U(2)$。

**多比特门**：CNOT（受控非，纠缠的生成器）、SWAP（=三个 CNOT）、Toffoli（受控受控非，经典可逆计算的通用门）。

**通用门集合**：一组能以任意精度模拟任何幺正变换的门。精度越高所需门越多。常用通用集 = $\{H, T, \text{CNOT}\}$ 等。

**量子线路规则**：无环（不出现回路）；不允许扇入（不可逆）和扇出（违反不可克隆定理）。

**量子隐形传态 (teleportation)**：用一对 Bell 态 + 2 比特经典通信，把未知量子态从 Alice 传给 Bob。本质是 LOCC（本地操作+经典通信）。不违反相对论（需经典信道）也不违反不可克隆（原态被测量破坏）。

**Deutsch 算法（量子并行的范例）**：用一次 $U_f$ 调用判断 $f$ 是常数型还是平衡型，经典需两次。启发：当经典计算获取的信息量超过问题答案所需信息量（存在计算冗余）时，量子有加速潜力。推广到 $n$ 位 = Deutsch-Jozsa 算法。

**量子算法两大家族**：① 基于量子 Fourier 变换（Shor 因数分解，经典 $O(N) \to$ 量子可多项式）；② 量子搜索（Grover，$O(N) \to O(\sqrt{N})$）；③ 量子模拟（Feynman 设想，模拟量子系统）。

**复杂性视角**：因数分解 $\in$ BQP。核心开放问题——是否 BPP $\subsetneq$ BQP（量子是否严格强于经典概率计算）。量子版丘奇-图灵论题：量子图灵机能高效模拟任何现实计算模型。

---

## 小节索引

| 小节 | 标题 | 关键概念 |
|---|---|---|
| [1.1](chapters/sec1.1-overview.md) | 量子计算和量子信息简介 | 可计算性、丘奇-图灵论题、复杂性类、发展简史 |
| [1.2](chapters/sec1.2-qubit.md) | 量子比特 | qubit、叠加、Bloch 矢量、测量、Bell 基 |
| [1.3](chapters/sec1.3-quantum-computation.md) | 量子计算 | 单/多比特门、z-y-z 分解、通用门、量子线路、隐形传态 |
| [1.4](chapters/sec1.4-algorithms.md) | 量子算法 | 可逆计算、量子并行、Deutsch 算法、算法家族 |
| [1.5](chapters/sec1.5-experiments.md) | 量子信息处理实验 | Stern-Gerlach、阈值定理、NISQ、物理实现平台 |
| [1.6](chapters/sec1.6-quantum-info.md) | 量子信息 | 经典 vs 量子信息论、量子信息的基本目标 |

## 主题索引

- **Bell 态 / 隐形传态** → 1.2, 1.3
- **Bloch 矢量** → 1.2
- **CNOT / Toffoli / SWAP** → 1.3
- **Deutsch / Deutsch-Jozsa** → 1.4
- **Hadamard / 相位门 / T 门** → 1.3
- **丘奇-图灵论题** → 1.1
- **可计算性 / 复杂性类 (BQP/BPP)** → 1.1, 1.4
- **量子并行** → 1.4
- **量子比特 / 叠加 / 测量** → 1.2
- **量子线路** → 1.3
- **量子算法家族 (Shor/Grover/模拟)** → 1.4
- **通用门集合** → 1.3
- **物理实现 / NISQ / 阈值定理** → 1.5
- **z-y-z 分解** → 1.3

## 辅助文件

- [glossary.md](glossary.md) — 关键术语表（中英对照）
- [patterns.md](patterns.md) — 量子线路构件与技巧
- [cheatsheet.md](cheatsheet.md) — 量子门速查与决策表

---

## 范围与限制

本 skill 仅覆盖 QCQI 第一章（量子计算简介）的概念框架，源自一份中文 Mathematica 笔记。公式以纯文本/Unicode 近似表示，精确推导请参阅原书。第 2 章起的线性代数、量子操作、纠错等内容不在此范围内。
