---
layout: default
title: "FNODE: Flow-Matching for data-driven simulation of constrained multibody systems"
---

# FNODE: Flow-Matching for data-driven simulation of constrained multibody systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00183" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00183v2</a>
  <a href="https://arxiv.org/pdf/2509.00183.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00183v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00183v2', 'FNODE: Flow-Matching for data-driven simulation of constrained multibody systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyu Wang, Jingquan Wang, Dan Negrut

**分类**: cs.LG

**发布日期**: 2025-08-29 (更新: 2025-09-09)

**备注**: 36 pages, 19 figures

---

## 💡 一句话要点

**提出FNODE以解决多体系统数据驱动模拟中的高计算成本问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `数据驱动建模` `多体系统` `神经网络` `加速度向量场` `物理仿真`

## 📋 核心要点

1. 现有的约束多体系统数据驱动建模方法面临高计算成本和长期预测精度不足的问题。
2. FNODE框架通过直接学习加速度向量场，避免了传统神经ODE中的反向传播瓶颈。
3. FNODE在多种基准测试中均表现优于现有方法，展现出更高的准确性和计算效率。

## 📝 摘要（中文）

数据驱动的约束多体系统建模面临高计算成本和有限的长期预测精度等挑战。为了解决这些问题，本文提出了流匹配神经常微分方程（FNODE）框架，该框架直接从轨迹数据中学习加速度向量场。通过重新构造训练目标以监督加速度而非集成状态，FNODE消除了通过ODE求解器反向传播的需求，这在传统神经ODE中是一个瓶颈。加速度目标通过数值微分技术高效计算，包括混合快速傅里叶变换（FFT）和有限差分（FD）方案。实验结果表明，FNODE在多个基准测试中表现优异，超越了现有方法，如多体动态神经ODE（MBD-NODE）、长短期记忆网络（LSTM）和全连接神经网络（FCNN），展现了良好的准确性、泛化能力和计算效率。

## 🔬 方法详解

**问题定义**：本文旨在解决约束多体系统数据驱动建模中的高计算成本和长期预测精度不足的问题。现有方法通常依赖于复杂的ODE求解器，导致计算效率低下。

**核心思路**：FNODE通过直接学习加速度向量场来简化模型训练过程，重新定义训练目标为监督加速度而非集成状态，从而避免了传统方法中的反向传播瓶颈。

**技术框架**：FNODE的整体架构包括数据采集、加速度向量场学习和模型评估三个主要模块。首先，通过数值微分技术获取加速度目标，然后使用神经网络学习这些加速度向量场，最后在多个基准测试中评估模型性能。

**关键创新**：FNODE的主要创新在于其流匹配机制，直接从轨迹数据中学习加速度，而不是依赖于状态的积分。这一设计显著提高了计算效率和模型的长期预测能力。

**关键设计**：FNODE采用混合快速傅里叶变换（FFT）和有限差分（FD）方案来高效计算加速度目标，损失函数设计为监督加速度的误差，网络结构则为全连接神经网络，确保了模型的灵活性和适应性。

## 📊 实验亮点

FNODE在多个基准测试中表现优异，超越了多体动态神经ODE（MBD-NODE）、长短期记忆网络（LSTM）和全连接神经网络（FCNN）。在所有测试中，FNODE展现出更高的准确性和计算效率，证明了其在数据驱动建模中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、物理仿真和动态系统建模等。FNODE能够在高效模拟复杂多体系统的同时，降低计算成本，具有重要的实际价值和广泛的应用前景。未来，FNODE可能推动更多领域的智能化和自动化进程。

## 📄 摘要（原文）

> Data-driven modeling of constrained multibody systems faces two persistent challenges: high computational cost and limited long-term prediction accuracy. To address these issues, we introduce the Flow-Matching Neural Ordinary Differential Equation (FNODE), a framework that learns acceleration vector fields directly from trajectory data. By reformulating the training objective to supervise accelerations rather than integrated states, FNODE eliminates the need for backpropagation through an ODE solver, which represents a bottleneck in traditional Neural ODEs. Acceleration targets are computed efficiently using numerical differentiation techniques, including a hybrid Fast Fourier Transform (FFT) and Finite Difference (FD) scheme. We evaluate FNODE on a diverse set of benchmarks, including the single and triple mass-spring-damper systems, double pendulum, slider-crank, and cart-pole. Across all cases, FNODE consistently outperforms existing approaches such as Multi-Body Dynamic Neural ODE (MBD-NODE), Long Short-Term Memory (LSTM) networks, and Fully Connected Neural Networks (FCNN), demonstrating good accuracy, generalization, and computational efficiency.

