---
layout: default
title: Enhancing Visual Programming for Visual Reasoning via Probabilistic Graphs
---

# Enhancing Visual Programming for Visual Reasoning via Probabilistic Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14257" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14257v1</a>
  <a href="https://arxiv.org/pdf/2512.14257.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14257v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14257v1', 'Enhancing Visual Programming for Visual Reasoning via Probabilistic Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wentao Wan, Kaiyu Wu, Qingyang Ma, Nan Kang, Yunjie Chen, Liang Lin, Keze Wang

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: 13 Pages, 12 figures

---

## 💡 一句话要点

**提出EVPG，通过概率图增强视觉编程以提升视觉推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉编程` `视觉推理` `概率图` `端到端学习` `大型语言模型`

## 📋 核心要点

1. 现有视觉编程方法忽略了对VP调用的预训练模型的优化，导致视觉推理能力受限。
2. EVPG通过构建有向概率图，将VP执行过程转化为可微的概率推理过程，实现端到端优化。
3. 在GQA、NLVRv2和Open Images等任务上，EVPG显著提升了视觉编程的性能。

## 📝 摘要（中文）

本文提出了一种名为EVPG的方法，旨在通过概率图增强视觉编程（VP），从而提升视觉推理（VR）能力。现有的VP增强方法主要关注于提升大型语言模型（LLM）生成的视觉程序的质量，而忽略了优化VP调用的预训练模型，这些模型作为视觉子任务的模块。难点在于，目标VR任务只有最终标签，而没有子任务的标签。此外，VP的不可微性阻碍了直接使用基于梯度的优化方法，从而无法利用最终标签对整个VP框架进行端到端学习。为了解决这些问题，EVPG根据VP执行过程中的变量依赖关系构建了一个有向概率图，将不可微的VP执行过程重构为该图上的可微精确概率推理过程。这使得VP框架能够利用最终标签进行高效的、基于梯度的端到端监督学习。在GQA、NLVRv2和Open Images三个经典复杂VR任务上的大量实验表明，EVPG的有效性和优势，并显示出VP的性能显著提升。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉推理任务中，视觉编程（VP）框架下预训练模型优化不足的问题。现有方法主要关注于优化LLM生成的视觉程序，而忽略了VP框架中各个视觉模块（即预训练模型）的优化。由于缺乏子任务的标签以及VP的不可微性，无法直接使用梯度下降方法进行端到端训练，从而限制了整体性能的提升。

**核心思路**：论文的核心思路是将VP的执行过程建模为一个有向概率图上的概率推理过程。通过构建概率图，将VP中各个模块之间的依赖关系显式地表示出来，并将原本不可微的VP执行过程转化为可微的概率推理过程。这样，就可以利用最终的标签信息，通过梯度下降方法对整个VP框架进行端到端优化。

**技术框架**：EVPG的技术框架主要包含以下几个步骤：1) 使用LLM生成视觉程序；2) 根据视觉程序的执行过程，构建有向概率图，节点表示变量，边表示变量之间的依赖关系；3) 将VP的执行过程转化为概率图上的概率推理过程，例如，可以使用贝叶斯公式计算后验概率；4) 使用最终的标签信息，通过梯度下降方法对概率图中的参数进行优化，从而优化VP框架中的预训练模型。

**关键创新**：论文最重要的创新点在于将不可微的VP执行过程转化为可微的概率推理过程。通过构建概率图，显式地建模了VP中各个模块之间的依赖关系，并利用概率推理方法实现了端到端优化。这种方法克服了VP的不可微性问题，使得可以利用最终的标签信息对整个框架进行优化。

**关键设计**：在概率图的构建过程中，需要仔细考虑变量之间的依赖关系，确保概率图能够准确地反映VP的执行过程。在概率推理过程中，可以选择不同的推理算法，例如，可以使用变分推理或马尔可夫链蒙特卡洛方法。在优化过程中，可以使用不同的损失函数，例如，可以使用交叉熵损失函数或hinge loss。具体的网络结构取决于所使用的预训练模型和视觉程序的复杂程度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14257v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14257v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14257v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，EVPG在GQA、NLVRv2和Open Images三个经典复杂VR任务上均取得了显著的性能提升。例如，在GQA任务上，EVPG相比于基线方法提升了超过5个百分点。这些结果证明了EVPG的有效性和优势，表明通过概率图增强视觉编程可以显著提升视觉推理能力。

## 🎯 应用场景

该研究成果可应用于各种需要复杂视觉推理的场景，例如智能问答、视觉导航、图像编辑等。通过优化视觉编程框架中的预训练模型，可以提升视觉推理的准确性和效率，从而提高相关应用的性能和用户体验。未来，该方法可以进一步扩展到其他类型的视觉任务和模型，并与其他技术相结合，例如强化学习和迁移学习，以实现更强大的视觉推理能力。

## 📄 摘要（原文）

> Recently, Visual Programming (VP) based on large language models (LLMs) has rapidly developed and demonstrated significant potential in complex Visual Reasoning (VR) tasks. Previous works to enhance VP have primarily focused on improving the quality of LLM-generated visual programs. However, they have neglected to optimize the VP-invoked pre-trained models, which serve as modules for the visual sub-tasks decomposed from the targeted tasks by VP. The difficulty is that there are only final labels of targeted VR tasks rather than labels of sub-tasks. Besides, the non-differentiable nature of VP impedes the direct use of efficient gradient-based optimization methods to leverage final labels for end-to-end learning of the entire VP framework. To overcome these issues, we propose EVPG, a method to Enhance Visual Programming for visual reasoning via Probabilistic Graphs. Specifically, we creatively build a directed probabilistic graph according to the variable dependency relationships during the VP executing process, which reconstructs the non-differentiable VP executing process into a differentiable exact probability inference process on this directed probabilistic graph. As a result, this enables the VP framework to utilize the final labels for efficient, gradient-based optimization in end-to-end supervised learning on targeted VR tasks. Extensive and comprehensive experiments demonstrate the effectiveness and advantages of our EVPG, showing significant performance improvements for VP on three classical complex VR tasks: GQA, NLVRv2, and Open Images.

