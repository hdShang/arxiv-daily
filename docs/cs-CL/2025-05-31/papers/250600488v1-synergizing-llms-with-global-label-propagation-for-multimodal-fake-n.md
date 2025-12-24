---
layout: default
title: Synergizing LLMs with Global Label Propagation for Multimodal Fake News Detection
---

# Synergizing LLMs with Global Label Propagation for Multimodal Fake News Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00488" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00488v1</a>
  <a href="https://arxiv.org/pdf/2506.00488.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00488v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00488v1', 'Synergizing LLMs with Global Label Propagation for Multimodal Fake News Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuguo Hu, Jun Hu, Huaiwen Zhang

**分类**: cs.CL

**发布日期**: 2025-05-31

**备注**: Accepted by ACL 2025 Main Conference

---

## 💡 一句话要点

**提出GLPN-LLM以解决多模态假新闻检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态假新闻检测` `大型语言模型` `标签传播` `伪标签生成` `深度学习`

## 📋 核心要点

1. 现有的假新闻检测方法在处理多模态数据时，依赖于传统的特征提取和分类技术，导致性能不足。
2. 本文提出GLPN-LLM模型，通过全球标签传播技术有效整合LLM生成的伪标签，提升假新闻检测的准确性。
3. 实验结果显示，GLPN-LLM在多个基准数据集上表现优越，相较于现有方法有显著性能提升。

## 📝 摘要（中文）

大型语言模型（LLMs）可以通过预测伪标签来辅助多模态假新闻检测。然而，单独使用LLM生成的伪标签在性能上较传统检测方法表现不佳，使得有效整合变得复杂。本文提出了全球标签传播网络与LLM基础伪标签化（GLPN-LLM），通过标签传播技术整合LLM能力。全球标签传播利用LLM生成的伪标签，通过在所有样本之间传播标签信息来提高预测准确性。为防止训练过程中标签泄漏，设计了一种基于掩码的机制，确保训练节点不会将自己的标签传播回自己。实验结果表明，通过将LLM与标签传播相结合，我们的模型在基准数据集上超越了现有的最先进基线。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态假新闻检测中，传统方法在处理LLM生成伪标签时性能不足的问题。现有方法往往无法有效利用LLM的潜力，导致检测效果不理想。

**核心思路**：提出GLPN-LLM模型，通过全球标签传播技术，利用LLM生成的伪标签来增强样本间的标签信息传播，从而提高整体预测准确性。设计掩码机制以防止标签泄漏，确保训练过程的有效性。

**技术框架**：GLPN-LLM模型包括伪标签生成模块和标签传播模块。伪标签生成模块利用LLM生成初步标签，标签传播模块则通过全局传播机制在样本间传递标签信息，最终形成更准确的标签。

**关键创新**：本研究的主要创新在于将LLM与标签传播技术相结合，形成了一种新的假新闻检测框架，显著提升了检测性能。与传统方法相比，GLPN-LLM能够更有效地利用多模态数据中的信息。

**关键设计**：模型中采用了掩码机制来防止标签泄漏，确保训练节点不会将自己的标签传播回自己。此外，损失函数的设计也考虑了标签传播的特性，以优化模型的学习过程。通过这些设计，模型在训练时能够更好地捕捉样本间的关系。

## 📊 实验亮点

在多个基准数据集上的实验结果表明，GLPN-LLM模型在假新闻检测任务中显著优于现有的最先进基线，提升幅度达到XX%（具体数据未知），验证了模型的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用场景包括社交媒体内容监测、新闻网站的假新闻检测以及信息传播的真实性验证等领域。通过提高假新闻检测的准确性，能够有效减少虚假信息对社会的负面影响，提升公众的信息获取质量。未来，该技术还可以扩展到其他多模态数据分析任务中，具有广泛的实际价值。

## 📄 摘要（原文）

> Large Language Models (LLMs) can assist multimodal fake news detection by predicting pseudo labels. However, LLM-generated pseudo labels alone demonstrate poor performance compared to traditional detection methods, making their effective integration non-trivial. In this paper, we propose Global Label Propagation Network with LLM-based Pseudo Labeling (GLPN-LLM) for multimodal fake news detection, which integrates LLM capabilities via label propagation techniques. The global label propagation can utilize LLM-generated pseudo labels, enhancing prediction accuracy by propagating label information among all samples. For label propagation, a mask-based mechanism is designed to prevent label leakage during training by ensuring that training nodes do not propagate their own labels back to themselves. Experimental results on benchmark datasets show that by synergizing LLMs with label propagation, our model achieves superior performance over state-of-the-art baselines.

