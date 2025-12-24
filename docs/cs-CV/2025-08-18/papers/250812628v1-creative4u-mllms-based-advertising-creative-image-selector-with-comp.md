---
layout: default
title: "Creative4U: MLLMs-based Advertising Creative Image Selector with Comparative Reasoning"
---

# Creative4U: MLLMs-based Advertising Creative Image Selector with Comparative Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12628" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12628v1</a>
  <a href="https://arxiv.org/pdf/2508.12628.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12628v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12628v1', 'Creative4U: MLLMs-based Advertising Creative Image Selector with Comparative Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yukang Lin, Xiang Zhang, Shichang Jia, Bowen Wan, Chenghan Fu, Xudong Ren, Yueran Liu, Wanxian Guan, Pengji Wang, Jian Xu, Bo Zheng, Baolin Liu

**分类**: cs.CV

**发布日期**: 2025-08-18

---

## 💡 一句话要点

**提出Creative4U以解决广告创意图像选择的可解释性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `广告创意` `多模态大语言模型` `可解释性` `创意选择` `强化学习` `自然语言生成` `数据集构建`

## 📋 核心要点

1. 现有方法主要集中于创意图像的排名，缺乏可解释的选择机制，导致广告主难以评估创意质量。
2. 本文提出Creative4U，基于多模态大语言模型，将创意图像的评估与选择整合为自然语言生成任务，提升选择的可解释性。
3. 通过离线和在线实验验证，Creative4U在创意图像选择上表现出色，准确性显著提升。

## 📝 摘要（中文）

广告中的创意图像是电子商务平台的核心。引人注目的创意图像能够提升用户购物体验，增加广告主收入和平台广告收益。随着AIGC技术的发展，广告主可以以最低成本生成大量创意图像，但在评估创意质量以进行选择时面临挑战。现有方法主要集中于创意排名，未能满足可解释的创意选择需求。本文提出了首个可解释的创意评估与选择范式，基于多模态大语言模型（MLLMs），将创意图像的评估与选择整合为自然语言生成任务。为此，我们构建了CreativePair数据集，包含8000对标注图像对，并引入Creative4U创意选择器，考虑用户兴趣。通过Reason-to-Select RFT，Creative4U能够准确评估和选择创意图像，实验结果表明该方法有效。

## 🔬 方法详解

**问题定义**：本文旨在解决广告创意图像选择中的可解释性问题。现有方法主要依赖于创意排名，无法提供足够的解释，导致广告主在选择创意时面临困难。

**核心思路**：我们提出了一种新的范式，将创意图像的评估与选择视为自然语言生成任务，利用多模态大语言模型（MLLMs）进行处理，以实现可解释的创意选择。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要阶段。首先，构建CreativePair数据集，包含8000对标注图像对；然后，利用MLLMs进行创意图像的评估与选择；最后，通过Reason-to-Select RFT进行模型的优化与评估。

**关键创新**：本文的主要创新在于将创意评估与选择整合为自然语言生成任务，并引入Reason-to-Select RFT，结合监督微调和基于强化学习的策略优化，显著提升了选择的准确性与可解释性。

**关键设计**：在模型设计中，采用了Chain-of-Thought（CoT-SFT）进行监督微调，并通过Group Relative Policy Optimization（GRPO）进行强化学习优化，确保模型能够有效评估和选择创意图像。具体的损失函数和参数设置将在代码中详细说明。

## 📊 实验亮点

实验结果表明，Creative4U在创意图像选择任务中表现优异，相较于传统方法，准确性提升显著。具体性能数据将在公开的代码和数据集中提供，验证了该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用场景包括电子商务平台、广告创意生成和用户个性化推荐等领域。通过提供可解释的创意选择机制，广告主能够更有效地选择适合目标用户的创意图像，从而提升广告效果和用户体验，推动广告行业的发展。

## 📄 摘要（原文）

> Creative image in advertising is the heart and soul of e-commerce platform. An eye-catching creative image can enhance the shopping experience for users, boosting income for advertisers and advertising revenue for platforms. With the advent of AIGC technology, advertisers can produce large quantities of creative images at minimal cost. However, they struggle to assess the creative quality to select. Existing methods primarily focus on creative ranking, which fails to address the need for explainable creative selection.
>   In this work, we propose the first paradigm for explainable creative assessment and selection. Powered by multimodal large language models (MLLMs), our approach integrates the assessment and selection of creative images into a natural language generation task. To facilitate this research, we construct CreativePair, the first comparative reasoning-induced creative dataset featuring 8k annotated image pairs, with each sample including a label indicating which image is superior. Additionally, we introduce Creative4U (pronounced Creative for You), a MLLMs-based creative selector that takes into account users' interests. Through Reason-to-Select RFT, which includes supervised fine-tuning with Chain-of-Thought (CoT-SFT) and Group Relative Policy Optimization (GRPO) based reinforcement learning, Creative4U is able to evaluate and select creative images accurately. Both offline and online experiments demonstrate the effectiveness of our approach. Our code and dataset will be made public to advance research and industrial applications.

