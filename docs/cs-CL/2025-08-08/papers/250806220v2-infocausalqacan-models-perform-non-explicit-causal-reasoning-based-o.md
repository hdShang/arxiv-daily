---
layout: default
title: "InfoCausalQA:Can Models Perform Non-explicit Causal Reasoning Based on Infographic?"
---

# InfoCausalQA:Can Models Perform Non-explicit Causal Reasoning Based on Infographic?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06220" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06220v2</a>
  <a href="https://arxiv.org/pdf/2508.06220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06220v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06220v2', 'InfoCausalQA:Can Models Perform Non-explicit Causal Reasoning Based on Infographic?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keummin Ka, Junhyeong Park, Jaehyun Jeon, Youngjae Yu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-08 (更新: 2025-08-13)

**备注**: 14 pages, 9 figures

---

## 💡 一句话要点

**提出InfoCausalQA以评估基于信息图的因果推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `因果推理` `多模态学习` `视觉-语言模型` `信息图` `数据集构建` `语义理解` `人工智能评估`

## 📋 核心要点

1. 现有的视觉-语言模型在因果推理方面能力不足，尤其是在多模态环境中表现不佳。
2. 论文提出InfoCausalQA基准，通过信息图结合文本上下文，评估因果推理能力，包含定量和语义因果推理任务。
3. 实验结果表明，当前VLM在因果推理任务中的表现显著低于人类，显示出在信息图信息利用方面的巨大差距。

## 📝 摘要（中文）

近年来，视觉-语言模型（VLMs）在感知和推理方面取得了显著进展。然而，因果推理能力，作为人类认知的核心方面，仍然未得到充分探索，尤其是在多模态环境中。本研究介绍了InfoCausalQA，一个新颖的基准，旨在评估基于信息图的因果推理能力。该基准包括两个任务：任务一关注基于推断的数值趋势进行定量因果推理，任务二则涉及五种因果关系的语义因果推理。我们从四个公共来源手动收集了494对信息图-文本，并使用GPT-4o生成了1482个高质量的多项选择问答对。这些问题经过人工仔细修订，确保不能仅通过表面线索回答，而需要真正的视觉基础。实验结果显示，当前的VLM在计算推理方面能力有限，语义因果推理的局限性更为明显，表明在利用基于信息图的信息进行因果推理方面存在显著差距。通过InfoCausalQA，我们强调了提升多模态AI系统因果推理能力的必要性。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有视觉-语言模型在因果推理能力不足的问题，尤其是在多模态环境中，缺乏有效的评估标准和基准。

**核心思路**：论文的核心思路是通过设计InfoCausalQA基准，结合信息图和文本，创建一个能够评估因果推理能力的框架，强调视觉基础的重要性。

**技术框架**：整体架构包括两个主要任务：任务一进行定量因果推理，任务二进行语义因果推理。数据集由494对信息图-文本对和1482个多项选择问答对组成，确保问题需要深层次的视觉理解。

**关键创新**：最重要的技术创新点在于通过信息图结合文本的方式，创建了一个新的因果推理评估基准，填补了现有方法在多模态因果推理评估中的空白。

**关键设计**：在数据集构建中，采用GPT-4o生成问答对，并经过人工修订，确保问题的复杂性和深度，避免仅依赖表面线索进行回答。实验设计中注重对比分析，评估VLM与人类在因果推理任务中的表现差异。

## 📊 实验亮点

实验结果显示，当前的视觉-语言模型在定量因果推理任务中的表现仅为人类的X%，而在语义因果推理任务中更是低于Y%。这些结果表明，现有模型在处理复杂因果关系时存在显著不足，强调了进一步研究的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、数据可视化和人机交互等。通过提升多模态AI系统的因果推理能力，可以更好地理解复杂信息，支持决策制定和知识传播，未来可能对智能助手和自动化分析工具产生深远影响。

## 📄 摘要（原文）

> Recent advances in Vision-Language Models (VLMs) have demonstrated impressive capabilities in perception and reasoning. However, the ability to perform causal inference -- a core aspect of human cognition -- remains underexplored, particularly in multimodal settings. In this study, we introduce InfoCausalQA, a novel benchmark designed to evaluate causal reasoning grounded in infographics that combine structured visual data with textual context. The benchmark comprises two tasks: Task 1 focuses on quantitative causal reasoning based on inferred numerical trends, while Task 2 targets semantic causal reasoning involving five types of causal relations: cause, effect, intervention, counterfactual, and temporal. We manually collected 494 infographic-text pairs from four public sources and used GPT-4o to generate 1,482 high-quality multiple-choice QA pairs. These questions were then carefully revised by humans to ensure they cannot be answered based on surface-level cues alone but instead require genuine visual grounding. Our experimental results reveal that current VLMs exhibit limited capability in computational reasoning and even more pronounced limitations in semantic causal reasoning. Their significantly lower performance compared to humans indicates a substantial gap in leveraging infographic-based information for causal inference. Through InfoCausalQA, we highlight the need for advancing the causal reasoning abilities of multimodal AI systems.

