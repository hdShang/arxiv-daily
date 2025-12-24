---
layout: default
title: "DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-based Human Action Segmentation"
---

# DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-based Human Action Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05543" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05543v1</a>
  <a href="https://arxiv.org/pdf/2509.05543.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05543v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05543v1', 'DuoCLR: Dual-Surrogate Contrastive Learning for Skeleton-based Human Action Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haitao Tian, Pierre Payeur

**分类**: cs.CV

**发布日期**: 2025-09-05

**备注**: ICCV 2025 accepted paper

---

## 💡 一句话要点

**DuoCLR：通过双代理对比学习增强骨骼动作分割**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `骨骼动作分割` `对比学习` `表示学习` `数据增强` `多尺度特征` `人体行为分析` `时空图卷积网络`

## 📋 核心要点

1. 现有动作识别方法难以有效利用多尺度信息和跨序列变化，限制了动作分割的性能。
2. 提出DuoCLR框架，通过Shuffle and Warp数据增强策略和双代理对比学习，学习更鲁棒的多尺度特征表示。
3. 实验表明，DuoCLR在多类和多标签动作分割任务中显著优于现有方法，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种对比表示学习框架，旨在通过使用裁剪过的（单动作）骨骼序列进行预训练，来增强人体动作分割。与之前针对动作识别且基于孤立序列表示的表示学习工作不同，该框架侧重于利用多尺度表示以及跨序列变化。更具体地说，它提出了一种新颖的数据增强策略“Shuffle and Warp”，该策略利用了各种多动作排列。后者有效地辅助了对比学习中引入的两个代理任务：跨排列对比(CPC)和相对顺序推理(ROR)。在优化过程中，CPC通过对比不同排列中相同动作类别的表示来学习类内相似性，而ROR通过预测两个排列之间的相对映射来推理类间上下文。这些任务共同使双代理对比学习(DuoCLR)网络能够学习针对动作分割优化的多尺度特征表示。在实验中，DuoCLR在裁剪后的骨骼数据集上进行预训练，并在未裁剪的数据集上进行评估，在多类和多标签动作分割任务中均表现出优于最先进水平的显著提升。最后，进行了消融研究，以评估所提出方法的每个组成部分的有效性。

## 🔬 方法详解

**问题定义**：现有基于骨骼的动作分割方法，特别是依赖于表示学习的方法，通常针对动作识别任务设计，忽略了动作分割对多尺度信息和跨序列上下文的特殊需求。这些方法难以有效利用不同动作排列中的信息，导致分割性能受限。

**核心思路**：本文的核心思路是利用对比学习，通过设计两个代理任务（跨排列对比CPC和相对顺序推理ROR）来学习对动作分割更有用的特征表示。通过Shuffle and Warp数据增强策略，生成不同的动作排列，并利用这些排列来训练网络区分相同动作的不同排列和不同动作之间的相对顺序。

**技术框架**：DuoCLR框架包含数据增强模块、特征提取模块和对比学习模块。首先，使用Shuffle and Warp策略对输入骨骼序列进行数据增强，生成不同的动作排列。然后，使用特征提取模块（例如，时空图卷积网络）提取多尺度特征表示。最后，通过CPC和ROR两个代理任务进行对比学习，优化特征表示。CPC任务旨在拉近相同动作类别的不同排列的表示，ROR任务旨在预测不同动作排列之间的相对顺序。

**关键创新**：DuoCLR的关键创新在于提出了双代理对比学习框架，该框架同时利用跨排列对比和相对顺序推理来学习特征表示。Shuffle and Warp数据增强策略能够生成多样化的动作排列，为对比学习提供了丰富的训练样本。

**关键设计**：Shuffle and Warp数据增强策略通过随机打乱和时间扭曲操作生成不同的动作排列。CPC任务使用InfoNCE损失函数，鼓励相同动作类别的不同排列的表示尽可能接近。ROR任务通过预测两个排列之间的相对映射关系来学习类间上下文信息。具体实现细节包括损失函数的权重、网络结构的参数选择等。

## 📊 实验亮点

DuoCLR在未裁剪的骨骼动作分割数据集上取得了显著的性能提升。在多类动作分割任务中，DuoCLR的性能优于现有方法，提升幅度达到显著水平。在多标签动作分割任务中，DuoCLR同样取得了优异的成绩，证明了其在复杂场景下的有效性。消融实验验证了Shuffle and Warp数据增强策略以及CPC和ROR两个代理任务的有效性。

## 🎯 应用场景

DuoCLR框架在人体动作分割领域具有广泛的应用前景，例如视频监控、人机交互、康复训练等。通过准确分割人体动作，可以实现异常行为检测、手势识别、运动评估等功能，具有重要的实际应用价值和潜在的社会影响。

## 📄 摘要（原文）

> In this paper, a contrastive representation learning framework is proposed to enhance human action segmentation via pre-training using trimmed (single action) skeleton sequences. Unlike previous representation learning works that are tailored for action recognition and that build upon isolated sequence-wise representations, the proposed framework focuses on exploiting multi-scale representations in conjunction with cross-sequence variations. More specifically, it proposes a novel data augmentation strategy, 'Shuffle and Warp', which exploits diverse multi-action permutations. The latter effectively assists two surrogate tasks that are introduced in contrastive learning: Cross Permutation Contrasting (CPC) and Relative Order Reasoning (ROR). In optimization, CPC learns intra-class similarities by contrasting representations of the same action class across different permutations, while ROR reasons about inter-class contexts by predicting relative mapping between two permutations. Together, these tasks enable a Dual-Surrogate Contrastive Learning (DuoCLR) network to learn multi-scale feature representations optimized for action segmentation. In experiments, DuoCLR is pre-trained on a trimmed skeleton dataset and evaluated on an untrimmed dataset where it demonstrates a significant boost over state-the-art comparatives in both multi-class and multi-label action segmentation tasks. Lastly, ablation studies are conducted to evaluate the effectiveness of each component of the proposed approach.

