---
layout: default
title: "More or Less Wrong: A Benchmark for Directional Bias in LLM Comparative Reasoning"
---

# More or Less Wrong: A Benchmark for Directional Bias in LLM Comparative Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03923" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03923v1</a>
  <a href="https://arxiv.org/pdf/2506.03923.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03923v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03923v1', 'More or Less Wrong: A Benchmark for Directional Bias in LLM Comparative Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammadamin Shafiei, Hamidreza Saffari, Nafise Sadat Moosavi

**分类**: cs.CL

**发布日期**: 2025-06-04

---

## 💡 一句话要点

**提出MathComp基准以解决LLM比较推理中的方向性偏差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `比较推理` `方向性偏差` `语义框架` `链式思维提示` `MathComp基准` `公平性评估`

## 📋 核心要点

1. 现有大型语言模型在处理比较数学问题时，容易受到输入措辞的影响，导致方向性偏差。
2. 本文提出MathComp基准，通过300个比较场景和14种提示变体，系统性研究语言引导对推理的影响。
3. 实验结果显示，链式思维提示能减少偏差，但效果因推理形式而异，且人口身份术语会加剧方向性漂移。

## 📝 摘要（中文）

大型语言模型（LLMs）对输入措辞敏感，但语义线索如何影响推理机制尚不清楚。本文在比较数学问题的背景下研究这一现象，揭示出一种一致且方向性的框架偏差：包含“更多”、“更少”或“相等”等词语的逻辑等价问题，系统性地引导预测朝向框架术语的方向。为研究这一效应，本文引入了MathComp，一个包含300个比较场景的控制基准，每个场景在三种LLM家族下评估14种提示变体。研究发现，模型错误常常反映语言引导，系统性地偏向提示中存在的比较术语。链式思维提示可以减少这些偏差，但其有效性有所不同：自由形式的推理更为稳健，而结构化格式可能保留或重新引入方向性漂移。最后，研究表明在输入场景中包含人口身份术语（如“女性”、“黑人”）会放大方向性漂移，尽管基础数量相同，突显了语义框架与社会参照之间的相互作用。这些发现揭示了标准评估中的关键盲点，并推动了针对推理稳健性和公平性的框架感知基准的建立。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在比较推理中存在的方向性偏差问题，现有方法未能充分理解语义线索对推理的影响。

**核心思路**：通过引入MathComp基准，系统性地评估不同提示对模型推理的影响，揭示语言引导的机制。

**技术框架**：整体架构包括300个比较场景，每个场景在三种LLM家族下评估14种提示变体，分析模型输出与输入提示的关系。

**关键创新**：最重要的技术创新在于识别并量化语言引导对模型推理的影响，尤其是比较术语的作用，这在现有研究中尚未得到充分探讨。

**关键设计**：在实验中，采用了多种提示变体和链式思维提示，分析其对模型输出的影响，特别关注自由形式推理与结构化格式的表现差异。

## 📊 实验亮点

实验结果显示，链式思维提示能够有效减少方向性偏差，尤其在自由形式推理中表现更为稳健。相比之下，结构化格式可能会保留或重新引入偏差。此外，包含人口身份术语的输入场景显著加剧了方向性漂移，强调了语义框架与社会参照的相互作用。

## 🎯 应用场景

该研究的潜在应用领域包括教育、心理学和社会科学等，能够帮助设计更公平和稳健的语言模型，减少因措辞引起的偏差，从而提高模型在实际应用中的可靠性和公正性。

## 📄 摘要（原文）

> Large language models (LLMs) are known to be sensitive to input phrasing, but the mechanisms by which semantic cues shape reasoning remain poorly understood. We investigate this phenomenon in the context of comparative math problems with objective ground truth, revealing a consistent and directional framing bias: logically equivalent questions containing the words ``more'', ``less'', or ``equal'' systematically steer predictions in the direction of the framing term. To study this effect, we introduce MathComp, a controlled benchmark of 300 comparison scenarios, each evaluated under 14 prompt variants across three LLM families. We find that model errors frequently reflect linguistic steering, systematic shifts toward the comparative term present in the prompt. Chain-of-thought prompting reduces these biases, but its effectiveness varies: free-form reasoning is more robust, while structured formats may preserve or reintroduce directional drift. Finally, we show that including demographic identity terms (e.g., ``a woman'', ``a Black person'') in input scenarios amplifies directional drift, despite identical underlying quantities, highlighting the interplay between semantic framing and social referents. These findings expose critical blind spots in standard evaluation and motivate framing-aware benchmarks for diagnosing reasoning robustness and fairness in LLMs.

