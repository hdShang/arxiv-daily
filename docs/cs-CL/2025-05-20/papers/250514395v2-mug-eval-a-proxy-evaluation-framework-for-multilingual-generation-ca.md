---
layout: default
title: "MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language"
---

# MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14395" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14395v2</a>
  <a href="https://arxiv.org/pdf/2505.14395.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14395v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14395v2', 'MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seyoung Song, Seogyeong Jeong, Eunsu Kim, Jiho Jin, Dongkwan Kim, Jay Shin, Alice Oh

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-09-19)

**备注**: To appear in Findings of EMNLP 2025

**DOI**: [10.18653/v1/2025.findings-emnlp.1061](https://doi.org/10.18653/v1/2025.findings-emnlp.1061)

---

## 💡 一句话要点

**提出MUG-Eval框架以评估多语言生成能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言生成` `评估框架` `大型语言模型` `低资源语言` `对话任务` `任务成功率` `自然语言处理` `标准化比较`

## 📋 核心要点

1. 现有评估方法在低资源语言中的应用有限，导致对多语言生成能力的评估面临挑战。
2. MUG-Eval框架通过将基准转化为对话任务，使用任务成功率作为评估指标，避免了对特定工具和数据集的依赖。
3. 在30种语言上评估8个LLMs，MUG-Eval与传统基准的相关性超过0.75，提供了标准化比较的可能性。

## 📝 摘要（中文）

评估大型语言模型（LLMs）的文本生成能力尤其在低资源语言中面临挑战，现有的直接评估方法稀缺。本文提出了MUG-Eval，一个新颖的框架，通过将现有基准转化为对话任务来评估LLMs的多语言生成能力，并测量其在这些任务上的准确性。我们设计的对话任务要求在目标语言中有效沟通，并使用任务成功率作为成功对话生成的代理指标。该方法具有两个主要优点：不依赖于特定语言的NLP工具或注释数据集，且不依赖于LLMs作为评判者。我们在30种语言上评估了8个LLMs，发现MUG-Eval与已建立的基准高度相关（$r$ > 0.75），并能够实现跨语言和模型的标准化比较。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多语言生成能力评估中的不足，尤其是在低资源语言中缺乏有效的评估方法。现有方法往往依赖于特定的NLP工具或高资源语言的评估标准，限制了其适用性。

**核心思路**：MUG-Eval框架通过将现有的评估基准转化为对话任务，设计出需要在目标语言中进行有效沟通的任务，从而使用任务成功率作为生成能力的代理指标。这种设计使得评估不再依赖于特定语言的工具和数据集。

**技术框架**：MUG-Eval的整体架构包括任务设计、执行和评估三个主要模块。首先，设计对话任务以适应不同语言的特点；其次，执行这些任务并收集生成结果；最后，通过计算任务成功率来评估生成能力。

**关键创新**：MUG-Eval的主要创新在于其不依赖于语言特定的工具和注释数据集，且不需要LLMs作为评判者，从而克服了现有方法的局限性。

**关键设计**：在设计过程中，任务成功率被选为评估指标，确保了评估的简洁性和有效性。此外，框架的灵活性使其能够扩展到数千种语言，具有广泛的适用性。

## 📊 实验亮点

在对8个大型语言模型的评估中，MUG-Eval在30种语言上表现出与传统基准的高度相关性（$r$ > 0.75），显示出其作为多语言生成能力评估工具的有效性和可靠性。这一结果表明，MUG-Eval能够实现跨语言和模型的标准化比较，具有重要的研究价值。

## 🎯 应用场景

MUG-Eval框架具有广泛的应用潜力，尤其是在多语言生成任务的评估中。它可以被用于低资源语言的研究，帮助开发更具包容性的语言模型。此外，该框架的标准化评估方法也可以促进跨语言模型的比较和优化，推动多语言处理技术的发展。

## 📄 摘要（原文）

> Evaluating text generation capabilities of large language models (LLMs) is challenging, particularly for low-resource languages where methods for direct assessment are scarce. We propose MUG-Eval, a novel framework that evaluates LLMs' multilingual generation capabilities by transforming existing benchmarks into conversational tasks and measuring the LLMs' accuracies on those tasks. We specifically designed these conversational tasks to require effective communication in the target language. Then, we simply use task success rate as a proxy for successful conversation generation. Our approach offers two key advantages: it is independent of language-specific NLP tools or annotated datasets, which are limited for most languages, and it does not rely on LLMs-as-judges, whose evaluation quality degrades outside a few high-resource languages. We evaluate 8 LLMs across 30 languages spanning high, mid, and low-resource categories, and we find that MUG-Eval correlates strongly with established benchmarks ($r$ > 0.75) while enabling standardized comparisons across languages and models. Our framework provides a robust and resource-efficient solution for evaluating multilingual generation that can be extended to thousands of languages.

