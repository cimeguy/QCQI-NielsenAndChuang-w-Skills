# 8.2 从蔡氏矩阵到 Kraus 算符

## 核心思想
蔡氏矩阵 $J(\mathcal{E})$ 是半正定矩阵，对它做谱分解（求本征值与本征态），每个本征对就给出一个 Kraus 算符。这是从信道矩阵表示恢复算符和表示的标准途径。

## 谱分解 → Kraus
- 对 $J(\mathcal{E})$ 做谱分解：$J = \sum_k \lambda_k \ketbra{v_k}{v_k}$，$\lambda_k\ge 0$（因 $J$ 半正定）。
- 每个本征向量 $\ket{v_k}$（$d^2$ 维）按"向量化逆操作"reshape 成 $d\times d$ 矩阵，再乘 $\sqrt{\lambda_k}$，即得一个 **Kraus 算符** $E_k = \sqrt{\lambda_k}\cdot\mathrm{mat}(\ket{v_k})$。
- 于是 $\mathcal{E}(\rho)=\sum_k E_k \rho E_k^\dagger$，且保迹 $\sum_k E_k^\dagger E_k=I$。

## 讨论蔡氏矩阵的本征值与本征态
- **非零本征值个数** = 信道的 **Kraus 秩**（最少需要的 Kraus 算符数）。
- 本征值 $\lambda_k$ 给出各 Kraus 通道的"权重"；$\lambda_k=0$ 的方向不贡献 Kraus 算符。
- **Kraus 表示不唯一**：任意一组 Kraus $\{E_k\}$ 与另一组 $\{F_j\}$ 等价 $\iff$ 差一个幺正混合 $F_j=\sum_k u_{jk}E_k$（谱分解给出的是正交规范的一组）。

## 关键要点
1. $J$ 半正定 $\Rightarrow$ 谱分解 $J=\sum_k\lambda_k\ketbra{v_k}{v_k}$，$\lambda_k\ge 0$。
2. 每个 $(\sqrt{\lambda_k}, \ket{v_k}) \to$ 一个 Kraus 算符 $E_k$（向量 reshape 成矩阵）。
3. 非零本征值数 = Kraus 秩；Kraus 表示差一个幺正自由度，不唯一。

## 关联
- **8.1**：$J$ 由信道 $\to$ 蔡氏矩阵得到。
- **8.3/8.4**：对典型信道与算例执行这套谱分解流程。
