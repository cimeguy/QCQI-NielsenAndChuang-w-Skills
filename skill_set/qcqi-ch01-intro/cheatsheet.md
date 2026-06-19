# 速查表 · QCQI 第一章

## 常用单比特门
| 门 | 矩阵 (计算基) | 作用 |
|---|---|---|
| X (NOT) | $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | 翻转，绕 $x$ 轴 $\pi$ |
| Y | $\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ | 绕 $y$ 轴 $\pi$ |
| Z | $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | 相位翻转 $\ket{\beta}\to-\ket{\beta}$ |
| H | $\tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ | 等权叠加；交换 $X\leftrightarrow Z$ |
| S | $\begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$ | $\pi/2$ 相位 |
| T | $\begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$ | $\pi/4$ 相位 ($\pi/8$ 门) |

## 决策：选哪个门 / 操作
- 要**等权叠加** → H（每比特一个）。
- 要**纠缠两比特** → CNOT（前置 H 制 Bell 态）。
- 要**翻转目标**（条件） → CNOT / Toffoli。
- 要**交换比特**且只有 CNOT → SWAP = 3×CNOT。
- 要**把经典函数塞进线路** → Toffoli + ancilla + uncompute。
- 要**编译任意 U(2)** → z-y-z 分解；离散集再用 Solovay-Kitaev。

## Bloch 球速记
- 纯态：球面，$\lVert r\rVert=1$；混合态：球内，$\lVert r\rVert<1$；最大混合 $\rho=I/2$ → 球心。
- $\ket{\psi}=\cos(\theta/2)\ket{0}+e^{i\phi}\sin(\theta/2)\ket{1}$；$r_i=\Tr(\rho\sigma_i)$。
- 门 = 旋转：$R_n(\theta)$ 绕轴 $n$ 转 $\theta$。

## 测量概率速记
- 计算基测 $\alpha\ket{0}+\beta\ket{1}$：$P(0)=\lvert\alpha\rvert^2$, $P(1)=\lvert\beta\rvert^2$。
- 测量后态塌缩到对应本征态；测量不对易（如 $Z$ 后测 $X$ 会"重置"$Z$ 信息）。

## 复杂性 / 加速判断
| 现象 | 含义 |
|---|---|
| 经典获取信息量 $>$ 答案所需信息量 | 有"计算冗余"→ 量子可能加速 |
| 问全局性质 (如 $f(0)\oplus f(1)$) | 适合量子并行+干涉 |
| 因数分解 / 求阶 | QFT 家族，$\in$ BQP |
| 非结构化搜索 | Grover，$O(N)\to O(\sqrt{N})$ |
| 模拟量子多体系统 | 量子模拟，指数→多项式 |
| BPP $\subsetneq$ BQP ? | 量子是否严格强于经典——核心开放问题 |

## 三条不可违反的红线
1. **不可克隆** → 禁止扇出/复制未知态。
2. **幺正可逆** → 禁止扇入、禁止环路。
3. **测量即塌缩** → 干涉做完再测，别中途窥探。

## 物理平台速记
光学 · 超导(transmon) · 离子阱 · 冷原子 · NV 色心 · NMR · 任意子。
阶段：小规模(通信) → NISQ(中等含噪) → 大规模(容错，靠阈值定理)。
