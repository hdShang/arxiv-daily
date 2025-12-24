---
layout: default
title: "BrowseMaster: Towards Scalable Web Browsing via Tool-Augmented Programmatic Agent Pair"
---

# BrowseMaster: Towards Scalable Web Browsing via Tool-Augmented Programmatic Agent Pair

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09129" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09129v1</a>
  <a href="https://arxiv.org/pdf/2508.09129.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09129v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09129v1', 'BrowseMaster: Towards Scalable Web Browsing via Tool-Augmented Programmatic Agent Pair')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianghe Pang, Shuo Tang, Rui Ye, Yuwen Du, Yaxin Du, Siheng Chen

**分类**: cs.AI

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出BrowseMaster以解决大规模网络浏览中的信息检索与推理平衡问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `信息检索` `大型语言模型` `推理能力` `程序增强` `智能代理`

## 📋 核心要点

1. 现有的LLM代理在信息检索中面临搜索广度和推理深度的平衡问题，导致性能受限。
2. BrowseMaster通过规划-执行代理对的设计，优化搜索策略和信息检索过程，提升了信息获取效率。
3. 在英语和中文的基准测试中，BrowseMaster的表现超越了多个开源和专有基线，显示出其强大的信息检索能力。

## 📝 摘要（中文）

在信息日益增长的数字环境中，有效的信息检索需要在广泛搜索与战略推理之间取得平衡。现有的大型语言模型（LLM）代理在搜索广度和推理深度上存在局限，导致慢速的串行查询限制了相关信息源的覆盖，而嘈杂的原始输入又干扰了多步推理的连续性。为了解决这些挑战，本文提出了BrowseMaster，一个基于程序增强的规划-执行代理对的可扩展框架。规划者根据任务约束制定和调整搜索策略，而执行者则进行高效、针对性的检索，为规划者提供简洁、相关的证据。这种分工保持了连贯的长远推理，同时支持广泛和系统的探索，克服了现有代理的局限。大量实验表明，BrowseMaster在复杂的推理密集型信息检索任务中表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM代理在信息检索中面临的搜索广度不足和推理深度不够的问题，尤其是在复杂任务中表现不佳。

**核心思路**：BrowseMaster通过引入一个程序增强的规划-执行代理对，优化了信息检索过程。规划者负责制定搜索策略，而执行者则专注于高效检索，从而实现了信息获取的高效性和推理的连贯性。

**技术框架**：BrowseMaster的整体架构包括两个主要模块：规划者和执行者。规划者根据任务需求动态调整搜索策略，执行者则进行针对性的检索，确保提供相关证据。

**关键创新**：该框架的核心创新在于将规划与执行分离，使得信息检索过程更加高效，克服了现有方法在推理和搜索之间的权衡。

**关键设计**：在设计中，规划者使用特定的算法来生成搜索策略，执行者则采用优化的检索算法，确保快速获取相关信息。

## 📊 实验亮点

在大量实验中，BrowseMaster在BrowseComp-en和BrowseComp-zh基准测试中分别取得了30.0和46.5的得分，显著超越了现有的开源和专有基线，展示了其在复杂推理任务中的卓越性能。

## 🎯 应用场景

BrowseMaster的研究成果在多个领域具有潜在应用价值，包括智能搜索引擎、虚拟助手和信息检索系统等。其高效的信息获取能力能够提升用户在复杂任务中的信息处理效率，未来可能对知识管理和决策支持系统产生深远影响。

## 📄 摘要（原文）

> Effective information seeking in the vast and ever-growing digital landscape requires balancing expansive search with strategic reasoning. Current large language model (LLM)-based agents struggle to achieve this balance due to limitations in search breadth and reasoning depth, where slow, serial querying restricts coverage of relevant sources and noisy raw inputs disrupt the continuity of multi-step reasoning. To address these challenges, we propose BrowseMaster, a scalable framework built around a programmatically augmented planner-executor agent pair. The planner formulates and adapts search strategies based on task constraints, while the executor conducts efficient, targeted retrieval to supply the planner with concise, relevant evidence. This division of labor preserves coherent, long-horizon reasoning while sustaining broad and systematic exploration, overcoming the trade-off that limits existing agents. Extensive experiments on challenging English and Chinese benchmarks show that BrowseMaster consistently outperforms open-source and proprietary baselines, achieving scores of 30.0 on BrowseComp-en and 46.5 on BrowseComp-zh, which demonstrates its strong capability in complex, reasoning-heavy information-seeking tasks at scale.

