---
layout: default
title: "CoTox: Chain-of-Thought-Based Molecular Toxicity Reasoning and Prediction"
---

# CoTox: Chain-of-Thought-Based Molecular Toxicity Reasoning and Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03159" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03159v2</a>
  <a href="https://arxiv.org/pdf/2508.03159.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03159v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03159v2', 'CoTox: Chain-of-Thought-Based Molecular Toxicity Reasoning and Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jueon Park, Yein Park, Minju Song, Soyon Park, Donghyeon Lee, Seungheun Baek, Jaewoo Kang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-05 (更新: 2025-11-05)

**备注**: Accepted to IEEE BIBM 2025

**🔗 代码/项目**: [GITHUB](https://github.com/dmis-lab/CoTox)

---

## 💡 一句话要点

**提出CoTox框架以解决药物毒性预测的可解释性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `药物毒性预测` `大语言模型` `链式推理` `生物信息学` `可解释性` `机器学习` `药物开发`

## 📋 核心要点

1. 现有机器学习模型在药物毒性预测中依赖标注数据，缺乏可解释性，难以捕捉复杂的生物机制。
2. CoTox框架结合大语言模型与链式推理，通过整合化学结构、生物通路和GO术语生成可解释的毒性预测。
3. 实验表明，CoTox在多种大语言模型中表现优异，尤其在使用IUPAC名称表示化学结构时，预测性能显著提升。

## 📝 摘要（中文）

药物毒性预测在药物开发中仍然是一个重大挑战。尽管近期机器学习模型在体外毒性预测上有所进展，但对标注数据的依赖和缺乏可解释性限制了其应用。为了解决这一问题，本文提出了CoTox，一个将大语言模型与链式推理相结合的多毒性预测框架。CoTox通过逐步推理结合化学结构数据、生物通路和基因本体（GO）术语，生成可解释的毒性预测。实验结果表明，CoTox在性能上优于传统机器学习和深度学习模型，且在药物开发中具有实用价值。

## 🔬 方法详解

**问题定义**：本文旨在解决药物毒性预测中的可解释性不足和对标注数据的依赖问题。现有方法难以捕捉由复杂生物机制驱动的器官特异性毒性。

**核心思路**：CoTox框架通过链式推理结合大语言模型，整合化学结构、生物通路和基因本体信息，生成逐步推理的毒性预测，从而提高可解释性。

**技术框架**：CoTox的整体架构包括数据输入模块（化学结构、通路和GO术语）、推理模块（链式推理过程）和输出模块（毒性预测结果），通过GPT-4o实现。

**关键创新**：CoTox的主要创新在于将大语言模型与生物学背景结合，提供透明的推理过程，与传统方法相比，显著提高了毒性预测的可解释性和准确性。

**关键设计**：在模型设计中，使用IUPAC名称表示化学结构，使得模型更易理解，此外，采用了适合生物学背景的损失函数和网络结构，以优化推理过程。

## 📊 实验亮点

实验结果显示，CoTox在多种大语言模型中均表现优异，尤其在使用IUPAC名称时，模型的推理能力和预测性能显著提升。与传统机器学习和深度学习模型相比，CoTox的性能提升明显，展示了其在药物毒性预测中的实际应用价值。

## 🎯 应用场景

CoTox框架在药物开发中具有广泛的应用潜力，能够为早期药物安全性评估提供支持。通过生成与生理反应一致的毒性预测，CoTox有助于提高药物研发的效率和安全性，降低潜在的药物安全风险。

## 📄 摘要（原文）

> Drug toxicity remains a major challenge in pharmaceutical development. Recent machine learning models have improved in silico toxicity prediction, but their reliance on annotated data and lack of interpretability limit their applicability. This limits their ability to capture organ-specific toxicities driven by complex biological mechanisms. Large language models (LLMs) offer a promising alternative through step-by-step reasoning and integration of textual data, yet prior approaches lack biological context and transparent rationale. To address this issue, we propose CoTox, a novel framework that integrates LLM with chain-of-thought (CoT) reasoning for multi-toxicity prediction. CoTox combines chemical structure data, biological pathways, and gene ontology (GO) terms to generate interpretable toxicity predictions through step-by-step reasoning. Using GPT-4o, we show that CoTox outperforms both traditional machine learning and deep learning model. We further examine its performance across various LLMs to identify where CoTox is most effective. Additionally, we find that representing chemical structures with IUPAC names, which are easier for LLMs to understand than SMILES, enhances the model's reasoning ability and improves predictive performance. To demonstrate its practical utility in drug development, we simulate the treatment of relevant cell types with drug and incorporated the resulting biological context into the CoTox framework. This approach allow CoTox to generate toxicity predictions aligned with physiological responses, as shown in case study. This result highlights the potential of LLM-based frameworks to improve interpretability and support early-stage drug safety assessment. The code and prompt used in this work are available at https://github.com/dmis-lab/CoTox.

