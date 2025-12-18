---
layout: default
title: Distillation-Guided Structural Transfer for Continual Learning Beyond Sparse Distributed Memory
---

# Distillation-Guided Structural Transfer for Continual Learning Beyond Sparse Distributed Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15267" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15267v1</a>
  <a href="https://arxiv.org/pdf/2512.15267.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15267v1" onclick="toggleFavorite(this, '2512.15267v1', 'Distillation-Guided Structural Transfer for Continual Learning Beyond Sparse Distributed Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huiyan Xue, Xuming Ran, Yaxin Li, Qi Xu, Enhui Li, Yi Xu, Qiang Zhang

**分类**: cs.LG

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出选择性子网络蒸馏(SSD)框架，提升稀疏神经网络的持续学习能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `持续学习` `稀疏神经网络` `知识蒸馏` `子网络` `结构学习`

## 📋 核心要点

1. 现有稀疏神经网络持续学习方法，如SDMLP，存在跨任务知识重用不足和高稀疏性下性能下降的问题。
2. 论文提出选择性子网络蒸馏(SSD)框架，通过结构引导的蒸馏，在稀疏网络中实现知识传递和结构重对齐。
3. 实验表明，SSD在Split CIFAR-10、CIFAR-100和MNIST数据集上，显著提高了准确性、保留率和表示覆盖率。

## 📝 摘要（中文）

稀疏神经网络因其模块化和低干扰性，在高效持续学习中越来越受欢迎。诸如稀疏分布式存储多层感知器(SDMLP)等架构通过Top-K激活构建特定于任务的子网络，并表现出对灾难性遗忘的抵抗力。然而，它们僵化的模块化限制了跨任务知识的重用，并导致在高稀疏性下性能下降。我们提出了选择性子网络蒸馏(SSD)，这是一个结构引导的持续学习框架，它将蒸馏视为拓扑对齐的信息通道，而不是正则化器。SSD识别具有高激活频率的神经元，并选择性地在先前的Top-K子网络和输出logits中提取知识，而无需重放或任务标签。这实现了结构重新对齐，同时保留了稀疏模块化。在Split CIFAR-10、CIFAR-100和MNIST上的实验表明，SSD提高了准确性、保留率和表示覆盖率，为稀疏持续学习提供了一个结构化的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决稀疏神经网络在持续学习中，由于其固有的模块化结构导致的知识重用不足和高稀疏性下的性能下降问题。现有的基于稀疏连接的持续学习方法，例如SDMLP，虽然能有效避免灾难性遗忘，但缺乏跨任务的知识迁移能力，限制了模型的整体性能。

**核心思路**：论文的核心思路是将蒸馏学习视为一种拓扑对齐的信息传递机制，而非简单的正则化手段。通过选择性地蒸馏高激活频率的神经元，实现知识在不同任务子网络间的迁移，从而在保留稀疏模块化结构的同时，促进知识的重用和整合。

**技术框架**：SSD框架主要包含以下几个阶段：1) 使用Top-K激活构建特定任务的子网络；2) 识别具有高激活频率的神经元；3) 选择性地蒸馏先前Top-K子网络和输出logits中的知识。该框架无需重放或任务标签，即可实现结构重新对齐。

**关键创新**：SSD的关键创新在于其结构引导的蒸馏方法。它不是简单地将整个网络的知识进行蒸馏，而是有选择性地针对高激活频率的神经元进行知识迁移，从而更有效地利用了稀疏网络的结构信息，实现了知识的有效重用。与现有方法相比，SSD更注重利用网络自身的拓扑结构来指导知识的传递。

**关键设计**：SSD的关键设计包括：1) 使用Top-K激活来维持网络的稀疏性；2) 通过激活频率来衡量神经元的重要性，并选择性地蒸馏高激活频率的神经元；3) 使用蒸馏损失函数来促使学生网络学习教师网络的知识，包括子网络内部的知识和输出logits。具体的损失函数形式和蒸馏温度等参数需要根据具体任务进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15267v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15267v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15267v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SSD在Split CIFAR-10、CIFAR-100和MNIST数据集上均取得了显著的性能提升。例如，在Split CIFAR-100数据集上，SSD相比于基线方法，在准确率、保留率和表示覆盖率方面均有明显提高，验证了其在稀疏持续学习中的有效性。

## 🎯 应用场景

该研究成果可应用于资源受限设备上的持续学习任务，例如移动机器人、边缘计算设备等。通过提升稀疏神经网络的持续学习能力，可以使这些设备在不断学习新任务的同时，保持较低的计算和存储开销，从而更好地适应动态变化的环境。

## 📄 摘要（原文）

> Sparse neural systems are gaining traction for efficient continual learning due to their modularity and low interference. Architectures such as Sparse Distributed Memory Multi-Layer Perceptrons (SDMLP) construct task-specific subnetworks via Top-K activation and have shown resilience against catastrophic forgetting. However, their rigid modularity limits cross-task knowledge reuse and leads to performance degradation under high sparsity. We propose Selective Subnetwork Distillation (SSD), a structurally guided continual learning framework that treats distillation not as a regularizer but as a topology-aligned information conduit. SSD identifies neurons with high activation frequency and selectively distills knowledge within previous Top-K subnetworks and output logits, without requiring replay or task labels. This enables structural realignment while preserving sparse modularity. Experiments on Split CIFAR-10, CIFAR-100, and MNIST demonstrate that SSD improves accuracy, retention, and representation coverage, offering a structurally grounded solution for sparse continual learning.

