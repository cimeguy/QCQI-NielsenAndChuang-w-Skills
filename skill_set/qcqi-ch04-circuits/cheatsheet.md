# 速查表 · QCQI 第四章

## 单比特门速查
| 门 | 矩阵 | 作用 |
|---|---|---|
| $R_x(\theta)$ | $\cos(\theta/2)I-i\sin(\theta/2)X$ | 绕 x 轴转 $\theta$ |
| $R_y(\theta)$ | $\cos(\theta/2)I-i\sin(\theta/2)Y$ | 绕 y 轴转 $\theta$；可生成所有单比特门 |
| $R_z(\theta)$ | $\mathrm{diag}(e^{-i\theta/2},e^{i\theta/2})$ | 绕 z 轴转 $\theta$ |
| H | $\tfrac{1}{\sqrt{2}}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$ | 等权叠加，交换 $X\leftrightarrow Z$ |
| S | $\mathrm{diag}(1,i)$ | $\pi/2$ 相位 |
| T | $\mathrm{diag}(1,e^{i\pi/4})$ | $\pi/4$ 相位 ($\pi/8$ 门) |

## 多比特门速查
| 门 | 作用 | 备注 |
|---|---|---|
| CNOT | 控制=1 翻转目标 | 纠缠生成器 |
| CZ | 控制=1 施 Z | 对称；= 目标侧 $H\cdot\mathrm{CNOT}\cdot H$ |
| SWAP | 交换两比特 | $= 3\times\mathrm{CNOT}$ |
| Toffoli | 双控制翻转 | 经典可逆通用门 |

## 通用性三步（决策）
1. 任意 $U(2^n)$ $\to$ **二级幺正门**之积。
2. 二级门 $\to$ **单比特门 + CNOT**。
3. 单比特门 $\to$ **$\{H, T\}$** 稠密逼近 $\Rightarrow$ 通用集 **$\{H, T, \mathrm{CNOT}\}$**。
- 逼近精度 $\varepsilon$：门数 $O(\log^c(1/\varepsilon))$（Solovay-Kitaev）。

## 测量原理速记
- **延迟测量**：中途测+经典控制 $\Leftrightarrow$ 量子受控门+末端测。
- **隐含测量**：末端未读比特 = 已测。
- **$U^2=I$ 的测量**：辅助比特 H–受控U–H–测，取 $\pm 1$ 投影。

## 量子模拟决策
| 想要 | 怎么做 |
|---|---|
| 模拟 $e^{-iHt}$, $H=\sum A_i$ | 切片 + Trotter |
| 误差 $O(\Delta t^2)$ | 1 阶 $\prod e^{-iA_i\Delta t}$ |
| 误差 $O(\Delta t^3)$ | 2 阶对称 Suzuki-Trotter |
| 估计误差 | 迹距离 / $\lVert U-\mathrm{Trotter}\rVert$ vs 门数 |
| 误差根源 | BCH：$[A,B]\ne 0$ |

## 量子计算机三环节
**初始化 $\to$ 幺正变换 $\to$ 测量**（DiVincenzo 五要素的核心）。

## 其他模型一览
绝热 · 拓扑(任意子) · 量子游走 · one-clean-qubit · MBQC/簇态 · 量子图灵机。
