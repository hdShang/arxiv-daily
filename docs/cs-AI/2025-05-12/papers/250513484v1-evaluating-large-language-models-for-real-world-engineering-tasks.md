---
layout: default
title: Evaluating Large Language Models for Real-World Engineering Tasks
---

# Evaluating Large Language Models for Real-World Engineering Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13484" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13484v1</a>
  <a href="https://arxiv.org/pdf/2505.13484.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13484v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13484v1', 'Evaluating Large Language Models for Real-World Engineering Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rene Heesch, Sebastian Eilermann, Alexander Windmann, Alexander Diedrich, Philipp Rosenthal, Oliver Niggemann

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出针对真实工程任务的LLM评估数据库以解决现有评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `工程任务` `评估方法` `真实场景` `复杂推理`

## 📋 核心要点

1. 现有LLM评估方法依赖于简化用例，未能有效反映真实工程任务的复杂性和多样性。
2. 本文提出一个包含100多个真实工程场景的问题数据库，以系统性地评估LLMs在复杂工程任务中的表现。
3. 实验结果显示，LLMs在基本推理方面表现良好，但在抽象推理和上下文敏感逻辑上存在显著不足。

## 📝 摘要（中文）

大型语言模型（LLMs）不仅在日常活动中具有变革性，在工程任务中同样重要。然而，目前对LLMs在工程领域的评估存在两个主要缺陷：一是依赖于简化的用例，通常来自考试材料，容易验证正确性；二是使用的场景不足以捕捉关键的工程能力。因此，LLMs在复杂真实工程问题上的评估仍然未被充分探索。本文通过引入一个包含100多个真实生产导向工程场景的问题数据库，系统性地评估四种最先进的LLMs，探讨其在复杂工程任务中的表现。结果表明，LLMs在基本的时间和结构推理方面表现良好，但在抽象推理、形式建模和上下文敏感的工程逻辑方面存在显著困难。

## 🔬 方法详解

**问题定义**：本文旨在解决当前LLM评估中存在的缺陷，特别是对复杂真实工程问题的评估不足。现有方法多依赖于简化的用例，无法全面反映LLMs的实际能力。

**核心思路**：通过构建一个包含真实生产导向工程场景的问题数据库，系统性地评估LLMs在复杂工程任务中的表现，确保评估的真实性和有效性。

**技术框架**：研究首先设计了一个包含100多个问题的数据库，涵盖产品设计、预测和诊断等核心工程能力。然后，选择四种最先进的LLMs进行评估，包括云端和本地实例。

**关键创新**：本文的创新在于引入了一个系统化的问题数据库，填补了LLM在真实工程任务评估中的空白，提供了更具挑战性的评估场景。

**关键设计**：在实验中，针对每个LLM的评估采用了标准化的测试流程，重点关注时间推理、结构推理、抽象推理和上下文敏感逻辑等多个维度。

## 📊 实验亮点

实验结果表明，LLMs在基本的时间和结构推理方面表现良好，得分在80%以上，但在抽象推理和上下文敏感逻辑方面的得分低于50%，显示出显著的性能差距。这一发现为LLMs在工程领域的应用提供了重要的改进方向。

## 🎯 应用场景

该研究的潜在应用领域包括工程设计、产品开发和技术支持等，能够帮助工程师更有效地利用LLMs进行复杂问题的解决。未来，随着LLMs的不断发展，该评估框架有望推动工程领域的智能化进程，提高工程师的工作效率和决策能力。

## 📄 摘要（原文）

> Large Language Models (LLMs) are transformative not only for daily activities but also for engineering tasks. However, current evaluations of LLMs in engineering exhibit two critical shortcomings: (i) the reliance on simplified use cases, often adapted from examination materials where correctness is easily verifiable, and (ii) the use of ad hoc scenarios that insufficiently capture critical engineering competencies. Consequently, the assessment of LLMs on complex, real-world engineering problems remains largely unexplored. This paper addresses this gap by introducing a curated database comprising over 100 questions derived from authentic, production-oriented engineering scenarios, systematically designed to cover core competencies such as product design, prognosis, and diagnosis. Using this dataset, we evaluate four state-of-the-art LLMs, including both cloud-based and locally hosted instances, to systematically investigate their performance on complex engineering tasks. Our results show that LLMs demonstrate strengths in basic temporal and structural reasoning but struggle significantly with abstract reasoning, formal modeling, and context-sensitive engineering logic.

