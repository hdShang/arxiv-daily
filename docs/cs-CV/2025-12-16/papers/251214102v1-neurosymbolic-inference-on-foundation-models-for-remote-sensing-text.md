---
layout: default
title: Neurosymbolic Inference On Foundation Models For Remote Sensing Text-to-image Retrieval With Complex Queries
---

# Neurosymbolic Inference On Foundation Models For Remote Sensing Text-to-image Retrieval With Complex Queries

**arXiv**: [2512.14102v1](https://arxiv.org/abs/2512.14102) | [PDF](https://arxiv.org/pdf/2512.14102.pdf)

**作者**: Emanuele Mezzi, Gertjan Burghouts, Maarten Kruithof

**分类**: cs.CV, cs.AI, cs.IR

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出RUNE方法，结合大语言模型与神经符号AI，解决遥感文本到图像检索中复杂空间关系处理与可解释性不足的问题。**

**关键词**: `遥感图像检索` `神经符号AI` `大语言模型` `一阶逻辑推理` `复杂查询处理` `可解释性AI` `多模态融合` `卫星图像分析`

## 📋 核心要点

1. 现有遥感文本到图像检索方法（如RS-LVLMs）存在可解释性不足和复杂空间关系处理能力差的问题，限制了实际应用。
2. 论文提出RUNE方法，结合大语言模型生成一阶逻辑表达式，并利用神经符号推理模块进行显式推理，提升检索性能和可解释性。
3. 实验表明，RUNE在复杂查询任务中优于现有RS-LVLMs，并引入新指标RRQC和RRIU验证其鲁棒性，展示了在洪水后卫星图像检索等场景的应用潜力。

## 📝 摘要（中文）

遥感领域的文本到图像检索随着针对航空和卫星影像定制的大型视觉语言模型（LVLMs）的兴起而迅速发展，最终形成了遥感大型视觉语言模型（RS-LVLMs）。然而，有限的可解释性和对复杂空间关系处理能力差仍然是实际应用中的关键挑战。为解决这些问题，我们引入了RUNE（使用神经符号实体进行推理），该方法将大语言模型（LLMs）与神经符号AI相结合，通过推理检测到的实体与从文本查询推导出的一阶逻辑（FOL）表达式之间的兼容性来检索图像。与依赖隐式联合嵌入的RS-LVLMs不同，RUNE执行显式推理，从而提升性能和可解释性。为实现可扩展性，我们提出了一种逻辑分解策略，该策略在检测到的实体的条件子集上操作，保证比神经方法更短的执行时间。我们不是将基础模型用于端到端检索，而是仅利用它们生成FOL表达式，将推理委托给神经符号推理模块。为了评估，我们重新利用了原本为物体检测设计的DOTA数据集，通过添加比现有基准更复杂的查询来增强它。我们展示了LLM在文本到逻辑翻译中的有效性，并将RUNE与最先进的RS-LVLMs进行比较，证明了其优越性能。我们引入了两个指标：检索对查询复杂性的鲁棒性（RRQC）和检索对图像不确定性的鲁棒性（RRIU），用于评估相对于查询复杂性和图像不确定性的性能。RUNE在复杂遥感检索任务中优于联合嵌入模型，在性能、鲁棒性和可解释性方面带来增益。我们通过一个关于洪水后卫星图像检索的用例展示了RUNE在现实世界遥感应用中的潜力。

## 🔬 方法详解

RUNE的整体框架包括两个核心模块：首先，使用大语言模型将文本查询翻译为一阶逻辑表达式；其次，通过神经符号推理模块，基于检测到的实体与逻辑表达式的兼容性进行显式推理来检索图像。关键技术创新点在于逻辑分解策略，该策略在检测到的实体的条件子集上操作，优化执行时间，确保可扩展性。与现有方法的主要区别在于，RUNE不依赖隐式联合嵌入，而是采用显式推理路径，将基础模型仅用于逻辑生成，推理任务由专门的神经符号模块处理，从而增强可解释性和处理复杂关系的能力。

## 📊 实验亮点

RUNE在复杂遥感检索任务中显著优于现有RS-LVLMs，性能提升明显；引入的RRQC和RRIU指标验证了其对查询复杂性和图像不确定性的鲁棒性；在DOTA数据集上的实验展示了LLM在文本到逻辑翻译中的有效性，并通过洪水后检索用例证明了实际应用价值。

## 🎯 应用场景

该研究在遥感领域具有广泛的应用潜力，例如在灾害响应中用于洪水后卫星图像检索，可快速定位受灾区域；还可应用于城市规划、环境监测和军事侦察等场景，通过复杂查询实现高效、可解释的图像检索，提升决策支持系统的实用性。

## 📄 摘要（原文）

> Text-to-image retrieval in remote sensing (RS) has advanced rapidly with the rise of large vision-language models (LVLMs) tailored for aerial and satellite imagery, culminating in remote sensing large vision-language models (RS-LVLMS). However, limited explainability and poor handling of complex spatial relations remain key challenges for real-world use. To address these issues, we introduce RUNE (Reasoning Using Neurosymbolic Entities), an approach that combines Large Language Models (LLMs) with neurosymbolic AI to retrieve images by reasoning over the compatibility between detected entities and First-Order Logic (FOL) expressions derived from text queries. Unlike RS-LVLMs that rely on implicit joint embeddings, RUNE performs explicit reasoning, enhancing performance and interpretability. For scalability, we propose a logic decomposition strategy that operates on conditioned subsets of detected entities, guaranteeing shorter execution time compared to neural approaches. Rather than using foundation models for end-to-end retrieval, we leverage them only to generate FOL expressions, delegating reasoning to a neurosymbolic inference module. For evaluation we repurpose the DOTA dataset, originally designed for object detection, by augmenting it with more complex queries than in existing benchmarks. We show the LLM's effectiveness in text-to-logic translation and compare RUNE with state-of-the-art RS-LVLMs, demonstrating superior performance. We introduce two metrics, Retrieval Robustness to Query Complexity (RRQC) and Retrieval Robustness to Image Uncertainty (RRIU), which evaluate performance relative to query complexity and image uncertainty. RUNE outperforms joint-embedding models in complex RS retrieval tasks, offering gains in performance, robustness, and explainability. We show RUNE's potential for real-world RS applications through a use case on post-flood satellite image retrieval.

