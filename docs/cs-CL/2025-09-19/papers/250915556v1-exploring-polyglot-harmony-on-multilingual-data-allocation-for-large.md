---
layout: default
title: "Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining"
---

# Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15556" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15556v1</a>
  <a href="https://arxiv.org/pdf/2509.15556.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15556v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15556v1', 'Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ping Guo, Yubing Ren, Binbin Liu, Fengze Liu, Haobin Lin, Yifan Zhang, Bingni Zhang, Taifeng Wang, Yin Zheng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**提出Climb框架，通过优化多语言数据分配提升大语言模型性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言学习` `大型语言模型` `数据分配` `跨语言交互` `预训练`

## 📋 核心要点

1. 现有方法在多语言LLM训练中难以确定最佳语言比例，忽略了跨语言交互和数据集规模的影响。
2. Climb框架通过引入跨语言交互感知语言比例，量化语言间的依赖关系，优化多语言数据分配。
3. 实验表明，Climb能准确衡量跨语言交互，提升LLM多语言性能，甚至媲美使用更多tokens训练的模型。

## 📝 摘要（中文）

大型语言模型（LLMs）已成为全球范围内各种应用不可或缺的一部分，从而推动了对有效多语言能力的空前全球需求。实现强大的多语言性能的关键在于训练语料库中语言比例的战略分配。然而，由于复杂的跨语言交互和对数据集规模的敏感性，确定最佳语言比例极具挑战性。本文介绍了一种名为Climb（跨语言交互感知多语言平衡）的新框架，旨在系统地优化多语言数据分配。Climb的核心是引入了一种跨语言交互感知语言比例，通过捕获语言间的依赖关系来显式量化每种语言的有效分配。利用该比例，Climb提出了一种原则性的两步优化程序——首先均衡各种语言的边际收益，然后最大化所得语言分配向量的大小——从而显著简化了固有多语言优化问题。大量实验证实，Climb可以准确衡量各种多语言环境下的跨语言交互。使用Climb导出的比例训练的LLM始终如一地实现了最先进的多语言性能，甚至实现了与使用更多tokens训练的开源LLM相媲美的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）多语言预训练中，如何确定各种语言的最佳数据分配比例的问题。现有方法通常难以处理复杂的跨语言交互，并且对数据集规模的敏感性较高，导致训练出的模型在多语言任务上的表现不佳。

**核心思路**：Climb框架的核心思路是引入“跨语言交互感知语言比例”这一概念，通过量化不同语言之间的依赖关系，更准确地评估每种语言对模型性能的贡献。基于此，Climb旨在优化语言分配，使得每种语言的边际收益相等，并最大化整体的语言分配向量，从而提升模型的多语言能力。

**技术框架**：Climb框架包含两个主要步骤：1) **跨语言交互感知语言比例计算**：该步骤旨在量化每种语言的有效分配，考虑了语言间的依赖关系。具体方法未知。2) **两步优化过程**：首先，均衡各种语言的边际收益，确保每种语言对模型性能的提升贡献相当；然后，最大化所得语言分配向量的大小，以充分利用所有语言的数据。

**关键创新**：Climb的关键创新在于其“跨语言交互感知语言比例”的概念，它能够更准确地衡量不同语言之间的相互影响，从而为多语言数据分配提供更合理的依据。与传统方法相比，Climb能够更好地捕捉语言间的复杂关系，从而提升模型的多语言性能。

**关键设计**：论文中并未详细描述跨语言交互感知语言比例的具体计算方法，以及两步优化过程中的具体参数设置和损失函数。这些细节可能包含在补充材料或后续研究中。具体网络结构未知。

## 📊 实验亮点

实验结果表明，使用Climb框架训练的LLM在多语言任务上取得了state-of-the-art的性能。更重要的是，Climb训练的模型甚至可以与使用更多tokens训练的开源LLM相媲美，这表明Climb在提升模型效率方面具有显著优势。具体性能数据未知。

## 🎯 应用场景

Climb框架可应用于各种需要多语言能力的大型语言模型预训练场景，例如机器翻译、跨语言信息检索、多语言文本生成等。通过优化多语言数据分配，Climb能够提升LLM在这些任务上的性能，从而为全球用户提供更优质的服务。该研究的成果有助于推动多语言自然语言处理技术的发展。

## 📄 摘要（原文）

> Large language models (LLMs) have become integral to a wide range of applications worldwide, driving an unprecedented global demand for effective multilingual capabilities. Central to achieving robust multilingual performance is the strategic allocation of language proportions within training corpora. However, determining optimal language ratios is highly challenging due to intricate cross-lingual interactions and sensitivity to dataset scale. This paper introduces Climb (Cross-Lingual Interaction-aware Multilingual Balancing), a novel framework designed to systematically optimize multilingual data allocation. At its core, Climb introduces a cross-lingual interaction-aware language ratio, explicitly quantifying each language's effective allocation by capturing inter-language dependencies. Leveraging this ratio, Climb proposes a principled two-step optimization procedure--first equalizing marginal benefits across languages, then maximizing the magnitude of the resulting language allocation vectors--significantly simplifying the inherently complex multilingual optimization problem. Extensive experiments confirm that Climb can accurately measure cross-lingual interactions across various multilingual settings. LLMs trained with Climb-derived proportions consistently achieve state-of-the-art multilingual performance, even achieving competitive performance with open-sourced LLMs trained with more tokens.

