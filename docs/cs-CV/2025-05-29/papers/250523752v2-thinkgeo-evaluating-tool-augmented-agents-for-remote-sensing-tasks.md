---
layout: default
title: "ThinkGeo: Evaluating Tool-Augmented Agents for Remote Sensing Tasks"
---

# ThinkGeo: Evaluating Tool-Augmented Agents for Remote Sensing Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23752" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23752v2</a>
  <a href="https://arxiv.org/pdf/2505.23752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23752v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23752v2', 'ThinkGeo: Evaluating Tool-Augmented Agents for Remote Sensing Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Akashah Shabbir, Muhammad Akhtar Munir, Akshay Dudhane, Muhammad Umer Sheikh, Muhammad Haris Khan, Paolo Fraccaro, Juan Bernabe Moreno, Fahad Shahbaz Khan, Salman Khan

**分类**: cs.CV

**发布日期**: 2025-05-29 (更新: 2025-10-09)

---

## 💡 一句话要点

**提出ThinkGeo以评估工具增强代理在遥感任务中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感` `工具增强` `大型语言模型` `空间推理` `多步骤规划` `评估基准` `人工智能` `数据分析`

## 📋 核心要点

1. 现有的评估方法主要集中在通用或多模态场景，缺乏针对遥感任务的专门基准，导致工具使用能力的评估不足。
2. 论文提出ThinkGeo基准，设计用于评估LLM驱动的代理在遥感任务中通过结构化工具使用和多步骤规划的能力。
3. 在486个结构化任务中进行评估，结果显示不同模型在工具准确性和规划一致性方面存在显著差异，提供了新的评估视角。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的进步，工具增强代理能够通过逐步推理解决复杂的现实任务。然而，现有评估往往集中于通用或多模态场景，缺乏针对遥感领域的特定基准。本文提出ThinkGeo，一个旨在通过结构化工具使用和多步骤规划评估LLM驱动代理在遥感任务中的表现的基准。ThinkGeo涵盖了城市规划、灾害评估、环境监测等多种实际应用，基于卫星或航空影像，要求代理通过多样的工具集进行推理。我们在486个结构化任务上评估了多种LLM，结果显示模型在工具准确性和规划一致性方面存在显著差异。ThinkGeo为评估工具增强LLM在遥感中的空间推理能力提供了首个广泛的测试平台。

## 🔬 方法详解

**问题定义**：本文旨在解决现有评估方法在遥感领域的不足，特别是缺乏针对工具使用能力的专门基准。现有方法未能充分评估LLM在复杂遥感任务中的表现。

**核心思路**：论文的核心思路是构建ThinkGeo基准，通过结构化工具使用和多步骤规划来评估LLM驱动的代理在遥感任务中的能力。这种设计旨在填补现有评估的空白，提供更具针对性的测试。

**技术框架**：ThinkGeo的整体架构包括人类策划的查询，涵盖城市规划、灾害评估等多个应用场景。评估过程中，代理需要基于卫星或航空影像进行推理，并使用多样的工具集。

**关键创新**：最重要的技术创新点在于提供了一个专门针对遥感任务的评估基准，首次系统性地评估工具增强LLM在空间推理中的表现。这与现有方法的本质区别在于其专注于领域特定的应用场景。

**关键设计**：在实验中，使用了ReAct风格的交互循环，评估了多种开源和闭源的LLM（如GPT-4o和Qwen2.5），并在486个任务中进行了1,773个专家验证的推理步骤，报告了逐步执行指标和最终答案的正确性。实验设计确保了评估的全面性和准确性。

## 📊 实验亮点

实验结果显示，ThinkGeo在486个结构化任务中评估了多种LLM，揭示了模型在工具准确性和规划一致性方面的显著差异，为未来的研究提供了重要的基准数据和分析视角。

## 🎯 应用场景

该研究的潜在应用领域包括城市规划、环境监测、灾害评估等，能够为相关领域的决策提供数据支持和智能分析。未来，ThinkGeo可能推动遥感技术与人工智能的深度融合，提升遥感数据的利用效率和决策质量。

## 📄 摘要（原文）

> Recent progress in large language models (LLMs) has enabled tool-augmented agents capable of solving complex real-world tasks through step-by-step reasoning. However, existing evaluations often focus on general-purpose or multimodal scenarios, leaving a gap in domain-specific benchmarks that assess tool-use capabilities in complex remote sensing use cases. We present ThinkGeo, an agentic benchmark designed to evaluate LLM-driven agents on remote sensing tasks via structured tool use and multi-step planning. Inspired by tool-interaction paradigms, ThinkGeo includes human-curated queries spanning a wide range of real-world applications such as urban planning, disaster assessment and change analysis, environmental monitoring, transportation analysis, aviation monitoring, recreational infrastructure, and industrial site analysis. Queries are grounded in satellite or aerial imagery, including both optical RGB and SAR data, and require agents to reason through a diverse toolset. We implement a ReAct-style interaction loop and evaluate both open and closed-source LLMs (e.g., GPT-4o, Qwen2.5) on 486 structured agentic tasks with 1,773 expert-verified reasoning steps. The benchmark reports both step-wise execution metrics and final answer correctness. Our analysis reveals notable disparities in tool accuracy and planning consistency across models. ThinkGeo provides the first extensive testbed for evaluating how tool-enabled LLMs handle spatial reasoning in remote sensing.

