---
layout: default
title: "Programming by Backprop: LLMs Acquire Reusable Algorithmic Abstractions During Code Training"
---

# Programming by Backprop: LLMs Acquire Reusable Algorithmic Abstractions During Code Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18777" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18777v1</a>
  <a href="https://arxiv.org/pdf/2506.18777.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18777v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18777v1', 'Programming by Backprop: LLMs Acquire Reusable Algorithmic Abstractions During Code Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jonathan Cook, Silvia Sapora, Arash Ahmadian, Akbir Khan, Tim Rocktaschel, Jakob Foerster, Laura Ruis

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-06-23

---

## 💡 一句话要点

**提出编程反向传播方法以提升LLMs的算法抽象能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `编程反向传播` `算法抽象` `源代码训练` `程序评估`

## 📋 核心要点

1. 现有方法对LLMs在源代码训练中推理能力的提升机制理解不足，缺乏有效的解释。
2. 本文提出编程反向传播（PBB）作为一种新方法，通过仅使用源代码训练模型来评估程序。
3. 实验结果显示，LLMs在没有输入/输出示例的情况下能够有效评估程序，且使用代码的效果优于语言描述。

## 📝 摘要（中文）

训练大型语言模型（LLMs）在源代码上显著增强了其通用推理能力，但其背后的机制尚不清楚。本文提出了编程反向传播（PBB）作为这一效应的潜在驱动因素，旨在通过仅训练源代码来教会模型评估程序。我们对LLMs进行了微调，使用了包含输入/输出示例和仅包含源代码的两组程序。结果表明，LLMs在没有输入/输出示例的情况下能够评估程序，并且在使用代码而非语义等价的语言描述时效果更佳。PBB方法使得LLMs在不同输入下的程序评估更加稳健，表明代码训练能够帮助LLMs内化可重用的算法抽象。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在源代码训练中推理能力提升的机制不明的问题。现有方法未能有效利用源代码进行模型训练，导致推理能力的提升缺乏解释。

**核心思路**：论文提出编程反向传播（PBB）方法，通过仅使用源代码来训练模型，使其能够在没有输入/输出示例的情况下评估程序。这一设计旨在让模型内化算法抽象，从而提升推理能力。

**技术框架**：整体架构包括两个主要阶段：首先，微调LLMs，分别使用包含输入/输出示例和仅包含源代码的程序集；其次，评估模型在不同实验设置下的表现，分析其对无输入/输出程序的评估能力。

**关键创新**：PBB方法的核心创新在于通过源代码训练模型，使其能够在没有示例的情况下进行程序评估。这与传统方法依赖输入/输出对的训练方式有本质区别。

**关键设计**：在实验中，模型的损失函数设计为关注程序评估的准确性，网络结构则采用了适合处理源代码的Transformer架构。模型在训练过程中通过链式思维逐步评估程序，提高了输出的可靠性。

## 📊 实验亮点

实验结果表明，使用PBB方法的模型在没有输入/输出示例的情况下，能够有效评估程序，且在使用源代码时的表现显著优于使用语义描述的模型。具体来说，PBB方法在多种实验设置中展现出更高的评估准确性和鲁棒性，表明其在算法抽象内化方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自动代码生成、程序分析和智能编程助手等。通过提升LLMs对算法抽象的理解能力，可以在软件开发、教育和研究等多个领域产生深远影响，促进人机协作的效率和质量。

## 📄 摘要（原文）

> Training large language models (LLMs) on source code significantly enhances their general-purpose reasoning abilities, but the mechanisms underlying this generalisation are poorly understood. In this paper, we propose Programming by Backprop (PBB) as a potential driver of this effect - teaching a model to evaluate a program for inputs by training on its source code alone, without ever seeing I/O examples. To explore this idea, we finetune LLMs on two sets of programs representing simple maths problems and algorithms: one with source code and I/O examples (w/ IO), the other with source code only (w/o IO). We find evidence that LLMs have some ability to evaluate w/o IO programs for inputs in a range of experimental settings, and make several observations. Firstly, PBB works significantly better when programs are provided as code rather than semantically equivalent language descriptions. Secondly, LLMs can produce outputs for w/o IO programs directly, by implicitly evaluating the program within the forward pass, and more reliably when stepping through the program in-context via chain-of-thought. We further show that PBB leads to more robust evaluation of programs across inputs than training on I/O pairs drawn from a distribution that mirrors naturally occurring data. Our findings suggest a mechanism for enhanced reasoning through code training: it allows LLMs to internalise reusable algorithmic abstractions. Significant scope remains for future work to enable LLMs to more effectively learn from symbolic procedures, and progress in this direction opens other avenues like model alignment by training on formal constitutional principles.

