---
layout: default
title: "Learning to Shop Like Humans: A Review-driven Retrieval-Augmented Recommendation Framework with LLMs"
---

# Learning to Shop Like Humans: A Review-driven Retrieval-Augmented Recommendation Framework with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00698" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00698v1</a>
  <a href="https://arxiv.org/pdf/2509.00698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00698v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00698v1', 'Learning to Shop Like Humans: A Review-driven Retrieval-Augmented Recommendation Framework with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiwen Wei, Jinpeng Gao, Jiang Zhong, Yuming Yang, Fengmao Lv, Zhenyang Li

**分类**: cs.CL

**发布日期**: 2025-08-31

---

## 💡 一句话要点

**提出RevBrowse框架以解决LLM推荐中的评论整合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长语言模型` `推荐系统` `用户评论` `动态偏好建模` `检索增强` `个性化推荐`

## 📋 核心要点

1. 现有方法在动态利用用户评论时效率低下，且缺乏优先考虑相关评论的机制。
2. RevBrowse框架通过整合用户评论到LLM重排序过程中，提升推荐的准确性和相关性。
3. 在四个亚马逊评论数据集上的实验显示，RevBrowse在性能上显著优于现有强基线，验证了其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在推荐任务中展现出强大的潜力，尤其是在基于评论的推荐中，能够利用用户生成的文本揭示细致的用户偏好和物品属性。然而，将评论有效整合进LLM推荐中仍面临挑战，包括在有限的上下文窗口中动态利用用户评论的效率低下，以及缺乏有效机制来优先考虑与用户当前决策上下文最相关的评论。为此，本文提出了RevBrowse，一个受“浏览后决策”过程启发的评论驱动推荐框架。RevBrowse将用户评论整合进LLM的重排序过程中，以增强其区分候选物品的能力。通过引入PrefRAG模块，RevBrowse提高了评论使用的相关性和效率，适应性地检索与目标物品相关的偏好内容。实验结果表明，RevBrowse在四个亚马逊评论数据集上显著优于强基线，展示了其建模动态用户偏好的有效性和通用性。

## 🔬 方法详解

**问题定义**：本文旨在解决在LLM推荐系统中有效整合用户评论的问题。现有方法在动态利用评论时效率低下，且未能优先考虑与用户当前决策最相关的评论。

**核心思路**：RevBrowse框架通过模拟“浏览后决策”的用户行为，将用户评论整合进LLM的重排序过程，以提高推荐的准确性和相关性。

**技术框架**：RevBrowse的整体架构包括两个主要模块：评论整合模块和PrefRAG检索增强模块。评论整合模块负责将用户评论与候选物品进行关联，而PrefRAG模块则负责根据目标物品动态检索相关的用户偏好内容。

**关键创新**：RevBrowse的核心创新在于其评论驱动的重排序机制和PrefRAG模块的引入，使得推荐系统能够更有效地利用用户评论，显著提升了推荐的相关性和准确性。

**关键设计**：在设计中，PrefRAG模块通过结构化用户和物品表示，适应性地检索与目标物品相关的评论内容，确保了评论的高效利用。

## 📊 实验亮点

在四个亚马逊评论数据集上的实验结果显示，RevBrowse在推荐性能上相较于强基线有显著提升，具体提升幅度达到XX%（具体数据待补充），验证了其在动态用户偏好建模中的有效性和通用性。

## 🎯 应用场景

RevBrowse框架具有广泛的应用潜力，尤其适用于电商平台、社交媒体和内容推荐系统等领域。通过提升推荐的准确性和用户体验，该研究为个性化推荐系统的发展提供了新的思路和方法，未来可能对用户决策过程产生深远影响。

## 📄 摘要（原文）

> Large language models (LLMs) have shown strong potential in recommendation tasks due to their strengths in language understanding, reasoning and knowledge integration. These capabilities are especially beneficial for review-based recommendation, which relies on semantically rich user-generated texts to reveal fine-grained user preferences and item attributes. However, effectively incorporating reviews into LLM-based recommendation remains challenging due to (1) inefficient to dynamically utilize user reviews under LLMs' constrained context windows, and (2) lacking effective mechanisms to prioritize reviews most relevant to the user's current decision context. To address these challenges, we propose RevBrowse, a review-driven recommendation framework inspired by the "browse-then-decide" decision process commonly observed in online user behavior. RevBrowse integrates user reviews into the LLM-based reranking process to enhance its ability to distinguish between candidate items. To improve the relevance and efficiency of review usage, we introduce PrefRAG, a retrieval-augmented module that disentangles user and item representations into structured forms and adaptively retrieves preference-relevant content conditioned on the target item. Extensive experiments on four Amazon review datasets demonstrate that RevBrowse achieves consistent and significant improvements over strong baselines, highlighting its generalizability and effectiveness in modeling dynamic user preferences. Furthermore, since the retrieval-augmented process is transparent, RevBrowse offers a certain level of interpretability by making visible which reviews influence the final recommendation.

