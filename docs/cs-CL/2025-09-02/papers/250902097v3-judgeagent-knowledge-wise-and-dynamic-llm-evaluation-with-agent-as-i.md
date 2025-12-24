---
layout: default
title: "JudgeAgent: Knowledge-wise and Dynamic LLM Evaluation with Agent-as-Interviewer"
---

# JudgeAgent: Knowledge-wise and Dynamic LLM Evaluation with Agent-as-Interviewer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02097" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02097v3</a>
  <a href="https://arxiv.org/pdf/2509.02097.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02097v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02097v3', 'JudgeAgent: Knowledge-wise and Dynamic LLM Evaluation with Agent-as-Interviewer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhichao Shi, Xuhui Jiang, Chengjin Xu, Cangli Yao, Zhenxin Huang, Shengjie Ma, Yinghan Shen, Jian Guo, Yuanzhuo Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-02 (更新: 2025-09-26)

**🔗 代码/项目**: [GITHUB](https://github.com/DataArcTech/JudgeAgent)

---

## 💡 一句话要点

**提出JudgeAgent，利用Agent-as-Interviewer进行知识驱动的LLM动态评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型评估` `动态评估` `Agent-as-Interviewer` `知识驱动` `难度控制` `多轮交互` `LLM优化`

## 📋 核心要点

1. 现有LLM评估方法存在高估、偏差和难度不匹配等问题，无法全面评估LLM的知识边界和能力。
2. Agent-as-Interviewer范式利用LLM Agent进行多轮交互，调用知识工具生成问题，并调整问题难度，实现动态评估。
3. JudgeAgent框架基于Agent-as-Interviewer，通过知识驱动的综合和难度评分，为LLM提供优化建议，实验验证了其有效性。

## 📝 摘要（中文）

当前大型语言模型(LLM)的评估范式存在高估、偏差以及问题难度不匹配等问题，导致对知识和能力边界的评估不完整，阻碍了其有效应用和优化。为了解决这些挑战，我们提出Agent-as-Interviewer，一种动态评估范式，它使用LLM Agent进行多轮交互以进行评估。与当前的基准测试或动态交互范式不同，Agent-as-Interviewer利用Agent调用知识工具，在动态多轮问题生成中获得更广泛和更深入的知识，从而实现对LLM知识边界的更全面评估。它还利用Agent来规划查询策略，以调整问题难度级别，从而增强难度控制以匹配目标LLM的实际能力。基于此范式，我们开发了JudgeAgent，一个知识驱动的动态评估框架，它采用知识驱动的综合作为Agent的工具，并使用难度评分作为策略指导，从而最终提供有价值的建议来帮助目标优化自身。大量的实验验证了JudgeAgent建议的有效性，表明Agent-as-Interviewer可以准确识别目标模型的知识和能力边界。

## 🔬 方法详解

**问题定义**：现有LLM评估方法存在局限性，例如静态基准测试难以覆盖LLM的全部知识范围，动态交互式评估可能存在偏差或难度不匹配，导致无法准确评估LLM的知识边界和能力上限。这些问题阻碍了LLM的有效应用和优化。

**核心思路**：论文的核心思路是利用LLM Agent模拟面试官，通过多轮交互动态地评估目标LLM。Agent可以调用外部知识工具来扩展问题范围，并根据目标LLM的回答调整问题难度，从而更全面、准确地评估其知识和能力。这种动态评估方式能够克服传统评估方法的局限性。

**技术框架**：JudgeAgent框架包含以下主要模块：1) **问题生成模块**：Agent根据已有的知识和目标LLM的回答，利用知识工具生成新的问题。2) **难度评估模块**：评估生成问题的难度，并根据目标LLM的能力水平进行调整。3) **回答评估模块**：评估目标LLM的回答质量，并给出反馈。4) **优化建议模块**：根据评估结果，为目标LLM提供优化建议。整个流程是一个迭代的过程，Agent不断生成问题、评估回答、调整难度，最终达到全面评估目标LLM的目的。

**关键创新**：论文的关键创新在于提出了Agent-as-Interviewer的动态评估范式。与传统的静态评估方法相比，Agent-as-Interviewer能够根据目标LLM的实际能力动态调整问题难度，从而更准确地评估其知识边界。此外，Agent还可以调用外部知识工具来扩展问题范围，从而更全面地评估LLM的知识覆盖面。

**关键设计**：JudgeAgent使用知识驱动的综合作为Agent的工具，具体实现方式未知。难度评分是策略指导的关键，具体评分标准和算法未知。论文中提到会提供优化建议，但具体建议生成方式未知。

## 📊 实验亮点

论文通过实验验证了JudgeAgent的有效性，表明Agent-as-Interviewer能够准确识别目标模型的知识和能力边界。具体性能数据、对比基线和提升幅度未知，但实验结果表明JudgeAgent提供的优化建议能够帮助目标LLM提升性能。

## 🎯 应用场景

该研究成果可应用于LLM的开发、测试和优化。开发者可以使用JudgeAgent评估LLM的性能，发现其知识盲区和能力瓶颈，并据此进行改进。此外，该方法还可以用于比较不同LLM的性能，为用户选择合适的LLM提供参考。未来，该方法有望推广到其他类型的人工智能系统评估中。

## 📄 摘要（原文）

> Current evaluation paradigms for large language models (LLMs) suffer from overestimated or biased evaluations and mismatched question difficulty, leading to incomplete evaluations of knowledge and capability boundaries, which hinder their effective application and optimization. To address these challenges, we propose Agent-as-Interviewer, a dynamic evaluation paradigm that employs LLM agents to conduct multi-turn interactions for evaluation. Unlike current benchmarking or dynamic interaction paradigms, Agent-as-Interviewer utilizes agents to invoke knowledge tools for wider and deeper knowledge in the dynamic multi-turn question generation, achieving more comprehensive evaluations of LLM's knowledge boundaries. It also leverages agents to plan query strategies for adjustment of the question difficulty levels, enhancing the difficulty control to match the actual capabilities of target LLMs. Based on this paradigm, we develop JudgeAgent, a knowledge-wise dynamic evaluation framework that employs knowledge-driven synthesis as the agent's tool and uses difficulty scoring as strategy guidance, thereby finally providing valuable suggestions to help targets optimize themselves. Extensive experiments validate the effectiveness of JudgeAgent's suggestions, demonstrating that Agent-as-Interviewer can accurately identify the knowledge and capability boundaries of target models. The source code is available on https://github.com/DataArcTech/JudgeAgent.

