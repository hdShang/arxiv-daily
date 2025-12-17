---
layout: default
title: Temporal Tokenization Strategies for Event Sequence Modeling with Large Language Models
---

# Temporal Tokenization Strategies for Event Sequence Modeling with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13618" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13618</a>
  <a href="https://arxiv.org/pdf/2512.13618.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13618" onclick="toggleFavorite(this, '2512.13618', 'Temporal Tokenization Strategies for Event Sequence Modeling with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zefang Liu, Nam H. Nguyen, Yinzhu Quan, Shi-Xiong Zhang

**分类**: cs.CL, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**针对LLM事件序列建模，提出时间Token化策略选择框架，适配不同数据分布。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列建模` `大型语言模型` `Token化策略` `事件序列` `数据分布`

## 📋 核心要点

1. 现有方法在利用LLM建模时序事件序列时，对连续时间的表示方法缺乏深入研究，最佳策略不明确。
2. 该论文提出了一种时间Token化策略选择框架，核心思想是根据数据的统计特性选择合适的Token化方法。
3. 通过在真实世界数据集上微调LLM进行评估，结果表明预测性能高度依赖于Token化器与数据统计属性的对齐。

## 📝 摘要（中文）

在使用大型语言模型（LLM）建模时序事件序列时，如何表示连续时间是一个至关重要但尚未充分探索的挑战。目前已提出多种策略，如字节级表示或日历Token。然而，考虑到真实世界事件数据分布的多样性（从平滑的对数正态分布到离散的尖峰模式），最佳方法仍不明确。本文首次对事件序列的时间Token化进行了实证研究，比较了不同的编码策略：朴素的数字字符串、高精度字节级表示、人类语义日历Token、经典均匀分箱和自适应残差标量量化。通过在具有代表性的真实世界数据集上微调LLM来评估这些策略。分析表明，没有一种策略是普遍优越的；相反，预测性能在很大程度上取决于Token化器与数据统计属性的对齐，其中基于对数的策略在偏斜分布上表现出色，而以人为中心的格式对于混合模态证明是稳健的。

## 🔬 方法详解

**问题定义**：论文旨在解决使用大型语言模型（LLM）建模时序事件序列时，如何有效地表示连续时间的问题。现有方法，如字节级表示或日历Token，各有优缺点，但缺乏系统性的比较和选择依据，尤其是在面对不同统计分布的真实世界数据时，难以确定最佳策略。现有方法的痛点在于缺乏对数据分布的适配性。

**核心思路**：论文的核心思路是根据时序事件数据的统计特性，选择合适的Token化策略。不同的数据分布（如对数正态分布、离散分布）可能需要不同的Token化方法才能达到最佳的建模效果。通过比较多种Token化策略在不同数据集上的性能，找到与数据分布相匹配的策略。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1）选择具有不同统计分布的真实世界事件序列数据集；2）实现并比较多种时间Token化策略，包括朴素的数字字符串、高精度字节级表示、人类语义日历Token、经典均匀分箱和自适应残差标量量化；3）使用这些Token化后的数据微调LLM；4）评估不同Token化策略在不同数据集上的预测性能；5）分析结果，得出Token化策略与数据分布之间的关系。

**关键创新**：该论文的关键创新在于首次对事件序列的时间Token化进行了全面的实证研究，并揭示了Token化策略与数据统计属性之间的重要关系。它表明，没有一种通用的最佳策略，而是需要根据数据的具体分布进行选择。这种针对数据分布的自适应Token化方法是与现有方法的本质区别。

**关键设计**：论文的关键设计包括：1）选择了具有代表性的真实世界数据集，涵盖了不同的统计分布；2）实现了多种具有代表性的时间Token化策略，包括数值型、字节型、语义型和分箱型；3）使用了标准的LLM微调流程进行评估；4）采用了多种评估指标来衡量预测性能。具体的参数设置和损失函数等细节可能因使用的LLM而异，但整体流程保持一致。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13618/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13618/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13618/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，没有一种时间Token化策略在所有数据集上都表现最佳。基于对数的策略在偏斜分布的数据集上表现出色，而以人为中心的格式对于混合模态的数据集表现稳健。这强调了根据数据统计属性选择Token化策略的重要性，为实际应用提供了指导。

## 🎯 应用场景

该研究成果可应用于各种需要对时序事件进行建模和预测的领域，例如医疗健康（预测疾病进展）、金融（预测股票价格波动）、物联网（预测设备故障）和推荐系统（预测用户行为）。通过选择合适的Token化策略，可以提高LLM在这些领域的预测精度和效率，从而带来实际价值和未来影响。

## 📄 摘要（原文）

> Representing continuous time is a critical and under-explored challenge in modeling temporal event sequences with large language models (LLMs). Various strategies like byte-level representations or calendar tokens have been proposed. However, the optimal approach remains unclear, especially given the diverse statistical distributions of real-world event data, which range from smooth log-normal to discrete, spiky patterns. This paper presents the first empirical study of temporal tokenization for event sequences, comparing distinct encoding strategies: naive numeric strings, high-precision byte-level representations, human-semantic calendar tokens, classic uniform binning, and adaptive residual scalar quantization. We evaluate these strategies by fine-tuning LLMs on real-world datasets that exemplify these diverse distributions. Our analysis reveals that no single strategy is universally superior; instead, prediction performance depends heavily on aligning the tokenizer with the data's statistical properties, with log-based strategies excelling on skewed distributions and human-centric formats proving robust for mixed modalities.

