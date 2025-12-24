---
layout: default
title: Spiking Neural Networks with Temporal Attention-Guided Adaptive Fusion for imbalanced Multi-modal Learning
---

# Spiking Neural Networks with Temporal Attention-Guided Adaptive Fusion for imbalanced Multi-modal Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14535" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14535v1</a>
  <a href="https://arxiv.org/pdf/2505.14535.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14535v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14535v1', 'Spiking Neural Networks with Temporal Attention-Guided Adaptive Fusion for imbalanced Multi-modal Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiangrong Shen, Yulin Xie, Qi Xu, Gang Pan, Huajin Tang, Badong Chen

**分类**: cs.LG, cs.HC

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出时序注意力引导的自适应融合以解决多模态学习不平衡问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `脉冲神经网络` `时序注意力` `自适应融合` `模态不平衡` `能效处理` `神经形态计算`

## 📋 核心要点

1. 现有多模态脉冲神经网络在模态不平衡和时间错位方面存在显著挑战，导致收敛速度不一致和融合机制静态化。
2. 提出的时序注意力引导的自适应融合框架通过动态分配重要性分数和调节学习率来解决模态不平衡问题。
3. 在CREMA-D、AVE和EAD数据集上，所提方法实现了显著的性能提升，准确率分别为77.55%、70.65%和97.5%。

## 📝 摘要（中文）

多模态脉冲神经网络（SNNs）在能效感知处理方面具有重要潜力，但面临模态不平衡和时间错位等关键挑战。现有方法在模态间收敛速度不协调和静态融合机制方面存在不足，无法有效处理时间变化的跨模态交互。本文提出了一种时序注意力引导的自适应融合框架，包含两个协同创新：1）时序注意力引导的自适应融合（TAAF）模块，动态分配每个时间步的融合脉冲特征的重要性分数；2）时序自适应平衡融合损失，根据注意力分数调节每个模态的学习率，防止主导模态垄断优化。该框架在时间维度上实现自适应融合，缓解多模态学习中的模态不平衡，模拟皮层多感官整合原理。实验结果表明，在CREMA-D、AVE和EAD数据集上，分别达到了77.55%、70.65%和97.5%的准确率，且具备能效优势。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态脉冲神经网络在模态不平衡和时间错位方面的挑战。现有方法在模态间收敛速度不一致，且静态融合机制无法有效应对时间变化的跨模态交互。

**核心思路**：提出的时序注意力引导的自适应融合框架通过动态分配每个时间步的融合特征重要性分数，结合时序自适应平衡融合损失，调节不同模态的学习率，从而实现模态间的协调优化。

**技术框架**：该框架主要包括两个模块：时序注意力引导的自适应融合（TAAF）模块和时序自适应平衡融合损失。TAAF模块负责动态分配重要性分数，而平衡融合损失则根据这些分数调整学习率。

**关键创新**：最重要的创新在于引入了时序注意力机制，使得融合过程能够根据时间变化动态调整，显著改善了模态不平衡问题。这与现有方法的静态融合机制形成了鲜明对比。

**关键设计**：在设计上，TAAF模块采用了层次化的特征集成方式，损失函数则根据模态的重要性分数进行调节，确保了各模态的学习率能够适应其实际贡献。

## 📊 实验亮点

实验结果显示，所提框架在CREMA-D、AVE和EAD数据集上分别达到了77.55%、70.65%和97.5%的准确率，显著优于基线脉冲神经网络，并且在能效方面表现出色，展示了其在多模态学习中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能感知系统、机器人视觉、医疗影像分析等，能够有效提升多模态数据处理的效率与准确性。未来，该框架有望在神经形态计算和生物启发的智能系统中发挥重要作用，推动机器智能向更高效的方向发展。

## 📄 摘要（原文）

> Multimodal spiking neural networks (SNNs) hold significant potential for energy-efficient sensory processing but face critical challenges in modality imbalance and temporal misalignment. Current approaches suffer from uncoordinated convergence speeds across modalities and static fusion mechanisms that ignore time-varying cross-modal interactions. We propose the temporal attention-guided adaptive fusion framework for multimodal SNNs with two synergistic innovations: 1) The Temporal Attention-guided Adaptive Fusion (TAAF) module that dynamically assigns importance scores to fused spiking features at each timestep, enabling hierarchical integration of temporally heterogeneous spike-based features; 2) The temporal adaptive balanced fusion loss that modulates learning rates per modality based on the above attention scores, preventing dominant modalities from monopolizing optimization. The proposed framework implements adaptive fusion, especially in the temporal dimension, and alleviates the modality imbalance during multimodal learning, mimicking cortical multisensory integration principles. Evaluations on CREMA-D, AVE, and EAD datasets demonstrate state-of-the-art performance (77.55\%, 70.65\% and 97.5\%accuracy, respectively) with energy efficiency. The system resolves temporal misalignment through learnable time-warping operations and faster modality convergence coordination than baseline SNNs. This work establishes a new paradigm for temporally coherent multimodal learning in neuromorphic systems, bridging the gap between biological sensory processing and efficient machine intelligence.

