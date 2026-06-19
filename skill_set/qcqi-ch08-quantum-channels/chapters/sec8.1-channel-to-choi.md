# 8.1 从信道到蔡氏矩阵（以比特翻转为例）

## 核心思想
量子信道 $\mathcal{E}$ 是描述开放系统演化的 CPTP 映射。把它作用在最大纠缠态的一半上，得到的矩阵就是**蔡氏矩阵 (Choi matrix)**——它把"映射"编码成一个普通矩阵，便于分析。

## 量子信道 (CPTP 映射)
- **完全正定 (CP)**：$\mathcal{E}\otimes I$ 对任意扩展系统都保持正定（保证物理性）。
- **保迹 (TP)**：$\Tr(\mathcal{E}(\rho))=\Tr(\rho)$（概率守恒）。

## 蔡氏矩阵 / Choi-Jamiołkowski 同构
- **定义**：$J(\mathcal{E}) = (\mathcal{E}\otimes I)(\ketbra{\Omega}{\Omega})$，其中 $\ket{\Omega}=\sum_i\ket{ii}$ 是（未归一）最大纠缠态。
- **意义**：信道 $\mathcal{E}\leftrightarrow$ 矩阵 $J(\mathcal{E})$ 一一对应（同构）。$\mathcal{E}$ 是 CP $\iff J(\mathcal{E})\ge 0$（半正定）；$\mathcal{E}$ 保迹 $\iff J$ 的部分迹 $= I$。
- **作用**：把"对所有输入 $\rho$ 的映射"压缩成一个有限维矩阵，可直接做谱分解。

## Worked Example：比特翻转信道
- 比特翻转信道：$\mathcal{E}(\rho)=(1-p)\rho + p X\rho X$（以概率 $p$ 施加 Pauli-X）。
- 把它作用在最大纠缠态一半上，按定义算出对应的蔡氏矩阵 $J$，作为后续（§8.2）谱分解 $\to$ Kraus 的输入。

## 关键要点
1. 量子信道 = CPTP 映射；CP 保证物理、TP 保证概率守恒。
2. 蔡氏矩阵 $J(\mathcal{E})=(\mathcal{E}\otimes I)\ketbra{\Omega}{\Omega}$ 把信道编码成一个矩阵。
3. CP $\iff J\ge 0$；这使"映射的正定性"变成"矩阵的半正定性"，便于检验与分解。

## 关联
- **8.2**：对 J 做谱分解即得 Kraus 算符。
- **8.3**：比特翻转是典型信道之一。
