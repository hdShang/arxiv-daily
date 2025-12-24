---
layout: default
title: "Bridging the Gap: Self-Optimized Fine-Tuning for LLM-based Recommender Systems"
---

# Bridging the Gap: Self-Optimized Fine-Tuning for LLM-based Recommender Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20771" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20771v1</a>
  <a href="https://arxiv.org/pdf/2505.20771.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20771v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20771v1', 'Bridging the Gap: Self-Optimized Fine-Tuning for LLM-based Recommender Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heng Tang, Feng Liu, Xinbo Chen, Jiawei Chen, Bohao Wang, Changwang Zhang, Jun Wang, Yuegang Sun, Bingde Hu, Can Wang

**分类**: cs.IR, cs.AI

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出自优化微调方法以提升LLM推荐系统性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推荐系统` `自优化微调` `自蒸馏` `课程学习` `推荐准确率` `机器学习`

## 📋 核心要点

1. 现有的推荐系统方法在利用大型语言模型时存在性能不足的问题，无法有效整合知识与推荐任务。
2. 本文提出的自优化微调（SOFT）方法结合了自蒸馏和自适应课程学习，旨在提升LLMs的推荐能力。
3. 实验结果显示，SOFT方法在推荐准确率上平均提升了37.59%，显著优于现有的基线方法。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在推荐系统领域的应用得到了广泛探索。目前主要有两种策略使LLMs具备推荐能力：一是“仅指导”策略，利用上下文学习增强LLMs的语义理解和推荐能力；二是“仅调优”策略，通过监督微调（SFT）使LLMs适应真实推荐数据。然而，这两种策略均未能有效弥合LLMs知识空间与推荐之间的差距，导致性能未达预期。为此，本文提出了一种新颖的“指导+调优”方法——自优化微调（SOFT），结合了课程学习的思想，通过自蒸馏构建易学的辅助数据集，并利用自适应课程调度器逐步引导LLMs从简单数据学习到更具挑战性的真实推荐数据。实验结果表明，SOFT显著提高了LLM方法的推荐准确率，平均提升达37.59%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM推荐系统中知识与推荐任务之间的差距，现有的“仅指导”和“仅调优”策略未能有效提升推荐性能。

**核心思路**：提出自优化微调（SOFT）方法，通过自蒸馏生成易学的辅助数据集，并利用自适应课程调度器逐步引导模型学习，从而提升推荐效果。

**技术框架**：SOFT方法包括两个主要阶段：首先进行自蒸馏，构建辅助数据集；然后通过自适应课程调度器，逐步引导模型从简单到复杂的数据进行学习。

**关键创新**：SOFT的核心创新在于结合了自蒸馏和课程学习的思想，形成了一种新的训练策略，区别于传统的单一指导或调优方法。

**关键设计**：在自蒸馏阶段，设计了特定的损失函数以确保生成数据的有效性；课程调度器的参数设置使得模型能够在不同难度的数据上进行有效学习。

## 📊 实验亮点

实验结果表明，SOFT方法在推荐准确率上平均提升了37.59%，显著优于现有的基线方法，显示出其在实际应用中的有效性和潜力。

## 🎯 应用场景

该研究的潜在应用领域包括电子商务、社交媒体和内容推荐等场景，能够帮助企业提升用户体验和满意度。未来，SOFT方法可能推动LLM在推荐系统中的更广泛应用，促进个性化推荐技术的发展。

## 📄 摘要（原文）

> Recent years have witnessed extensive exploration of Large Language Models (LLMs) on the field of Recommender Systems (RS). There are currently two commonly used strategies to enable LLMs to have recommendation capabilities: 1) The "Guidance-Only" strategy uses in-context learning to exploit and amplify the inherent semantic understanding and item recommendation capabilities of LLMs; 2) The "Tuning-Only" strategy uses supervised fine-tuning (SFT) to fine-tune LLMs with the aim of fitting them to real recommendation data. However, neither of these strategies can effectively bridge the gap between the knowledge space of LLMs and recommendation, and their performance do not meet our expectations.
>   To better enable LLMs to learn recommendation knowledge, we combine the advantages of the above two strategies and proposed a novel "Guidance+Tuning" method called Self-Optimized Fine-Tuning (SOFT), which adopts the idea of curriculum learning. It first employs self-distillation to construct an auxiliary easy-to-learn but meaningful dataset from a fine-tuned LLM. Then it further utilizes a self-adaptive curriculum scheduler to enable LLMs to gradually learn from simpler data (self-distilled data) to more challenging data (real RS data). Extensive experiments demonstrate that SOFT significantly enhances the recommendation accuracy (37.59\% on average) of LLM-based methods. The code is available via https://anonymous.4open.science/r/Self-Optimized-Fine-Tuning-264E

