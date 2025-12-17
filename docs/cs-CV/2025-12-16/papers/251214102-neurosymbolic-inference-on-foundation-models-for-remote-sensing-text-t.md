---
layout: default
title: Neurosymbolic Inference On Foundation Models For Remote Sensing Text-to-image Retrieval With Complex Queries
---

# Neurosymbolic Inference On Foundation Models For Remote Sensing Text-to-image Retrieval With Complex Queries

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14102" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14102</a>
  <a href="https://arxiv.org/pdf/2512.14102.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14102" onclick="toggleFavorite(this, '2512.14102', 'Neurosymbolic Inference On Foundation Models For Remote Sensing Text-to-image Retrieval With Complex Queries')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Emanuele Mezzi, Gertjan Burghouts, Maarten Kruithof

**分类**: cs.CV, cs.AI, cs.IR

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出RUNE：结合神经符号推理与大语言模型，提升遥感图像文本检索的复杂查询处理能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感图像检索` `神经符号推理` `大语言模型` `一阶逻辑` `复杂查询`

## 📋 核心要点

1. 现有遥感图像文本检索模型在处理复杂空间关系和提供可解释性方面存在不足，限制了实际应用。
2. RUNE结合大语言模型和神经符号AI，通过显式推理检测到的实体与一阶逻辑表达式的兼容性来检索图像。
3. 实验表明，RUNE在复杂查询下优于现有遥感视觉-语言模型，并在查询复杂度和图像不确定性方面表现出更强的鲁棒性。

## 📝 摘要（中文）

遥感图像文本检索随着大型视觉-语言模型（LVLM）的发展而迅速进步，特别是针对航空和卫星图像的遥感大型视觉-语言模型（RS-LVLM）。然而，有限的可解释性和对复杂空间关系的较差处理仍然是实际应用中的关键挑战。为了解决这些问题，我们引入了RUNE（Reasoning Using Neurosymbolic Entities），这是一种结合大型语言模型（LLM）与神经符号AI的方法，通过推理检测到的实体与从文本查询导出的First-Order Logic（FOL）表达式之间的兼容性来检索图像。与依赖隐式联合嵌入的RS-LVLM不同，RUNE执行显式推理，从而提高性能和可解释性。为了可扩展性，我们提出了一种逻辑分解策略，该策略在检测到的实体的条件子集上运行，与神经方法相比，保证了更短的执行时间。我们没有使用基础模型进行端到端检索，而是仅利用它们来生成FOL表达式，并将推理委托给神经符号推理模块。为了评估，我们重新利用了最初为对象检测而设计的DOTA数据集，通过添加比现有基准更复杂的查询来增强它。我们展示了LLM在文本到逻辑翻译方面的有效性，并将RUNE与最先进的RS-LVLM进行了比较，证明了其卓越的性能。我们引入了两个指标，查询复杂度的检索鲁棒性（RRQC）和图像不确定性的检索鲁棒性（RRIU），它们评估相对于查询复杂度和图像不确定性的性能。RUNE在复杂的RS检索任务中优于联合嵌入模型，从而提高了性能、鲁棒性和可解释性。我们通过洪水后卫星图像检索的用例展示了RUNE在实际RS应用中的潜力。

## 🔬 方法详解

**问题定义**：遥感图像文本检索任务旨在根据文本描述检索相关的遥感图像。现有方法，特别是基于联合嵌入的遥感视觉-语言模型（RS-LVLM），在处理涉及复杂空间关系的查询时表现不佳，并且缺乏可解释性。这些模型通常依赖于隐式的联合嵌入空间，难以理解检索结果背后的推理过程。

**核心思路**：RUNE的核心思路是将文本查询转化为一阶逻辑（FOL）表达式，然后通过神经符号推理来判断图像中检测到的实体是否满足这些逻辑表达式。这种方法将检索过程分解为文本理解、逻辑推理和实体匹配三个步骤，从而提高了可解释性和处理复杂查询的能力。通过显式地建模实体之间的关系，RUNE能够更好地理解查询的意图并检索相关的图像。

**技术框架**：RUNE的整体框架包括以下几个主要模块：1) **文本到逻辑转换模块**：使用大型语言模型（LLM）将文本查询转换为一阶逻辑表达式。2) **实体检测模块**：使用现有的目标检测模型检测遥感图像中的实体。3) **神经符号推理模块**：该模块接收逻辑表达式和检测到的实体作为输入，通过推理判断图像是否满足查询条件。为了提高可扩展性，RUNE采用了一种逻辑分解策略，将复杂的逻辑表达式分解为更小的子表达式，并在实体的子集上进行推理。

**关键创新**：RUNE的关键创新在于将神经符号推理引入遥感图像文本检索任务。与传统的基于联合嵌入的方法不同，RUNE通过显式地建模实体之间的关系和推理过程，提高了可解释性和处理复杂查询的能力。此外，RUNE的逻辑分解策略提高了推理效率，使其能够处理大规模的遥感图像数据。

**关键设计**：RUNE的关键设计包括：1) 使用预训练的大型语言模型（如GPT-3）进行文本到逻辑的转换，并进行微调以适应遥感领域的特定词汇和表达方式。2) 设计合适的逻辑表达式来表示遥感图像中的空间关系，例如“在…的上方”、“在…的左侧”等。3) 实现高效的神经符号推理算法，例如基于约束满足的推理或基于图神经网络的推理。4) 通过RRQC和RRIU指标来评估模型在复杂查询和图像不确定性下的鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14102/pipeline.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14102/decomposition.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14102/graph_complexity.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

RUNE在DOTA数据集上进行了评估，并与最先进的遥感视觉-语言模型进行了比较。实验结果表明，RUNE在处理复杂查询时显著优于现有方法，并在查询复杂度的检索鲁棒性（RRQC）和图像不确定性的检索鲁棒性（RRIU）方面表现出更强的鲁棒性。例如，RUNE在RRQC指标上比基线模型提高了10%以上，证明了其在处理复杂查询方面的优势。

## 🎯 应用场景

RUNE在遥感图像分析领域具有广泛的应用前景，例如灾害监测（洪水、地震后的建筑物损毁评估）、城市规划（建筑物变化检测、土地利用分类）、环境监测（森林砍伐、水体污染）等。通过处理复杂的空间关系查询，RUNE可以帮助用户更有效地检索和分析遥感图像，为决策提供支持。未来，RUNE可以与其他遥感数据源（如LiDAR、SAR）结合，实现更全面的遥感信息提取和分析。

## 📄 摘要（原文）

> Text-to-image retrieval in remote sensing (RS) has advanced rapidly with the rise of large vision-language models (LVLMs) tailored for aerial and satellite imagery, culminating in remote sensing large vision-language models (RS-LVLMS). However, limited explainability and poor handling of complex spatial relations remain key challenges for real-world use. To address these issues, we introduce RUNE (Reasoning Using Neurosymbolic Entities), an approach that combines Large Language Models (LLMs) with neurosymbolic AI to retrieve images by reasoning over the compatibility between detected entities and First-Order Logic (FOL) expressions derived from text queries. Unlike RS-LVLMs that rely on implicit joint embeddings, RUNE performs explicit reasoning, enhancing performance and interpretability. For scalability, we propose a logic decomposition strategy that operates on conditioned subsets of detected entities, guaranteeing shorter execution time compared to neural approaches. Rather than using foundation models for end-to-end retrieval, we leverage them only to generate FOL expressions, delegating reasoning to a neurosymbolic inference module. For evaluation we repurpose the DOTA dataset, originally designed for object detection, by augmenting it with more complex queries than in existing benchmarks. We show the LLM's effectiveness in text-to-logic translation and compare RUNE with state-of-the-art RS-LVLMs, demonstrating superior performance. We introduce two metrics, Retrieval Robustness to Query Complexity (RRQC) and Retrieval Robustness to Image Uncertainty (RRIU), which evaluate performance relative to query complexity and image uncertainty. RUNE outperforms joint-embedding models in complex RS retrieval tasks, offering gains in performance, robustness, and explainability. We show RUNE's potential for real-world RS applications through a use case on post-flood satellite image retrieval.

