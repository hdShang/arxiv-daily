---
layout: default
title: "WSS-CL: Weight Saliency Soft-Guided Contrastive Learning for Efficient Machine Unlearning Image Classification"
---

# WSS-CL: Weight Saliency Soft-Guided Contrastive Learning for Efficient Machine Unlearning Image Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04308" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04308v1</a>
  <a href="https://arxiv.org/pdf/2508.04308.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04308v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04308v1', 'WSS-CL: Weight Saliency Soft-Guided Contrastive Learning for Efficient Machine Unlearning Image Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thang Duc Tran, Thai Hoang Le

**分类**: cs.LG

**发布日期**: 2025-08-06

**备注**: 17th International Conference on Computational Collective Intelligence 2025

---

## 💡 一句话要点

**提出WSS-CL以解决高效机器遗忘问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器遗忘` `图像分类` `对比学习` `自监督学习` `权重显著性` `Kullback-Leibler散度` `模型更新`

## 📋 核心要点

1. 现有机器遗忘方法在精确遗忘、稳定性和跨领域适用性方面存在显著挑战。
2. 本文提出WSS-CL方法，通过权重显著性引导遗忘过程，分为遗忘阶段和对抗微调阶段。
3. 实验表明，WSS-CL在遗忘效率上显著提升，性能损失极小，适用于监督和自监督设置。

## 📝 摘要（中文）

机器遗忘是指在训练模型中高效删除特定数据影响的过程，仍然是一个具有挑战性的问题。现有的机器遗忘方法主要集中在数据中心或基于权重的策略，常常面临精确遗忘、稳定性和跨领域适用性等挑战。本文提出了一种新的两阶段高效机器遗忘方法WSS-CL，利用权重显著性聚焦于关键模型参数的遗忘过程。该方法通过最大化输出logits与聚合伪标签之间的Kullback-Leibler散度来实现高效遗忘，并在对抗微调阶段引入自监督的对比学习。实验结果表明，WSS-CL在遗忘效率上显著提升，且与现有最先进方法相比，性能损失微乎其微。

## 🔬 方法详解

**问题定义**：本文旨在解决机器遗忘中的高效删除特定数据影响的问题。现有方法在精确遗忘和稳定性方面存在不足，难以在不同领域中广泛应用。

**核心思路**：WSS-CL方法通过权重显著性来聚焦关键模型参数的遗忘过程，分为两个阶段：遗忘阶段和对抗微调阶段，以提高遗忘效率并减少性能损失。

**技术框架**：该方法的整体架构包括两个主要阶段：首先是遗忘阶段，通过最大化输出logits与聚合伪标签之间的Kullback-Leibler散度实现高效遗忘；其次是对抗微调阶段，采用自监督的对比学习来优化特征表示。

**关键创新**：WSS-CL的核心创新在于利用权重显著性引导遗忘过程，显著缩小了与“精确”遗忘之间的性能差距。这一方法在特征空间中最大化遗忘样本与保留样本之间的距离，形成正负样本对。

**关键设计**：在对比损失计算中，遗忘样本与配对的增强样本作为正样本，而保留样本作为负样本。该设计确保了在特征空间中有效区分遗忘与保留的数据样本。实验中，采用了适当的超参数设置以优化模型性能。

## 📊 实验亮点

实验结果显示，WSS-CL在遗忘效率上显著提升，与现有最先进方法相比，性能损失几乎可以忽略不计。这表明该方法在监督和自监督学习设置中的广泛适用性，具有较高的实用价值。

## 🎯 应用场景

该研究的潜在应用领域包括图像分类、数据隐私保护和模型更新等场景。随着数据隐私法规的日益严格，WSS-CL为高效删除敏感数据提供了一种有效的解决方案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Machine unlearning, the efficient deletion of the impact of specific data in a trained model, remains a challenging problem. Current machine unlearning approaches that focus primarily on data-centric or weight-based strategies frequently encounter challenges in achieving precise unlearning, maintaining stability, and ensuring applicability across diverse domains. In this work, we introduce a new two-phase efficient machine unlearning method for image classification, in terms of weight saliency, leveraging weight saliency to focus the unlearning process on critical model parameters. Our method is called weight saliency soft-guided contrastive learning for efficient machine unlearning image classification (WSS-CL), which significantly narrows the performance gap with "exact" unlearning. First, the forgetting stage maximizes kullback-leibler divergence between output logits and aggregated pseudo-labels for efficient forgetting in logit space. Next, the adversarial fine-tuning stage introduces contrastive learning in a self-supervised manner. By using scaled feature representations, it maximizes the distance between the forgotten and retained data samples in the feature space, with the forgotten and the paired augmented samples acting as positive pairs, while the retained samples act as negative pairs in the contrastive loss computation. Experimental evaluations reveal that our proposed method yields much-improved unlearning efficacy with negligible performance loss compared to state-of-the-art approaches, indicative of its usability in supervised and self-supervised settings.

