---
layout: default
title: "Towards Fair Rankings: Leveraging LLMs for Gender Bias Detection and Measurement"
---

# Towards Fair Rankings: Leveraging LLMs for Gender Bias Detection and Measurement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22372" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22372v1</a>
  <a href="https://arxiv.org/pdf/2506.22372.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22372v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22372v1', 'Towards Fair Rankings: Leveraging LLMs for Gender Bias Detection and Measurement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maryam Mousavian, Zahra Abbasiantaeb, Mohammad Aliannejadi, Fabio Crestani

**分类**: cs.IR, cs.CL

**发布日期**: 2025-06-27

**备注**: Accepted by ACM SIGIR Conference on Innovative Concepts and Theories in Information Retrieval (ICTIR 2025)

**DOI**: [10.1145/3731120.3744620](https://doi.org/10.1145/3731120.3744620)

---

## 💡 一句话要点

**利用大型语言模型检测和测量性别偏见以实现公平排名**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `性别偏见` `大型语言模型` `信息检索` `公平性评估` `自然语言处理` `数据集构建` `算法公平性`

## 📋 核心要点

1. 现有的性别公平度量方法主要依赖于词汇和频率基础的测量，无法有效捕捉微妙的性别差异。
2. 本文提出了一种基于大型语言模型的性别偏见检测方法，并引入了新的性别公平度量CWEx，以克服现有方法的不足。
3. 实验结果显示，所提度量在公平性评估上比之前的度量更为详细，与人类标签的对齐度显著提高。

## 📝 摘要（中文）

社会偏见在自然语言处理和信息检索系统中的存在是一个持续的挑战，这凸显了开发强大方法以识别和评估这些偏见的重要性。本文旨在通过利用大型语言模型（LLMs）来检测和测量段落排名中的性别偏见。现有的性别公平度量依赖于词汇和频率基础的测量，导致各种局限性，例如错过微妙的性别差异。基于我们的LLM性别偏见检测方法，我们提出了一种新的性别公平度量，称为类加权曝光（CWEx），旨在解决现有的局限性。为了测量我们提出的度量的有效性并研究LLMs在检测性别偏见方面的有效性，我们对MS MARCO段落排名集合的一个子集进行了标注，并发布了新的性别偏见集合MSMGenderBias，以促进该领域未来的研究。我们的广泛实验结果表明，我们提出的度量提供了比以前的度量更详细的公平性评估，且与人类标签的对齐度有显著改善。

## 🔬 方法详解

**问题定义**：本文解决的是自然语言处理和信息检索系统中的性别偏见检测与测量问题。现有方法在捕捉微妙性别差异方面存在局限性，导致偏见评估不够全面。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）进行性别偏见的检测，并提出一种新的性别公平度量CWEx，以更准确地评估性别偏见的存在。通过这种方式，能够更好地识别和量化性别偏见。

**技术框架**：研究首先对MS MARCO段落排名集合的子集进行标注，构建新的性别偏见数据集MSMGenderBias。然后，利用LLMs进行性别偏见检测，并通过CWEx度量进行评估。

**关键创新**：最重要的技术创新点在于提出了CWEx这一新的性别公平度量，能够更细致地评估性别偏见，并与人类标签的对齐度显著提高，克服了传统度量的不足。

**关键设计**：在实验中，采用了Cohen's Kappa作为一致性度量，评估了Grep-BiasIR和MSMGenderBias的对齐度，分别达到了58.77%和18.51%。

## 📊 实验亮点

实验结果表明，所提出的CWEx度量在公平性评估上显著优于传统度量，Grep-BiasIR和MSMGenderBias的对齐度分别达到了58.77%和18.51%，显示出更强的性别偏见区分能力。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索系统、推荐系统和社交媒体平台等，能够帮助开发更公平的算法，减少性别偏见对用户体验的影响。未来，随着对性别偏见的深入研究，可能会推动更广泛的社会公平性提升。

## 📄 摘要（原文）

> The presence of social biases in Natural Language Processing (NLP) and Information Retrieval (IR) systems is an ongoing challenge, which underlines the importance of developing robust approaches to identifying and evaluating such biases. In this paper, we aim to address this issue by leveraging Large Language Models (LLMs) to detect and measure gender bias in passage ranking. Existing gender fairness metrics rely on lexical- and frequency-based measures, leading to various limitations, e.g., missing subtle gender disparities. Building on our LLM-based gender bias detection method, we introduce a novel gender fairness metric, named Class-wise Weighted Exposure (CWEx), aiming to address existing limitations. To measure the effectiveness of our proposed metric and study LLMs' effectiveness in detecting gender bias, we annotate a subset of the MS MARCO Passage Ranking collection and release our new gender bias collection, called MSMGenderBias, to foster future research in this area. Our extensive experimental results on various ranking models show that our proposed metric offers a more detailed evaluation of fairness compared to previous metrics, with improved alignment to human labels (58.77% for Grep-BiasIR, and 18.51% for MSMGenderBias, measured using Cohen's Kappa agreement), effectively distinguishing gender bias in ranking. By integrating LLM-driven bias detection, an improved fairness metric, and gender bias annotations for an established dataset, this work provides a more robust framework for analyzing and mitigating bias in IR systems.

