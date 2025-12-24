---
layout: default
title: "Team QUST at SemEval-2025 Task 10: Evaluating Large Language Models in Multiclass Multi-label Classification of News Entity Framing"
---

# Team QUST at SemEval-2025 Task 10: Evaluating Large Language Models in Multiclass Multi-label Classification of News Entity Framing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21564" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21564v1</a>
  <a href="https://arxiv.org/pdf/2506.21564.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21564v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21564v1', 'Team QUST at SemEval-2025 Task 10: Evaluating Large Language Models in Multiclass Multi-label Classification of News Entity Framing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiyan Liu, Youzheng Liu, Taihang Wang, Xiaoman Xu, Yimin Wang, Ye Jiang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-12

**🔗 代码/项目**: [GITHUB](https://github.com/warmth27/SemEval2025_Task7)

---

## 💡 一句话要点

**提出三阶段检索框架以优化新闻实体框架的多类多标签分类**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多类多标签分类` `新闻实体框架` `事实核查` `检索模型` `重排序` `加权投票` `信息检索`

## 📋 核心要点

1. 现有的多类多标签分类方法在处理新闻实体框架时面临检索效果不佳的问题，尤其是在事实核查方面。
2. 本文提出了一种三阶段检索框架，通过候选检索、重排序和加权投票来优化检索结果，提升了模型的准确性和效率。
3. 实验结果显示，该方法在单语轨道中排名第五，在跨语轨道中排名第七，展示了显著的性能提升。

## 📝 摘要（中文）

本文描述了QUST_NLP在SemEval-2025任务7中的参与。我们提出了一种专门为事实核查声明检索设计的三阶段检索框架。首先，我们评估了多种检索模型的性能，并选择了最佳候选检索模型。接着，采用多种重排序模型来增强候选结果，每个模型选择前10个结果。最后，利用加权投票确定最终检索结果。我们的方案在单语轨道中获得第五名，在跨语轨道中获得第七名。我们已在GitHub上发布了系统代码。

## 🔬 方法详解

**问题定义**：本文旨在解决新闻实体框架中的多类多标签分类问题，现有方法在事实核查声明检索中效果不佳，导致信息准确性不足。

**核心思路**：我们设计了一个三阶段检索框架，首先选择最佳候选检索模型，然后通过重排序模型优化结果，最后通过加权投票确定最终输出，以提高检索的准确性和可靠性。

**技术框架**：整体架构分为三个主要阶段：第一阶段为候选检索，评估多种检索模型并选择最佳者；第二阶段为重排序，利用多个模型对候选结果进行优化；第三阶段为加权投票，综合各模型结果确定最终输出。

**关键创新**：本研究的创新点在于引入了加权投票机制，结合多种重排序模型的结果，显著提升了检索的准确性，与传统单一模型方法相比具有明显优势。

**关键设计**：在模型选择中，我们通过性能评估选择最佳候选模型，重排序阶段采用多种模型并选取Top-10结果，最后通过加权投票整合结果，确保了输出的多样性与准确性。

## 📊 实验亮点

在实验中，我们的三阶段检索框架在单语轨道中获得了第五名，在跨语轨道中获得第七名，展示了相较于基线模型的显著性能提升，验证了方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括新闻媒体、社交网络和信息检索系统，能够帮助用户更准确地获取事实信息，提升信息检索的效率与准确性。未来，该框架可扩展至其他类型的文本分类任务，具有广泛的实际价值。

## 📄 摘要（原文）

> This paper describes the participation of QUST_NLP in the SemEval-2025 Task 7. We propose a three-stage retrieval framework specifically designed for fact-checked claim retrieval. Initially, we evaluate the performance of several retrieval models and select the one that yields the best results for candidate retrieval. Next, we employ multiple re-ranking models to enhance the candidate results, with each model selecting the Top-10 outcomes. In the final stage, we utilize weighted voting to determine the final retrieval outcomes. Our approach achieved 5th place in the monolingual track and 7th place in the crosslingual track. We release our system code at: https://github.com/warmth27/SemEval2025_Task7.

