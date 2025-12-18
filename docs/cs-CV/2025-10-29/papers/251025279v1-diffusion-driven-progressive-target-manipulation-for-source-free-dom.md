---
layout: default
title: Diffusion-Driven Progressive Target Manipulation for Source-Free Domain Adaptation
---

# Diffusion-Driven Progressive Target Manipulation for Source-Free Domain Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.25279" class="toolbar-btn" target="_blank">📄 arXiv: 2510.25279v1</a>
  <a href="https://arxiv.org/pdf/2510.25279.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.25279v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.25279v1', 'Diffusion-Driven Progressive Target Manipulation for Source-Free Domain Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuyang Huang, Yabo Chen, Junyu Zhou, Wenrui Dai, Xiaopeng Zhang, Junni Zou, Hongkai Xiong, Qi Tian

**分类**: cs.CV

**发布日期**: 2025-10-29

**备注**: Accepted by NeurIPS 2025

---

## 💡 一句话要点

**提出扩散驱动的渐进式目标域操控方法，解决无源域自适应中的域差异问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `无源域自适应` `领域自适应` `扩散模型` `伪标签` `目标域操控`

## 📋 核心要点

1. 现有无源域自适应方法在处理源域和目标域差异较大时，伪标签质量差或生成伪数据引入更大差异。
2. 提出扩散驱动的渐进式目标域操控方法，利用扩散模型生成并逐步优化伪目标域，缩小域差异。
3. 实验表明，该方法在多个数据集上显著优于现有方法，尤其在域差异大的情况下性能提升显著。

## 📝 摘要（中文）

无源域自适应(SFDA)是一项具有挑战性的任务，它仅使用预训练的源模型和无标签的目标数据来解决域偏移问题。现有的SFDA方法受到源域和目标域差异的基本限制。非生成式SFDA方法在具有较大域差异的挑战性场景中，会受到不可靠的伪标签的影响，而基于生成的SFDA方法由于在创建伪源数据时扩大了域差异而明显退化。为了解决这个限制，我们提出了一种新的基于生成的框架，名为扩散驱动的渐进式目标域操控(DPTM)，该框架利用无标签的目标数据作为参考，以可靠地生成和逐步细化伪目标域，用于SFDA。具体来说，我们根据伪标签的可靠性将目标样本分为信任集和非信任集，以充分且可靠地利用它们的信息。对于来自非信任集的样本，我们开发了一种操控策略，以语义方式将它们转换为新分配的类别，同时通过潜在扩散模型将它们保持在目标分布中。此外，我们设计了一种渐进式细化机制，通过迭代细化逐步减少伪目标域和真实目标域之间的域差异。实验结果表明，DPTM优于现有方法，并在具有不同规模的四个主流SFDA基准数据集上实现了最先进的性能。值得注意的是，DPTM可以在源域和目标域差距较大的情况下显著提高性能，最高可达18.6%。

## 🔬 方法详解

**问题定义**：无源域自适应(SFDA)旨在仅利用预训练的源域模型和无标签的目标域数据，将知识迁移到目标域。现有方法在处理源域和目标域差异较大时面临挑战。非生成式方法依赖伪标签，但域差异导致伪标签质量下降。生成式方法尝试生成伪源域数据，但生成过程可能进一步扩大域差异，导致性能下降。

**核心思路**：本文的核心思路是利用扩散模型，以目标域数据为参考，生成并逐步优化伪目标域数据。通过将不可靠的目标域样本转换到新的类别，并使用扩散模型保持其目标域分布，从而创建一个更接近真实目标域的伪目标域。渐进式细化机制进一步缩小伪目标域和真实目标域之间的差距。

**技术框架**：DPTM框架包含以下主要模块：1) 信任集和非信任集划分模块：根据伪标签的置信度将目标域样本划分为信任集和非信任集。2) 扩散驱动的目标域操控模块：对于非信任集样本，使用扩散模型将其语义转换为新的类别，同时保持其目标域分布。3) 渐进式细化模块：通过迭代细化，逐步缩小伪目标域和真实目标域之间的域差异。

**关键创新**：该方法最重要的创新点在于利用扩散模型进行目标域操控，能够在语义转换的同时保持目标域分布，避免了传统生成方法可能引入的域差异扩大问题。此外，渐进式细化机制进一步提升了伪目标域的质量。

**关键设计**：关键设计包括：1) 信任集和非信任集的划分标准，例如使用伪标签的置信度阈值。2) 扩散模型的选择和训练，需要保证生成样本的多样性和真实性。3) 渐进式细化机制的迭代次数和学习率等参数设置。4) 损失函数的设计，例如使用交叉熵损失和域对抗损失等。

## 📊 实验亮点

实验结果表明，DPTM在四个主流SFDA基准数据集上取得了state-of-the-art的性能。尤其是在源域和目标域差距较大的情况下，DPTM的性能提升显著，最高可达18.6%。这表明该方法能够有效解决域差异带来的挑战，具有很强的鲁棒性和泛化能力。

## 🎯 应用场景

该研究成果可应用于各种无源域自适应场景，例如：医学图像分析、自动驾驶、机器人导航等。在这些场景中，获取大量标注的目标域数据成本高昂，而该方法能够有效利用已有的源域知识和无标注的目标域数据，提升模型在目标域的性能，具有重要的实际应用价值和潜力。

## 📄 摘要（原文）

> Source-free domain adaptation (SFDA) is a challenging task that tackles domain shifts using only a pre-trained source model and unlabeled target data. Existing SFDA methods are restricted by the fundamental limitation of source-target domain discrepancy. Non-generation SFDA methods suffer from unreliable pseudo-labels in challenging scenarios with large domain discrepancies, while generation-based SFDA methods are evidently degraded due to enlarged domain discrepancies in creating pseudo-source data. To address this limitation, we propose a novel generation-based framework named Diffusion-Driven Progressive Target Manipulation (DPTM) that leverages unlabeled target data as references to reliably generate and progressively refine a pseudo-target domain for SFDA. Specifically, we divide the target samples into a trust set and a non-trust set based on the reliability of pseudo-labels to sufficiently and reliably exploit their information. For samples from the non-trust set, we develop a manipulation strategy to semantically transform them into the newly assigned categories, while simultaneously maintaining them in the target distribution via a latent diffusion model. Furthermore, we design a progressive refinement mechanism that progressively reduces the domain discrepancy between the pseudo-target domain and the real target domain via iterative refinement. Experimental results demonstrate that DPTM outperforms existing methods by a large margin and achieves state-of-the-art performance on four prevailing SFDA benchmark datasets with different scales. Remarkably, DPTM can significantly enhance the performance by up to 18.6% in scenarios with large source-target gaps.

