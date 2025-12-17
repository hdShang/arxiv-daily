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

**提出RUNE：结合神经符号推理与大模型，提升遥感图像文图检索的性能与可解释性**

🎯 **匹配领域**: **具身智能与表征学习 (Embodied AI & Representation)**

**关键词**: `遥感图像检索` `神经符号推理` `大型语言模型` `一阶逻辑` `可解释性`

## 📋 核心要点

1. 现有遥感文图检索模型可解释性差，难以处理复杂的空间关系，限制了实际应用。
2. RUNE结合大语言模型和神经符号AI，通过显式推理实体关系来检索图像，提升可解释性。
3. 实验表明RUNE在复杂查询和图像不确定性下表现优异，优于现有遥感视觉语言模型。

## 📝 摘要（中文）

遥感领域的文图检索随着大型视觉语言模型（LVLMs）的发展而迅速进步，特别是针对航空和卫星图像的遥感大型视觉语言模型（RS-LVLMs）。然而，有限的可解释性和对复杂空间关系的较差处理仍然是实际应用中的关键挑战。为了解决这些问题，我们引入了RUNE（Reasoning Using Neurosymbolic Entities），这是一种将大型语言模型（LLMs）与神经符号AI相结合的方法，通过推理检测到的实体与从文本查询导出的First-Order Logic（FOL）表达式之间的兼容性来检索图像。与依赖隐式联合嵌入的RS-LVLMs不同，RUNE执行显式推理，从而提高性能和可解释性。为了可扩展性，我们提出了一种逻辑分解策略，该策略在检测到的实体的条件子集上运行，与神经方法相比，保证了更短的执行时间。我们没有使用基础模型进行端到端检索，而是仅利用它们来生成FOL表达式，将推理委托给神经符号推理模块。为了评估，我们重新利用了最初为对象检测而设计的DOTA数据集，通过添加比现有基准更复杂的查询来增强它。我们展示了LLM在文本到逻辑翻译方面的有效性，并将RUNE与最先进的RS-LVLMs进行了比较，证明了其卓越的性能。我们引入了两个指标，查询复杂度的检索鲁棒性（RRQC）和图像不确定性的检索鲁棒性（RRIU），它们评估相对于查询复杂度和图像不确定性的性能。RUNE在复杂的RS检索任务中优于联合嵌入模型，从而提高了性能、鲁棒性和可解释性。我们通过洪水后卫星图像检索的用例展示了RUNE在实际RS应用中的潜力。

## 🔬 方法详解

**问题定义**：遥感图像的文图检索任务旨在根据文本描述检索相关的遥感图像。现有方法，特别是基于大型视觉语言模型（LVLMs）的方法，在处理复杂空间关系和提供可解释性方面存在不足。这些模型通常依赖于隐式的联合嵌入，难以理解模型做出决策的原因。

**核心思路**：RUNE的核心思路是将文本查询转换为一阶逻辑（FOL）表达式，然后通过神经符号推理来判断图像中检测到的实体是否满足这些逻辑表达式。这种方法将检索过程分解为文本理解、逻辑推理和实体匹配三个步骤，从而提高了可解释性和处理复杂查询的能力。

**技术框架**：RUNE的整体框架包括以下几个主要模块：1) **文本到逻辑转换模块**：使用大型语言模型（LLMs）将文本查询转换为FOL表达式。2) **实体检测模块**：使用预训练的对象检测模型检测遥感图像中的实体。3) **神经符号推理模块**：该模块接收FOL表达式和检测到的实体作为输入，通过推理判断图像是否满足查询条件。为了提高可扩展性，RUNE采用了一种逻辑分解策略，将复杂的FOL表达式分解为更小的子表达式，并在实体的条件子集上进行推理。

**关键创新**：RUNE的关键创新在于将神经符号推理引入到遥感文图检索任务中。与传统的基于联合嵌入的方法不同，RUNE执行显式的逻辑推理，从而提高了可解释性和处理复杂查询的能力。此外，RUNE的逻辑分解策略提高了推理效率，使其能够处理大规模的遥感图像数据。

**关键设计**：RUNE的关键设计包括：1) 使用预训练的LLM进行文本到逻辑的转换，利用LLM的强大语言理解能力。2) 设计了一种逻辑分解策略，将复杂的FOL表达式分解为更小的子表达式，以提高推理效率。3) 引入了两个新的评估指标，查询复杂度的检索鲁棒性（RRQC）和图像不确定性的检索鲁棒性（RRIU），以更全面地评估模型的性能。

## 📊 实验亮点

RUNE在DOTA数据集上进行了评估，并与最先进的遥感视觉语言模型进行了比较。实验结果表明，RUNE在处理复杂查询和图像不确定性方面表现优异，显著优于基于联合嵌入的方法。RUNE在查询复杂度的检索鲁棒性（RRQC）和图像不确定性的检索鲁棒性（RRIU）方面均取得了显著提升，证明了其在实际应用中的潜力。

## 🎯 应用场景

RUNE在遥感领域具有广泛的应用前景，例如灾害监测（洪水、地震等）、城市规划、农业监测和环境监测等。通过结合文本查询和遥感图像，RUNE可以帮助用户快速找到所需的信息，例如“查找洪水淹没的区域”或“查找特定类型的农作物分布情况”。RUNE的可解释性使其能够为用户提供更可靠的检索结果，并有助于用户理解模型做出决策的原因。

## 📄 摘要（原文）

> Text-to-image retrieval in remote sensing (RS) has advanced rapidly with the rise of large vision-language models (LVLMs) tailored for aerial and satellite imagery, culminating in remote sensing large vision-language models (RS-LVLMS). However, limited explainability and poor handling of complex spatial relations remain key challenges for real-world use. To address these issues, we introduce RUNE (Reasoning Using Neurosymbolic Entities), an approach that combines Large Language Models (LLMs) with neurosymbolic AI to retrieve images by reasoning over the compatibility between detected entities and First-Order Logic (FOL) expressions derived from text queries. Unlike RS-LVLMs that rely on implicit joint embeddings, RUNE performs explicit reasoning, enhancing performance and interpretability. For scalability, we propose a logic decomposition strategy that operates on conditioned subsets of detected entities, guaranteeing shorter execution time compared to neural approaches. Rather than using foundation models for end-to-end retrieval, we leverage them only to generate FOL expressions, delegating reasoning to a neurosymbolic inference module. For evaluation we repurpose the DOTA dataset, originally designed for object detection, by augmenting it with more complex queries than in existing benchmarks. We show the LLM's effectiveness in text-to-logic translation and compare RUNE with state-of-the-art RS-LVLMs, demonstrating superior performance. We introduce two metrics, Retrieval Robustness to Query Complexity (RRQC) and Retrieval Robustness to Image Uncertainty (RRIU), which evaluate performance relative to query complexity and image uncertainty. RUNE outperforms joint-embedding models in complex RS retrieval tasks, offering gains in performance, robustness, and explainability. We show RUNE's potential for real-world RS applications through a use case on post-flood satellite image retrieval.

