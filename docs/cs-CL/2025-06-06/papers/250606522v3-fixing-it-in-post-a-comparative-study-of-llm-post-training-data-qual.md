---
layout: default
title: "Fixing It in Post: A Comparative Study of LLM Post-Training Data Quality and Model Performance"
---

# Fixing It in Post: A Comparative Study of LLM Post-Training Data Quality and Model Performance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06522" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06522v3</a>
  <a href="https://arxiv.org/pdf/2506.06522.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06522v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06522v3', 'Fixing It in Post: A Comparative Study of LLM Post-Training Data Quality and Model Performance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aladin Djuhera, Swanand Ravindra Kadhe, Syed Zawad, Farhan Ahmed, Heiko Ludwig, Holger Boche

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-12-15)

**期刊**: The Thirty-Ninth Annual Conference on Neural Information Processing Systems (NeurIPS) 2025

---

## 💡 一句话要点

**提出TuluTalk数据集以提升LLM后训练性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `后训练` `数据集构建` `性能提升` `自然语言处理`

## 📋 核心要点

1. 现有的后训练数据集缺乏透明度，导致对其构建过程和数据质量的了解有限。
2. 本文通过对两个开放后训练数据集进行比较分析，提出了新的数据混合TuluTalk，以提升模型性能。
3. 实验结果表明，TuluTalk在样本数量减少的情况下，能够在关键基准上匹配或超越源数据集的性能。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的研究越来越关注后训练和与数据集的对齐，以增强指令遵循、世界知识和专业技能。然而，许多领先的LLM所使用的后训练数据集对公众不可获取，缺乏透明度。本文首次对两个开放后训练数据集Tulu-3-SFT-Mix和SmolTalk进行了全面的比较分析，并基于分析结果设计了新的数据混合TuluTalk，样本数量减少14%，但在关键基准上表现相当或更优。研究结果为构建更有效的后训练数据集提供了可行的见解，并公开了注释的源数据集和TuluTalk混合数据集。

## 🔬 方法详解

**问题定义**：本文旨在解决后训练数据集的透明度不足和对模型性能影响的不确定性。现有方法缺乏系统比较，导致难以评估数据质量对下游任务的影响。

**核心思路**：通过对Tulu-3-SFT-Mix和SmolTalk两个开放数据集进行详细的质量指标注释，分析其结构和质量差异，并基于此设计新的数据混合TuluTalk，以提高模型性能。

**技术框架**：研究采用Magpie框架对样本进行注释，主要模块包括数据集选择、质量指标评估、数据混合设计和性能评估。

**关键创新**：本文的主要创新在于首次系统性比较开放后训练数据集，并提出了基于数据质量分析的新数据混合方法TuluTalk，显著提升了数据集的有效性。

**关键设计**：在数据混合过程中，注重样本的回合结构、任务类别、输入质量和响应质量等关键参数设置，确保新数据集在性能上优于源数据集。

## 📊 实验亮点

实验结果显示，TuluTalk在样本数量减少14%的情况下，能够在多个关键基准上匹配或超越Tulu-3-SFT-Mix和SmolTalk的性能。这一发现为后训练数据集的构建提供了新的思路和方法。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等。通过构建更有效的后训练数据集，研究能够帮助提升模型在实际应用中的表现，降低资源消耗，并推动相关领域的进一步研究与发展。

## 📄 摘要（原文）

> Recent work on large language models (LLMs) has increasingly focused on post-training and alignment with datasets curated to enhance instruction following, world knowledge, and specialized skills. However, most post-training datasets used in leading open- and closed-source LLMs remain inaccessible to the public, with limited information about their construction process. This lack of transparency has motivated the recent development of open-source post-training corpora. While training on these open alternatives can yield performance comparable to that of leading models, systematic comparisons remain challenging due to the significant computational cost of conducting them rigorously at scale, and are therefore largely absent. As a result, it remains unclear how specific samples, task types, or curation strategies influence downstream performance when assessing data quality. In this work, we conduct the first comprehensive side-by-side analysis of two prominent open post-training datasets: Tulu-3-SFT-Mix and SmolTalk. Using the Magpie framework, we annotate each sample with detailed quality metrics, including turn structure (single-turn vs. multi-turn), task category, input quality, and response quality, and we derive statistics that reveal structural and qualitative similarities and differences between the two datasets. Based on these insights, we design a principled curation recipe that produces a new data mixture, TuluTalk, which contains 14% fewer samples than either source dataset while matching or exceeding their performance on key benchmarks. Our findings offer actionable insights for constructing more effective post-training datasets that improve model performance within practical resource limits. To support future research, we publicly release both the annotated source datasets and our curated TuluTalk mixture.

