---
name: qcqi-ch04-circuits
description: "《量子计算与量子信息》(Nielsen & Chuang) 第四章「量子线路与量子模拟」知识库。涵盖单比特门 U(2) 与旋转、z-y-z 分解与欧拉角、受控门 (CNOT/CZ/SWAP/Toffoli)、测量原理（延迟/隐含测量、Bell 基测量、对算符测量）、通用门集合三步证明、量子计算机五要素、其他量子计算模型（绝热/拓扑/MBQC 等）、量子模拟与 Trotter/BCH 公式。当用户学习或引用 QCQI 第四章、需要量子线路构造、通用门、或量子模拟/Trotter 分解时使用。"
---

<!-- argument-hint: [主题、概念名 或 小节号 如 4.2 / sec4.2] -->

# 量子计算与量子信息 · 第四章 量子线路与量子模拟
**原著**: M. Nielsen & I. Chuang《Quantum Computation and Quantum Information》| **来源**: 中文学习笔记 (.nb) | **生成**: 2026-06-19

## 如何使用本 skill

- **不带参数** — 加载第四章的核心线路/模拟框架
- **带主题** — 问 `CNOT`、`Toffoli`、`通用门`、`Trotter`、`欧拉角` 等，我会读对应小节文件再回答
- **带小节号** — 问 `4.4` 或 `sec4.4`，加载该小节
- **浏览** — 问"有哪些小节？"查看完整索引

当你问的主题不在下面的核心框架里，我会先读相关小节文件再回答。

---

## 核心概念框架

**量子线路 = 量子计算的通用语言**：用幺正门组成的有向无环图操纵 qubit。已知的两大基础算法（QFT、量子搜索）都由这些线路构造。

**单比特门 = U(2) 旋转**：任意单比特门可视为 qubit 所在希尔伯特空间（2 维）的一次旋转，对应 Bloch 球（3 维）的 SO(3) 旋转，通过 SU(2) 群表示联系。基本门：Rx/Ry/Rz/Rn(θ)、H、相位门 S、T 门。

**z-y-z 分解（欧拉角）**：任意单比特门 = e^{iα}Rz(β)Ry(γ)Rz(δ)。旋转既可一次实现，也可分三次（欧拉角）实现。Ry 可生成所有单比特门（配合相位）。

**受控门 U(2ⁿ)**：CNOT（纠缠生成器）、CZ、SWAP（=3 CNOT）、Toffoli（CCNOT，经典可逆计算通用门）。一般受控-U 门有标准构造法。

**测量原理**：延迟测量（测量可推迟到线路末端，对应经典 if-then）、隐含测量（线路末端未测的比特可视为已测，简化分析）、Bell 基测量、对算符 U 的测量（既要概率分布又要测后态）。

**通用门集合（三步证明）**：① 二级幺正门通用；② 单比特门 + CNOT 通用；③ {H, T, CNOT} 通用。复杂度：达到精度 ε 需 O(log^c(1/ε)) 个门（Solovay-Kitaev）。

**量子计算机五要素**（DiVincenzo）：可扩展的 qubit、初始化、长相干、通用门集、可靠测量——核心是初始化、幺正变换、测量三环节。

**量子线路以外的模型**：绝热量子计算、拓扑量子计算、量子随机游走、one-clean-qubit、基于测量的量子计算 (MBQC)/单向/簇态、量子图灵机。计算本质是物理过程（Landauer 原理）。

**量子模拟**：把演化时间切片，用 Trotter 公式把每片 e^{−iHΔt} 拆成局域哈密顿量演化的乘积；阶数越高、步数越多，与精确 U(t) 的迹距离越小。配合 BCH 公式分析误差。

---

## 小节索引

| 小节 | 标题 | 关键概念 |
|---|---|---|
| [4.1](chapters/sec4.1-single-qubit-gates.md) | 单比特门 U(2) | Rx/Ry/Rz/Rn、H、S、T、门=旋转、z-y-z 分解、无通用非门 |
| [4.2](chapters/sec4.2-controlled-gates.md) | 受控门 | CNOT、CZ、SWAP=3CNOT、Toffoli、一般受控-U、线路特性 |
| [4.3](chapters/sec4.3-measurement.md) | 测量 | 延迟测量、隐含测量、Bell 基测量、对算符 U 测量 |
| [4.4](chapters/sec4.4-universal-gates.md) | 通用量子门 | 三步通用性证明、{H,T,CNOT}、复杂度 |
| [4.5](chapters/sec4.5-models.md) | 量子计算机要素与其他模型 | 五要素、绝热/拓扑/MBQC/量子游走、Landauer |
| [4.6](chapters/sec4.6-simulation.md) | 量子模拟 | 局域哈密顿量、Trotter 公式、BCH、Trotterization 误差 |

## 主题索引

- **BCH 公式 / 矩阵指数恒等式** → 4.6
- **CNOT / CZ / SWAP / Toffoli** → 4.2
- **Hadamard / S / T 门** → 4.1
- **Rn(θ) / 门=旋转 / SU(2)-SO(3)** → 4.1
- **Trotter 分解 / 量子模拟** → 4.6
- **z-y-z 分解 / 欧拉角** → 4.1
- **延迟测量 / 隐含测量** → 4.3
- **量子计算机五要素** → 4.5
- **通用门 / {H,T,CNOT}** → 4.4
- **其他计算模型（绝热/拓扑/MBQC）** → 4.5

## 辅助文件

- [glossary.md](glossary.md) — 关键术语表（中英对照）
- [patterns.md](patterns.md) — 线路构造与模拟技巧
- [cheatsheet.md](cheatsheet.md) — 门速查与模拟决策表

---

## 范围与限制

本 skill 仅覆盖 QCQI 第四章（量子线路与量子模拟）的概念框架，源自一份中文 Mathematica 笔记。公式以纯文本/Unicode 近似表示。笔记中的 Wolfram 量子框架代码、线路图、Trotter 误差曲线图未完整转录，精确实现请参阅原书与原笔记。
