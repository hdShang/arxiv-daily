---
layout: default
title: Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training
---

# Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13996" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13996</a>
  <a href="https://arxiv.org/pdf/2512.13996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13996" onclick="toggleFavorite(this, '2512.13996', 'Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Can Jin, Hongwu Peng, Mingcan Xiang, Qixin Zhang, Xiangchi Yuan, Amit Hasan, Ohiremen Dibua, Yifan Gong, Yan Kang, Dimitris N. Metaxas

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出DTop-p MoE，实现稀疏度可控的动态Top-p路由，提升大模型预训练效果。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `MoE` `稀疏路由` `Top-p路由` `动态阈值` `PI控制器` `大模型预训练` `计算效率`

## 📋 核心要点

1. 传统Top-k路由在MoE中强制统一稀疏性，忽略了不同token的难度差异，而固定阈值的Top-p路由难以控制计算成本。
2. DTop-p MoE利用PI控制器动态调整Top-p阈值，使激活专家数量与目标稀疏度对齐，实现稀疏度可控。
3. 实验表明，DTop-p在LLM和Diffusion Transformer上优于Top-k和固定阈值Top-p，并展现出良好的扩展性。

## 📝 摘要（中文）

稀疏混合专家(MoE)架构通过仅激活每个输入token的专家子集来有效地扩展模型容量。然而，标准的Top-k路由策略施加了一种统一的稀疏模式，忽略了token难度的变化。虽然Top-p路由提供了一种灵活的替代方案，但现有的实现通常依赖于固定的全局概率阈值，这导致了不可控的计算成本和对超参数选择的敏感性。本文提出了DTop-p MoE，一种稀疏度可控的动态Top-p路由机制。为了解决优化不可微阈值的挑战，我们利用比例-积分(PI)控制器动态调整概率阈值，使运行激活的专家稀疏度与指定的target对齐。此外，我们引入了一种动态路由归一化机制，该机制调整层级的路由logits，允许不同的层学习不同的专家选择模式，同时使用全局概率阈值。在大型语言模型和扩散Transformer上的大量实验表明，DTop-p始终优于Top-k和固定阈值Top-p基线。我们的分析证实，DTop-p保持对激活专家数量的精确控制，同时自适应地在不同的token和层之间分配资源。此外，DTop-p在专家粒度、专家容量、模型大小和数据集大小方面表现出强大的缩放特性，为大规模MoE预训练提供了一个鲁棒的框架。

## 🔬 方法详解

**问题定义**：现有MoE模型中的Top-k路由策略对所有token采用相同的稀疏度，无法根据token的难易程度自适应地分配计算资源。而Top-p路由虽然可以自适应地选择专家，但依赖于固定的全局概率阈值，难以控制计算成本，且对超参数敏感。这限制了MoE模型在大规模预训练中的应用。

**核心思路**：DTop-p MoE的核心思路是引入一个动态调整的Top-p阈值，该阈值由一个比例-积分(PI)控制器控制。PI控制器根据当前激活的专家数量与目标稀疏度之间的差异，动态地调整概率阈值，从而实现对激活专家数量的精确控制。同时，引入动态路由归一化机制，允许不同层学习不同的专家选择模式。

**技术框架**：DTop-p MoE的整体框架与标准的MoE模型类似，主要区别在于路由机制。对于每个输入token，首先计算路由logits。然后，通过动态Top-p路由选择激活的专家。PI控制器根据激活的专家数量与目标稀疏度之间的差异，动态调整Top-p阈值。最后，将token分配给选定的专家进行处理。

**关键创新**：DTop-p MoE的关键创新在于：1) 提出了一种稀疏度可控的动态Top-p路由机制，解决了传统Top-p路由难以控制计算成本的问题。2) 利用PI控制器动态调整Top-p阈值，实现了对激活专家数量的精确控制。3) 引入动态路由归一化机制，允许不同层学习不同的专家选择模式。

**关键设计**：PI控制器的参数（比例增益和积分增益）需要根据具体任务进行调整。动态路由归一化机制通过学习每个层的缩放因子来实现。损失函数包括标准的预训练损失和用于控制稀疏度的辅助损失。目标稀疏度是一个重要的超参数，需要根据计算资源和模型性能进行权衡。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13996/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13996/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13996/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，DTop-p MoE在大型语言模型和扩散Transformer上均优于Top-k和固定阈值Top-p基线。例如，在语言模型预训练中，DTop-p在保持相同计算成本的情况下，能够获得更高的perplexity。此外，DTop-p在不同专家粒度、专家容量、模型大小和数据集大小下均表现出良好的扩展性。

## 🎯 应用场景

DTop-p MoE可应用于大规模语言模型、视觉模型等各种深度学习模型的预训练，尤其适用于计算资源有限的场景。通过精确控制稀疏度，可以在保证模型性能的同时，降低计算成本，加速模型训练。该方法有望推动更大规模、更高效的AI模型的发展。

## 📄 摘要（原文）

> Sparse Mixture-of-Experts (MoE) architectures effectively scale model capacity by activating only a subset of experts for each input token. However, the standard Top-k routing strategy imposes a uniform sparsity pattern that ignores the varying difficulty of tokens. While Top-p routing offers a flexible alternative, existing implementations typically rely on a fixed global probability threshold, which results in uncontrolled computational costs and sensitivity to hyperparameter selection. In this paper, we propose DTop-p MoE, a sparsity-controllable dynamic Top-p routing mechanism. To resolve the challenge of optimizing a non-differentiable threshold, we utilize a Proportional-Integral (PI) Controller that dynamically adjusts the probability threshold to align the running activated-expert sparsity with a specified target. Furthermore, we introduce a dynamic routing normalization mechanism that adapts layer-wise routing logits, allowing different layers to learn distinct expert-selection patterns while utilizing a global probability threshold. Extensive experiments on Large Language Models and Diffusion Transformers demonstrate that DTop-p consistently outperforms both Top-k and fixed-threshold Top-p baselines. Our analysis confirms that DTop-p maintains precise control over the number of activated experts while adaptively allocating resources across different tokens and layers. Furthermore, DTop-p exhibits strong scaling properties with respect to expert granularity, expert capacity, model size, and dataset size, offering a robust framework for large-scale MoE pre-training.

