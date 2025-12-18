---
layout: default
title: LinVideo: A Post-Training Framework towards O(n) Attention in Efficient Video Generation
---

# LinVideo: A Post-Training Framework towards O(n) Attention in Efficient Video Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08318" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08318v2</a>
  <a href="https://arxiv.org/pdf/2510.08318.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08318v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.08318v2', 'LinVideo: A Post-Training Framework towards O(n) Attention in Efficient Video Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yushi Huang, Xingtong Ge, Ruihao Gong, Chengtao Lv, Jun Zhang

**分类**: cs.CV

**发布日期**: 2025-10-09 (更新: 2025-11-21)

**备注**: Code will be released upon acceptance

---

## 💡 一句话要点

**LinVideo：一种后训练框架，实现高效视频生成中O(n)复杂度Attention**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `视频生成` `扩散模型` `线性注意力` `后训练` `模型加速` `选择性迁移` `分布匹配`

## 📋 核心要点

1. 视频扩散模型计算成本随序列长度呈二次方增长，主要瓶颈在于自注意力机制的二次复杂度。
2. LinVideo提出一种后训练框架，通过选择性地将部分自注意力层替换为线性注意力层，降低计算复杂度。
3. 实验表明，LinVideo在保持生成质量的同时，实现了显著的加速，并且可以通过蒸馏进一步降低延迟。

## 📝 摘要（中文）

视频扩散模型(DMs)实现了高质量的视频合成。然而，由于自注意力机制的二次复杂度，其计算成本随序列长度呈二次方增长。虽然线性注意力降低了成本，但由于线性注意力有限的表达能力以及视频生成中时空建模的复杂性，完全替换二次注意力需要昂贵的预训练。本文提出LinVideo，一种高效的无数据后训练框架，用线性注意力替换目标数量的自注意力模块，同时保持原始模型的性能。首先，我们观察到不同层的可替换性存在显著差异。我们没有采用手动或启发式选择，而是将层选择定义为二元分类问题，并提出了选择性迁移，自动且渐进地将层转换为线性注意力，同时对性能的影响最小。此外，为了克服现有目标函数在此迁移过程中的无效性和低效性，我们引入了一种随时分布匹配(ADM)目标，该目标对齐了沿采样轨迹任何时间步长的样本分布。该目标是高效的，并且可以恢复模型性能。大量实验表明，我们的方法在保持生成质量的同时，实现了1.25-2.00倍的加速，而我们的4步蒸馏模型进一步实现了15.92倍的延迟降低，且视觉质量下降最小。

## 🔬 方法详解

**问题定义**：视频扩散模型在生成长视频时，自注意力机制的计算复杂度呈二次方增长，导致计算成本过高。直接用线性注意力替换所有自注意力层会严重影响模型性能，需要昂贵的预训练才能弥补性能损失。因此，如何在不进行额外预训练的情况下，高效地降低视频扩散模型的计算复杂度是一个关键问题。

**核心思路**：LinVideo的核心思路是并非所有自注意力层都同等重要，部分层可以用线性注意力替换而对性能影响很小。通过选择性地迁移部分层到线性注意力，可以在降低计算复杂度的同时，最大程度地保留原始模型的性能。此外，设计有效的训练目标来弥补替换注意力机制带来的性能损失。

**技术框架**：LinVideo是一个后训练框架，主要包含两个阶段：1) **选择性迁移**：将层选择问题建模为二元分类问题，自动选择可以替换为线性注意力的层。2) **随时分布匹配 (ADM)**：使用ADM目标函数来对齐原始模型和替换后的模型在采样过程中的分布，从而恢复模型性能。整体流程是在预训练好的视频扩散模型上，先进行选择性迁移，然后使用ADM目标函数进行微调。

**关键创新**：LinVideo的关键创新在于：1) **选择性迁移策略**：通过二元分类的方式自动选择可替换的层，避免了手动或启发式选择的局限性。2) **随时分布匹配 (ADM) 目标函数**：ADM目标函数能够有效地对齐采样轨迹上任意时间步长的样本分布，从而恢复模型性能，并且计算效率高。

**关键设计**：1) **选择性迁移的二元分类器**：使用一个轻量级的分类器来预测每个自注意力层是否可以被线性注意力层替换。分类器的输入是该层的激活值，输出是二元标签（可替换/不可替换）。2) **ADM目标函数**：ADM目标函数的目标是最小化原始模型和替换后的模型在采样轨迹上任意时间步长上的样本分布差异。具体实现上，可以使用KL散度或JS散度来衡量分布差异。

## 📊 实验亮点

LinVideo在多个视频生成数据集上进行了实验，结果表明，LinVideo可以在保持生成质量的同时，实现1.25-2.00倍的加速。通过4步蒸馏，LinVideo进一步实现了15.92倍的延迟降低，且视觉质量下降最小。这些结果表明，LinVideo是一种高效且有效的视频生成加速方法。

## 🎯 应用场景

LinVideo可以应用于各种需要高效视频生成的场景，例如实时视频编辑、低延迟视频流媒体、移动设备上的视频生成等。通过降低计算复杂度，LinVideo使得在资源受限的设备上进行高质量视频生成成为可能，并加速了视频生成技术的普及。

## 📄 摘要（原文）

> Video diffusion models (DMs) have enabled high-quality video synthesis. However, their computation costs scale quadratically with sequence length because self-attention has quadratic complexity. While linear attention lowers the cost, fully replacing quadratic attention requires expensive pretraining due to the limited expressiveness of linear attention and the complexity of spatiotemporal modeling in video generation. In this paper, we present LinVideo, an efficient data-free post-training framework that replaces a target number of self-attention modules with linear attention while preserving the original model's performance. First, we observe a significant disparity in the replaceability of different layers. Instead of manual or heuristic choices, we frame layer selection as a binary classification problem and propose selective transfer, which automatically and progressively converts layers to linear attention with minimal performance impact. Additionally, to overcome the ineffectiveness and inefficiency of existing objectives for this transfer process, we introduce an anytime distribution matching (ADM) objective that aligns the distributions of samples across any timestep along the sampling trajectory. This objective is efficient and recovers model performance. Extensive experiments show that our method achieves a 1.25-2.00x speedup while preserving generation quality, and our 4-step distilled model further delivers a 15.92x latency reduction with minimal visual quality drop.

