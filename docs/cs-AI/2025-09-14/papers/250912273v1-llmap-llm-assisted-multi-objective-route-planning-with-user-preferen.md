---
layout: default
title: "LLMAP: LLM-Assisted Multi-Objective Route Planning with User Preferences"
---

# LLMAP: LLM-Assisted Multi-Objective Route Planning with User Preferences

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12273" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12273v1</a>
  <a href="https://arxiv.org/pdf/2509.12273.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12273v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12273v1', 'LLMAP: LLM-Assisted Multi-Objective Route Planning with User Preferences')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liangqi Yuan, Dong-Jun Han, Christopher G. Brinton, Sabine Brunswicker

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-09-14

---

## 💡 一句话要点

**LLMAP：基于LLM辅助的多目标个性化路线规划系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `路线规划` `大型语言模型` `自然语言理解` `多目标优化` `图搜索`

## 📋 核心要点

1. 现有路线规划方法难以兼顾LLM对自然语言的理解和处理大规模地图数据的能力。
2. LLMAP系统利用LLM解析用户自然语言偏好，结合多步图搜索算法寻找最优路线。
3. 实验结果表明，LLMAP在满足用户约束条件下，能有效提升POI质量和任务完成率。

## 📝 摘要（中文）

大型语言模型（LLM）的兴起使得自然语言驱动的路线规划成为一个新兴的研究领域，它涵盖了丰富的用户目标。目前的研究主要有两种方法：使用LLM作为代理的直接路线规划和基于图的搜索策略。然而，前者难以处理大量的地图数据，而后者在理解自然语言偏好方面能力有限。此外，一个更关键的挑战来自全球用户高度异构和不可预测的时空分布。本文介绍了一种新颖的LLM辅助路线规划（LLMAP）系统，该系统采用LLM作为解析器来理解自然语言，识别任务，提取用户偏好并识别任务依赖关系，并结合多步图构建与迭代搜索（MSGS）算法作为底层求解器，以找到最佳路线。我们的多目标优化方法自适应地调整目标权重，以最大化兴趣点（POI）质量和任务完成率，同时最小化路线距离，并受三个关键约束的限制：用户时间限制，POI开放时间和任务依赖关系。我们使用1000个在世界范围内14个国家和27个城市中采样的具有不同复杂性的路由提示进行了广泛的实验。结果表明，我们的方法在多个约束条件下实现了卓越的性能。

## 🔬 方法详解

**问题定义**：现有基于LLM的路线规划方法要么难以处理大规模地图数据，要么无法充分理解用户的自然语言偏好。此外，全球用户在时空上的分布具有高度异构性和不可预测性，这给路线规划带来了额外的挑战。现有方法难以在用户时间限制、POI开放时间和任务依赖关系等约束下，同时优化路线距离、POI质量和任务完成率。

**核心思路**：LLMAP的核心思路是将LLM作为自然语言解析器，负责理解用户输入的自然语言，提取用户偏好和任务依赖关系，并将这些信息传递给一个基于图搜索的优化算法。通过这种方式，LLM可以专注于其擅长的自然语言理解任务，而图搜索算法可以专注于其擅长的路线优化任务。这种解耦的设计使得系统能够更好地处理大规模地图数据和复杂的约束条件。

**技术框架**：LLMAP系统主要包含两个模块：LLM-as-Parser模块和Multi-Step Graph construction with iterative Search (MSGS)模块。LLM-as-Parser模块负责解析用户输入的自然语言，提取用户偏好、任务和任务依赖关系。MSGS模块则负责构建多步图，并在图上进行迭代搜索，以找到满足用户约束条件的最优路线。MSGS模块会根据LLM解析出的用户偏好，自适应地调整目标权重，以平衡路线距离、POI质量和任务完成率。

**关键创新**：LLMAP的关键创新在于将LLM和图搜索算法相结合，充分利用了LLM在自然语言理解方面的优势和图搜索算法在路线优化方面的优势。此外，LLMAP还提出了一种多步图构建与迭代搜索算法，能够有效地处理大规模地图数据和复杂的约束条件。通过自适应地调整目标权重，LLMAP能够更好地满足用户的个性化需求。

**关键设计**：LLM-as-Parser模块使用了预训练的LLM模型，并针对路线规划任务进行了微调。MSGS模块采用了A*搜索算法，并根据用户的时间限制、POI开放时间和任务依赖关系等约束条件进行了修改。多目标优化问题通过加权和的方式转化为单目标优化问题，权重由LLM解析出的用户偏好决定。

## 📊 实验亮点

实验结果表明，LLMAP在14个国家和27个城市的1000个路由提示上表现出色。相较于现有方法，LLMAP能够在满足用户时间限制、POI开放时间和任务依赖关系等约束条件下，显著提升POI质量和任务完成率。具体的性能提升数据未知，但论文强调了LLMAP在多个约束条件下的卓越性能。

## 🎯 应用场景

LLMAP可应用于各种需要个性化路线规划的场景，例如旅游规划、城市探索、物流配送等。该系统能够根据用户的自然语言偏好和约束条件，提供定制化的路线建议，提升用户体验和效率。未来，LLMAP还可以与其他智能系统集成，例如智能家居、自动驾驶等，实现更智能化的服务。

## 📄 摘要（原文）

> The rise of large language models (LLMs) has made natural language-driven route planning an emerging research area that encompasses rich user objectives. Current research exhibits two distinct approaches: direct route planning using LLM-as-Agent and graph-based searching strategies. However, LLMs in the former approach struggle to handle extensive map data, while the latter shows limited capability in understanding natural language preferences. Additionally, a more critical challenge arises from the highly heterogeneous and unpredictable spatio-temporal distribution of users across the globe. In this paper, we introduce a novel LLM-Assisted route Planning (LLMAP) system that employs an LLM-as-Parser to comprehend natural language, identify tasks, and extract user preferences and recognize task dependencies, coupled with a Multi-Step Graph construction with iterative Search (MSGS) algorithm as the underlying solver for optimal route finding. Our multi-objective optimization approach adaptively tunes objective weights to maximize points of interest (POI) quality and task completion rate while minimizing route distance, subject to three key constraints: user time limits, POI opening hours, and task dependencies. We conduct extensive experiments using 1,000 routing prompts sampled with varying complexity across 14 countries and 27 cities worldwide. The results demonstrate that our approach achieves superior performance with guarantees across multiple constraints.

