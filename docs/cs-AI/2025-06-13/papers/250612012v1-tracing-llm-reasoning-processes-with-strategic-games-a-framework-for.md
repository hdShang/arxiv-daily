---
layout: default
title: "Tracing LLM Reasoning Processes with Strategic Games: A Framework for Planning, Revision, and Resource-Constrained Decision Making"
---

# Tracing LLM Reasoning Processes with Strategic Games: A Framework for Planning, Revision, and Resource-Constrained Decision Making

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12012" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12012v1</a>
  <a href="https://arxiv.org/pdf/2506.12012.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12012v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12012v1', 'Tracing LLM Reasoning Processes with Strategic Games: A Framework for Planning, Revision, and Resource-Constrained Decision Making')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaopeng Yuan, Xingjian Zhang, Ke Xu, Yifan Xu, Lijun Yu, Jindong Wang, Yushun Dong, Haohan Wang

**分类**: cs.AI

**发布日期**: 2025-06-13

**备注**: 19 pages, 7 figures. Under review

---

## 💡 一句话要点

**提出战略游戏框架以评估LLM推理过程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理过程` `战略游戏` `评估框架` `资源约束决策` `修正成功率` `模型性能`

## 📋 核心要点

1. 现有方法主要关注LLMs的最终决策，缺乏对中间推理过程的深入分析，导致对模型行为的理解不足。
2. 本文提出了一个基于战略游戏的评估框架，旨在通过规划、修正和资源约束决策三个维度来全面评估LLMs的推理过程。
3. 实验结果显示，ChatGPT-o3-mini在4320轮对抗中取得了74.7%的胜率和78.6%的修正成功率，验证了该框架的有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在复杂推理任务中的应用日益增多，但现有基准主要关注最终结果，忽视了中间推理步骤，如规划、修正和资源约束下的决策。本文提出使用战略游戏作为评估环境，构建了一个评估框架，涵盖规划、修正和资源约束决策三个核心维度，并定义了超越胜率的评估指标。通过4320轮对抗实验，ChatGPT-o3-mini在多个指标上表现优异，显示出评估LLMs推理过程的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决对大型语言模型推理过程的评估不足，现有方法未能深入分析模型在决策过程中的中间步骤和行为表现。

**核心思路**：通过引入战略游戏作为评估环境，构建一个综合评估框架，关注模型在规划、修正和资源约束决策中的表现，强调中间推理过程的重要性。

**技术框架**：该框架包括三个主要模块：规划模块、修正模块和资源约束决策模块，利用清晰的状态和自动反馈机制来评估模型的推理过程。

**关键创新**：引入了超越胜率的多维度评估指标，如过度修正风险率、修正成功率、改进斜率和超预算比率，提供了更全面的模型性能评估视角。

**关键设计**：在实验中，设置了4320轮对抗测试，采用了多种模型进行比较，特别关注了资源使用情况与决策成功率之间的关系。

## 📊 实验亮点

实验结果显示，ChatGPT-o3-mini在4320轮对抗中获得74.7%的胜率和78.6%的修正成功率，改进斜率为0.041，表现优于其他模型，特别是Qwen-Plus的25.6%胜率和81.6%过度修正风险率，强调了评估推理过程的重要性。

## 🎯 应用场景

该研究的评估框架可广泛应用于大型语言模型的开发和优化，帮助研究人员理解模型的推理过程，从而提升模型的可靠性和决策能力。未来，该框架还可扩展到其他类型的智能系统，推动智能决策领域的发展。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used for tasks that require complex reasoning. Most benchmarks focus on final outcomes but overlook the intermediate reasoning steps - such as planning, revision, and decision making under resource constraints. We argue that measuring these internal processes is essential for understanding model behavior and improving reliability. We propose using strategic games as a natural evaluation environment: closed, rule-based systems with clear states, limited resources, and automatic feedback. We introduce a framework that evaluates LLMs along three core dimensions: planning, revision, and resource-constrained decision making. To operationalize this, we define metrics beyond win rate, including overcorrection risk rate, correction success rate, improvement slope, and over-budget ratio. In 4320 adversarial rounds across 12 leading models, ChatGPT-o3-mini achieves the top composite score, with a win rate of 74.7 percent, a correction success rate of 78.6 percent, and an improvement slope of 0.041. By contrast, Qwen-Plus, despite an overcorrection risk rate of 81.6 percent, wins only 25.6 percent of its matches - primarily due to excessive resource use. We also observe a negative correlation between overcorrection risk rate and correction success rate (Pearson r = -0.51, p = 0.093), suggesting that more frequent edits do not always improve outcomes. Our findings highlight the value of assessing not only what LLMs decide but how they arrive at those decisions

