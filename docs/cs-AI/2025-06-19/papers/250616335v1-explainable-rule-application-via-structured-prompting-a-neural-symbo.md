---
layout: default
title: "Explainable Rule Application via Structured Prompting: A Neural-Symbolic Approach"
---

# Explainable Rule Application via Structured Prompting: A Neural-Symbolic Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16335" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16335v1</a>
  <a href="https://arxiv.org/pdf/2506.16335.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16335v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16335v1', 'Explainable Rule Application via Structured Prompting: A Neural-Symbolic Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Albert Sadowski, Jarosław A. Chudziak

**分类**: cs.AI, cs.CL

**发布日期**: 2025-06-19

**备注**: Accepted for publication at the 29th International Conference on Knowledge-Based and Intelligent Information \& Engineering Systems (KES 2025)

**期刊**: Procedia Computer Science 270 (2025) 2166-2175

**DOI**: [10.1016/j.procs.2025.09.337](https://doi.org/10.1016/j.procs.2025.09.337)

---

## 💡 一句话要点

**提出结构化提示框架以解决法律分析中的规则应用问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `结构化提示` `符号推理` `法律分析` `可解释AI` `混合神经-符号系统` `逻辑推理`

## 📋 核心要点

1. 现有大型语言模型在规则应用和例外处理上存在不足，尤其是在法律分析等领域，缺乏一致性和可解释性。
2. 本文提出的结构化提示框架通过将推理过程分解为实体识别、属性提取和符号规则应用三个步骤，解决了上述问题。
3. 在LegalBench传闻判断任务中，本文方法显著提升了模型性能，o1模型的F1得分达到0.929，优于基线的0.714。

## 📝 摘要（中文）

大型语言模型（LLMs）在复杂推理任务中表现出色，但在一致性规则应用、例外处理和可解释性方面存在挑战，尤其是在法律分析等需要自然语言理解和精确逻辑推理的领域。本文提出了一种结构化提示框架，将推理分解为三个可验证的步骤：实体识别、属性提取和符号规则应用。通过整合神经和符号方法，我们的方法利用了LLMs的解释灵活性，同时通过形式验证确保逻辑一致性。该框架外部化任务定义，使领域专家能够在不改变架构的情况下优化逻辑结构。在LegalBench传闻判断任务上的评估显示，我们的方法显著优于基线，OpenAI o系列模型表现出显著改进，o1模型的F1得分达到0.929，o3-mini模型达到0.867，相较于其少量样本基线的0.714和0.74，提升显著。该混合神经-符号系统为透明和一致的基于规则的推理提供了有前景的路径，暗示在结构化法律推理任务中的可解释AI应用潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在法律分析中规则应用不一致和缺乏可解释性的问题。现有方法在处理复杂推理和例外情况时表现不佳，导致逻辑推理的可靠性不足。

**核心思路**：论文提出的结构化提示框架通过将推理过程分解为三个可验证的步骤，增强了模型的逻辑一致性和可解释性。这种设计使得领域专家能够在不改变模型架构的情况下优化推理过程。

**技术框架**：整体架构包括三个主要模块：实体识别、属性提取和符号规则应用。每个模块负责特定的推理步骤，确保整个过程的透明性和可验证性。

**关键创新**：最重要的创新在于将神经网络与符号推理相结合，形成混合神经-符号系统。这种方法不仅提高了推理的准确性，还增强了可解释性，与传统的单一方法相比，提供了更强的逻辑一致性。

**关键设计**：在模型设计中，采用了结构化提示和补充谓词的方式来优化推理过程。损失函数和网络结构经过精心调整，以确保在不同步骤之间的有效信息传递。

## 📊 实验亮点

在实验中，本文方法在LegalBench传闻判断任务中表现优异，o1模型的F1得分达到0.929，o3-mini模型达到0.867，均显著高于其少量样本基线得分0.714和0.74，展示了结构化提示框架的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括法律分析、合规检查和其他需要精确逻辑推理的领域。通过提供可解释的推理过程，该框架能够帮助法律专家更好地理解和应用规则，提升法律决策的透明度和可靠性。未来，该方法可能在其他领域的可解释AI应用中发挥重要作用。

## 📄 摘要（原文）

> Large Language Models (LLMs) excel in complex reasoning tasks but struggle with consistent rule application, exception handling, and explainability, particularly in domains like legal analysis that require both natural language understanding and precise logical inference. This paper introduces a structured prompting framework that decomposes reasoning into three verifiable steps: entity identification, property extraction, and symbolic rule application. By integrating neural and symbolic approaches, our method leverages LLMs' interpretive flexibility while ensuring logical consistency through formal verification. The framework externalizes task definitions, enabling domain experts to refine logical structures without altering the architecture. Evaluated on the LegalBench hearsay determination task, our approach significantly outperformed baselines, with OpenAI o-family models showing substantial improvements - o1 achieving an F1 score of 0.929 and o3-mini reaching 0.867 using structured decomposition with complementary predicates, compared to their few-shot baselines of 0.714 and 0.74 respectively. This hybrid neural-symbolic system offers a promising pathway for transparent and consistent rule-based reasoning, suggesting potential for explainable AI applications in structured legal reasoning tasks.

