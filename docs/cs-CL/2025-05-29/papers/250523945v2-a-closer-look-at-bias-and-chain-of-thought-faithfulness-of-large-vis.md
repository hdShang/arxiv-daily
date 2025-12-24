---
layout: default
title: A Closer Look at Bias and Chain-of-Thought Faithfulness of Large (Vision) Language Models
---

# A Closer Look at Bias and Chain-of-Thought Faithfulness of Large (Vision) Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23945" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23945v2</a>
  <a href="https://arxiv.org/pdf/2505.23945.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23945v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23945v2', 'A Closer Look at Bias and Chain-of-Thought Faithfulness of Large (Vision) Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sriram Balasubramanian, Samyadeep Basu, Soheil Feizi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-29 (更新: 2025-11-01)

**备注**: Accepted in EMNLP 2025, 34 pages, 25 figures

---

## 💡 一句话要点

**提出新评估管道以解决大规模视觉语言模型的偏见与推理忠实性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `链式推理` `偏见分析` `多模态学习` `推理忠实性` `非一致性推理` `细粒度评估` `人工智能公平性`

## 📋 核心要点

1. 现有方法在评估大型视觉语言模型的推理忠实性时，未能充分考虑图像偏见的影响。
2. 本文提出了一种新颖的细粒度评估管道，能够更精确地分析和分类偏见表达模式。
3. 实验结果显示，图像偏见的表达较少，而许多模型存在非一致性推理现象，影响推理的可靠性。

## 📝 摘要（中文）

链式推理（CoT）增强了大型语言模型的性能，但其推理过程是否忠实于模型内部机制仍存疑。本文首次全面研究了大型视觉语言模型（LVLMs）中的CoT忠实性，探讨了文本和图像偏见如何影响推理及偏见表达。我们引入了一种新颖的细粒度评估管道，用于分类偏见表达模式，从而实现比以往方法更精确的CoT推理分析。研究发现，细微的图像偏见较少被表达，而许多模型表现出一种新现象，即“非一致性”推理，可能成为检测不忠实CoT的警示信号。我们还将该评估管道应用于语言模型（LLMs），发现当前语言推理模型在表达隐含线索方面仍存在困难。

## 🔬 方法详解

**问题定义**：本文旨在解决大型视觉语言模型在链式推理中偏见表达和忠实性的问题。现有方法未能有效捕捉图像偏见对推理的影响，导致分析不够全面。

**核心思路**：通过引入一种新颖的细粒度评估管道，本文能够更准确地分类和分析偏见表达模式，从而揭示模型在处理不同类型偏见时的差异。

**技术框架**：该评估管道包括多个模块，首先对模型的推理过程进行记录，然后分析文本和图像输入的偏见影响，最后通过细粒度分类评估推理的忠实性。

**关键创新**：最重要的创新在于提出了针对图像偏见的评估方法，并发现了“非一致性”推理现象，这在以往的研究中未被识别。

**关键设计**：评估管道的设计包括对偏见表达的细粒度分类，采用特定的损失函数来优化模型在偏见表达上的表现，同时确保推理过程的透明性和可解释性。

## 📊 实验亮点

实验结果表明，细微的图像偏见在推理中较少被表达，而许多模型展现出非一致性推理现象，可能影响推理的准确性。这些发现为未来的模型设计提供了重要的改进方向。

## 🎯 应用场景

该研究的潜在应用领域包括多模态人工智能系统、自动化内容生成和人机交互等。通过提高模型对偏见的识别和表达能力，可以增强系统的公平性和可靠性，推动更安全的AI应用发展。

## 📄 摘要（原文）

> Chain-of-thought (CoT) reasoning enhances performance of large language models, but questions remain about whether these reasoning traces faithfully reflect the internal processes of the model. We present the first comprehensive study of CoT faithfulness in large vision-language models (LVLMs), investigating how both text-based and previously unexplored image-based biases affect reasoning and bias articulation. Our work introduces a novel, fine-grained evaluation pipeline for categorizing bias articulation patterns, enabling significantly more precise analysis of CoT reasoning than previous methods. This framework reveals critical distinctions in how models process and respond to different types of biases, providing new insights into LVLM CoT faithfulness. Our findings reveal that subtle image-based biases are rarely articulated compared to explicit text-based ones, even in models specialized for reasoning. Additionally, many models exhibit a previously unidentified phenomenon we term ``inconsistent'' reasoning - correctly reasoning before abruptly changing answers, serving as a potential canary for detecting biased reasoning from unfaithful CoTs. We then apply the same evaluation pipeline to revisit CoT faithfulness in LLMs across various levels of implicit cues. Our findings reveal that current language-only reasoning models continue to struggle with articulating cues that are not overtly stated.

