---
layout: default
title: "LogiPlan: A Structured Benchmark for Logical Planning and Relational Reasoning in LLMs"
---

# LogiPlan: A Structured Benchmark for Logical Planning and Relational Reasoning in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10527" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10527v1</a>
  <a href="https://arxiv.org/pdf/2506.10527.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10527v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10527v1', 'LogiPlan: A Structured Benchmark for Logical Planning and Relational Reasoning in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanan Cai, Ahmed Salem, Besmira Nushi, Mark Russinovich

**分类**: cs.AI, cs.PF

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出LogiPlan以评估大语言模型在逻辑规划中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `逻辑规划` `关系推理` `大语言模型` `评估基准` `自我纠正能力` `复杂任务` `推理能力`

## 📋 核心要点

1. 现有方法在处理复杂关系结构时，缺乏有效的评估基准，导致逻辑推理能力的评估不够全面。
2. LogiPlan通过动态调整任务复杂性，设计了三个互补任务，全面评估LLMs在逻辑规划和关系推理中的表现。
3. 实验结果显示，尽管一些增强推理能力的模型在简单实例上表现良好，但在更复杂的配置中仍面临挑战。

## 📝 摘要（中文）

我们介绍了LogiPlan，这是一个新颖的基准，旨在评估大语言模型（LLMs）在复杂关系结构上的逻辑规划和推理能力。逻辑关系推理对于依赖LLMs生成和查询结构化关系图的应用至关重要，如网络基础设施、知识库或业务流程模式。我们的框架通过控制对象数量、关系和关系链的最小深度，动态变化任务复杂性，从而提供对模型性能的细致评估。LogiPlan包含三个互补任务：计划生成、一致性检测和比较问题。此外，我们还评估了模型的自我纠正能力，要求它们验证和完善初始解决方案。我们对多种最先进模型进行了评估，揭示了与模型规模和架构相关的显著性能差距。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有大语言模型在逻辑规划和关系推理能力评估中的不足，尤其是在处理复杂关系结构时的性能差距。现有方法缺乏系统性和动态性，无法全面评估模型的推理能力。

**核心思路**：LogiPlan的核心思路是通过设计三个互补的任务来评估模型的逻辑规划能力，允许动态调整任务的复杂性，以便更细致地分析模型在不同难度下的表现。

**技术框架**：LogiPlan的整体架构包括三个主要模块：计划生成、检测一致性和比较问题。每个模块针对不同的逻辑推理能力进行评估，并通过控制任务的复杂性来实现细致的性能分析。

**关键创新**：LogiPlan的主要创新在于其动态复杂性调整机制和三个互补任务的设计，使得模型在逻辑推理能力的评估上更加全面和细致。这与现有方法的静态评估方式形成了鲜明对比。

**关键设计**：在关键设计上，LogiPlan允许用户设置对象数量、关系种类和关系链的深度等参数，以便于生成不同复杂度的任务。此外，模型的自我纠正能力也被纳入评估，进一步提升了评估的全面性。

## 📊 实验亮点

实验结果表明，尽管一些最新的推理增强模型在简单任务上表现良好，但在复杂任务中存在显著性能差距。例如，GPT-4.5和Llama 3.1在复杂配置下的表现明显低于预期，显示出逻辑规划能力的不足。

## 🎯 应用场景

LogiPlan的研究成果在多个领域具有潜在应用价值，包括智能问答系统、知识图谱构建和业务流程优化等。通过提升大语言模型在逻辑推理和关系推理方面的能力，能够更好地支持复杂决策和信息检索任务，推动人工智能在实际应用中的发展。

## 📄 摘要（原文）

> We introduce LogiPlan, a novel benchmark designed to evaluate the capabilities of large language models (LLMs) in logical planning and reasoning over complex relational structures. Logical relational reasoning is important for applications that may rely on LLMs to generate and query structured graphs of relations such as network infrastructure, knowledge bases, or business process schema. Our framework allows for dynamic variation of task complexity by controlling the number of objects, relations, and the minimum depth of relational chains, providing a fine-grained assessment of model performance across difficulty levels. LogiPlan encompasses three complementary tasks: (1) Plan Generation, where models must construct valid directed relational graphs meeting specified structural constraints; (2) Consistency Detection, testing models' ability to identify inconsistencies in relational structures; and (3) Comparison Question, evaluating models' capacity to determine the validity of queried relationships within a given graph. Additionally, we assess models' self-correction capabilities by prompting them to verify and refine their initial solutions. We evaluate state-of-the-art models including DeepSeek R1, Gemini 2.0 Pro, Gemini 2 Flash Thinking, GPT-4.5, GPT-4o, Llama 3.1 405B, O3-mini, O1, and Claude 3.7 Sonnet across these tasks, revealing significant performance gaps that correlate with model scale and architecture. Our analysis demonstrates that while recent reasoning-enhanced models show promising results on simpler instances, they struggle with more complex configurations requiring deeper logical planning.

