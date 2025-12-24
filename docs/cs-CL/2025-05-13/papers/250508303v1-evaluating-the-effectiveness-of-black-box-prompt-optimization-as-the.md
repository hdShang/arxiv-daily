---
layout: default
title: Evaluating the Effectiveness of Black-Box Prompt Optimization as the Scale of LLMs Continues to Grow
---

# Evaluating the Effectiveness of Black-Box Prompt Optimization as the Scale of LLMs Continues to Grow

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08303" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08303v1</a>
  <a href="https://arxiv.org/pdf/2505.08303.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08303v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08303v1', 'Evaluating the Effectiveness of Black-Box Prompt Optimization as the Scale of LLMs Continues to Grow')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyu Zhou, Yihang Wu, Jingyuan Yang, Zhan Xiao, Rongjun Li

**分类**: cs.CL

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**评估黑箱提示优化在大规模LLM中的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `黑箱优化` `大型语言模型` `自然语言处理` `模型规模` `性能评估` `逆缩放规律` `提示优化`

## 📋 核心要点

1. 现有的黑箱提示优化方法在小规模模型上表现良好，但在大规模模型上效果有限，尚未得到充分验证。
2. 本文评估三种黑箱优化方法在大型LLM上的有效性，探讨模型规模对优化效果的影响。
3. 实验结果表明，随着模型规模的增加，黑箱优化方法的有效性显著降低，验证了模型规模对性能的影响。

## 📝 摘要（中文）

黑箱提示优化方法作为一种有前景的策略，旨在通过优化输入提示来更好地对齐大型语言模型（LLMs），从而提升其任务性能。尽管这些方法在小规模模型（如7B、14B）或早期版本（如GPT-3.5）上取得了良好效果，但在大规模模型（如DeepSeek V3，671B）上，其有效性仍然未知。本文选择三种知名的黑箱优化方法，在大型LLM（DeepSeek V3和Gemini 2.0 Flash）上进行评估，结果显示这些方法在大规模LLM上仅提供有限的性能提升。我们假设模型规模是导致观察到的有限收益的主要因素，并通过对不同规模的LLM（Qwen 2.5系列，7B至72B）进行实验，观察到黑箱优化方法的有效性随着模型规模的增加而减弱。

## 🔬 方法详解

**问题定义**：本文旨在解决黑箱提示优化方法在大规模语言模型中的有效性问题。现有研究主要集中在小规模模型上，缺乏对大规模模型的深入探讨。

**核心思路**：通过选择三种知名的黑箱优化方法，评估其在不同规模LLM上的性能，探索模型规模对优化效果的影响。

**技术框架**：研究采用了对比实验的方法，选取DeepSeek V3和Gemini 2.0 Flash作为大型LLM，使用四个自然语言理解（NLU）和自然语言生成（NLG）数据集进行评估。

**关键创新**：本文的创新点在于首次系统性地评估黑箱提示优化方法在超大规模LLM上的有效性，提出模型规模是影响优化效果的关键因素。

**关键设计**：实验中对不同规模的LLM（如Qwen 2.5系列，7B至72B）进行了对比，观察到黑箱优化方法的有效性随着模型规模的增加而减弱，验证了逆缩放规律。

## 📊 实验亮点

实验结果显示，黑箱提示优化方法在DeepSeek V3和Gemini 2.0 Flash等大规模LLM上仅提供有限的性能提升，且随着模型规模的增加，优化效果显著减弱，验证了模型规模对优化效果的影响。具体而言，随着模型规模从7B增加到72B，优化方法的有效性呈现出逆缩放规律。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等。通过优化大规模语言模型的输入提示，可以提升其在实际应用中的表现，进而推动智能系统的智能化和人机交互的自然性。未来，随着模型规模的进一步扩大，理解其优化机制将对模型的实际应用产生深远影响。

## 📄 摘要（原文）

> Black-Box prompt optimization methods have emerged as a promising strategy for refining input prompts to better align large language models (LLMs), thereby enhancing their task performance. Although these methods have demonstrated encouraging results, most studies and experiments have primarily focused on smaller-scale models (e.g., 7B, 14B) or earlier versions (e.g., GPT-3.5) of LLMs. As the scale of LLMs continues to increase, such as with DeepSeek V3 (671B), it remains an open question whether these black-box optimization techniques will continue to yield significant performance improvements for models of such scale. In response to this, we select three well-known black-box optimization methods and evaluate them on large-scale LLMs (DeepSeek V3 and Gemini 2.0 Flash) across four NLU and NLG datasets. The results show that these black-box prompt optimization methods offer only limited improvements on these large-scale LLMs. Furthermore, we hypothesize that the scale of the model is the primary factor contributing to the limited benefits observed. To explore this hypothesis, we conducted experiments on LLMs of varying sizes (Qwen 2.5 series, ranging from 7B to 72B) and observed an inverse scaling law, wherein the effectiveness of black-box optimization methods diminished as the model size increased.

