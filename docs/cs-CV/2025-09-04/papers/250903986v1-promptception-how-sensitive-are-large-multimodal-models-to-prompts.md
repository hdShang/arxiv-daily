---
layout: default
title: "Promptception: How Sensitive Are Large Multimodal Models to Prompts?"
---

# Promptception: How Sensitive Are Large Multimodal Models to Prompts?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03986" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03986v1</a>
  <a href="https://arxiv.org/pdf/2509.03986.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03986v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03986v1', 'Promptception: How Sensitive Are Large Multimodal Models to Prompts?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohamed Insaf Ismithdeen, Muhammad Uzair Khattak, Salman Khan

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-09-04

**备注**: Accepted to EMNLP 2025

---

## 💡 一句话要点

**Promptception框架揭示多模态大模型对提示词的敏感性，并提出优化原则。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大模型` `提示词工程` `敏感性分析` `多项选择问答` `模型评估`

## 📋 核心要点

1. 现有LMM评估中，提示词的微小变化可能导致模型性能显著波动，影响评估的公平性和透明性。
2. Promptception框架通过系统性地测试不同类型的提示词，量化LMM对提示词的敏感程度。
3. 实验表明，专有模型对提示词更敏感，而开源模型更稳定，并据此提出了针对不同类型LMM的提示原则。

## 📝 摘要（中文）

近年来，大型多模态模型（LMMs）取得了显著进展，但针对多项选择问答（MCQA）任务的LMM提示词设计仍然缺乏深入理解。研究表明，即使提示词的措辞和结构发生细微变化，也可能导致某些提示词和模型的准确率偏差高达15%。这种可变性对透明和公平的LMM评估构成了挑战，因为模型通常会报告使用精心选择的提示词获得的最佳性能。为了解决这个问题，本文提出了Promptception，一个用于评估LMM中提示词敏感性的系统框架。它包含61种提示词类型，涵盖15个类别和6个超类别，每个类别都针对提示词制定的特定方面。该框架用于评估10个LMM，范围从轻量级开源模型到GPT-4o和Gemini 1.5 Pro，并使用MMStar、MMMU-Pro、MVBench这3个MCQA基准。研究结果表明，专有模型对提示词措辞的敏感性更高，反映了与指令语义的更紧密对齐，而开源模型则更稳定，但在细致和复杂的措辞方面表现不佳。基于此分析，本文提出了针对专有和开源LMM量身定制的提示原则，从而实现更强大和公平的模型评估。

## 🔬 方法详解

**问题定义**：论文旨在解决大型多模态模型（LMMs）在多项选择问答（MCQA）任务中，性能对提示词的敏感性问题。现有方法通常依赖于精心设计的少量提示词来评估模型，忽略了提示词的微小变化可能带来的性能波动，导致评估结果缺乏可靠性和公平性。

**核心思路**：论文的核心思路是通过构建一个全面的提示词集合，系统性地评估LMM对不同类型提示词的敏感程度。通过分析模型在不同提示词下的性能表现，揭示模型对提示词的依赖性，并据此提出更鲁棒的评估方法和提示词设计原则。

**技术框架**：Promptception框架包含以下几个主要组成部分：1) 提示词集合构建：设计了61种提示词类型，涵盖15个类别和6个超类别，针对提示词的不同方面进行测试。2) 模型评估：使用构建的提示词集合，在多个MCQA基准数据集上评估不同的LMM。3) 敏感性分析：分析模型在不同提示词下的性能表现，量化模型对提示词的敏感程度。4) 提示原则：基于分析结果，提出针对不同类型LMM的提示原则。

**关键创新**：该论文最重要的技术创新在于提出了一个系统性的框架，用于评估LMM对提示词的敏感性。与现有方法相比，Promptception框架更加全面和系统，能够更准确地评估模型的性能，并为提示词设计提供指导。

**关键设计**：Promptception框架的关键设计包括：1) 提示词集合的设计：提示词集合的设计需要覆盖提示词的各个方面，包括措辞、结构、上下文等。2) 评估指标的选择：评估指标需要能够准确地反映模型在不同提示词下的性能表现。3) 敏感性分析方法：敏感性分析方法需要能够量化模型对提示词的敏感程度。

## 📊 实验亮点

实验结果表明，专有模型（如GPT-4o和Gemini 1.5 Pro）对提示词措辞的敏感性高于开源模型，但开源模型在处理复杂提示词时表现较差。某些提示词的微小变化会导致模型准确率偏差高达15%。基于这些发现，论文提出了针对专有和开源LMM的提示原则，为更公平和鲁棒的模型评估提供了指导。

## 🎯 应用场景

该研究成果可应用于多模态大模型的评测基准构建、模型鲁棒性提升和提示词工程优化。通过Promptception框架，可以更全面地评估模型的性能，发现模型的弱点，并据此改进模型的设计和训练。此外，该研究提出的提示原则可以指导用户设计更有效的提示词，提高模型在实际应用中的性能。

## 📄 摘要（原文）

> Despite the success of Large Multimodal Models (LMMs) in recent years, prompt design for LMMs in Multiple-Choice Question Answering (MCQA) remains poorly understood. We show that even minor variations in prompt phrasing and structure can lead to accuracy deviations of up to 15% for certain prompts and models. This variability poses a challenge for transparent and fair LMM evaluation, as models often report their best-case performance using carefully selected prompts. To address this, we introduce Promptception, a systematic framework for evaluating prompt sensitivity in LMMs. It consists of 61 prompt types, spanning 15 categories and 6 supercategories, each targeting specific aspects of prompt formulation, and is used to evaluate 10 LMMs ranging from lightweight open-source models to GPT-4o and Gemini 1.5 Pro, across 3 MCQA benchmarks: MMStar, MMMU-Pro, MVBench. Our findings reveal that proprietary models exhibit greater sensitivity to prompt phrasing, reflecting tighter alignment with instruction semantics, while open-source models are steadier but struggle with nuanced and complex phrasing. Based on this analysis, we propose Prompting Principles tailored to proprietary and open-source LMMs, enabling more robust and fair model evaluation.

