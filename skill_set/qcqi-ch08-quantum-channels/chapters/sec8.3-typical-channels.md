# 8.3 几种典型信道的 Kraus 算符与 Bloch 仿射变换

## 核心思想
单 qubit 信道既可用 Kraus 算符描述，也可用 **Bloch 向量仿射变换** $\vec r \mapsto M\vec r + \vec c$ 描述（$M$ 是 $3\times 3$ 矩阵、$\vec c$ 是平移向量）——后者直观展示信道如何压缩/平移 Bloch 球。

## 典型信道的 Kraus 算符
（$p$ 为出错概率，$\sigma$ 为 Pauli 矩阵）
- **比特翻转**：$E_0=\sqrt{1-p}\,I$，$E_1=\sqrt{p}\,X$。
- **相位翻转**：$E_0=\sqrt{1-p}\,I$，$E_1=\sqrt{p}\,Z$。
- **相位阻尼 (phase damping)**：与相位翻转效果一致（笔记原话："相位阻尼和相位反转一样"）——同样只衰减相干（off-diagonal）项，等价于一个退相位过程。
- **比特-相位翻转**：$E_0=\sqrt{1-p}\,I$，$E_1=\sqrt{p}\,Y$。
- **去极化 (depolarizing)**：$E_0=\sqrt{1-3p/4}\,I$，$E_1=\sqrt{p/4}\,X$，$E_2=\sqrt{p/4}\,Y$，$E_3=\sqrt{p/4}\,Z$（以概率 $p$ 把态替换为最大混合）。
- **振幅阻尼 (amplitude damping)**：$E_0=\begin{pmatrix}1&0\\0&\sqrt{1-\gamma}\end{pmatrix}$，$E_1=\begin{pmatrix}0&\sqrt{\gamma}\\0&0\end{pmatrix}$（描述能量耗散 $\ket{1}\to\ket{0}$）。

## Bloch 向量仿射变换矩阵 r → Mr + c
- **比特翻转**：$M=\mathrm{diag}(1,\, 1-2p,\, 1-2p)$，$\vec c=0$（沿 $y$、$z$ 收缩）。
- **相位翻转 / 相位阻尼**：$M=\mathrm{diag}(1-2p,\, 1-2p,\, 1)$，$\vec c=0$（沿 $x$、$y$ 收缩，$z$ 不变）。
- **去极化**：$M=\mathrm{diag}(1-p,\, 1-p,\, 1-p)$，$\vec c=0$（各向同性缩小，整球向球心收缩）。
- **振幅阻尼**：$M=\mathrm{diag}(\sqrt{1-\gamma},\, \sqrt{1-\gamma},\, 1-\gamma)$，$\vec c=(0,0,\gamma)$（球收缩并向北极 $\ket{0}$ 平移）——这是唯一带非零平移 $\vec c$ 的典型例子。

## 关键要点
1. 相位阻尼与相位翻转效果一致：都只衰减相干项。
2. Kraus 与 Bloch 仿射变换是同一信道的两种描述；仿射形 $\vec r\mapsto M\vec r+\vec c$。
3. 去极化各向同性收缩 $(\vec c=0)$；振幅阻尼收缩并平移 $(\vec c\ne 0)$，反映能量耗散的不可逆性。

## 关联
- **8.2**：这些 Kraus 算符可由各自蔡氏矩阵谱分解得到。
- **8.4**：算例中在不同基底下展开同一信道的 Kraus 算符。
