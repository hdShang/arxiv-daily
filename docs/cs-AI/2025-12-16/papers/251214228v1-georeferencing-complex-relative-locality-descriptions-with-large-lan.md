---
layout: default
title: Georeferencing complex relative locality descriptions with large language models
---

# Georeferencing complex relative locality descriptions with large language models

**arXiv**: [2512.14228v1](https://arxiv.org/abs/2512.14228) | [PDF](https://arxiv.org/pdf/2512.14228.pdf)

**作者**: Aneesha Fernando, Surangika Ranathunga, Kristin Stock, Raj Prasanna, Christopher B. Jones

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: Provisionally accepted for publication in the International Journal of Geographical Information Science

---

## 💡 一句话要点

**提出基于大语言模型的复杂相对位置描述地理编码方法，以解决生物多样性记录中位置描述自动化处理难题。**

**关键词**: `地理编码` `大语言模型` `生物多样性记录` `相对位置描述` `QLoRA微调` `自然语言处理` `空间关系解析` `自动化地理信息提取`

## 📋 核心要点

1. 现有方法主要依赖地名或地理指示词进行地理编码，难以处理包含空间关系的复杂相对位置描述，导致准确性不足。
2. 论文提出使用大语言模型，通过有效提示模式和QLoRA微调技术，自动解析和地理编码复杂位置描述，提升处理能力。
3. 实验结果显示，该方法在多个数据集上平均65%的记录在10公里半径内准确，纽约州最佳结果达85%在10公里内和67%在1公里内。

## 📝 摘要（中文）

地理编码文本文档通常依赖于基于地名录的方法为地名分配地理坐标，或通过语言建模方法将文本术语与地理位置关联。然而，许多位置描述通过空间关系相对指定位置，使得仅基于地名或地理指示词的地理编码不准确。这一问题在生物标本采集记录中尤为常见，这些记录中的位置通常以叙述形式描述而非坐标，尤其是在GPS出现之前的记录。准确的地理编码对生物多样性研究至关重要，但该过程仍然劳动密集，导致对自动化地理编码解决方案的需求。本文探讨了大语言模型自动地理编码复杂位置描述的潜力，重点关注生物多样性收集领域。我们首先确定了有效的提示模式，然后使用量化低秩适应在多区域和多语言的生物多样性数据集上对大语言模型进行微调。我们的方法在固定训练数据量下，平均在65%的记录中实现了10公里半径内的地理编码，优于现有基线。最佳结果（纽约州）为85%在10公里内和67%在1公里内。所选大语言模型在处理冗长、复杂的描述时表现良好，突显了其在处理复杂位置描述地理编码方面的潜力。

## 🔬 方法详解

论文提出一个基于大语言模型的自动化地理编码框架。整体框架包括：首先识别有效的提示模式以引导模型理解复杂位置描述；然后使用量化低秩适应技术在大规模生物多样性数据集上进行微调，这些数据集涵盖多区域和多语言，以增强模型的泛化能力。关键技术创新点在于结合大语言模型的自然语言理解能力与QLoRA高效微调，直接处理包含空间关系的文本描述，而无需依赖传统的地名录或简单关键词匹配。与现有方法的主要区别在于，它能够处理冗长、叙述性的位置描述，通过端到端学习实现更准确的地理坐标预测，突破了基于地名或地理指示词的局限性。

## 📊 实验亮点

实验表明，在固定训练数据量下，该方法平均在65%的记录中实现10公里半径内的地理编码，优于现有基线。最佳性能在纽约州数据集上达到85%在10公里内和67%在1公里内，突显了大语言模型在处理复杂描述时的优越性。

## 🎯 应用场景

该研究主要应用于生物多样性领域，特别是生物标本采集记录的地理编码，可自动化处理历史记录中的叙述性位置描述，支持生物多样性研究和保护工作。此外，也可扩展至其他需要从文本中提取地理信息的场景，如灾害报告、考古记录或社交媒体分析。

## 📄 摘要（原文）

> Georeferencing text documents has typically relied on either gazetteer-based methods to assign geographic coordinates to place names, or on language modelling approaches that associate textual terms with geographic locations. However, many location descriptions specify positions relatively with spatial relationships, making geocoding based solely on place names or geo-indicative words inaccurate. This issue frequently arises in biological specimen collection records, where locations are often described through narratives rather than coordinates if they pre-date GPS. Accurate georeferencing is vital for biodiversity studies, yet the process remains labour-intensive, leading to a demand for automated georeferencing solutions. This paper explores the potential of Large Language Models (LLMs) to georeference complex locality descriptions automatically, focusing on the biodiversity collections domain. We first identified effective prompting patterns, then fine-tuned an LLM using Quantized Low-Rank Adaptation (QLoRA) on biodiversity datasets from multiple regions and languages. Our approach outperforms existing baselines with an average, across datasets, of 65% of records within a 10 km radius, for a fixed amount of training data. The best results (New York state) were 85% within 10km and 67% within 1km. The selected LLM performs well for lengthy, complex descriptions, highlighting its potential for georeferencing intricate locality descriptions.

