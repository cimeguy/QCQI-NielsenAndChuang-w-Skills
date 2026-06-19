# 1.2 量子比特

## 核心思想
量子比特 (qubit) 是量子信息的基本单元：可处于 $\ket{0}$ 与 $\ket{1}$ 的线性叠加；测量塌缩为基态、概率为幅的模方；纯态可用 Bloch 球面上的点几何表示。

## 关键概念
- **qubit**：$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}$，$\alpha,\beta\in\mathbb{C}$，$\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1$。计算基 $\{\ket{0},\ket{1}\}$ 是常用 ONB（标准正交基）。
- **态矢量与密度矩阵**：密度矩阵 $\rho = \ketbra{\psi}{\psi}$，$\Tr(\rho)=\lvert\alpha\rvert^2+\lvert\beta\rvert^2 = 1$（迹为 1 即各测量结果概率归一）。
- **物理状态与物理量**：经典——状态是确定值；量子——状态是叠加，物理量由算符（如 Pauli $\sigma_x,\sigma_y,\sigma_z$）刻画，测量得本征值且概率性塌缩。

## 心智模型
- **Bloch 矢量**：纯态参数化 $\ket{\psi} = \cos(\theta/2)\ket{0} + e^{i\phi}\sin(\theta/2)\ket{1}$，对应单位球面点 $r = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$。$\theta$ 为纬度角、$\phi$ 为经度角。可用 $r_i = \Tr(\rho \sigma_i)$ 计算 Bloch 分量。
- **态的制备 = 旋转**：任意 qubit 态 $\ket{\psi}$ 都能找到 $U\in U(2)$ 使 $\ket{\psi} = U\ket{0}$——几何上是绕躺在 $x$-$y$ 平面的某根轴旋转某角度。（思考：实现同一目标的转轴/转角不唯一。）

## 测量
- **计算基测量**：测 $\ket{\psi}=\alpha\ket{0}+\beta\ket{1}$，得 $\ket{0}$ 概率 $\lvert\alpha\rvert^2$，得 $\ket{1}$ 概率 $\lvert\beta\rvert^2$。
- **非计算基测量**：可测 $\sigma_x$ 等其它可观测量，等价于先旋转到该基再做计算基测量。

## 多比特与 Bell 基
- **多比特计算基**：$n$ 比特张成 $2^n$ 维空间，基矢 $\ket{00\dots0}\dots\ket{11\dots1}$。
- **Bell 基（最大纠缠）**：$\ket{\Phi^\pm}=(\ket{00}\pm\ket{11})/\sqrt{2}$，$\ket{\Psi^\pm}=(\ket{01}\pm\ket{10})/\sqrt{2}$。
- **Bell 关联**：在计算基下测量 Bell 态（如 $\ket{\Phi^+}$），两比特总是得到**相同**结果——纠缠的标志。

## 关键要点
1. qubit 的"信息"藏在概率幅里，测量只给出概率性的一比特结果。
2. 单 qubit 纯态 $\leftrightarrow$ Bloch 球面点；混合态 $\leftrightarrow$ 球内点（$\lVert r\rVert<1$）。
3. Bell 态体现纠缠：局部测量结果强关联，无法写成张量积。

## 关联
- **1.3**：单比特门 = Bloch 球上的旋转；Bell 态由 H+CNOT 制备。
- **1.6**：测量概率性是量子信息论的出发点。
