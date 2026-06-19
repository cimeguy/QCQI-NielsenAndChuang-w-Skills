# 速查表 · QCQI 第八章补充（量子信道）

## 三种等价描述
| 描述 | 形式 | 合法性条件 |
|---|---|---|
| 信道映射 $\mathcal{E}$ | $\rho \to \mathcal{E}(\rho)$ | CPTP |
| Kraus | $\mathcal{E}(\rho)=\sum_k E_k\rho E_k^\dagger$ | $\sum_k E_k^\dagger E_k=I$ |
| 蔡氏矩阵 $J$ | $(\mathcal{E}\otimes I)\ketbra{\Omega}{\Omega}$ | $J\ge 0$ 且部分迹$=I$ |

## 转换路线
```
信道 ℰ ──(ℰ⊗I)|Ω⟩⟨Ω|──► 蔡氏矩阵 J ──谱分解──► Kraus {E_k}
ℰ ──M_ij=½Tr(σ_iℰ(σ_j))──► Bloch 仿射 r→Mr+c  (单 qubit)
```

## 典型单 qubit 信道：Kraus
| 信道 | Kraus |
|---|---|
| 比特翻转 | $\sqrt{1-p}\,I,\ \sqrt{p}\,X$ |
| 相位翻转 | $\sqrt{1-p}\,I,\ \sqrt{p}\,Z$ |
| 相位阻尼 | 同相位翻转（退相干） |
| 比特-相位翻转 | $\sqrt{1-p}\,I,\ \sqrt{p}\,Y$ |
| 去极化 | $\sqrt{1-3p/4}\,I,\ \sqrt{p/4}\,\{X,Y,Z\}$ |
| 振幅阻尼 | $\left[\begin{smallmatrix}1&0\\0&\sqrt{1-\gamma}\end{smallmatrix}\right],\ \left[\begin{smallmatrix}0&\sqrt{\gamma}\\0&0\end{smallmatrix}\right]$ |

## 典型信道：Bloch 仿射 $\vec r\to M\vec r+\vec c$
| 信道 | $M=\mathrm{diag}(\cdot)$ | $\vec c$ |
|---|---|---|
| 比特翻转 | $(1,\ 1-2p,\ 1-2p)$ | $0$ |
| 相位翻转/阻尼 | $(1-2p,\ 1-2p,\ 1)$ | $0$ |
| 去极化 | $(1-p,\ 1-p,\ 1-p)$ | $0$ |
| 振幅阻尼 | $(\sqrt{1-\gamma},\ \sqrt{1-\gamma},\ 1-\gamma)$ | $(0,0,\gamma)$ |

## 关键判据
- **CP** $\iff$ 蔡氏矩阵 $J\ge 0$。
- **TP** $\iff \sum_k E_k^\dagger E_k=I$（$\iff J$ 部分迹$=I$）。
- **Kraus 秩** $=J$ 的非零本征值个数。
- **Kraus 非唯一**：差一个幺正混合 $F_j=\sum_k u_{jk}E_k$。

## 记忆点
- 相位阻尼 $\equiv$ 相位翻转（都只衰减相干项）。
- 去极化各向同性收缩；振幅阻尼收缩 + 向 $\ket{0}$ 平移（唯一 $\vec c\ne 0$）。
- Perturbative QEC：公式 (18) $\equiv$ (20)，数值验证通过。
