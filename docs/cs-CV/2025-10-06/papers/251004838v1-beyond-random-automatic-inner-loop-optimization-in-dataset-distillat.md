---
layout: default
title: Beyond Random: Automatic Inner-loop Optimization in Dataset Distillation
---

# Beyond Random: Automatic Inner-loop Optimization in Dataset Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04838" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04838v1</a>
  <a href="https://arxiv.org/pdf/2510.04838.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04838v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.04838v1', 'Beyond Random: Automatic Inner-loop Optimization in Dataset Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muquan Li, Hang Gou, Dongyang Zhang, Shuang Liang, Xiurui Xie, Deqiang Ouyang, Ke Qin

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-06

---

## 💡 一句话要点

**提出AT-BPTT，通过自动内循环优化提升数据集蒸馏性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `数据集蒸馏` `内循环优化` `反向传播` `梯度截断` `自适应学习`

## 📋 核心要点

1. 现有数据集蒸馏方法依赖随机截断策略，忽略了神经网络在不同训练阶段的学习动态差异，导致性能受限。
2. AT-BPTT 框架通过概率机制选择时间步，并根据梯度变化自适应调整窗口大小，实现动态截断反向传播。
3. 实验结果表明，AT-BPTT 在多个数据集上显著提升了模型准确率，并加速了内循环优化，降低了内存消耗。

## 📝 摘要（中文）

为了应对高效深度学习日益增长的需求，数据集蒸馏已成为一种关键技术，它能够在压缩训练数据集的同时保持模型性能。然而，现有的数据集蒸馏内循环优化方法通常依赖于随机截断策略，缺乏灵活性，并且常常产生次优结果。本文观察到神经网络在不同的训练阶段（早期、中期和晚期）表现出不同的学习动态，这使得随机截断变得无效。为了解决这个局限性，我们提出了一种新的框架——自动截断反向传播时间（AT-BPTT），它可以根据内在的梯度行为动态地调整截断位置和窗口大小。AT-BPTT 引入了三个关键组件：（1）一种用于阶段感知时间步选择的概率机制，（2）一种基于梯度变化的自适应窗口大小调整策略，以及（3）一种用于降低计算开销的低秩 Hessian 近似。在 CIFAR-10、CIFAR-100、Tiny-ImageNet 和 ImageNet-1K 上的大量实验表明，AT-BPTT 实现了最先进的性能，与基线方法相比，平均提高了 6.16% 的准确率。此外，我们的方法将内循环优化加速了 3.9 倍，同时节省了 63% 的内存成本。

## 🔬 方法详解

**问题定义**：数据集蒸馏旨在用远小于原始数据集的合成数据集训练模型，使其达到与在原始数据集上训练相似的性能。现有的内循环优化方法，如随机截断反向传播（BPTT），在处理不同训练阶段的学习动态时缺乏适应性，导致蒸馏出的数据集质量不高，模型性能受限。

**核心思路**：论文的核心思路是根据神经网络在训练过程中不同阶段的梯度行为，动态地调整 BPTT 的截断位置和窗口大小。通过自适应地选择更重要的时间步进行梯度更新，并调整窗口大小以适应梯度变化，从而更有效地进行数据集蒸馏。

**技术框架**：AT-BPTT 框架包含三个主要组件：1) **阶段感知时间步选择**：使用概率机制，根据当前训练阶段（早期、中期、晚期）的重要性，选择参与梯度更新的时间步。2) **自适应窗口大小调整**：根据梯度变化动态调整 BPTT 的窗口大小，确保重要梯度信息能够被有效传播。3) **低秩 Hessian 近似**：使用低秩 Hessian 近似来降低计算复杂度，提高优化效率。

**关键创新**：AT-BPTT 的关键创新在于其动态调整 BPTT 截断位置和窗口大小的能力。与传统的随机截断方法相比，AT-BPTT 能够更好地适应神经网络在不同训练阶段的学习动态，从而更有效地进行数据集蒸馏。此外，低秩 Hessian 近似的使用显著降低了计算开销。

**关键设计**：阶段感知时间步选择使用一个概率分布来表示每个时间步的重要性，该分布根据训练阶段进行调整。自适应窗口大小调整基于梯度变化的统计量，例如方差或均值，来动态调整窗口大小。低秩 Hessian 近似使用 Lanczos 算法来估计 Hessian 矩阵的特征值和特征向量，从而降低计算复杂度。

## 📊 实验亮点

AT-BPTT 在 CIFAR-10、CIFAR-100、Tiny-ImageNet 和 ImageNet-1K 数据集上取得了显著的性能提升，平均准确率比基线方法提高了 6.16%。此外，AT-BPTT 将内循环优化加速了 3.9 倍，同时节省了 63% 的内存成本，表明该方法在效率和性能方面都具有优势。

## 🎯 应用场景

该研究成果可应用于资源受限的场景，例如移动设备或嵌入式系统，通过数据集蒸馏减少存储和计算需求。此外，该方法可以加速模型训练，提高开发效率，并为大规模数据集的训练提供了一种可行的解决方案。未来，该技术有望应用于联邦学习、持续学习等领域。

## 📄 摘要（原文）

> The growing demand for efficient deep learning has positioned dataset distillation as a pivotal technique for compressing training dataset while preserving model performance. However, existing inner-loop optimization methods for dataset distillation typically rely on random truncation strategies, which lack flexibility and often yield suboptimal results. In this work, we observe that neural networks exhibit distinct learning dynamics across different training stages-early, middle, and late-making random truncation ineffective. To address this limitation, we propose Automatic Truncated Backpropagation Through Time (AT-BPTT), a novel framework that dynamically adapts both truncation positions and window sizes according to intrinsic gradient behavior. AT-BPTT introduces three key components: (1) a probabilistic mechanism for stage-aware timestep selection, (2) an adaptive window sizing strategy based on gradient variation, and (3) a low-rank Hessian approximation to reduce computational overhead. Extensive experiments on CIFAR-10, CIFAR-100, Tiny-ImageNet, and ImageNet-1K show that AT-BPTT achieves state-of-the-art performance, improving accuracy by an average of 6.16% over baseline methods. Moreover, our approach accelerates inner-loop optimization by 3.9x while saving 63% memory cost.

