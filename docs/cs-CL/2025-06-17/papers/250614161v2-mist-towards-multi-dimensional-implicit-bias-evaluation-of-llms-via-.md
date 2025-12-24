---
layout: default
title: "MIST: Towards Multi-dimensional Implicit BiaS Evaluation of LLMs via Theory of Mind"
---

# MIST: Towards Multi-dimensional Implicit BiaS Evaluation of LLMs via Theory of Mind

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14161" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14161v2</a>
  <a href="https://arxiv.org/pdf/2506.14161.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14161v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14161v2', 'MIST: Towards Multi-dimensional Implicit BiaS Evaluation of LLMs via Theory of Mind')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanlin Li, Hao Liu, Huimin Liu, Kun Wang, Yinwei Wei, Yupeng Hu

**分类**: cs.CL

**发布日期**: 2025-06-17 (更新: 2025-10-08)

---

## 💡 一句话要点

**提出多维隐性偏见评估框架以解决大型语言模型的偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `隐性偏见` `心智理论` `刻板印象内容模型` `评估框架` `词汇联想测试` `情感归因测试` `多维评估`

## 📋 核心要点

1. 现有评估方法在识别大型语言模型的隐性偏见时存在局限，容易受到社会期望效应的影响，无法准确捕捉偏见的多维特性。
2. 本文提出的评估框架通过刻板印象内容模型，将偏见视为心智理论的多维失败，并设计了两个间接任务以探测隐性偏见。
3. 实验结果显示，该框架能够有效揭示复杂的偏见结构，提供了比传统方法更为全面的隐性偏见评估手段。

## 📝 摘要（中文）

大型语言模型（LLMs）中的心智理论（ToM）指的是其推理心理状态的能力，但这一能力的缺陷常常表现为系统性的隐性偏见。传统的直接查询方法在评估偏见时容易受到社会期望效应的影响，无法捕捉其微妙的多维特性。为此，本文提出了一种评估框架，利用刻板印象内容模型（SCM）将偏见重新概念化为ToM在能力、社交性和道德性方面的多维失败。该框架引入了两个间接任务：词汇联想偏见测试（WABT）用于评估隐性词汇联想，情感归因测试（AAT）用于测量隐性情感倾向，旨在探测潜在的刻板印象而不触发模型的回避反应。对8个最先进的LLMs进行的广泛实验表明，该框架能够揭示复杂的偏见结构，包括普遍的社交性偏见、多维偏离和不对称的刻板印象放大，从而提供了一种更稳健的方法来识别隐性偏见的结构特性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在心智理论推理中的隐性偏见评估问题。现有方法由于直接查询的局限性，无法有效捕捉偏见的微妙和多维特性。

**核心思路**：论文提出了一种基于刻板印象内容模型的评估框架，将偏见重新定义为心智理论在能力、社交性和道德性方面的多维失败，通过间接任务来探测隐性偏见。

**技术框架**：整体架构包括两个主要模块：词汇联想偏见测试（WABT）和情感归因测试（AAT）。WABT用于评估隐性词汇联想，AAT则用于测量潜在的情感倾向。

**关键创新**：最重要的技术创新在于将偏见视为多维的心智理论失败，并通过间接任务设计避免了传统方法的局限，能够更全面地揭示隐性偏见的结构。

**关键设计**：在任务设计中，WABT和AAT的具体实现细节包括词汇选择、情感标注和模型响应的分析方法，以确保能够有效探测潜在的刻板印象而不引发模型的回避反应。

## 📊 实验亮点

实验结果表明，提出的评估框架能够有效揭示复杂的偏见结构，包括普遍的社交性偏见和多维偏离。与传统方法相比，该框架在识别隐性偏见方面的表现显著提升，能够更全面地反映模型的偏见特征。

## 🎯 应用场景

该研究的评估框架可广泛应用于大型语言模型的偏见检测与修正，尤其在社会科学、心理学和人工智能伦理等领域具有重要的实际价值。未来，该框架有望推动更公平和透明的AI系统设计，减少模型在实际应用中的偏见表现。

## 📄 摘要（原文）

> Theory of Mind (ToM) in Large Language Models (LLMs) refers to their capacity for reasoning about mental states, yet failures in this capacity often manifest as systematic implicit bias. Evaluating this bias is challenging, as conventional direct-query methods are susceptible to social desirability effects and fail to capture its subtle, multi-dimensional nature. To this end, we propose an evaluation framework that leverages the Stereotype Content Model (SCM) to reconceptualize bias as a multi-dimensional failure in ToM across Competence, Sociability, and Morality. The framework introduces two indirect tasks: the Word Association Bias Test (WABT) to assess implicit lexical associations and the Affective Attribution Test (AAT) to measure covert affective leanings, both designed to probe latent stereotypes without triggering model avoidance. Extensive experiments on 8 State-of-the-Art LLMs demonstrate our framework's capacity to reveal complex bias structures, including pervasive sociability bias, multi-dimensional divergence, and asymmetric stereotype amplification, thereby providing a more robust methodology for identifying the structural nature of implicit bias.

