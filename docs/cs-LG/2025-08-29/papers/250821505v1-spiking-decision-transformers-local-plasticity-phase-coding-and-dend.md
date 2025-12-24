---
layout: default
title: "Spiking Decision Transformers: Local Plasticity, Phase-Coding, and Dendritic Routing for Low-Power Sequence Control"
---

# Spiking Decision Transformers: Local Plasticity, Phase-Coding, and Dendritic Routing for Low-Power Sequence Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21505" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21505v1</a>
  <a href="https://arxiv.org/pdf/2508.21505.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21505v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21505v1', 'Spiking Decision Transformers: Local Plasticity, Phase-Coding, and Dendritic Routing for Low-Power Sequence Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vishal Pandey, Debasmita Biswas

**分类**: cs.LG

**发布日期**: 2025-08-29

**备注**: Preprint (31 pages, 19 images, 7 tables)

---

## 💡 一句话要点

**提出脉冲决策变换器以解决低功耗序列控制问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `脉冲神经网络` `低功耗计算` `序列决策` `强化学习` `生物启发机制` `嵌入式系统` `能效提升`

## 📋 核心要点

1. 现有基于变换器的强化学习方法依赖密集矩阵运算，难以在能量受限的边缘设备上应用。
2. 论文提出脉冲决策变换器（SNN-DT），通过嵌入脉冲神经元和生物启发的可塑性机制，实现低功耗序列控制。
3. 实验结果表明，SNN-DT在经典控制基准上表现优异，每次决策发射的脉冲少于十个，能量消耗显著降低。

## 📝 摘要（中文）

基于变换器架构的强化学习代理在序列决策任务中表现出色，但其对密集矩阵运算的依赖使其不适合能量受限的边缘平台。脉冲神经网络承诺实现超低功耗的事件驱动推理，但之前的工作未能将脉冲动态与回报条件序列建模无缝结合。本文提出脉冲决策变换器（SNN-DT），在每个自注意力模块中嵌入泄漏积分发火神经元，通过替代梯度进行端到端训练，并结合生物启发的三因素可塑性、相位偏移的脉冲位置编码和轻量级树突路由模块。我们的实现在线性控制基准（如CartPole-v1、MountainCar-v0等）上匹配或超过标准决策变换器的性能，同时每个决策发射的脉冲少于十个，表明每次推理能量减少了四个数量级。通过将序列建模与神经形态效率结合，SNN-DT为嵌入式和可穿戴设备上的实时低功耗控制开辟了新路径。

## 🔬 方法详解

**问题定义**：本文旨在解决现有基于变换器的强化学习方法在能量受限环境中的应用问题，尤其是其对密集矩阵运算的依赖导致的高能耗。

**核心思路**：提出脉冲决策变换器（SNN-DT），通过将脉冲神经元嵌入自注意力模块，结合生物启发的可塑性机制，实现低功耗的序列决策。

**技术框架**：SNN-DT的整体架构包括脉冲神经元、三因素可塑性模块、相位偏移的脉冲位置编码和树突路由模块，支持端到端训练。

**关键创新**：最重要的创新在于将脉冲动态与回报条件序列建模相结合，形成了一种新的低功耗序列控制方法，与传统方法相比，能效显著提升。

**关键设计**：在设计中，采用了替代梯度进行训练，设置了轻量级的树突路由模块，确保每次决策的脉冲发射量少于十个，从而实现了能量的极大减少。

## 📊 实验亮点

实验结果显示，SNN-DT在经典控制基准（如CartPole-v1、MountainCar-v0等）上表现优异，性能与标准决策变换器相当或更好，同时每次决策发射的脉冲少于十个，表明其能量消耗减少了四个数量级，具有显著的能效提升。

## 🎯 应用场景

该研究的潜在应用领域包括嵌入式系统、可穿戴设备和其他对能量效率要求高的实时控制场景。通过实现低功耗的序列决策，SNN-DT能够推动智能设备在实际应用中的普及与发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement learning agents based on Transformer architectures have achieved impressive performance on sequential decision-making tasks, but their reliance on dense matrix operations makes them ill-suited for energy-constrained, edge-oriented platforms. Spiking neural networks promise ultra-low-power, event-driven inference, yet no prior work has seamlessly merged spiking dynamics with return-conditioned sequence modeling. We present the Spiking Decision Transformer (SNN-DT), which embeds Leaky Integrate-and-Fire neurons into each self-attention block, trains end-to-end via surrogate gradients, and incorporates biologically inspired three-factor plasticity, phase-shifted spike-based positional encodings, and a lightweight dendritic routing module. Our implementation matches or exceeds standard Decision Transformer performance on classic control benchmarks (CartPole-v1, MountainCar-v0, Acrobot-v1, Pendulum-v1) while emitting fewer than ten spikes per decision, an energy proxy suggesting over four orders-of-magnitude reduction in per inference energy. By marrying sequence modeling with neuromorphic efficiency, SNN-DT opens a pathway toward real-time, low-power control on embedded and wearable devices.

