---
layout: default
title: Enhancing Visual Programming for Visual Reasoning via Probabilistic Graphs
---

# Enhancing Visual Programming for Visual Reasoning via Probabilistic Graphs

**arXiv**: [2512.14257v1](https://arxiv.org/abs/2512.14257) | [PDF](https://arxiv.org/pdf/2512.14257.pdf)

**作者**: Wentao Wan, Kaiyu Wu, Qingyang Ma, Nan Kang, Yunjie Chen, Liang Lin, Keze Wang

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: 13 Pages, 12 figures

---

## 💡 一句话要点

**提出EVPG方法，通过概率图将不可微视觉编程重构为可微推理过程，以增强复杂视觉推理任务性能。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `视觉编程` `概率图模型` `视觉推理` `端到端学习` `大语言模型` `多模态学习` `可微优化` `监督学习`

## 📋 核心要点

1. 现有视觉编程方法主要优化大语言模型生成的程序，但忽略了预训练子任务模块的优化，且缺乏子任务标签，导致端到端学习困难。
2. EVPG通过构建有向概率图，将不可微的视觉编程执行过程转化为可微的概率推理，实现基于梯度的端到端优化。
3. 在GQA、NLVRv2和Open Images等复杂视觉推理任务上，EVPG显著提升了视觉编程的性能，验证了其有效性。

## 📝 摘要（中文）

近年来，基于大语言模型的视觉编程在复杂视觉推理任务中展现出巨大潜力。先前增强视觉编程的研究主要关注提升大语言模型生成的视觉程序质量，但忽略了优化视觉编程调用的预训练模型，这些模型作为视觉编程分解出的视觉子任务模块。困难在于只有目标视觉推理任务的最终标签，而没有子任务标签。此外，视觉编程的不可微特性阻碍了直接使用高效的基于梯度的优化方法，以利用最终标签进行整个视觉编程框架的端到端学习。为克服这些问题，我们提出EVPG，一种通过概率图增强视觉编程进行视觉推理的方法。具体而言，我们根据视觉编程执行过程中的变量依赖关系，创新性地构建了一个有向概率图，将不可微的视觉编程执行过程重构为该有向概率图上的可微精确概率推理过程。这使得视觉编程框架能够利用最终标签，在目标视觉推理任务上进行高效的、基于梯度的端到端监督学习优化。广泛而全面的实验证明了EVPG的有效性和优势，在GQA、NLVRv2和Open Images三个经典复杂视觉推理任务上，视觉编程性能显著提升。

## 🔬 方法详解

EVPG的整体框架基于视觉编程，核心创新在于构建有向概率图来建模视觉编程执行过程中的变量依赖关系。该图将每个视觉子任务模块的输出视为概率变量，通过精确概率推理计算最终预测的概率，从而将不可微的视觉编程过程重构为可微的推理过程。这使得整个框架可以利用目标任务的最终标签，通过梯度下降进行端到端监督学习，优化预训练子任务模块。与现有方法的主要区别在于，EVPG不仅关注程序生成质量，还通过概率图机制实现了对子任务模块的联合优化，解决了视觉编程中不可微和标签缺失的挑战。

## 📊 实验亮点

实验在GQA、NLVRv2和Open Images三个基准数据集上进行，EVPG相比基线视觉编程方法取得了显著性能提升，具体提升幅度未知，但论文报告了全面的实验结果，证明了该方法在复杂视觉推理任务中的有效性和优势。

## 🎯 应用场景

EVPG可应用于需要复杂视觉推理的领域，如智能问答系统、视觉语言导航、自动驾驶中的场景理解，以及教育或医疗领域的多模态分析任务，提升模型在真实世界复杂视觉任务中的准确性和鲁棒性。

## 📄 摘要（原文）

> Recently, Visual Programming (VP) based on large language models (LLMs) has rapidly developed and demonstrated significant potential in complex Visual Reasoning (VR) tasks. Previous works to enhance VP have primarily focused on improving the quality of LLM-generated visual programs. However, they have neglected to optimize the VP-invoked pre-trained models, which serve as modules for the visual sub-tasks decomposed from the targeted tasks by VP. The difficulty is that there are only final labels of targeted VR tasks rather than labels of sub-tasks. Besides, the non-differentiable nature of VP impedes the direct use of efficient gradient-based optimization methods to leverage final labels for end-to-end learning of the entire VP framework. To overcome these issues, we propose EVPG, a method to Enhance Visual Programming for visual reasoning via Probabilistic Graphs. Specifically, we creatively build a directed probabilistic graph according to the variable dependency relationships during the VP executing process, which reconstructs the non-differentiable VP executing process into a differentiable exact probability inference process on this directed probabilistic graph. As a result, this enables the VP framework to utilize the final labels for efficient, gradient-based optimization in end-to-end supervised learning on targeted VR tasks. Extensive and comprehensive experiments demonstrate the effectiveness and advantages of our EVPG, showing significant performance improvements for VP on three classical complex VR tasks: GQA, NLVRv2, and Open Images.

