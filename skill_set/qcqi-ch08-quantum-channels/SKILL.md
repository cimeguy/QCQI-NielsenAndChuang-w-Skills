---
name: qcqi-ch08-quantum-channels
description: "《量子计算与量子信息》(Nielsen & Chuang) 第八章补充「量子信道 quantum channel」知识库。涵盖量子信道的三种等价描述（信道映射、Kraus 算符、蔡氏矩阵 Choi matrix）及其相互转换、典型信道（比特翻转/相位翻转/相位阻尼/去极化/振幅阻尼）的 Kraus 算符与 Bloch 向量仿射变换矩阵、多个信道→Kraus 算例、扰动量子纠错 (Perturbative QEC) 公式的数值验证。当用户学习量子信道、Kraus 表示、Choi-蔡氏矩阵、或在信道/Kraus/仿射变换之间转换时使用。"
---

<!-- argument-hint: [主题、概念名 或 小节号 如 8.2 / sec8.2] -->

# 量子计算与量子信息 · 第八章补充 量子信道
**原著**: M. Nielsen & I. Chuang《Quantum Computation and Quantum Information》第八章补充 | **来源**: 中文学习笔记 (.nb) | **生成**: 2026-06-19

## 如何使用本 skill

- **不带参数** — 加载量子信道的三种描述与转换框架
- **带主题** — 问 `Kraus`、`蔡氏矩阵`、`相位阻尼`、`Bloch 仿射` 等，我会读对应小节文件再回答
- **带小节号** — 问 `8.2` 或 `sec8.2`，加载该小节
- **浏览** — 问"有哪些小节？"查看完整索引

当你问的主题不在下面的核心框架里，我会先读相关小节文件再回答。

---

## 核心概念框架

**量子信道 = CPTP 映射**：开放量子系统的演化由完全正定且保迹 (Completely Positive Trace-Preserving) 的映射 $\mathcal{E}(\rho)$ 描述。它有三种等价描述，本补充围绕它们之间的相互转换展开。

**三种等价描述**：
1. **信道映射 $\mathcal{E}$**：直接给出 $\rho \to \mathcal{E}(\rho)$。
2. **Kraus 算符** $\{E_k\}$：$\mathcal{E}(\rho)=\sum_k E_k \rho E_k^\dagger$，保迹条件 $\sum_k E_k^\dagger E_k = I$。
3. **蔡氏矩阵 (Choi matrix)** $J(\mathcal{E})$：把信道作用在最大纠缠态上得到的矩阵，$J(\mathcal{E})=(\mathcal{E}\otimes I)(\ketbra{\Omega}{\Omega})$。

**转换路径（本补充主线）**：信道 $\to$ 蔡氏矩阵（以比特翻转为例）$\to$ 对蔡氏矩阵做谱分解（本征值/本征态）$\to$ Kraus 算符。Choi-Jamiołkowski 同构是这条路径的理论基础。

**典型信道**：比特翻转、相位翻转、相位阻尼（与相位翻转效果一致）、去极化、振幅阻尼——每个都有标准 Kraus 算符与对应的 **Bloch 向量仿射变换矩阵**（$\vec r \mapsto M\vec r + \vec c$，描述 Bloch 球如何被压缩/平移）。

**应用**：用上述工具数值验证扰动量子纠错 (Perturbative Quantum Error Correction) 中两个公式 (18) 与 (20) 的等价性。

---

## 小节索引

| 小节 | 标题 | 关键概念 |
|---|---|---|
| [8.1](chapters/sec8.1-channel-to-choi.md) | 从信道到蔡氏矩阵 | CPTP、Choi 矩阵定义、比特翻转为例 |
| [8.2](chapters/sec8.2-choi-to-kraus.md) | 从蔡氏矩阵到 Kraus 算符 | 谱分解、本征值/本征态 $\to$ Kraus |
| [8.3](chapters/sec8.3-typical-channels.md) | 典型信道 | Kraus 算符 + Bloch 仿射变换矩阵 |
| [8.4](chapters/sec8.4-examples.md) | 算例与验证 | 信道 $\to$ Kraus 多例、换基、Perturbative QEC 验证 |

## 主题索引

- **Bloch 向量仿射变换** $\to$ 8.3
- **CPTP / 完全正定保迹** $\to$ 8.1
- **Choi / 蔡氏矩阵** $\to$ 8.1, 8.2
- **Kraus 算符** $\to$ 8.2, 8.3, 8.4
- **去极化 / 振幅阻尼** $\to$ 8.3
- **比特翻转 / 相位翻转 / 相位阻尼** $\to$ 8.1, 8.3
- **扰动量子纠错验证** $\to$ 8.4
- **谱分解（蔡氏矩阵）** $\to$ 8.2

## 辅助文件

- [glossary.md](glossary.md) — 关键术语表（中英对照）
- [patterns.md](patterns.md) — 信道/Kraus/蔡氏矩阵转换技巧
- [cheatsheet.md](cheatsheet.md) — 典型信道 Kraus 与仿射变换速查

---

## 范围与限制

本 skill 来自一份内容较"骨架化"的 Mathematica 补充笔记——原文主要由标题、公式单元与数值代码构成，散文说明很少。因此本 skill 的小节在忠实转录笔记结构的基础上，结合量子信道的标准知识补全了概念脉络；具体的矩阵数值、谱分解结果、QEC 公式 (18)/(20) 的完整表达式与数值验证代码未在笔记文本层中完整保留。精确公式与数值请参阅原书第 8 章与原笔记。
