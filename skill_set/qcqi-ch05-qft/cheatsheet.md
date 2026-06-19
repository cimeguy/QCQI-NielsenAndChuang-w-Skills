# 速查表 · QCQI 第五章

## QFT 核心公式
- **QFT**：$\ket{j} \to \tfrac{1}{\sqrt{N}} \sum_k e^{2\pi i jk/N} \ket{k}$，$N=2^n$。
- **因式分解**：$\ket{j} \to \bigotimes_{l=1}^n (\ket{0} + e^{2\pi i\cdot 0.j_l\dots j_n}\ket{1})/\sqrt{2}$。
- **线路**：每比特 $H$ + 受控相位门 $R_k$ + 末端 SWAP；门数 **$O(n^2)$**。
- **二进制小数**：$0.a_1 a_2\dots = \sum a_l 2^{-l}$。

## 算法流程速记
| 算法 | 输入 | 量子核心 | 读出 |
|---|---|---|---|
| Deutsch(-Jozsa) | $\ket{-}$ 辅助 | $U_f$ 相位回踢 + $H$ | 常数/平衡 |
| 相位估计 | $U$ 本征态 $\ket{u}$ | 受控-$U^{2^k}$ + 逆 QFT | 相位 $\varphi$ |
| Shor 求阶 | $\ket{1}(=\sum\ket{u_s})$ | 受控模乘 + 逆 QFT | $s/r$ → 连分数 → $r$ |

## 相位估计精度
- $\varphi$ 是完美 $t$ 位二进制小数 → 估计**精确**。
- 否则 → 高概率给最佳 $t$ 位近似；$t\uparrow \Rightarrow$ 精度↑、成功率↑。

## Shor 决策流程
1. $N$ 偶？→ 直接除 2。
2. $N=a^b$？→ 取根。
3. 取随机 $y$，$\gcd(y,N)>1$？→ 直接得因子。
4. 量子求阶得 $r$。
5. $r$ 奇 或 $y^{r/2}\equiv -1\pmod N$？→ 换 $y$ 重试。
6. 否则 $\gcd(y^{r/2}\pm 1, N)$ = 非平凡因子。

## 复杂度对比
| 任务 | 经典 | 量子 |
|---|---|---|
| 傅里叶变换 | FFT $O(N\log N)$ | QFT $O(\log^2 N)$ |
| 大数分解 | 数域筛 超多项式 | Shor 多项式 |
| Deutsch-Jozsa | 最坏 $2^{n-1}+1$ | 1 次 |

## HSP 速记
- 框架：$f:G\to X$ 隐藏子群 $H$，求 $H$ 生成元。
- 特例：Deutsch-Jozsa($\mathbb{Z}_2^n$)、Simon、求阶/Shor($\mathbb{Z}$)、离散对数。
- **阿贝尔**：高效解决；**非阿贝尔**：开放。

## 核心提醒
- Fourier 结果藏在概率幅，**不可直接读**。
- 求阶输入 $\ket{1}$ = 所有本征态均匀叠加（免制备）。
- 端到端成本含经典后处理（连分数、GCD）。
