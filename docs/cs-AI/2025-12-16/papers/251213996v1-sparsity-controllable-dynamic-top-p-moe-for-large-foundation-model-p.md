---
layout: default
title: Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training
---

# Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13996" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13996v1</a>
  <a href="https://arxiv.org/pdf/2512.13996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13996v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.13996v1', 'Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Can Jin, Hongwu Peng, Mingcan Xiang, Qixin Zhang, Xiangchi Yuan, Amit Hasan, Ohiremen Dibua, Yifan Gong, Yan Kang, Dimitris N. Metaxas

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出DTop-p MoE，实现稀疏度可控的动态Top-p路由，提升大模型预训练效果。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `MoE` `Top-p路由` `动态稀疏性` `PI控制器` `大模型预训练` `自然语言处理` `扩散模型`

## 📋 核心要点

1. 现有Top-k MoE路由策略对所有token采用统一稀疏度，忽略了token难度的差异，限制了模型性能。
2. DTop-p MoE利用PI控制器动态调整Top-p阈值，实现稀疏度可控，并自适应地为不同token分配计算资源。
3. 实验表明，DTop-p在多种模型和数据集上优于Top-k和固定阈值Top-p，并展现出良好的扩展性。

## 📝 摘要（中文）

稀疏混合专家(MoE)架构通过仅激活每个输入token的专家子集来有效地扩展模型容量。然而，标准的Top-k路由策略施加了一种统一的稀疏模式，忽略了token难度的变化。虽然Top-p路由提供了一种灵活的替代方案，但现有的实现通常依赖于固定的全局概率阈值，这导致了不可控的计算成本和对超参数选择的敏感性。本文提出了DTop-p MoE，一种稀疏度可控的动态Top-p路由机制。为了解决优化不可微阈值的挑战，我们利用比例-积分(PI)控制器动态调整概率阈值，使运行激活的专家稀疏度与指定的target对齐。此外，我们引入了一种动态路由归一化机制，该机制自适应地调整层级的路由logits，允许不同的层学习不同的专家选择模式，同时使用全局概率阈值。在大型语言模型和扩散Transformer上的大量实验表明，DTop-p始终优于Top-k和固定阈值Top-p基线。我们的分析证实，DTop-p保持对激活专家数量的精确控制，同时自适应地在不同的token和层之间分配资源。此外，DTop-p在专家粒度、专家容量、模型大小和数据集大小方面表现出强大的缩放特性，为大规模MoE预训练提供了一个鲁棒的框架。

## 🔬 方法详解

**问题定义**：现有Top-k路由在MoE模型中强制执行统一的稀疏性，无法根据输入token的复杂程度动态调整激活的专家数量。固定阈值的Top-p路由虽然可以自适应地选择专家，但对超参数敏感，且难以控制计算成本，导致训练不稳定和性能下降。

**核心思路**：DTop-p MoE的核心在于使用一个比例-积分(PI)控制器来动态调整Top-p路由的概率阈值。通过将实际激活的专家数量与预设的目标稀疏度进行比较，PI控制器自动调整阈值，从而实现对计算成本的精确控制，并允许模型根据token的难度自适应地选择专家。

**技术框架**：DTop-p MoE的整体框架包括一个标准的MoE层，其中每个token通过路由网络选择一组专家。关键在于路由机制，它包含以下几个步骤：首先，计算每个token到各个专家的logits。然后，应用动态Top-p路由，其中概率阈值由PI控制器动态调整。最后，使用动态路由归一化来调整每层的logits分布，使得不同层可以学习不同的专家选择模式。

**关键创新**：DTop-p MoE的关键创新在于使用PI控制器来动态调整Top-p阈值，从而实现稀疏度可控。与固定阈值的Top-p路由相比，DTop-p可以自动适应不同的训练阶段和数据分布，避免了手动调整超参数的麻烦。此外，动态路由归一化允许不同层学习不同的专家选择模式，进一步提高了模型的灵活性和表达能力。

**关键设计**：PI控制器的设计是DTop-p的关键。控制器根据实际激活的专家数量与目标稀疏度之间的误差来调整阈值。比例项根据当前误差进行调整，积分项则累积历史误差，从而实现更稳定的控制。动态路由归一化通过对每层的logits进行缩放和平移来实现，其参数是可学习的，允许网络自动学习最佳的logits分布。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13996v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13996v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13996v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，DTop-p MoE在大型语言模型和扩散Transformer上均优于Top-k和固定阈值Top-p基线。例如，在语言模型预训练中，DTop-p在保持相同计算成本的情况下，能够显著提高模型的困惑度。此外，DTop-p在不同专家粒度、专家容量、模型大小和数据集大小方面均表现出良好的扩展性。

## 🎯 应用场景

DTop-p MoE适用于各种需要大规模模型和高效计算的场景，例如自然语言处理中的大型语言模型预训练、图像生成中的扩散模型训练等。它可以降低计算成本，提高训练效率，并提升模型性能，从而加速AI技术的应用和发展。

## 📄 摘要（原文）

> Sparse Mixture-of-Experts (MoE) architectures effectively scale model capacity by activating only a subset of experts for each input token. However, the standard Top-k routing strategy imposes a uniform sparsity pattern that ignores the varying difficulty of tokens. While Top-p routing offers a flexible alternative, existing implementations typically rely on a fixed global probability threshold, which results in uncontrolled computational costs and sensitivity to hyperparameter selection. In this paper, we propose DTop-p MoE, a sparsity-controllable dynamic Top-p routing mechanism. To resolve the challenge of optimizing a non-differentiable threshold, we utilize a Proportional-Integral (PI) Controller that dynamically adjusts the probability threshold to align the running activated-expert sparsity with a specified target. Furthermore, we introduce a dynamic routing normalization mechanism that adapts layer-wise routing logits, allowing different layers to learn distinct expert-selection patterns while utilizing a global probability threshold. Extensive experiments on Large Language Models and Diffusion Transformers demonstrate that DTop-p consistently outperforms both Top-k and fixed-threshold Top-p baselines. Our analysis confirms that DTop-p maintains precise control over the number of activated experts while adaptively allocating resources across different tokens and layers. Furthermore, DTop-p exhibits strong scaling properties with respect to expert granularity, expert capacity, model size, and dataset size, offering a robust framework for large-scale MoE pre-training.

