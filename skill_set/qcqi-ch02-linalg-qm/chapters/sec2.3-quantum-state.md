# 2.3 量子态

## 核心思想
量子态 = 迹为 1 的正定算符 $\rho$。纯态是其极端情形（秩 1），混态是纯态的概率混合。单 qubit 可用 Bloch 矢量几何化。

## 框架
- **物理状态 vs 物理量（经典 vs 量子）**：经典态是相空间一点、物理量是其上的函数；量子态是 $\rho$、物理量是 Hermite 算符，二者通过 $\Tr(\rho A)$ 配对得期望。
- **单 qubit 参数化**：$\ket{\psi}=\cos(\theta/2)\ket{0}+e^{i\phi}\sin(\theta/2)\ket{1}$ ↔ Bloch 矢量 $r=(\sin\theta\cos\phi,\ \sin\theta\sin\phi,\ \cos\theta)$。U3 门 = 用欧拉角参数化 $U(2)$ 群元。
- **密度算符**：$\rho=\sum_i p_i \ketbra{\psi_i}{\psi_i}$，$\Tr(\rho)=1$，$\rho\ge0$。$r_i=\Tr(\rho\sigma_i)$ 给出 Bloch 分量。
- **多比特计算基与 Bell 基**：$n$ 比特计算基 $\{\ket{0\cdots0},\dots,\ket{1\cdots1}\}$；Bell 基是 4 个最大纠缠两比特态。在计算基下测量 Bell 态，Alice 和 Bob 总是得到相同结果（强关联）。
- **希尔伯特空间上的距离**：$d(u,v)$ 由内积导出，如 $\mathrm{Re}\,\braket{u}{v}$ 相关的保真度/迹距离类度量。

## 纯态 vs 混态判据
- **纯态**：$\Tr(\rho^2)=1$；不能写成另外两个量子态的凸线性组合；密度矩阵秩为 1；Bloch 矢量在球面 $\lvert r\rvert=1$。
- **混态**：$\Tr(\rho^2)<1$；秩 $>1$；$\lvert r\rvert<1$（球内）；最大混合 $\rho=I/2$ → 球心。

## 关键要点
1. $\rho$ 是迹 1 正定算符；它编码系统所有可测统计信息。
2. 单 qubit ↔ Bloch 球：纯态在面、混态在内、最大混合在心。
3. 纯/混判据：$\Tr(\rho^2)$、秩、凸组合可分解性、$\lvert r\rvert$ 四者等价。

## 关联
- **2.2**：$\rho$ 是 Hermite 正定算符，用本征分解写成纯态混合。
- **2.4**：$\rho$ 经幺正演化 $\rho\to U\rho U^\dagger$；测量给出 $\Tr(\rho P_i)$。
- **2.5**：约化密度矩阵通常是混态，即使全局是纯态（纠缠的标志）。
