# 速查表 · QCQI 第六章

## 算法流程
1. **初始化**：$H^{\otimes n}\ket{0}$ = 均匀叠加 $\ket{\psi}$；（辅助比特 $\ket{-}$）。
2. **重复 $G$** 约 $(\pi/4)\sqrt{N/M}$ 次。
3. **测量** index register → 高概率得解。

## Grover 迭代 G = −H·O
| 部件 | 作用 | 几何 |
|---|---|---|
| O（预言机） | $O\ket{x}=(-1)^{f(x)}\ket{x}$ | 关于 $\ket{\alpha}$ 反射 |
| H（$2\ketbra{\psi}{\psi}-I$） | 对均值翻转 | 关于 $\ket{\psi}$ 反射 |
| $G=-HO$ | 一次迭代 | 转角 $\theta$ 的旋转 |

## 关键数字
- **旋转角**：$\sin(\theta/2)=\sqrt{M/N}$，$M\ll N$ 时 $\theta\approx 2\sqrt{M/N}$。
- **最优迭代次数**：$R \approx (\pi/4)\sqrt{N/M}$；$M=1$ → $(\pi/4)\sqrt{N}$。
- **复杂度**：$O(\sqrt{N})$ 查询（经典 $O(N)$）——平方加速。
- $N=64,M=1$ → $R\approx 6$。

## 预言机两型
| 类型 | 形式 | 备注 |
|---|---|---|
| 布尔 | $U_f\ket{x}\ket{q}=\ket{x}\ket{q\oplus f(x)}$ | 用辅助比特记 $f$ |
| 相位翻转 | $O\ket{x}=(-1)^{f(x)}\ket{x}$ | 辅助 $\ket{-}$+回踢从布尔得到 |

## 几何要点
- 平面：$\ket{\alpha}$（非解）、$\ket{\beta}$（解）。
- 初态 $\ket{\psi}=\sqrt{(N-M)/N}\ket{\alpha}+\sqrt{M/N}\ket{\beta}$。
- 反射 = Householder；两次反射 = 一次旋转。

## 注意事项
- 成功概率随迭代次数**振荡**，必须卡准次数（过冲会下降）。
- 多解 $M>1$：得到随机一个解；$M$ 未知先做量子计数或指数猜测。
- 布尔（辅助 $\ket{0}$/$\ket{1}$）与相位翻转实现成功概率相同。

## 启发式来源
$H=\ketbra{\psi}{\psi}+\ketbra{x}{x}$ → Trotter，$t=\pi$ → 两反射复合 = $G=-HO$。
