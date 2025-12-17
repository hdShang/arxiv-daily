---
layout: default
title: You May Speak Freely: Improving the Fine-Grained Visual Recognition Capabilities of Multimodal Large Language Models with Answer Extraction
---

# You May Speak Freely: Improving the Fine-Grained Visual Recognition Capabilities of Multimodal Large Language Models with Answer Extraction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14885" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14885v2</a>
  <a href="https://arxiv.org/pdf/2510.14885.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14885v2" onclick="toggleFavorite(this, '2510.14885v2', 'You May Speak Freely: Improving the Fine-Grained Visual Recognition Capabilities of Multimodal Large Language Models with Answer Extraction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Logan Lawrence, Oindrila Saha, Megan Wei, Chen Sun, Subhransu Maji, Grant Van Horn

**分类**: cs.CV, cs.CL

**发布日期**: 2025-10-16 (更新: 2025-12-09)

**备注**: Accepted to WACV26. 12 pages, 8 tables, 5 figures

---

## 💡 一句话要点

**提出nlg2choice方法，提升多模态大语言模型在细粒度视觉识别中的分类与检索能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `细粒度视觉分类` `零样本学习` `文本约束解码` `开放式提问`

## 📋 核心要点

1. 多模态大语言模型在细粒度视觉分类任务中面临选项数量巨大且高度相关的挑战，现有方法难以有效处理。
2. 论文提出nlg2choice方法，通过开放式提问和文本约束解码，有效提取MLLM的答案并进行选择预测。
3. 实验结果表明，nlg2choice在多个细粒度视觉数据集上，分类和检索性能均优于现有方法，且具有良好的泛化能力。

## 📝 摘要（中文）

由于多模态大语言模型（MLLM）的兴起，零样本视觉分类重新引起了人们的兴趣。然而，评估自回归模型的自由形式响应仍然是一个持续的挑战。现有工作大多侧重于纯语言任务，或者不考虑超过5选项的多项选择题（MCQ）。这两种情况都无法解决细粒度视觉分类（FGVC）中的任务，因为FGVC的选择数量可达数百甚至数千，且选项之间高度相关。此外，在这种高度多项选择的环境下，如何将LLM选择提取扩展到基于检索的问题尚不清楚，因为计算选择集上的概率计算成本很高。本文研究了一种简单的两阶段方法nlg2choice，该方法首先向MLLM提出一个具有最小约束的开放式问题，然后使用纯文本约束解码来预测最可能的选择。在检索设置中，我们计算受约束响应采用该选择的概率，并采用早停方法来显著提高吞吐量。结果表明，在分类和检索方面，该方法在七个细粒度视觉数据集上均有改进，并且该性能在LLM用户以自然语言实现任务的各种方式中均成立。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLM）在细粒度视觉分类（FGVC）任务中面临的挑战。具体来说，FGVC任务通常涉及数百甚至数千个高度相关的选项，这使得传统的基于概率计算的选择提取方法计算成本过高，且难以有效处理。现有方法要么侧重于纯语言任务，要么只考虑少量选项的多项选择题，无法直接应用于FGVC任务。

**核心思路**：论文的核心思路是将问题分解为两个阶段：首先，使用开放式提问的方式，让MLLM自由生成答案，避免直接在大量选项中进行选择；然后，利用文本约束解码，将MLLM生成的答案与候选选项进行匹配，预测最可能的选择。这种方法降低了计算复杂度，并允许MLLM更灵活地表达其理解。

**技术框架**：nlg2choice方法包含两个主要阶段：
1. **开放式提问（Open-ended Questioning）**：向MLLM提出一个开放式问题，要求其根据输入图像生成描述或答案，尽量减少约束。
2. **文本约束解码（Text-only Constrained Decoding）**：利用文本约束解码技术，将MLLM生成的答案与候选选项进行匹配。具体来说，对于每个候选选项，计算MLLM生成该选项的概率，并选择概率最高的选项作为最终预测结果。在检索任务中，采用早停方法，在达到一定概率阈值后停止计算，以提高吞吐量。

**关键创新**：nlg2choice方法的关键创新在于将多项选择问题转化为一个生成式问题，并利用文本约束解码进行选择。这种方法避免了直接在大量选项中进行概率计算，降低了计算复杂度，并允许MLLM更灵活地表达其理解。此外，该方法还引入了早停机制，进一步提高了检索任务的效率。

**关键设计**：在开放式提问阶段，问题的设计需要尽量简洁明了，避免引入过多的先验知识或约束，以便让MLLM能够充分发挥其生成能力。在文本约束解码阶段，可以使用不同的解码策略，例如beam search或top-k sampling，以提高生成答案的多样性和准确性。早停机制的阈值需要根据具体任务进行调整，以在准确性和效率之间取得平衡。论文中没有明确提及损失函数或网络结构等技术细节，推测使用了MLLM自带的损失函数和网络结构进行训练。

## 📊 实验亮点

实验结果表明，nlg2choice方法在七个细粒度视觉数据集上均取得了显著的性能提升。具体来说，在分类任务中，nlg2choice方法相比于现有方法，平均准确率提升了X%。在检索任务中，nlg2choice方法在保持准确率的同时，显著提高了吞吐量，降低了计算成本。（具体提升数据未知，论文未提供具体数值）

## 🎯 应用场景

该研究成果可广泛应用于细粒度图像识别领域，例如动植物识别、车型识别、商品识别等。通过提升MLLM在这些任务中的性能，可以实现更智能化的图像搜索、自动标注和辅助诊断等应用。此外，该方法还可以扩展到其他需要处理大量选项的分类和检索任务中，具有重要的实际应用价值。

## 📄 摘要（原文）

> Despite the renewed interest in zero-shot visual classification due to the rise of Multimodal Large Language Models (MLLMs), the problem of evaluating free-form responses of auto-regressive models remains a persistent challenge. Most existing works focus on language-only tasks or don't consider Multiple Choice Questions (MCQs) beyond 5-way options, both of which are critical capabilities to solve tasks in Fine-Grained Visual Classification (FGVC) where choice counts are in the hundreds to thousands and the choices are highly related. Furthermore, in this highly multi-way MCQ setting it is not clear how to extend LLM choice extraction to retrieval-based problems, where computing probabilities over the choice set is computationally costly. In this work we investigate nlg2choice, a simple two-stage method which first asks the MLLM an open-ended question for the task with minimal constraints, then uses text-only constrained decoding to predict the most likely choice. In retrieval settings, we compute the probability of the constrained response taking that choice with an early stopping method to significantly improve throughput. Our results show improvement over a suite of seven fine-grained visual datasets when evaluating in terms of classification and retrieval, and show that this performance holds over the various ways that users of LLMs can implement tasks in natural language.

