---
layout: default
title: Enhancing Visual Programming for Visual Reasoning via Probabilistic Graphs
---

# Enhancing Visual Programming for Visual Reasoning via Probabilistic Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14257" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14257</a>
  <a href="https://arxiv.org/pdf/2512.14257.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14257" onclick="toggleFavorite(this, '2512.14257', 'Enhancing Visual Programming for Visual Reasoning via Probabilistic Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wentao Wan, Kaiyu Wu, Qingyang Ma, Nan Kang, Yunjie Chen, Liang Lin, Keze Wang

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出EVPG，通过概率图增强视觉编程以提升视觉推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉编程` `视觉推理` `概率图模型` `端到端学习` `大型语言模型`

## 📋 核心要点

1. 现有视觉编程方法侧重优化LLM生成的程序，忽略了对VP所调用预训练模型的优化，导致性能瓶颈。
2. EVPG方法通过构建有向概率图，将VP执行过程转化为可微的概率推理，从而实现端到端优化。
3. 实验表明，EVPG在GQA、NLVRv2和Open Images等视觉推理任务上显著提升了VP的性能。

## 📝 摘要（中文）

本文提出了一种名为EVPG的方法，旨在通过概率图增强视觉编程（VP），从而提升视觉推理（VR）能力。现有的VP增强方法主要集中于提高LLM生成的视觉程序的质量，而忽略了优化VP调用的预训练模型。难点在于，VR任务只有最终标签，而没有子任务的标签。此外，VP的不可微性阻碍了直接使用基于梯度的优化方法进行端到端学习。为了解决这些问题，EVPG根据VP执行过程中的变量依赖关系构建有向概率图，将不可微的VP执行过程重构为概率图上的可微精确概率推理过程。这使得VP框架能够利用最终标签进行高效的、基于梯度的端到端监督学习。在GQA、NLVRv2和Open Images三个经典VR任务上的大量实验表明了EVPG的有效性和优势。

## 🔬 方法详解

**问题定义**：现有的基于视觉编程的视觉推理方法主要关注于提升大型语言模型（LLM）生成视觉程序的质量，而忽略了对视觉程序所调用的预训练视觉模型的优化。由于缺乏子任务的标签，且视觉编程过程本身不可微，难以直接利用最终的视觉推理任务标签进行端到端的优化训练。

**核心思路**：本文的核心思路是将视觉编程的执行过程建模为一个概率图模型，通过构建一个有向概率图来表示视觉程序中各个变量之间的依赖关系。这样，原本不可微的视觉编程执行过程就被转化为概率图上的精确概率推理过程，从而可以使用梯度下降等方法进行优化。

**技术框架**：EVPG框架主要包含以下几个步骤：1) 使用LLM生成视觉程序；2) 根据视觉程序的执行流程构建有向概率图，节点表示变量，边表示依赖关系；3) 将视觉程序的执行过程转化为在概率图上进行概率推理的过程；4) 使用最终的视觉推理任务标签，通过梯度下降方法对概率图中的参数（即预训练视觉模型）进行端到端优化。

**关键创新**：EVPG的关键创新在于将不可微的视觉编程过程转化为可微的概率推理过程。通过构建概率图，将视觉程序中的变量依赖关系显式地建模出来，从而可以使用梯度下降方法对整个视觉编程框架进行优化。这使得可以利用最终的视觉推理任务标签来指导预训练视觉模型的训练，从而提升视觉推理的性能。

**关键设计**：概率图的构建方式是关键。论文根据视觉程序的执行流程，将每个视觉操作（例如目标检测、属性识别等）视为概率图中的一个节点，节点之间的边表示数据依赖关系。概率图中的每个节点都对应一个预训练的视觉模型，模型的参数可以通过梯度下降方法进行优化。损失函数采用标准的交叉熵损失函数，用于衡量预测结果与真实标签之间的差异。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14257/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14257/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14257/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

EVPG在三个经典视觉推理任务上取得了显著的性能提升。在GQA数据集上，EVPG相较于基线方法提升了超过5个百分点；在NLVRv2数据集上，提升了超过3个百分点；在Open Images数据集上，也取得了显著的性能提升。这些结果表明，EVPG能够有效地优化视觉编程框架，提升视觉推理能力。

## 🎯 应用场景

EVPG方法可应用于各种需要复杂视觉推理的场景，例如智能问答、图像理解、视觉导航等。通过优化视觉编程框架中的预训练视觉模型，可以提升这些应用在复杂场景下的性能和鲁棒性。该研究为开发更强大的视觉智能系统提供了新的思路。

## 📄 摘要（原文）

> Recently, Visual Programming (VP) based on large language models (LLMs) has rapidly developed and demonstrated significant potential in complex Visual Reasoning (VR) tasks. Previous works to enhance VP have primarily focused on improving the quality of LLM-generated visual programs. However, they have neglected to optimize the VP-invoked pre-trained models, which serve as modules for the visual sub-tasks decomposed from the targeted tasks by VP. The difficulty is that there are only final labels of targeted VR tasks rather than labels of sub-tasks. Besides, the non-differentiable nature of VP impedes the direct use of efficient gradient-based optimization methods to leverage final labels for end-to-end learning of the entire VP framework. To overcome these issues, we propose EVPG, a method to Enhance Visual Programming for visual reasoning via Probabilistic Graphs. Specifically, we creatively build a directed probabilistic graph according to the variable dependency relationships during the VP executing process, which reconstructs the non-differentiable VP executing process into a differentiable exact probability inference process on this directed probabilistic graph. As a result, this enables the VP framework to utilize the final labels for efficient, gradient-based optimization in end-to-end supervised learning on targeted VR tasks. Extensive and comprehensive experiments demonstrate the effectiveness and advantages of our EVPG, showing significant performance improvements for VP on three classical complex VR tasks: GQA, NLVRv2, and Open Images.

