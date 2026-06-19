# 2.4 演化与测量

## 核心思想
封闭系统按幺正变换演化（公理 2）；测量按 PVM/POVM 给出概率与测后态（公理 3）。这两条把"态如何变化"和"如何提取信息"精确化。

## 幺正演化
- **薛定谔方程**：$i\hbar\, d\ket{\psi}/dt = H\ket{\psi}$，解为 $\ket{\psi(t)}=U(t)\ket{\psi(0)}$，$U=e^{-iHt/\hbar}$ 幺正。
- **定态**：哈密顿量本征态 $H\ket{E}=E\ket{E}$，演化只是乘相位 $e^{-iEt/\hbar}$，概率分布不随时间变化。
- **密度算符演化**：$\rho\to U\rho U^\dagger$。

## 测量：PVM 与 POVM
- **PVM（投影算符值测度）**：一族投影 $\{P_i\}$，满足 $P_i$ 正交幂等 $+\ \sum_i P_i=I$。从 PVM 构建物理量 $A=\sum_i a_i P_i$（Hermite）。
  - 结果 $i$ 的概率 $=\Tr(\rho P_i)$（纯态 $=\bra{\psi}P_i\ket{\psi}$）；测后态 $=P_i\rho P_i/\Tr(\rho P_i)$。
- **POVM**：一族正定算符 $\{E_i\}$，只需 $E_i\ge0$ 且 $\sum_i E_i=I$（不要求正交/幂等）。是 PVM 的推广，用于不关心测后态、只求最优区分概率的场景。
- **单 qubit 测量**：计算基测量 = 用 $\{\ketbra{0}{0},\ketbra{1}{1}\}$；测 $\sigma_x$ 则用 $\{\ketbra{+}{+},\ketbra{-}{-}\}$（非计算基方向）。
- **Bell 基测量**：在计算基下测 Bell 态，两方结果总相同（关联）。

## 统计量与不确定性
- **期望**：$\langle A\rangle=\Tr(\rho A)$。
- **方差**：$(\Delta A)^2=\langle A^2\rangle-\langle A\rangle^2$。
- **海森堡不确定性关系**：$\Delta A\cdot\Delta B \ge \tfrac{1}{2}\lvert\langle[A,B]\rangle\rvert$，源于算符不对易。

## 关键要点
1. 演化幺正、可逆；测量非幺正、不可逆且改变态。
2. 可观测量 ↔ PVM ↔ Hermite 算符，三位一体。
3. POVM 比 PVM 更灵活，是态区分等任务的最优测量框架。
4. 不对易算符不能同时确定 ⇒ 不确定性关系。

## 关联
- **2.1**：本节是公理 2、3 的展开。
- **2.3**：测量作用于 $\rho$，给出 $\Tr(\rho P_i)$。
- **2.6**：POVM 用于非正交态的最优区分。
