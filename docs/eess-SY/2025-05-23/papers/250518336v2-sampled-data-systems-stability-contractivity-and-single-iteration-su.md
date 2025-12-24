---
layout: default
title: "Sampled-data Systems: Stability, Contractivity and Single-iteration Suboptimal MPC"
---

# Sampled-data Systems: Stability, Contractivity and Single-iteration Suboptimal MPC

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.18336" class="toolbar-btn" target="_blank">📄 arXiv: 2505.18336v2</a>
  <a href="https://arxiv.org/pdf/2505.18336.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.18336v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.18336v2', 'Sampled-data Systems: Stability, Contractivity and Single-iteration Suboptimal MPC')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiting Chen, Francesco Bullo, Emiliano Dall'Anese

**分类**: eess.SY, math.OC

**发布日期**: 2025-05-23 (更新: 2025-08-29)

**备注**: Modifications relative to version 1: Figure updated

---

## 💡 一句话要点

**提出采样数据系统的稳定性分析以优化模型预测控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `采样数据系统` `稳定性分析` `收缩性` `实时控制` `优化算法` `小增益理论`

## 📋 核心要点

1. 现有的模型预测控制（MPC）方法在实时控制中面临稳定性和收敛性的问题，尤其是在采样数据系统中。
2. 本文提出了一种新的理论框架，通过引入简化模型，分析CT和DT系统的稳定性，特别是在单次迭代情况下的收敛性。
3. 研究结果表明，在特定条件下，CT-DT系统的互连可以实现指数稳定性，为实时控制应用提供了新的收敛保证。

## 📝 摘要（中文）

本文分析了通过采样和零阶保持机制耦合的连续时间（CT）和离散时间（DT）系统的稳定性。DT系统以固定时间间隔$T>0$更新其输出，通过对给定映射的$n$次复合来实现。该设置源于基于优化的控制器的在线和采样数据实现，尤其是模型预测控制（MPC），其中DT系统模拟近似优化问题解的算法的$n$次迭代。我们引入了一个简化模型的概念，定义为采样数据系统在$T 	o 0^+$和$n 	o +	ext{∞}$时的极限行为。我们的主要理论贡献是，当简化模型是收缩的时，对于每个迭代次数$n$，存在一个阈值持续时间$T(n)$，使得CT-DT互连在所有采样周期$T < T(n)$下实现指数稳定性。最后，在CT和DT系统均为收缩的更强条件下，我们使用小增益论证了它们互连的指数稳定性。我们的理论结果为次优MPC的稳定性提供了新见解，表明即使使用优化算法的单次迭代，收敛保证仍然成立，这对实时控制应用具有重要意义。

## 🔬 方法详解

**问题定义**：本文旨在解决在采样数据系统中，模型预测控制（MPC）方法的稳定性和收敛性问题。现有方法在处理连续时间与离散时间系统的耦合时，往往难以保证稳定性，尤其是在实时控制场景中。

**核心思路**：论文的核心思路是引入简化模型，分析采样数据系统在极限情况下的行为，并建立其收缩性与稳定性之间的关系。通过这种方式，可以在单次迭代的情况下，确保系统的收敛性和稳定性。

**技术框架**：整体架构包括对CT和DT系统的建模，分析其在采样周期$T$和迭代次数$n$变化下的稳定性。主要模块包括简化模型的定义、收缩性条件的建立以及小增益理论的应用。

**关键创新**：最重要的技术创新在于提出了简化模型的概念，并证明了在该模型收缩的情况下，CT-DT系统的互连可以实现指数稳定性。这一发现与现有方法的本质区别在于，允许在单次迭代下仍能保证系统的收敛性。

**关键设计**：关键设计包括对采样周期$T$和迭代次数$n$的阈值$T(n)$的定义，以及在收缩条件下的稳定性分析。这些设计为实时控制应用提供了理论支持。

## 📊 实验亮点

实验结果表明，在特定条件下，CT-DT系统的互连能够实现指数稳定性，且即使在单次迭代的情况下，收敛保证依然成立。这一发现为实时控制应用提供了新的理论依据，具有显著的实用价值。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、工业自动化和智能制造等实时控制系统。通过优化模型预测控制的稳定性，能够提升系统在动态环境下的响应能力和安全性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> This paper analyzes the stability of interconnected continuous-time (CT) and discrete-time (DT) systems coupled through sampling and zero-order hold mechanisms. The DT system updates its output at regular intervals $T>0$ by applying an $n$-fold composition of a given map. This setup is motivated by online and sampled-data implementations of optimization-based controllers - particularly model predictive control (MPC) - where the DT system models $n$ iterations of an algorithm approximating the solution of an optimization problem.
>   We introduce the concept of a reduced model, defined as the limiting behavior of the sampled-data system as $T \to 0^+$ and $n \to +\infty$. Our main theoretical contribution establishes that when the reduced model is contractive, there exists a threshold duration $T(n)$ for each iteration count $n$ such that the CT-DT interconnection achieves exponential stability for all sampling periods $T < T(n)$. Finally, under the stronger condition that both the CT and DT systems are contractive, we show exponential stability of their interconnection using a small-gain argument. Our theoretical results provide new insights into suboptimal MPC stability, showing that convergence guarantees hold even when using a single iteration of the optimization algorithm - a practically significant finding for real-time control applications.

