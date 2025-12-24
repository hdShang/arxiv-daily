---
layout: default
title: "RewardRank: Optimizing True Learning-to-Rank Utility"
---

# RewardRank: Optimizing True Learning-to-Rank Utility

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14180" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14180v2</a>
  <a href="https://arxiv.org/pdf/2508.14180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14180v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14180v2', 'RewardRank: Optimizing True Learning-to-Rank Utility')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gaurav Bhatt, Kiran Koshy Thekumparampil, Tanmay Gangwani, Tesi Xiao, Leonid Sigal

**分类**: cs.IR, cs.LG

**发布日期**: 2025-08-19 (更新: 2025-10-17)

**🔗 代码/项目**: [GITHUB](https://github.com/GauravBh1010tt/RewardRank)

---

## 💡 一句话要点

**提出RewardRank以优化真实学习排序效用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `学习排序` `反事实优化` `用户行为建模` `数据驱动方法` `推荐系统`

## 📋 核心要点

1. 现有的排序系统往往依赖于简化的用户行为假设，导致无法有效提升真实的用户效用。
2. 论文提出RewardRank框架，通过学习用户交互数据中的奖励模型，直接优化反事实效用。
3. 实验结果显示，RewardRank在多个基准测试中超越了传统方法，提升了离线相关性性能。

## 📝 摘要（中文）

传统的排序系统通常优化离线代理目标，这些目标依赖于对用户行为的过于简化的假设，往往忽视了位置偏差和项目多样性等因素。因此，这些模型在在线A/B测试中无法提高真实的反事实效用，如点击率或购买概率。我们提出了RewardRank，这是一种数据驱动的学习排序框架，旨在最大化反事实效用。RewardRank首先从记录的用户交互中学习奖励模型，预测任何排序的效用，然后训练排序器使用可微分的软排列操作来最大化该奖励。为了实现严格和可重复的评估，我们进一步提出了两个基准套件：参数化Oracle评估（PO-Eval）和LLM作为用户评估（LAU-Eval）。RewardRank在这两个基准上都实现了最高的反事实效用，并证明优化经典指标如NDCG对于最大化真实用户效用是次优的。最终，使用来自Baidu-ULTR数据集的真实用户反馈，RewardRank在离线相关性性能上建立了新的状态。我们的结果表明，学习排序可以重新表述为反事实效用的直接优化，且以纯数据驱动的方式实现，无需依赖位置偏差等显式建模假设。

## 🔬 方法详解

**问题定义**：论文要解决的问题是现有排序系统在优化用户效用时的不足，尤其是未能考虑位置偏差和项目多样性等因素，导致在线测试中的效果不佳。

**核心思路**：RewardRank的核心思路是通过数据驱动的方法，直接从用户交互中学习奖励模型，并利用该模型优化排序，而不是依赖于传统的代理目标。

**技术框架**：RewardRank的整体架构包括两个主要模块：首先是奖励模型的学习，接着是基于该模型的排序器训练，使用可微分的软排列操作来实现优化。

**关键创新**：最重要的技术创新在于将学习排序问题重新定义为反事实效用的直接优化，避免了传统方法中的简化假设，从而更真实地反映用户行为。

**关键设计**：在设计上，RewardRank使用了特定的损失函数来最大化预测的奖励，并通过可微分的操作实现了排序的优化，确保了模型的灵活性和有效性。

## 📊 实验亮点

在实验中，RewardRank在两个基准测试中均实现了最高的反事实效用，超越了传统的NDCG优化方法，显示出优化用户效用的有效性。具体而言，RewardRank在Baidu-ULTR数据集上设立了新的离线相关性性能记录，证明了其在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括电子商务、搜索引擎和推荐系统等，能够有效提升用户体验和商业转化率。通过优化真实的用户效用，RewardRank有望在实际应用中带来显著的经济效益和用户满意度提升。未来，该方法还可以扩展到更多的在线学习和个性化推荐场景。

## 📄 摘要（原文）

> Traditional ranking systems optimize offline proxy objectives that rely on oversimplified assumptions about user behavior, often neglecting factors such as position bias and item diversity. Consequently, these models fail to improve true counterfactual utilities such as such as click-through rate or purchase probability, when evaluated in online A/B tests. We introduce RewardRank, a data-driven learning-to-rank (LTR) framework for counterfactual utility maximization. RewardRank first learns a reward model that predicts the utility of any ranking directly from logged user interactions, and then trains a ranker to maximize this reward using a differentiable soft permutation operator. To enable rigorous and reproducible evaluation, we further propose two benchmark suites: (i) Parametric Oracle Evaluation (PO-Eval), which employs an open-source click model as a counterfactual oracle on the Baidu-ULTR dataset, and (ii) LLM-as-User Evaluation (LAU-Eval), which simulates realistic user behavior via large language models on the Amazon-KDD-Cup dataset. RewardRank achieves the highest counterfactual utility across both benchmarks and demonstrates that optimizing classical metrics such as NDCG is sub-optimal for maximizing true user utility. Finally, using real user feedback from the Baidu-ULTR dataset, RewardRank establishes a new state of the art in offline relevance performance. Overall, our results show that learning-to-rank can be reformulated as direct optimization of counterfactual utility, achieved in a purely data-driven manner without relying on explicit modeling assumptions such as position bias. Our code is available at: $https://github.com/GauravBh1010tt/RewardRank$

