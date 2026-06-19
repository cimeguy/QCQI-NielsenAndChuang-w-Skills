# 6.3 Grover 算法的几何意义

## 核心思想
Grover 迭代在一个 2 维平面内是固定角度的旋转。把高维搜索压缩到这个平面，算法的行为一目了然。

## 2 维平面
- 定义两个正交态：
  - **$\ket{\beta}$**：所有解的均匀叠加（解空间，$M$ 个）。
  - **$\ket{\alpha}$**：所有非解的均匀叠加（非解空间，$N-M$ 个）。
- 初态 $\ket{\psi} = \sqrt{(N-M)/N}\ket{\alpha} + \sqrt{M/N}\ket{\beta}$ 落在 $\ket{\alpha}$-$\ket{\beta}$ 平面内。当 $M\ll N$ 时，初态与 $\ket{\alpha}$ 很接近（离解很远）。

## Householder 变换（反射）
- 关于态 $\ket{\psi}$ 的反射算符是一个 **Householder 变换** $u = 2\ketbra{\psi}{\psi}-I$（$u^H=\bra{\psi}$ 相关），把向量关于 $\ket{\psi}$ 轴做镜像反射。
- 预言机 $O$ 是关于 $\ket{\alpha}$ 的反射（把 $\ket{\beta}$ 分量取负）。

## 每次迭代 = 固定角度的 2 维旋转
- **$G = -HO$** = 两次反射（先关于 $\ket{\alpha}$，再关于 $\ket{\psi}$）的复合 = 一次**旋转**。
- 旋转角 $\theta$ 满足 $\sin(\theta/2)=\sqrt{M/N}$（初态与 $\ket{\alpha}$ 夹角 $\theta/2$）。
- 每作用一次 $G$，态在平面内朝 $\ket{\beta}$（解空间）转过固定角 $\theta$。
- **综合**：两次反射 ⇒ 一次旋转，是 Householder/反射几何的标准结论。

## 关键要点
1. 搜索发生在 $\ket{\alpha}$（非解）与 $\ket{\beta}$（解）张成的 2 维平面。
2. 反射 = Householder 变换；预言机与"对均值翻转"各是一次反射。
3. 两次反射复合 = 固定角 $\theta$ 旋转，$\sin(\theta/2)=\sqrt{M/N}$，朝解空间转。

## 关联
- **6.2**：$G=-HO$ 的代数形式在此获得几何解释。
- **6.4**：旋转角 $\theta$ 决定最优迭代次数 $\sim(\pi/4)\sqrt{N/M}$。
- **第四章 4.1**：单比特门=旋转的几何直觉在此推广到搜索平面。
