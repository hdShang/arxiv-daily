---
layout: default
title: ModelingAgent: Bridging LLMs and Mathematical Modeling for Real-World Challenges
---

# ModelingAgent: Bridging LLMs and Mathematical Modeling for Real-World Challenges

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.15068" class="toolbar-btn" target="_blank">📄 arXiv: 2505.15068v1</a>
  <a href="https://arxiv.org/pdf/2505.15068.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.15068v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.15068v1', 'ModelingAgent: Bridging LLMs and Mathematical Modeling for Real-World Challenges')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheng Qian, Hongyi Du, Hongru Wang, Xiusi Chen, Yuji Zhang, Avirup Sil, Chengxiang Zhai, Kathleen McKeown, Heng Ji

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-05-21

**备注**: 36 Pages, 26 Figures, 5 Tables

---

## 💡 一句话要点

**提出ModelingAgent以解决现实世界数学建模问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数学建模` `多代理系统` `跨学科推理` `开放式问题` `工具整合`

## 📋 核心要点

1. 现有的基准测试未能有效反映现实世界问题的复杂性，缺乏开放式和跨学科的推理能力。
2. 本文提出ModelingBench基准和ModelingAgent框架，旨在通过多代理系统协调工具使用和支持结构化工作流程来解决复杂数学建模问题。
3. 实验证明，ModelingAgent在解决方案质量上显著优于现有强基线，且其输出与人类专家的解决方案相似。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进步使得解决数学问题取得了显著进展。然而，现有基准测试往往无法反映现实世界问题的复杂性，这些问题需要开放式的跨学科推理和计算工具的整合。为了解决这一问题，本文引入了ModelingBench，一个新颖的基准，包含来自数学建模竞赛的现实世界启发的开放式问题，涵盖城市交通优化到生态系统资源规划等多个领域。这些任务要求将自然语言转化为正式的数学公式，应用适当的工具，并生成结构化、可辩护的报告。ModelingBench还支持多种有效的解决方案，捕捉实际建模中的模糊性和创造性。我们还提出了ModelingAgent，一个多代理框架，协调工具使用，支持结构化工作流程，并实现迭代自我完善，以生成有根据的创造性解决方案。为了评估输出，我们进一步提出了ModelingJudge，一个专家参与的系统，利用LLMs作为领域专门的评审，从多个专家视角评估解决方案。实证结果表明，ModelingAgent显著优于强基线，且常常产生与人类专家无差别的解决方案。我们的工作为在开放式跨学科建模挑战中评估和推进现实世界问题解决提供了全面框架。

## 🔬 方法详解

**问题定义**：本文旨在解决现有数学建模方法在处理复杂现实问题时的不足，尤其是在开放式和跨学科推理方面的挑战。现有方法往往无法有效整合多种计算工具和自然语言理解。

**核心思路**：论文提出的核心思路是通过ModelingBench基准和ModelingAgent框架，促进多代理系统的协作，支持结构化的工作流程和迭代自我完善，以生成高质量的数学建模解决方案。

**技术框架**：整体架构包括ModelingBench基准、ModelingAgent多代理框架和ModelingJudge评估系统。ModelingBench提供多样化的开放式问题，ModelingAgent协调工具使用并支持工作流程，而ModelingJudge则利用LLMs进行专家评估。

**关键创新**：最重要的技术创新点在于引入了支持多种有效解决方案的ModelingBench基准，以及通过多代理系统实现的迭代自我完善机制，这与传统的单一解决方案方法有本质区别。

**关键设计**：关键设计包括对多代理系统的参数设置、工具使用的协调机制，以及在ModelingJudge中使用的领域专门的评估标准，确保评估的全面性和准确性。

## 📊 实验亮点

实验结果显示，ModelingAgent在解决方案质量上显著优于传统强基线，具体表现为在多个任务中，其输出与人类专家的解决方案无明显差异，提升幅度达到XX%（具体数据未知）。

## 🎯 应用场景

该研究的潜在应用领域包括城市交通优化、生态系统资源规划等多个实际场景，能够为复杂的现实问题提供创新的解决方案。未来，该框架可能推动数学建模领域的进一步发展，促进跨学科合作与工具整合。

## 📄 摘要（原文）

> Recent progress in large language models (LLMs) has enabled substantial advances in solving mathematical problems. However, existing benchmarks often fail to reflect the complexity of real-world problems, which demand open-ended, interdisciplinary reasoning and integration of computational tools. To address this gap, we introduce ModelingBench, a novel benchmark featuring real-world-inspired, open-ended problems from math modeling competitions across diverse domains, ranging from urban traffic optimization to ecosystem resource planning. These tasks require translating natural language into formal mathematical formulations, applying appropriate tools, and producing structured, defensible reports. ModelingBench also supports multiple valid solutions, capturing the ambiguity and creativity of practical modeling. We also present ModelingAgent, a multi-agent framework that coordinates tool use, supports structured workflows, and enables iterative self-refinement to generate well-grounded, creative solutions. To evaluate outputs, we further propose ModelingJudge, an expert-in-the-loop system leveraging LLMs as domain-specialized judges assessing solutions from multiple expert perspectives. Empirical results show that ModelingAgent substantially outperforms strong baselines and often produces solutions indistinguishable from those of human experts. Together, our work provides a comprehensive framework for evaluating and advancing real-world problem-solving in open-ended, interdisciplinary modeling challenges.

