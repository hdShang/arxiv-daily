---
layout: default
title: "Dynamic Sensitivity Filter Pruning using Multi-Agent Reinforcement Learning For DCNN's"
---

# Dynamic Sensitivity Filter Pruning using Multi-Agent Reinforcement Learning For DCNN's

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05446" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05446v1</a>
  <a href="https://arxiv.org/pdf/2509.05446.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05446v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05446v1', 'Dynamic Sensitivity Filter Pruning using Multi-Agent Reinforcement Learning For DCNN\'s')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Iftekhar Haider Chowdhury, Zaed Ikbal Syed, Ahmed Faizul Haque Dhrubo, Mohammad Abdul Qayum

**分类**: cs.CV

**发布日期**: 2025-09-05

**备注**: This paper includes figures and two tables, and our work outperforms the existing research that has been published in a journal

---

## 💡 一句话要点

**提出差分敏感度融合剪枝算法，用于高效压缩深度卷积神经网络**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模型剪枝` `深度卷积神经网络` `模型压缩` `滤波器选择` `敏感度分析`

## 📋 核心要点

1. 深度卷积网络计算和内存开销大，限制了其在资源受限设备上的部署。
2. 提出差分敏感度融合剪枝，通过融合多种敏感度指标来评估滤波器的重要性，并进行单次剪枝。
3. 实验表明，该方法在显著降低模型复杂度的同时，保持了较高的准确率，优于传统方法。

## 📝 摘要（中文）

深度卷积神经网络在各种计算机视觉任务中取得了最先进的性能，但其计算和内存开销限制了实际部署。本文提出了一种新颖的单次滤波器剪枝框架——差分敏感度融合剪枝（Differential Sensitivity Fusion Pruning）。该框架侧重于评估滤波器重要性评分在多个标准下的稳定性和冗余性。差分敏感度融合剪枝通过融合基于梯度的敏感度、一阶泰勒展开和激活分布的KL散度之间的差异，为每个滤波器计算差分敏感度评分。采用指数缩放机制来强调在不同指标下重要性不一致的滤波器，从而识别结构不稳定或对模型性能不太关键的候选滤波器。与迭代或基于强化学习的剪枝策略不同，差分敏感度融合剪枝是高效且确定性的，只需要一次前向-后向传递即可进行评分和剪枝。在50%到70%的不同剪枝率下进行的大量实验表明，差分敏感度融合剪枝显著降低了模型复杂度，实现了超过80%的每秒浮点运算次数（FLOPS）的减少，同时保持了较高的准确率。例如，在70%的剪枝率下，该方法保留了高达98.23%的基线准确率，在压缩和泛化方面均优于传统启发式方法。该方法为可扩展和自适应的深度卷积神经网络压缩提供了一种有效的解决方案，为在边缘和移动平台上高效部署铺平了道路。

## 🔬 方法详解

**问题定义**：论文旨在解决深度卷积神经网络（DCNN）模型过大，计算和内存开销高的问题，这限制了它们在边缘设备和移动平台上的部署。现有剪枝方法，如迭代剪枝或基于强化学习的剪枝，通常计算成本高昂，或者需要多次迭代才能达到理想的压缩效果。传统启发式方法在压缩率较高时，容易导致模型性能显著下降。

**核心思路**：论文的核心思路是通过融合多种滤波器敏感度指标，综合评估每个滤波器的重要性，并进行单次剪枝。通过关注滤波器在不同指标下的稳定性，识别出冗余或不重要的滤波器。这种方法旨在实现高效且准确的模型压缩，避免了迭代剪枝的计算开销和性能损失。

**技术框架**：该框架主要包含以下几个步骤：1) 计算基于梯度的敏感度、一阶泰勒展开和激活分布的KL散度等多种滤波器敏感度指标。2) 计算这些指标之间的差异，得到每个滤波器的差分敏感度评分。3) 应用指数缩放机制，放大不稳定的滤波器的评分。4) 根据评分进行单次剪枝，移除评分较低的滤波器。

**关键创新**：该方法最重要的创新点在于提出了差分敏感度融合的概念，通过融合多种敏感度指标的差异来评估滤波器的重要性。与传统的单一指标方法相比，该方法能够更全面地评估滤波器的贡献，从而更准确地识别冗余滤波器。此外，单次剪枝的设计避免了迭代剪枝的计算开销。

**关键设计**：论文的关键设计包括：1) 选择了基于梯度的敏感度、一阶泰勒展开和激活分布的KL散度作为敏感度指标。2) 使用指数缩放机制来强调不稳定的滤波器，具体缩放因子未知。3) 剪枝率的选择，论文在50%到70%的不同剪枝率下进行了实验，具体如何选择最佳剪枝率未知。

## 📊 实验亮点

实验结果表明，该方法在50%到70%的剪枝率下，能够显著降低模型复杂度，实现超过80%的FLOPS减少，同时保持较高的准确率。例如，在70%的剪枝率下，该方法保留了高达98.23%的基线准确率，优于传统的启发式剪枝方法。这些结果表明，该方法在模型压缩和泛化能力方面具有优势。

## 🎯 应用场景

该研究成果可应用于各种需要高效部署深度学习模型的场景，例如移动设备上的图像识别、自动驾驶中的目标检测、以及物联网设备上的智能监控等。通过降低模型的计算和内存开销，该方法能够使深度学习模型在资源受限的平台上运行，从而拓展了深度学习的应用范围。

## 📄 摘要（原文）

> Deep Convolutional Neural Networks have achieved state of the art performance across various computer vision tasks, however their practical deployment is limited by computational and memory overhead. This paper introduces Differential Sensitivity Fusion Pruning, a novel single shot filter pruning framework that focuses on evaluating the stability and redundancy of filter importance scores across multiple criteria. Differential Sensitivity Fusion Pruning computes a differential sensitivity score for each filter by fusing the discrepancies among gradient based sensitivity, first order Taylor expansion, and KL divergence of activation distributions. An exponential scaling mechanism is applied to emphasize filters with inconsistent importance across metrics, identifying candidates that are structurally unstable or less critical to the model performance. Unlike iterative or reinforcement learning based pruning strategies, Differential Sensitivity Fusion Pruning is efficient and deterministic, requiring only a single forward-backward pass for scoring and pruning. Extensive experiments across varying pruning rates between 50 to 70 percent demonstrate that Differential Sensitivity Fusion Pruning significantly reduces model complexity, achieving over 80 percent Floating point Operations Per Seconds reduction while maintaining high accuracy. For instance, at 70 percent pruning, our approach retains up to 98.23 percent of baseline accuracy, surpassing traditional heuristics in both compression and generalization. The proposed method presents an effective solution for scalable and adaptive Deep Convolutional Neural Networks compression, paving the way for efficient deployment on edge and mobile platforms.

