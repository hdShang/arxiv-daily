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

**提出RUNE方法，结合大语言模型与神经符号AI，解决遥感文本到图像检索中复杂查询的推理与可解释性问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `遥感文本到图像检索` `神经符号AI` `大语言模型` `谓词逻辑推理` `复杂查询处理` `可解释性增强` `遥感应用` `性能鲁棒性评估`

## 📋 核心要点

1. 现有遥感文本到图像检索方法（如RS-LVLMs）存在可解释性差和难以处理复杂空间关系的挑战，限制了实际应用。
2. 论文提出RUNE方法，结合大语言模型生成谓词逻辑表达式，并利用神经符号AI进行显式推理，提升检索性能和可解释性。
3. 实验表明，RUNE在复杂查询任务中优于现有RS-LVLMs，并引入新指标评估鲁棒性，展示了在洪水后卫星图像检索等场景的应用潜力。

## 📝 摘要（中文）

遥感领域的文本到图像检索随着针对航空和卫星影像定制的大型视觉语言模型（RS-LVLMs）的兴起而快速发展。然而，有限的可解释性和对复杂空间关系处理能力差仍是实际应用中的关键挑战。为解决这些问题，我们引入了RUNE（使用神经符号实体进行推理），该方法将大语言模型与神经符号AI相结合，通过推理检测到的实体与从文本查询导出的谓词逻辑表达式之间的兼容性来检索图像。与依赖隐式联合嵌入的RS-LVLMs不同，RUNE执行显式推理，从而提升性能和可解释性。为扩展性，我们提出一种逻辑分解策略，在检测实体的条件子集上操作，保证比神经方法更短的执行时间。我们仅利用基础模型生成谓词逻辑表达式，将推理委托给神经符号推理模块，而非用于端到端检索。为评估，我们重新利用原本为物体检测设计的DOTA数据集，通过添加比现有基准更复杂的查询来增强它。我们展示了大语言模型在文本到逻辑翻译中的有效性，并将RUNE与最先进的RS-LVLMs进行比较，证明了其优越性能。我们引入了两个指标：检索对查询复杂性的鲁棒性和检索对图像不确定性的鲁棒性，评估性能相对于查询复杂性和图像不确定性的表现。RUNE在复杂遥感检索任务中优于联合嵌入模型，在性能、鲁棒性和可解释性方面带来增益。我们通过一个洪水后卫星图像检索的用例展示了RUNE在现实世界遥感应用中的潜力。

## 🔬 方法详解

RUNE的整体框架包括两个核心模块：大语言模型用于将文本查询翻译为谓词逻辑表达式，以及神经符号推理模块用于基于检测到的实体进行显式推理。关键技术创新在于逻辑分解策略，它通过操作检测实体的条件子集来保证更短的执行时间，提高可扩展性。与现有方法的主要区别在于，RUNE不依赖隐式联合嵌入，而是执行显式推理，从而增强可解释性和处理复杂查询的能力，同时仅利用基础模型生成逻辑表达式，而非端到端检索。

## 📊 实验亮点

RUNE在复杂遥感检索任务中显著优于最先进的RS-LVLMs，通过引入检索对查询复杂性和图像不确定性的鲁棒性指标，展示了更高的性能和鲁棒性，并在DOTA数据集增强版本上验证了有效性。

## 🎯 应用场景

该研究在遥感领域具有广泛潜在应用，如洪水后卫星图像检索、城市规划中的复杂场景分析，以及环境监测中的多目标识别任务，能提升检索的准确性和可解释性，支持决策制定。

## 📄 摘要（原文）

> Text-to-image retrieval in remote sensing (RS) has advanced rapidly with the rise of large vision-language models (LVLMs) tailored for aerial and satellite imagery, culminating in remote sensing large vision-language models (RS-LVLMS). However, limited explainability and poor handling of complex spatial relations remain key challenges for real-world use. To address these issues, we introduce RUNE (Reasoning Using Neurosymbolic Entities), an approach that combines Large Language Models (LLMs) with neurosymbolic AI to retrieve images by reasoning over the compatibility between detected entities and First-Order Logic (FOL) expressions derived from text queries. Unlike RS-LVLMs that rely on implicit joint embeddings, RUNE performs explicit reasoning, enhancing performance and interpretability. For scalability, we propose a logic decomposition strategy that operates on conditioned subsets of detected entities, guaranteeing shorter execution time compared to neural approaches. Rather than using foundation models for end-to-end retrieval, we leverage them only to generate FOL expressions, delegating reasoning to a neurosymbolic inference module. For evaluation we repurpose the DOTA dataset, originally designed for object detection, by augmenting it with more complex queries than in existing benchmarks. We show the LLM's effectiveness in text-to-logic translation and compare RUNE with state-of-the-art RS-LVLMs, demonstrating superior performance. We introduce two metrics, Retrieval Robustness to Query Complexity (RRQC) and Retrieval Robustness to Image Uncertainty (RRIU), which evaluate performance relative to query complexity and image uncertainty. RUNE outperforms joint-embedding models in complex RS retrieval tasks, offering gains in performance, robustness, and explainability. We show RUNE's potential for real-world RS applications through a use case on post-flood satellite image retrieval.

