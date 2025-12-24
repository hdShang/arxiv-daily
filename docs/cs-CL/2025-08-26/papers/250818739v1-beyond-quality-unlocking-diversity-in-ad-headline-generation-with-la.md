---
layout: default
title: "Beyond Quality: Unlocking Diversity in Ad Headline Generation with Large Language Models"
---

# Beyond Quality: Unlocking Diversity in Ad Headline Generation with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18739" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18739v1</a>
  <a href="https://arxiv.org/pdf/2508.18739.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18739v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18739v1', 'Beyond Quality: Unlocking Diversity in Ad Headline Generation with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chang Wang, Siyu Yan, Depeng Yuan, Yuqi Chen, Yanhua Huang, Yuanhang Zheng, Shuhao Li, Yinqi Zhang, Kedi Chen, Mingrui Zhu, Ruiwen Xu

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出DIVER框架以解决广告标题生成中的多样性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `广告标题生成` `多样性优化` `大型语言模型` `强化学习` `监督微调` `数据生成管道` `文本生成`

## 📋 核心要点

1. 现有广告标题生成方法主要关注质量或点击率，忽视了多样性，导致输出结果同质化。
2. 本文提出DIVER框架，通过语义和风格感知的数据生成管道，实现高质量和多样化标题的联合优化。
3. 在真实数据集上的实验结果显示，DIVER有效提升了广告主价值和点击率，验证了其实际应用效果。

## 📝 摘要（中文）

广告标题的生成在现代广告中至关重要，质量和多样性都是吸引广泛受众的关键。现有方法主要优化语言模型以提高标题质量或点击率（CTR），但往往忽视多样性，导致输出同质化。为了解决这一局限性，本文提出了DIVER，一个基于大型语言模型（LLMs）的新框架，旨在同时优化多样性和质量。我们设计了一个语义和风格感知的数据生成管道，自动生成高质量的广告内容和多样化标题的训练对。通过多阶段多目标优化框架结合监督微调（SFT）和强化学习（RL），DIVER在真实工业数据集上的实验表明，能够有效平衡质量与多样性，并在大型内容分享平台上提升广告主价值（ADVV）和CTR，分别提高4.0%和1.4%。

## 🔬 方法详解

**问题定义**：本文旨在解决广告标题生成中的多样性不足问题。现有方法通常只优化标题质量或点击率，导致生成的标题缺乏多样性，无法有效吸引不同的受众群体。

**核心思路**：DIVER框架的核心思想是通过联合优化质量和多样性，利用大型语言模型生成多样化的广告标题。通过设计一个语义和风格感知的数据生成管道，自动生成高质量的训练对，以支持多样性目标的实现。

**技术框架**：DIVER框架包括多个模块，首先是数据生成管道，接着是多阶段多目标优化过程，结合监督微调（SFT）和强化学习（RL），以实现高效的标题生成。

**关键创新**：DIVER的主要创新在于其多目标优化策略，能够在单次前向传播中同时考虑标题的质量与多样性，这与传统方法的单一优化目标形成鲜明对比。

**关键设计**：在DIVER中，采用了特定的损失函数来平衡质量与多样性，并设计了适应性的网络结构，以支持多样化标题的生成。

## 📊 实验亮点

实验结果表明，DIVER框架在真实工业数据集上显著提升了广告主价值（ADVV）4.0%和点击率（CTR）1.4%。这些结果表明，DIVER在平衡质量与多样性方面的有效性，超越了传统的广告标题生成方法。

## 🎯 应用场景

该研究的潜在应用领域包括在线广告、社交媒体内容生成及市场营销等。通过提升广告标题的多样性和质量，DIVER框架能够帮助广告主更好地吸引目标受众，从而提高广告效果和投资回报率。未来，该技术有望扩展到其他文本生成任务中，推动内容创作的智能化发展。

## 📄 摘要（原文）

> The generation of ad headlines plays a vital role in modern advertising, where both quality and diversity are essential to engage a broad range of audience segments. Current approaches primarily optimize language models for headline quality or click-through rates (CTR), often overlooking the need for diversity and resulting in homogeneous outputs. To address this limitation, we propose DIVER, a novel framework based on large language models (LLMs) that are jointly optimized for both diversity and quality. We first design a semantic- and stylistic-aware data generation pipeline that automatically produces high-quality training pairs with ad content and multiple diverse headlines. To achieve the goal of generating high-quality and diversified ad headlines within a single forward pass, we propose a multi-stage multi-objective optimization framework with supervised fine-tuning (SFT) and reinforcement learning (RL). Experiments on real-world industrial datasets demonstrate that DIVER effectively balances quality and diversity. Deployed on a large-scale content-sharing platform serving hundreds of millions of users, our framework improves advertiser value (ADVV) and CTR by 4.0% and 1.4%.

