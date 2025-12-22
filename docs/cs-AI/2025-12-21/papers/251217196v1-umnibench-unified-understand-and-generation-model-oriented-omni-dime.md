---
layout: default
title: UmniBench: Unified Understand and Generation Model Oriented Omni-dimensional Benchmark
---

# UmniBench: Unified Understand and Generation Model Oriented Omni-dimensional Benchmark

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17196" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17196v1</a>
  <a href="https://arxiv.org/pdf/2512.17196.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17196v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17196v1', 'UmniBench: Unified Understand and Generation Model Oriented Omni-dimensional Benchmark')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai Liu, Leyang Chen, Wenbo Li, Zhikai Chen, Zhixin Wang, Renjing Pei, Linghe Kong, Yulun Zhang

**分类**: cs.AI

**发布日期**: 2025-12-19

**备注**: Project Page: https://umnibench.github.io/

---

## 💡 一句话要点

**提出 UmniBench，用于统一多模态模型在理解、生成和编辑能力上的全面评估。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `统一多模态模型` `多模态评估` `理解能力` `生成能力` `编辑能力` `基准测试` `自评估`

## 📋 核心要点

1. 现有统一多模态模型（UMM）的评估方式割裂，缺乏统一的基准来同时评估理解、生成和编辑能力。
2. UmniBench 提出了一种新的评估范式，利用 UMM 本身来评估其生成和编辑能力，同时结合理解能力进行综合评估。
3. UmniBench 覆盖 13 个领域和 200 多个概念，并对 24 个模型进行了基准测试，为 UMM 的发展提供支持。

## 📝 摘要（中文）

统一多模态理解和生成在先进的专有系统中展现了令人印象深刻的能力。然而，统一多模态模型（UMM）的评估仍然是分离的，使用相应的数据集分别评估其理解和生成能力。为了解决这个问题，我们提出了 UmniBench，这是一个为 UMM 量身定制的基准，具有全方位评估能力。首先，UmniBench 可以在单个评估过程中评估理解、生成和编辑能力。基于人工检查的提示和问答对，UmniBench 利用 UMM 本身来评估其生成和编辑能力以及理解能力。这种简单而有效的范例可以对 UMM 进行全面评估。其次，UmniBench 涵盖 13 个主要领域和 200 多个概念，确保对 UMM 进行彻底检查。此外，UmniBench 还可以分离并分别评估理解、生成和编辑能力，从而提供细粒度的评估。基于 UmniBench，我们对 24 个流行的模型进行了基准测试，包括 UMM 和单能力大型模型。我们希望这个基准能够为统一模型提供更全面和客观的视角，并为提高社区模型的性能提供后勤支持。

## 🔬 方法详解

**问题定义**：现有统一多模态模型（UMM）的评估通常是分离的，即使用不同的数据集和指标分别评估模型的理解和生成能力。这种评估方式无法全面反映 UMM 的综合能力，也难以发现模型在不同能力之间的潜在关联和瓶颈。此外，缺乏统一的基准使得不同 UMM 之间的比较变得困难。现有方法的痛点在于缺乏一个能够同时评估理解、生成和编辑能力，并提供细粒度评估结果的基准。

**核心思路**：UmniBench 的核心思路是利用 UMM 自身的能力来评估其性能。具体来说，它基于人工设计的提示和问答对，让 UMM 生成答案或编辑内容，然后利用 UMM 自身的理解能力来评估生成或编辑结果的质量。这种自评估的方式可以避免引入额外的评估模型，并能够更直接地反映 UMM 的真实能力。 这种设计思路的优势在于简单有效，能够全面评估 UMM 的各项能力。

**技术框架**：UmniBench 的整体框架包括以下几个主要部分：1) 数据集构建：构建包含 13 个领域和 200 多个概念的提示和问答对数据集。2) 评估流程：针对每个提示，让 UMM 生成答案或编辑内容。3) 自评估：利用 UMM 自身的理解能力评估生成或编辑结果的质量。4) 结果分析：对评估结果进行统计分析，提供细粒度的性能报告。该框架支持对理解、生成和编辑能力进行联合评估，也支持对各项能力进行单独评估。

**关键创新**：UmniBench 的最重要创新点在于其自评估的范式。与传统的依赖外部评估模型的方法不同，UmniBench 利用 UMM 自身的能力来评估其生成和编辑结果。这种自评估的方式可以更直接地反映 UMM 的真实能力，并避免引入额外的偏差。此外，UmniBench 还通过构建包含多个领域和概念的综合数据集，实现了对 UMM 的全面评估。

**关键设计**：UmniBench 的关键设计包括：1) 人工设计的提示和问答对，确保评估的准确性和可靠性。2) 基于 UMM 自身的理解能力构建的评估指标，例如，使用 UMM 判断生成答案与正确答案的相似度。3) 细粒度的性能报告，提供对 UMM 在不同领域和概念上的性能分析。 4) 评估指标的设计需要仔细考虑，以确保能够准确反映 UMM 的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17196v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17196v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17196v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

UmniBench 对 24 个流行的模型进行了基准测试，包括 UMM 和单能力大型模型。实验结果表明，不同的模型在不同的领域和能力上表现出不同的优势和劣势。UmniBench 能够提供细粒度的性能报告，帮助研究人员深入了解模型的性能特点，并为模型改进提供指导。

## 🎯 应用场景

UmniBench 可用于评估和比较不同的统一多模态模型，帮助研究人员和开发者选择合适的模型并改进其性能。该基准还可以用于诊断 UMM 的弱点，指导模型架构设计和训练策略的优化。此外，UmniBench 有助于推动多模态理解和生成技术在智能助手、图像编辑、内容创作等领域的应用。

## 📄 摘要（原文）

> Unifying multimodal understanding and generation has shown impressive capabilities in cutting-edge proprietary systems. However, evaluations of unified multimodal models (UMMs) remain decoupled, assessing their understanding and generation abilities separately with corresponding datasets. To address this, we propose UmniBench, a benchmark tailored for UMMs with omni-dimensional evaluation. First, UmniBench can assess the understanding, generation, and editing ability within a single evaluation process. Based on human-examined prompts and QA pairs, UmniBench leverages UMM itself to evaluate its generation and editing ability with its understanding ability. This simple but effective paradigm allows comprehensive evaluation of UMMs. Second, UmniBench covers 13 major domains and more than 200 concepts, ensuring a thorough inspection of UMMs. Moreover, UmniBench can also decouple and separately evaluate understanding, generation, and editing abilities, providing a fine-grained assessment. Based on UmniBench, we benchmark 24 popular models, including both UMMs and single-ability large models. We hope this benchmark provides a more comprehensive and objective view of unified models and logistical support for improving the performance of the community model.

