---
layout: default
title: Split-Layer: Enhancing Implicit Neural Representation by Maximizing the Dimensionality of Feature Space
---

# Split-Layer: Enhancing Implicit Neural Representation by Maximizing the Dimensionality of Feature Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10142" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10142v1</a>
  <a href="https://arxiv.org/pdf/2511.10142.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10142v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.10142v1', 'Split-Layer: Enhancing Implicit Neural Representation by Maximizing the Dimensionality of Feature Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhicheng Cai, Hao Zhu, Linsen Chen, Qiu Shen, Xun Cao

**分类**: cs.CV

**发布日期**: 2025-11-13

**备注**: AAAI 2026

---

## 💡 一句话要点

**提出Split-Layer以提升隐式神经表示的特征空间维度，增强表征能力**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `隐式神经表示` `多层感知机` `特征空间扩展` `Hadamard积` `高阶多项式` `图像重建` `新视角合成`

## 📋 核心要点

1. 传统MLP结构的INR受限于低维特征空间，限制了其表征能力，加宽MLP虽能提升维度，但计算成本随之二次增长。
2. 论文提出split-layer，将MLP层拆分为多个并行分支，通过Hadamard积整合输出，构建高阶多项式空间，扩展特征空间维度。
3. 实验结果表明，split-layer显著提升了INR在图像拟合、CT重建、形状表示和新视角合成等任务中的性能，优于现有方法。

## 📝 摘要（中文）

隐式神经表示(INR)使用神经网络将信号建模为连续函数，为跨学科的反问题提供高效且可微的优化。然而，INR的表征能力受到传统多层感知机(MLP)架构中低维特征空间的限制。虽然加宽MLP可以线性增加特征空间维度，但也会导致计算和内存成本的二次增长。为了解决这个限制，我们提出split-layer，一种MLP构建的新颖重构。split-layer将每一层分成多个并行分支，并通过Hadamard积整合它们的输出，有效地构建高阶多项式空间。这种方法通过扩展特征空间维度，显著增强了INR的表征能力，而不会产生过高的计算开销。大量实验表明，split-layer显著提高了INR的性能，在包括2D图像拟合、2D CT重建、3D形状表示和5D新视角合成等多个任务中超越了现有方法。

## 🔬 方法详解

**问题定义**：论文旨在解决隐式神经表示(INR)中，由于传统多层感知机(MLP)的低维特征空间导致的表征能力不足问题。现有方法如简单地加宽MLP虽然可以增加特征维度，但会带来计算和内存成本的显著增加，使其难以应用于复杂场景。

**核心思路**：论文的核心思路是通过一种新的MLP层结构——split-layer，在不显著增加计算成本的前提下，有效地扩展特征空间的维度。split-layer通过将每一层拆分为多个并行分支，并利用Hadamard积整合这些分支的输出，从而构建一个高阶多项式空间。

**技术框架**：split-layer可以被嵌入到任何基于MLP的INR架构中。整体流程是：输入信号首先经过一系列split-layer，每个split-layer将输入特征分成多个分支，每个分支进行线性变换和激活函数处理，然后所有分支的输出通过Hadamard积进行融合，得到该层的输出。最终的输出用于预测目标信号。

**关键创新**：split-layer的关键创新在于其通过并行分支和Hadamard积的组合，实现了特征空间的非线性扩展。与直接加宽MLP相比，split-layer能够在计算成本增加较小的情况下，获得更高的特征维度和更强的表征能力。本质区别在于，split-layer构建的是一个高阶多项式空间，而传统MLP主要依赖于线性变换和非线性激活函数的组合。

**关键设计**：split-layer的关键设计包括分支的数量、每个分支的神经元数量以及Hadamard积的使用。分支数量决定了特征空间扩展的程度，每个分支的神经元数量影响了模型的容量。Hadamard积的选择是因为它能够有效地将不同分支的信息进行非线性组合，从而构建高阶多项式空间。损失函数通常采用均方误差(MSE)等回归损失函数，用于衡量预测信号与真实信号之间的差异。

## 📊 实验亮点

实验结果表明，split-layer在多个任务上显著优于现有方法。例如，在2D图像拟合任务中，split-layer能够更快地收敛并达到更低的误差。在3D形状表示任务中，split-layer能够更准确地重建复杂的几何形状，并减少细节信息的丢失。在5D新视角合成任务中，split-layer能够生成更清晰、更逼真的新视角图像，PSNR指标平均提升超过1dB。

## 🎯 应用场景

该研究成果可广泛应用于计算机视觉、图形学和医学图像处理等领域。例如，在医学CT重建中，可以利用split-layer增强INR对复杂解剖结构的表征能力，提高重建图像的质量。在三维建模和新视角合成中，split-layer可以提升模型对复杂几何形状和光照效果的建模能力，从而生成更逼真的三维模型和图像。未来，该技术有望推动相关领域的发展，实现更高效、更精确的信号表示和重建。

## 📄 摘要（原文）

> Implicit neural representation (INR) models signals as continuous functions using neural networks, offering efficient and differentiable optimization for inverse problems across diverse disciplines. However, the representational capacity of INR defined by the range of functions the neural network can characterize, is inherently limited by the low-dimensional feature space in conventional multilayer perceptron (MLP) architectures. While widening the MLP can linearly increase feature space dimensionality, it also leads to a quadratic growth in computational and memory costs. To address this limitation, we propose the split-layer, a novel reformulation of MLP construction. The split-layer divides each layer into multiple parallel branches and integrates their outputs via Hadamard product, effectively constructing a high-degree polynomial space. This approach significantly enhances INR's representational capacity by expanding the feature space dimensionality without incurring prohibitive computational overhead. Extensive experiments demonstrate that the split-layer substantially improves INR performance, surpassing existing methods across multiple tasks, including 2D image fitting, 2D CT reconstruction, 3D shape representation, and 5D novel view synthesis.

