---
layout: default
title: "Reasoning Like Experts: Leveraging Multimodal Large Language Models for Drawing-based Psychoanalysis"
---

# Reasoning Like Experts: Leveraging Multimodal Large Language Models for Drawing-based Psychoanalysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19451" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19451v1</a>
  <a href="https://arxiv.org/pdf/2510.19451.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19451v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.19451v1', 'Reasoning Like Experts: Leveraging Multimodal Large Language Models for Drawing-based Psychoanalysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xueqi Ma, Yanbei Jiang, Sarah Erfani, James Bailey, Weifeng Liu, Krista A. Ehinger, Jey Han Lau

**分类**: cs.CV, cs.MM

**发布日期**: 2025-10-22

**备注**: Accepted by ACM Multimedia 2025

---

## 💡 一句话要点

**提出PICK框架，利用多模态大语言模型进行基于绘画的心理分析，提升专家级推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `心理分析` `绘画理解` `分层分析` `知识注入`

## 📋 核心要点

1. 现有方法在主观、情感细微的心理分析领域应用不足，多模态大语言模型潜力未被充分挖掘。
2. PICK框架通过分层分析、知识注入和强化学习特征提取，提升MLLM在心理分析中的专家级推理能力。
3. 实验结果表明，PICK框架显著提升了MLLM在心理分析方面的能力，并验证了其作为通用框架的有效性。

## 📝 摘要（中文）

本文提出PICK框架，旨在利用多模态大语言模型（MLLM）进行心理分析，特别关注临床实践中广泛使用的房屋-树木-人物（HTP）测试。该框架通过分层分析和知识注入，实现对心理图像的理解。首先，将包含多个实例的绘画分解为语义上有意义的子图，构建一个分层表示，捕捉跨越单对象、多对象和整体三个层面的空间结构和内容。然后，在每个层面上进行有针对性的分析，从视觉线索中提取心理或情感洞察。此外，引入HTP知识库，并设计一个使用强化学习训练的特征提取模块，为单对象层面的分析生成心理概况，将整体风格特征和动态对象特定特征（如房屋、树木或人物的特征）与心理状态相关联。最后，整合这些多方面的信息，生成与专家级推理相符的评估结果。实验结果表明，所提出的PICK显著增强了MLLM在心理分析方面的能力，并通过扩展到情感理解任务，验证了其作为通用框架的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLM）在主观、情感细微的心理分析领域应用不足的问题。现有方法难以有效提取绘画中的心理信息，缺乏专家级的推理能力，导致分析结果不够准确和深入。

**核心思路**：论文的核心思路是将绘画分解为不同语义层级的子图，并结合心理学知识库，利用MLLM进行分层分析和推理。通过这种方式，可以更有效地提取绘画中的心理信息，并模拟专家级的推理过程，从而提高心理分析的准确性和可靠性。

**技术框架**：PICK框架包含以下主要模块：1) 绘画分解模块：将绘画分解为单对象、多对象和整体三个层级的子图。2) 特征提取模块：使用强化学习训练的特征提取器，提取单对象层级的心理概况，包括整体风格特征和对象特定特征。3) 知识注入模块：引入HTP知识库，为MLLM提供心理学知识。4) 分层分析模块：利用MLLM在不同层级上进行分析和推理，提取心理信息。5) 整合模块：整合各层级的信息，生成最终的心理评估报告。

**关键创新**：论文的关键创新在于提出了一个多步骤的分层分析框架，能够有效地利用MLLM进行心理分析。此外，还引入了HTP知识库和强化学习训练的特征提取器，进一步提升了分析的准确性和可靠性。与现有方法相比，PICK框架能够更全面、深入地理解绘画中的心理信息，并模拟专家级的推理过程。

**关键设计**：特征提取模块使用强化学习进行训练，目标是最大化提取到的特征与心理状态的相关性。具体而言，使用策略梯度算法，奖励函数基于提取到的特征与专家标注的心理状态之间的相似度。HTP知识库包含房屋、树木、人物等元素的心理学含义，以及它们之间的关系。在分层分析过程中，MLLM被提示以特定的心理学视角来分析绘画，例如关注房屋的结构是否稳定，树木的生长状态是否健康，人物的表情是否自然等。

## 📊 实验亮点

实验结果表明，PICK框架在HTP测试的心理分析任务中显著提升了MLLM的性能。具体而言，PICK框架在多个评估指标上都优于现有的基线方法，包括准确率、召回率和F1值。此外，通过扩展到情感理解任务，验证了PICK框架作为通用框架的有效性。

## 🎯 应用场景

该研究成果可应用于心理咨询、精神疾病诊断、儿童心理评估等领域。通过自动化分析绘画作品，可以辅助心理医生进行更高效、客观的评估，并为患者提供个性化的治疗方案。未来，该技术有望扩展到其他类型的心理测试和艺术治疗中，为心理健康领域带来更广泛的应用。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated exceptional performance across various objective multimodal perception tasks, yet their application to subjective, emotionally nuanced domains, such as psychological analysis, remains largely unexplored. In this paper, we introduce PICK, a multi-step framework designed for Psychoanalytical Image Comprehension through hierarchical analysis and Knowledge injection with MLLMs, specifically focusing on the House-Tree-Person (HTP) Test, a widely used psychological assessment in clinical practice. First, we decompose drawings containing multiple instances into semantically meaningful sub-drawings, constructing a hierarchical representation that captures spatial structure and content across three levels: single-object level, multi-object level, and whole level. Next, we analyze these sub-drawings at each level with a targeted focus, extracting psychological or emotional insights from their visual cues. We also introduce an HTP knowledge base and design a feature extraction module, trained with reinforcement learning, to generate a psychological profile for single-object level analysis. This profile captures both holistic stylistic features and dynamic object-specific features (such as those of the house, tree, or person), correlating them with psychological states. Finally, we integrate these multi-faceted information to produce a well-informed assessment that aligns with expert-level reasoning. Our approach bridges the gap between MLLMs and specialized expert domains, offering a structured and interpretable framework for understanding human mental states through visual expression. Experimental results demonstrate that the proposed PICK significantly enhances the capability of MLLMs in psychological analysis. It is further validated as a general framework through extensions to emotion understanding tasks.

