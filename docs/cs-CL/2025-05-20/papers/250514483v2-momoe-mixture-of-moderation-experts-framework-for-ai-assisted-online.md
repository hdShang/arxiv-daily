---
layout: default
title: "MoMoE: Mixture of Moderation Experts Framework for AI-Assisted Online Governance"
---

# MoMoE: Mixture of Moderation Experts Framework for AI-Assisted Online Governance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14483" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14483v2</a>
  <a href="https://arxiv.org/pdf/2505.14483.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14483v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14483v2', 'MoMoE: Mixture of Moderation Experts Framework for AI-Assisted Online Governance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Agam Goyal, Xianyang Zhan, Yilun Chen, Koustuv Saha, Eshwar Chandrasekharan

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-10-23)

**备注**: EMNLP 2025 (Oral)

---

## 💡 一句话要点

**提出MoMoE框架以解决在线社区内容审核透明性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内容审核` `在线社区` `透明性` `人工智能治理` `语言模型` `模块化设计` `专家模型`

## 📋 核心要点

1. 现有的内容审核方法需要为每个社区单独训练模型，且决策过程缺乏透明性，限制了其在实际中的应用。
2. 本文提出的MoMoE框架通过模块化设计，结合多个专家模型，实现跨社区的可扩展内容审核，并提供事后解释。
3. 在实验中，MoMoE在30个未见的子版块上取得了高达0.72的Micro-F1分数，表现优于传统的微调基线，同时提供可靠的解释。

## 📝 摘要（中文）

大型语言模型（LLMs）在标记在线社区中的有害内容方面展现了巨大潜力。然而，现有的审核方法需要为每个社区单独训练模型，且决策过程不透明，限制了其实际应用。本文提出了混合审核专家框架（MoMoE），这是一个模块化的跨社区框架，能够为可扩展的内容审核提供事后解释。MoMoE协调四个操作符——分配、预测、聚合和解释，并实例化为七个社区专用专家（MoMoE-Community）和五个规范违规专家（MoMoE-NormVio）。在30个未见的子版块上，最佳变体分别获得了0.72和0.67的Micro-F1分数，匹配或超越了强大的微调基线，同时始终产生简洁可靠的解释。尽管社区专用专家提供了最高的峰值准确率，但规范违规专家在各个领域提供了更稳定的表现。这些发现表明，MoMoE能够实现可扩展、透明的审核，而无需针对每个社区进行微调。

## 🔬 方法详解

**问题定义**：本文旨在解决现有内容审核方法在透明性和可扩展性方面的不足，尤其是每个社区需要单独模型的问题。

**核心思路**：MoMoE框架通过模块化设计，整合多个专家模型，提供跨社区的内容审核解决方案，并在审核后提供可解释性。

**技术框架**：MoMoE框架包括四个主要操作符：分配（Allocate）、预测（Predict）、聚合（Aggregate）和解释（Explain），并通过社区专用专家和规范违规专家的组合实现。

**关键创新**：MoMoE的主要创新在于其模块化设计和跨社区的专家组合，能够在不需要针对每个社区微调的情况下，实现高效且透明的内容审核。

**关键设计**：在设计中，MoMoE使用了七个社区专用专家和五个规范违规专家，采用了特定的损失函数和网络结构，以确保在不同社区和规范违规场景下的稳定性能。

## 📊 实验亮点

在实验中，MoMoE在30个未见的子版块上取得了Micro-F1分数0.72和0.67，分别对应社区专用专家和规范违规专家，超越了传统的微调基线，且始终提供简洁可靠的解释，显示出其在内容审核中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体平台、在线论坛和任何需要内容审核的社区。通过提供透明的审核过程，MoMoE能够增强用户对平台的信任，并促进更健康的在线交流环境。未来，该框架的设计理念也可能影响其他领域的人工智能治理研究。

## 📄 摘要（原文）

> Large language models (LLMs) have shown great potential in flagging harmful content in online communities. Yet, existing approaches for moderation require a separate model for every community and are opaque in their decision-making, limiting real-world adoption. We introduce Mixture of Moderation Experts (MoMoE), a modular, cross-community framework that adds post-hoc explanations to scalable content moderation. MoMoE orchestrates four operators -- Allocate, Predict, Aggregate, Explain -- and is instantiated as seven community-specialized experts (MoMoE-Community) and five norm-violation experts (MoMoE-NormVio). On 30 unseen subreddits, the best variants obtain Micro-F1 scores of 0.72 and 0.67, respectively, matching or surpassing strong fine-tuned baselines while consistently producing concise and reliable explanations. Although community-specialized experts deliver the highest peak accuracy, norm-violation experts provide steadier performance across domains. These findings show that MoMoE yields scalable, transparent moderation without needing per-community fine-tuning. More broadly, they suggest that lightweight, explainable expert ensembles can guide future NLP and HCI research on trustworthy human-AI governance of online communities.

