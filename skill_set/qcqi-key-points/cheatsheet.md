# 速记总表 · QCQI 各章关键点

## 一页纸概览
| 章 | 一句话 | 三个关键词 |
|---|---|---|
| 2 线代+量力 | 四公理 + 数学工具 | $\rho$=迹1正定、PVM/POVM、纠缠/Bell |
| 4 线路+模拟 | 门→通用→模拟 | z-y-z、$\{H,T,\mathrm{CNOT}\}$、Trotter/BCH |
| 5 QFT 家族 | 并行→QFT→Shor | 因式分解、相位估计、求阶/HSP |

## 第 2 章速记
- 投影=命题；$\rho$=迹1正定；$\langle A\rangle=\Tr(\rho A)$。
- 可观测量 ↔ PVM ↔ Hermite；POVM 推广。
- 演化幺正、定态乘相位；复合=张量积。
- $\mathrm{SVD}=UDV^\dagger$；Schmidt=SVD 物理版；Bell 违反 → 否定局域实在论。

## 第 4 章速记
- 单比特门=旋转，z-y-z 三次；$R_y$ 生成所有。
- CNOT/CZ/SWAP=3CNOT/Toffoli；CU 用 ABC+2CNOT。
- 延迟/隐含测量；通用集 $\{H,T,\mathrm{CNOT}\}$，门数 $O(\log^c(1/\varepsilon))$。
- 三环节：初始化/幺正/测量；Trotter 误差 ← $[A,B]\ne 0$（BCH）。

## 第 5 章速记
- Deutsch-Jozsa：一次 $U_f$ 判常数/平衡。
- QFT：$\ket{j}\to\tfrac{1}{\sqrt{N}}\sum e^{2\pi i jk/N}\ket{k}$，$O(n^2)$门，结果在幅里。
- 相位估计：受控-$U^{2^k}$+逆 QFT 读 $\varphi$（需本征态）。
- Shor：分解→求阶→相位估计；$\ket{1}=\sum\ket{u_s}$；连分数+GCD。
- HSP：阿贝尔已解，非阿贝尔开放。

## 复杂度对照
| 任务 | 经典 | 量子 |
|---|---|---|
| 傅里叶 | $O(N\log N)$ | $O(\log^2 N)$ |
| 分解 | 超多项式 | 多项式 (Shor) |
| 无结构搜索 | $O(N)$ | $O(\sqrt{N})$ (Grover, 第6章) |
| Deutsch-Jozsa | 最坏 $2^{n-1}+1$ | 1 次 |

## 三条贯穿全书的红线
1. **不可克隆** → 禁扇出。
2. **幺正可逆** → 禁扇入/环路。
3. **测量即塌缩** → 信息藏在幅里，干涉后再测。
