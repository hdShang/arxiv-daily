---
layout: default
title: LADY: Linear Attention for Autonomous Driving Efficiency without Transformers
---

# LADY: Linear Attention for Autonomous Driving Efficiency without Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15038" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15038v1</a>
  <a href="https://arxiv.org/pdf/2512.15038.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15038v1" onclick="toggleFavorite(this, '2512.15038v1', 'LADY: Linear Attention for Autonomous Driving Efficiency without Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jihao Huang, Xi Xia, Zhiyuan Li, Tianle Liu, Jingke Wang, Junbo Chen, Tengju Ye

**分类**: cs.AI

**发布日期**: 2025-12-17

**备注**: Under review

---

## 💡 一句话要点

**提出LADY：一种基于线性注意力的高效自动驾驶模型，无需Transformer。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `自动驾驶` `线性注意力` `端到端学习` `跨模态融合` `边缘计算`

## 📋 核心要点

1. Transformer在自动驾驶中的应用受限于其二次方级别的计算复杂度，难以处理长时序数据，尤其是在边缘设备上。
2. LADY通过完全线性注意力机制，实现了对长程时序上下文的有效建模，同时保持了恒定的计算和内存成本。
3. 实验表明，LADY在自动驾驶基准测试中取得了最先进的性能，并在边缘设备上成功部署，验证了其有效性。

## 📝 摘要（中文）

端到端范式在自动驾驶领域展现出巨大潜力。然而，现有方法大多基于Transformer架构，其二次方级别的注意力计算成本限制了对长时空序列的建模能力，尤其是在资源受限的边缘平台上。由于自动驾驶本质上需要高效的时序建模，这一挑战严重限制了其部署和实时性能。近年来，线性注意力机制因其优越的时空复杂度而备受关注。然而，现有的线性注意力架构仅限于自注意力，缺乏对跨模态和跨时序交互的支持，而这对于自动驾驶至关重要。本文提出了LADY，这是第一个完全基于线性注意力的生成式端到端自动驾驶模型。LADY能够在推理时融合长程时序上下文，且计算和内存成本恒定，不受相机和激光雷达特征历史长度的影响。此外，我们引入了一种轻量级的线性交叉注意力机制，能够实现有效的跨模态信息交换。在NAVSIM和Bench2Drive基准测试上的实验表明，LADY以恒定的时间和内存复杂度实现了最先进的性能，提供了改进的规划性能并显著降低了计算成本。该模型已在边缘设备上部署和验证，证明了其在资源受限场景中的实用性。

## 🔬 方法详解

**问题定义**：现有基于Transformer的自动驾驶模型计算复杂度高，难以处理长时序数据，限制了其在资源受限的边缘设备上的部署和实时性能。现有线性注意力方法缺乏对跨模态（如相机和激光雷达）和跨时序信息的有效融合。

**核心思路**：LADY的核心思路是利用线性注意力机制替代Transformer中的传统注意力机制，从而将计算复杂度从二次方降低到线性级别。通过设计新的线性交叉注意力机制，实现跨模态信息的有效融合，从而提升自动驾驶系统的感知和决策能力。

**技术框架**：LADY是一个端到端的生成式模型，其整体架构包括特征提取模块、线性注意力模块和控制预测模块。特征提取模块负责从相机和激光雷达数据中提取特征。线性注意力模块负责融合长程时序上下文和跨模态信息。控制预测模块根据融合后的特征预测车辆的控制指令。

**关键创新**：LADY的关键创新在于提出了第一个完全基于线性注意力的端到端自动驾驶模型，并设计了一种轻量级的线性交叉注意力机制。这种线性交叉注意力机制能够有效地融合来自不同模态（如相机和激光雷达）的信息，同时保持较低的计算复杂度。与现有方法相比，LADY能够在处理长时序数据时保持恒定的计算和内存成本。

**关键设计**：LADY使用了线性化的注意力计算方法，例如使用核函数将query和key的乘积转化为特征的线性组合。线性交叉注意力模块的设计考虑了不同模态特征的差异性，采用了独立的线性变换来处理不同模态的特征。损失函数包括控制指令预测的损失和轨迹预测的损失，用于优化模型的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15038v1/figures/cover_photo.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15038v1/figures/new_whole.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15038v1/figures/rwkv.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

LADY在NAVSIM和Bench2Drive基准测试中取得了最先进的性能，证明了其在自动驾驶任务中的有效性。与基于Transformer的模型相比，LADY在保持甚至提升规划性能的同时，显著降低了计算成本，实现了恒定的时间和内存复杂度。此外，LADY已成功部署在边缘设备上，验证了其在实际应用中的可行性。

## 🎯 应用场景

LADY适用于各种自动驾驶应用场景，尤其是在资源受限的边缘计算平台上。它可以应用于低功耗自动驾驶车辆、机器人以及其他需要实时感知和决策的嵌入式系统。LADY的低计算成本和高效率使其能够部署在算力有限的设备上，从而推动自动驾驶技术的普及和应用。

## 📄 摘要（原文）

> End-to-end paradigms have demonstrated great potential for autonomous driving. Additionally, most existing methods are built upon Transformer architectures. However, transformers incur a quadratic attention cost, limiting their ability to model long spatial and temporal sequences-particularly on resource-constrained edge platforms. As autonomous driving inherently demands efficient temporal modeling, this challenge severely limits their deployment and real-time performance. Recently, linear attention mechanisms have gained increasing attention due to their superior spatiotemporal complexity. However, existing linear attention architectures are limited to self-attention, lacking support for cross-modal and cross-temporal interactions-both crucial for autonomous driving. In this work, we propose LADY, the first fully linear attention-based generative model for end-to-end autonomous driving. LADY enables fusion of long-range temporal context at inference with constant computational and memory costs, regardless of the history length of camera and LiDAR features. Additionally, we introduce a lightweight linear cross-attention mechanism that enables effective cross-modal information exchange. Experiments on the NAVSIM and Bench2Drive benchmarks demonstrate that LADY achieves state-of-the-art performance with constant-time and memory complexity, offering improved planning performance and significantly reduced computational cost. Additionally, the model has been deployed and validated on edge devices, demonstrating its practicality in resource-limited scenarios.

