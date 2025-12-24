---
layout: default
title: Task-Oriented Multimodal Token Transmission in Resource-Constrained Multiuser Networks
---

# Task-Oriented Multimodal Token Transmission in Resource-Constrained Multiuser Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07841" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07841v3</a>
  <a href="https://arxiv.org/pdf/2505.07841.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07841v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07841v3', 'Task-Oriented Multimodal Token Transmission in Resource-Constrained Multiuser Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhe Zhang, Wanli Ni, Pengwei Wang, Dongyu Wang

**分类**: cs.NI, cs.LG

**发布日期**: 2025-05-06 (更新: 2025-11-03)

**DOI**: [10.1109/LWC.2025.3628928](https://doi.org/10.1109/LWC.2025.3628928)

---

## 💡 一句话要点

**提出任务导向的多模态令牌传输方案以解决资源受限网络中的效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态信息融合` `令牌传输` `任务导向` `滑动窗口池化` `优化算法` `资源受限网络` `变换器架构`

## 📋 核心要点

1. 现有的基于变换器的多模态模型在令牌传输中面临带宽开销大、功耗高和延迟增加等挑战。
2. 提出了一种任务导向的多模态令牌传输方案，结合两阶段训练算法和滑动窗口池化技术，以提高传输效率。
3. 仿真结果显示，该算法在不同带宽和功率预算下均优于基线方法，并在各种信噪比下实现了更高的准确率。

## 📝 摘要（中文）

随着基于大模型的智能体的出现，广泛采用的基于变换器的架构不可避免地产生过长的令牌嵌入，这可能导致高带宽开销、增加功耗和延迟。本文提出了一种任务导向的多模态令牌传输方案，以提高多模态信息的融合和利用效率。为提高令牌传输效率，设计了包括跨模态对齐和任务导向微调的两阶段训练算法。同时，采用滑动窗口池化操作进行令牌压缩，以节省通信资源。为平衡压缩带来的延迟与模型性能之间的权衡，构建了一个关于延迟和验证损失的加权和优化问题。通过交替优化方法联合优化用户的带宽、功率分配和令牌长度。仿真结果表明，所提算法在不同的带宽和功率预算下优于基线方法。

## 🔬 方法详解

**问题定义**：本文旨在解决在资源受限的多用户网络中，基于变换器的多模态模型在令牌传输时产生的高带宽开销和延迟等问题。现有方法在处理多模态信息时效率低下，无法满足实际应用需求。

**核心思路**：提出的方案通过任务导向的多模态令牌传输，结合两阶段训练算法，优化令牌的传输效率。通过跨模态对齐和任务导向微调，提升了信息融合的效果。

**技术框架**：整体架构分为两个主要阶段：第一阶段为跨模态对齐，第二阶段为任务导向微调。同时，采用滑动窗口池化操作进行令牌压缩，节省通信资源。

**关键创新**：最重要的创新在于提出了加权和优化问题，平衡延迟与模型性能之间的权衡，采用交替优化方法联合优化带宽、功率分配和令牌长度。与现有方法相比，具有更高的灵活性和效率。

**关键设计**：在设计中，采用了滑动窗口池化作为令牌压缩技术，并通过加权和损失函数来优化延迟和验证损失，确保模型在不同条件下的性能表现。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，所提算法在不同带宽和功率预算下的性能均优于基线方法，尤其在信噪比变化的情况下，准确率提升显著，证明了两阶段训练算法的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通、物联网和智能家居等多模态信息处理场景。通过提高令牌传输的效率，可以显著降低系统的功耗和延迟，提升用户体验，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> With the emergence of large model-based agents, widely adopted transformer-based architectures inevitably produce excessively long token embeddings for transmission, which may result in high bandwidth overhead, increased power consumption and latency. In this letter, we propose a task-oriented multimodal token transmission scheme for efficient multimodal information fusion and utilization. To improve the efficiency of token transmission, we design a two-stage training algotithm, including cross-modal alignment and task-oriented fine-tuning, for large model-based token communication. Meanwhile, token compression is performed using a sliding window pooling operation to save communication resources. To balance the trade-off between latency and model performance caused by compression, we formulate a weighted-sum optimization problem over latency and validation loss. We jointly optimizes bandwidth, power allocation, and token length across users by using an alternating optimization method. Simulation results demonstrate that the proposed algorithm outperforms the baseline under different bandwidth and power budgets. Moreover, the two-stage training algorithm achieves higher accuracy across various signal-to-noise ratios than the method without cross-modal alignment.

