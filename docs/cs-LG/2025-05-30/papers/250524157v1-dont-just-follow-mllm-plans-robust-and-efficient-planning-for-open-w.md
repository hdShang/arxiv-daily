---
layout: default
title: Don't Just Follow MLLM Plans: Robust and Efficient Planning for Open-world Agents
---

# Don't Just Follow MLLM Plans: Robust and Efficient Planning for Open-world Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24157" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24157v1</a>
  <a href="https://arxiv.org/pdf/2505.24157.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24157v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24157v1', 'Don\'t Just Follow MLLM Plans: Robust and Efficient Planning for Open-world Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seungjoon Lee, Suhwan Kim, Minhyeon Oh, Youngsik Yoon, Jungseul Ok

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出REPOA框架以解决开放世界智能体的规划效率与鲁棒性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `开放世界智能体` `规划效率` `鲁棒性` `自适应学习` `失败感知` `基于难度的探索` `大型语言模型` `复杂任务`

## 📋 核心要点

1. 现有方法在规划中依赖不准确的知识或不切实际的环境假设，导致智能体在复杂任务中的表现不佳。
2. REPOA框架通过自适应依赖学习和失败感知操作记忆来增强鲁棒性，同时采用基于难度的探索策略提高学习效率。
3. 在两个开放世界测试平台上的评估结果显示，REPOA在获取挑战性物品方面表现优于以往方法，展现出更强的规划能力。

## 📝 摘要（中文）

开发能够在不可预测的交互环境中掌握复杂多步骤任务的自主智能体面临重大挑战。尽管大型语言模型（LLMs）在规划方面展现出潜力，但现有方法往往依赖于有问题的内部知识或不切实际的环境假设。本文提出了鲁棒且高效的开放世界智能体规划框架（REPOA），通过自适应依赖学习、细粒度失败感知操作记忆和基于难度的探索，显著提升了规划的鲁棒性和效率。实验结果表明，REPOA在两个开放世界测试平台上表现出色，成功获取了以往方法无法达到的挑战性游戏后期物品。

## 🔬 方法详解

**问题定义**：本文旨在解决开放世界智能体在复杂任务中规划的鲁棒性与效率问题。现有方法往往依赖于不准确的知识或不切实际的假设，导致智能体在真实环境中的表现不理想。

**核心思路**：REPOA框架的核心思路是通过自适应学习和失败感知机制来增强智能体对知识不准确性的鲁棒性，同时通过难度驱动的探索策略提高学习效率。这样的设计使得智能体能够在真实环境中更有效地学习规划知识。

**技术框架**：REPOA的整体架构包括三个主要模块：自适应依赖学习模块、细粒度失败感知操作记忆模块和基于难度的探索模块。自适应依赖学习模块负责识别和调整知识依赖关系，失败感知操作记忆模块则记录和分析失败案例以优化决策，而基于难度的探索模块则引导智能体在学习过程中选择更具挑战性的任务。

**关键创新**：REPOA的关键创新在于其结合了自适应依赖学习与失败感知机制，显著提高了智能体在面对不准确知识时的鲁棒性。这一设计与传统方法的主要区别在于不再依赖外部知识，而是通过内部学习来获取规划知识。

**关键设计**：在参数设置上，REPOA采用了动态调整的学习率和探索策略，以适应不同任务的复杂性。此外，损失函数设计上考虑了失败案例的权重，使得智能体在学习过程中更关注于改进其弱点。

## 📊 实验亮点

在两个开放世界测试平台上的实验结果显示，REPOA在获取挑战性游戏后期物品方面的成功率显著高于以往方法，表现出更强的鲁棒性和效率。这一成果表明，REPOA能够有效应对复杂环境中的规划挑战。

## 🎯 应用场景

REPOA框架具有广泛的应用潜力，特别是在需要自主决策的领域，如机器人导航、游戏AI和智能家居系统。其高效的学习能力和鲁棒性使得智能体能够在复杂和动态的环境中表现出色，未来可能推动自主智能体在实际应用中的普及与发展。

## 📄 摘要（原文）

> Developing autonomous agents capable of mastering complex, multi-step tasks in unpredictable, interactive environments presents a significant challenge. While Large Language Models (LLMs) offer promise for planning, existing approaches often rely on problematic internal knowledge or make unrealistic environmental assumptions. Although recent work explores learning planning knowledge, they still retain limitations due to partial reliance on external knowledge or impractical setups. Indeed, prior research has largely overlooked developing agents capable of acquiring planning knowledge from scratch, directly in realistic settings. While realizing this capability is necessary, it presents significant challenges, primarily achieving robustness given the substantial risk of incorporating LLMs' inaccurate knowledge. Moreover, efficiency is crucial for practicality as learning can demand prohibitive exploration. In response, we introduce Robust and Efficient Planning for Open-world Agents (REPOA), a novel framework designed to tackle these issues. REPOA features three key components: adaptive dependency learning and fine-grained failure-aware operation memory to enhance robustness to knowledge inaccuracies, and difficulty-based exploration to improve learning efficiency. Our evaluation in two established open-world testbeds demonstrates REPOA's robust and efficient planning, showcasing its capability to successfully obtain challenging late-game items that were beyond the reach of prior approaches.

