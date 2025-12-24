---
layout: default
title: "Synthline: A Product Line Approach for Synthetic Requirements Engineering Data Generation using Large Language Models"
---

# Synthline: A Product Line Approach for Synthetic Requirements Engineering Data Generation using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03265" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03265v1</a>
  <a href="https://arxiv.org/pdf/2505.03265.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03265v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03265v1', 'Synthline: A Product Line Approach for Synthetic Requirements Engineering Data Generation using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abdelkarim El-Hajjami, Camille Salinesi

**分类**: cs.SE, cs.AI

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出Synthline以解决需求工程数据稀缺问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `需求工程` `合成数据` `机器学习` `大型语言模型` `产品线方法` `数据稀缺` `模型训练`

## 📋 核心要点

1. 现有的需求工程方法在高质量数据集稀缺的情况下，导致模型训练效果不佳。
2. Synthline通过产品线方法，利用大型语言模型生成合成需求工程数据，系统性解决数据稀缺问题。
3. 实验结果显示，合成数据与真实数据结合使用，能显著提升模型的精度和召回率，达到85%的精度提升和2倍的召回率提升。

## 📝 摘要（中文）

现代需求工程（RE）在很大程度上依赖自然语言处理和机器学习技术，但高质量数据集的稀缺限制了其有效性。本文提出了Synthline，一种基于产品线的方法，利用大型语言模型系统地生成合成RE数据，适用于分类任务。通过在识别需求规范缺陷的背景下进行的实证评估，我们考察了生成数据的多样性及其在训练下游模型中的实用性。结果表明，尽管合成数据集的多样性低于真实数据，但仍可作为有效的训练资源。此外，合成数据与真实数据的结合显著提高了模型性能，混合方法在精度上提升了85%，召回率提高了2倍。这些发现展示了基于产品线的合成数据生成在解决RE数据稀缺问题上的潜力。我们公开了实现和生成的数据集，以支持领域内的可重复性和进步。

## 🔬 方法详解

**问题定义**：本文旨在解决需求工程中高质量数据集稀缺的问题。现有方法在缺乏足够真实数据的情况下，导致机器学习模型的训练效果不理想。

**核心思路**：Synthline采用产品线方法，利用大型语言模型生成合成需求工程数据，旨在系统性地提供足够的训练数据，以提高模型的性能。

**技术框架**：整体架构包括数据生成模块和模型训练模块。数据生成模块利用大型语言模型生成多样化的合成数据，模型训练模块则使用合成数据与真实数据结合进行训练。

**关键创新**：Synthline的核心创新在于结合产品线方法与大型语言模型，系统性地生成合成数据。这一方法与传统依赖真实数据的方式有本质区别，能够有效缓解数据稀缺问题。

**关键设计**：在合成数据生成过程中，采用特定的参数设置和损失函数，以确保生成数据的质量和多样性。模型训练时，结合合成数据与真实数据的混合策略，优化模型性能。

## 📊 实验亮点

实验结果表明，使用Synthline生成的合成数据与真实数据结合后，模型的精度提升了85%，召回率提高了2倍。这一显著的性能提升展示了合成数据在需求工程中的实际应用价值。

## 🎯 应用场景

该研究的潜在应用领域包括软件工程、需求分析和机器学习模型训练等。通过提供高质量的合成数据，Synthline可以帮助企业和研究机构在数据稀缺的情况下，提升需求工程的效率和准确性，推动相关领域的进一步发展。

## 📄 摘要（原文）

> While modern Requirements Engineering (RE) heavily relies on natural language processing and Machine Learning (ML) techniques, their effectiveness is limited by the scarcity of high-quality datasets. This paper introduces Synthline, a Product Line (PL) approach that leverages Large Language Models to systematically generate synthetic RE data for classification-based use cases. Through an empirical evaluation conducted in the context of using ML for the identification of requirements specification defects, we investigated both the diversity of the generated data and its utility for training downstream models. Our analysis reveals that while synthetic datasets exhibit less diversity than real data, they are good enough to serve as viable training resources. Moreover, our evaluation shows that combining synthetic and real data leads to substantial performance improvements. Specifically, hybrid approaches achieve up to 85% improvement in precision and a 2x increase in recall compared to models trained exclusively on real data. These findings demonstrate the potential of PL-based synthetic data generation to address data scarcity in RE. We make both our implementation and generated datasets publicly available to support reproducibility and advancement in the field.

