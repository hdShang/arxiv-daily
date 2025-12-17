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

**提出EVPG方法，通过概率图将不可微的视觉编程执行过程转化为可微的概率推理，以增强视觉推理任务中的视觉编程性能。**

**关键词**: `视觉编程` `概率图模型` `视觉推理` `端到端学习` `大语言模型` `多模态AI` `梯度优化` `监督学习`

## 📋 核心要点

1. 现有方法主要优化LLM生成的视觉程序，但忽略了VP调用的预训练模型优化，且缺乏子任务标签，导致难以进行端到端学习。
2. EVPG通过构建有向概率图，将VP的不可微执行过程转化为可微的概率推理，从而支持基于梯度的优化。
3. 在GQA、NLVRv2和Open Images等VR任务上，EVPG显著提升了VP的性能，证明了其有效性和优势。

## 📝 摘要（中文）

近年来，基于大语言模型（LLMs）的视觉编程（VP）在复杂视觉推理（VR）任务中迅速发展并展现出巨大潜力。先前增强VP的工作主要集中于提高LLM生成的视觉程序质量，但忽略了优化VP调用的预训练模型，这些模型作为VP从目标任务分解出的视觉子任务的模块。困难在于只有目标VR任务的最终标签，而没有子任务的标签。此外，VP的不可微性阻碍了直接使用高效的基于梯度的优化方法，以利用最终标签进行整个VP框架的端到端学习。为克服这些问题，我们提出了EVPG，一种通过概率图增强视觉编程以进行视觉推理的方法。具体而言，我们根据VP执行过程中的变量依赖关系，创造性地构建了一个有向概率图，将不可微的VP执行过程重构为该有向概率图上的可微精确概率推理过程。这使得VP框架能够利用最终标签，在目标VR任务的端到端监督学习中实现高效的基于梯度的优化。广泛而全面的实验证明了我们EVPG的有效性和优势，在三个经典复杂VR任务（GQA、NLVRv2和Open Images）上显示出VP的显著性能提升。

## 🔬 方法详解

EVPG的整体框架基于视觉编程（VP），核心创新在于构建一个有向概率图来建模VP执行过程中的变量依赖关系。该方法将VP的不可微执行过程重构为在该概率图上的可微精确概率推理过程，从而允许使用最终任务标签进行梯度反向传播，实现端到端监督学习。与现有方法的主要区别在于，它不仅关注程序生成质量，还通过概率图优化了VP调用的预训练模型，解决了子任务标签缺失和不可微性问题。

## 📊 实验亮点

在GQA、NLVRv2和Open Images三个经典VR任务上，EVPG显著提升了视觉编程的性能，通过实验验证了其有效性和优势，具体性能提升数据未知，但论文报告了广泛而全面的实验结果。

## 🎯 应用场景

该研究可应用于复杂视觉推理任务，如视觉问答（VQA）、图像-文本匹配和开放域图像理解，提升多模态AI系统在自动驾驶、智能助手和内容分析等领域的实际性能。

## 📄 摘要（原文）

> Recently, Visual Programming (VP) based on large language models (LLMs) has rapidly developed and demonstrated significant potential in complex Visual Reasoning (VR) tasks. Previous works to enhance VP have primarily focused on improving the quality of LLM-generated visual programs. However, they have neglected to optimize the VP-invoked pre-trained models, which serve as modules for the visual sub-tasks decomposed from the targeted tasks by VP. The difficulty is that there are only final labels of targeted VR tasks rather than labels of sub-tasks. Besides, the non-differentiable nature of VP impedes the direct use of efficient gradient-based optimization methods to leverage final labels for end-to-end learning of the entire VP framework. To overcome these issues, we propose EVPG, a method to Enhance Visual Programming for visual reasoning via Probabilistic Graphs. Specifically, we creatively build a directed probabilistic graph according to the variable dependency relationships during the VP executing process, which reconstructs the non-differentiable VP executing process into a differentiable exact probability inference process on this directed probabilistic graph. As a result, this enables the VP framework to utilize the final labels for efficient, gradient-based optimization in end-to-end supervised learning on targeted VR tasks. Extensive and comprehensive experiments demonstrate the effectiveness and advantages of our EVPG, showing significant performance improvements for VP on three classical complex VR tasks: GQA, NLVRv2, and Open Images.

