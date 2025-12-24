---
layout: default
title: "Oblivionis: A Lightweight Learning and Unlearning Framework for Federated Large Language Models"
---

# Oblivionis: A Lightweight Learning and Unlearning Framework for Federated Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08875" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08875v2</a>
  <a href="https://arxiv.org/pdf/2508.08875.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08875v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08875v2', 'Oblivionis: A Lightweight Learning and Unlearning Framework for Federated Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fuyao Zhang, Xinyu Yan, Tiantong Wu, Wenjie Li, Tianxiang Chen, Yang Cao, Ran Yan, Longtao Huang, Wei Yang Bryan Lim, Qiang Yang

**分类**: cs.LG, cs.AI, cs.CR

**发布日期**: 2025-08-12 (更新: 2025-11-08)

---

## 💡 一句话要点

**提出Oblivionis框架以解决联邦大语言模型的遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `联邦学习` `数据遗忘` `隐私保护` `大语言模型` `算法比较` `合规性` `机器学习`

## 📋 核心要点

1. 现有的联邦学习框架缺乏有效的机制来满足GDPR等法规的要求，特别是在数据遗忘方面。
2. 本文提出了Oblivionis框架，允许客户端在联邦LLM训练中选择性地移除私有数据，从而提高合规性和信任度。
3. 实验结果表明，Oblivionis在遗忘效果和模型效用之间取得了良好的平衡，优于传统的本地训练方法。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地利用联邦学习（FL）来利用私有的、特定任务的数据集进行微调，同时保护数据隐私。然而，现有的联邦LLM框架缺乏内置的合规机制，如GDPR的被遗忘权。集成私有数据加剧了数据质量和长期治理的担忧，而现有的分布式训练框架没有提供在训练后选择性移除特定客户端贡献的原则性方法。为了解决这一问题，本文提出了Oblivionis，一个轻量级的学习与遗忘框架，使客户端能够在联邦LLM训练过程中选择性地移除特定私有数据，从而增强可信度和合规性。通过将FL和遗忘统一为双重优化目标，本文整合了6种FL算法和5种遗忘算法进行全面评估和比较分析，建立了一个强大的联邦LLM遗忘管道。实验表明，Oblivionis在遗忘效果和模型效用之间实现了良好的平衡，跨算法比较为未来LLM的发展提供了明确的方向。

## 🔬 方法详解

**问题定义**：本文旨在解决联邦学习中缺乏有效数据遗忘机制的问题，现有方法无法在训练后选择性移除特定客户端的数据贡献，导致合规性不足。

**核心思路**：Oblivionis框架通过将联邦学习与遗忘机制结合，设计为双重优化目标，使得在训练过程中可以灵活处理私有数据的遗忘需求。

**技术框架**：该框架包括数据选择模块、模型训练模块和遗忘模块，形成一个完整的联邦学习与遗忘的管道，支持多种算法的集成与评估。

**关键创新**：最重要的创新在于将FL与遗忘机制统一为一个优化目标，提供了一种系统化的方法来处理数据遗忘问题，显著提升了模型的合规性和信任度。

**关键设计**：在设计中，采用了6种不同的FL算法和5种遗忘算法，结合特定的损失函数和参数设置，以确保在遗忘过程中尽量减少对模型效用的影响。通过这些设计，Oblivionis能够在多种场景下实现高效的遗忘与学习。

## 📊 实验亮点

实验结果显示，Oblivionis在遗忘效果上优于传统本地训练方法，能够在保持模型效用的同时实现高效的遗忘。具体而言，Oblivionis在多个算法的比较中表现出更好的平衡，提供了清晰的未来研究方向。

## 🎯 应用场景

Oblivionis框架在多个领域具有广泛的应用潜力，尤其是在需要遵循数据隐私法规的行业，如金融、医疗和社交媒体等。通过提供合规的数据遗忘机制，该框架能够增强用户对数据处理的信任，促进数据共享与合作，同时确保法律法规的遵循。未来，该框架可能会推动更多基于隐私保护的机器学习应用的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) increasingly leverage Federated Learning (FL) to utilize private, task-specific datasets for fine-tuning while preserving data privacy. However, while federated LLM frameworks effectively enable collaborative training without raw data sharing, they critically lack built-in mechanisms for regulatory compliance like GDPR's right to be forgotten. Integrating private data heightens concerns over data quality and long-term governance, yet existing distributed training frameworks offer no principled way to selectively remove specific client contributions post-training. Due to distributed data silos, stringent privacy constraints, and the intricacies of interdependent model aggregation, federated LLM unlearning is significantly more complex than centralized LLM unlearning. To address this gap, we introduce Oblivionis, a lightweight learning and unlearning framework that enables clients to selectively remove specific private data during federated LLM training, enhancing trustworthiness and regulatory compliance. By unifying FL and unlearning as a dual optimization objective, we incorporate 6 FL and 5 unlearning algorithms for comprehensive evaluation and comparative analysis, establishing a robust pipeline for federated LLM unlearning. Extensive experiments demonstrate that Oblivionis outperforms local training, achieving a robust balance between forgetting efficacy and model utility, with cross-algorithm comparisons providing clear directions for future LLM development.

