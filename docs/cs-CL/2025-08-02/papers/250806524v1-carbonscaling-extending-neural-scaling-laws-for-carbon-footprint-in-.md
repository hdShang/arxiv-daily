---
layout: default
title: "CarbonScaling: Extending Neural Scaling Laws for Carbon Footprint in Large Language Models"
---

# CarbonScaling: Extending Neural Scaling Laws for Carbon Footprint in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06524" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06524v1</a>
  <a href="https://arxiv.org/pdf/2508.06524.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06524v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06524v1', 'CarbonScaling: Extending Neural Scaling Laws for Carbon Footprint in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lei Jiang, Fan Chen

**分类**: cs.CL, cs.AI, cs.CY, cs.DC, cs.LG

**发布日期**: 2025-08-02

**备注**: 8 pages

---

## 💡 一句话要点

**提出CarbonScaling框架以解决大型语言模型的碳足迹问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `碳足迹` `大型语言模型` `神经扩展法则` `可持续AI` `训练优化`

## 📋 核心要点

1. 现有的神经扩展法则未考虑大型语言模型训练中的碳排放问题，导致对环境影响的忽视。
2. 论文提出CarbonScaling框架，通过整合多种模型，定量分析模型准确性与碳足迹之间的关系。
3. 实验结果显示，虽然准确性与碳排放之间存在幂律关系，但实际低效显著增加了扩展因子，优化措施能有效降低碳排放。

## 📝 摘要（中文）

神经网络扩展法则推动了大型语言模型（LLMs）的发展，将准确性提升与参数数量、数据集规模和计算能力的增长联系起来。然而，这些法则忽视了与LLM规模呈指数增长的碳排放。本文提出了CarbonScaling，一个分析框架，扩展了神经扩展法则，以纳入LLM训练中的操作碳和隐含碳。通过整合神经扩展模型、GPU硬件演变、并行优化和碳估算，CarbonScaling定量连接了模型准确性与碳足迹。结果表明，尽管准确性与碳之间存在幂律关系，但现实中的低效显著增加了扩展因子。硬件技术扩展降低了小到中型模型的碳排放，但对于极大型LLMs，由于通信开销和GPU利用不足，收益递减。训练优化，特别是激进的关键批量大小扩展，有助于缓解这种低效。CarbonScaling为训练更可持续和碳高效的LLMs提供了关键见解。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型训练过程中碳排放未被充分考虑的问题。现有方法未能量化模型规模与碳足迹之间的关系，导致环境影响评估不足。

**核心思路**：CarbonScaling框架通过整合神经扩展法则、GPU硬件演变、并行优化和碳估算模型，建立了模型准确性与碳排放之间的定量联系，从而为可持续训练提供指导。

**技术框架**：该框架包括四个主要模块：1) 神经扩展模型，分析参数与准确性的关系；2) GPU硬件演变模型，评估技术进步对碳排放的影响；3) 并行优化模块，优化训练过程中的资源利用；4) 碳估算模型，量化训练过程中的碳排放。

**关键创新**：CarbonScaling的创新在于将碳排放纳入神经扩展法则的分析中，揭示了在不同规模模型中碳排放的非线性特征，与传统方法相比，提供了更全面的环境影响评估。

**关键设计**：在设计中，采用了关键批量大小扩展策略，以提高训练效率并降低碳排放。此外，模型中还考虑了GPU利用率和通信开销等因素，以优化整体训练过程。

## 📊 实验亮点

实验结果表明，尽管准确性与碳排放之间存在幂律关系，但实际的低效使得扩展因子显著增加。通过优化训练过程，尤其是批量大小的调整，能够有效降低碳排放，提升模型的环境友好性。

## 🎯 应用场景

CarbonScaling框架可广泛应用于大型语言模型的训练与优化，尤其是在需要考虑环境影响的场景中。该研究为开发更可持续的AI系统提供了理论基础，未来可能推动行业标准的制定，促进绿色计算的发展。

## 📄 摘要（原文）

> Neural scaling laws have driven the development of increasingly large language models (LLMs) by linking accuracy improvements to growth in parameter count, dataset size, and compute. However, these laws overlook the carbon emissions that scale exponentially with LLM size. This paper presents \textit{CarbonScaling}, an analytical framework that extends neural scaling laws to incorporate both operational and embodied carbon in LLM training. By integrating models for neural scaling, GPU hardware evolution, parallelism optimization, and carbon estimation, \textit{CarbonScaling} quantitatively connects model accuracy to carbon footprint. Results show that while a power-law relationship between accuracy and carbon holds, real-world inefficiencies significantly increase the scaling factor. Hardware technology scaling reduces carbon emissions for small to mid-sized models, but offers diminishing returns for extremely large LLMs due to communication overhead and underutilized GPUs. Training optimizations-especially aggressive critical batch size scaling-help alleviate this inefficiency. \textit{CarbonScaling} offers key insights for training more sustainable and carbon-efficient LLMs.

