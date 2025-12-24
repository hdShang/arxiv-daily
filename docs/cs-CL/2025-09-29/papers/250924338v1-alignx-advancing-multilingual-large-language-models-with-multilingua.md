---
layout: default
title: "AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment"
---

# AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24338" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24338v1</a>
  <a href="https://arxiv.org/pdf/2509.24338.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24338v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24338v1', 'AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mengyu Bu, Shaolei Zhang, Zhongjun He, Hua Wu, Yang Feng

**分类**: cs.CL

**发布日期**: 2025-09-29

**备注**: Accepted to EMNLP 2025 Main Conference. The code will be available at https://github.com/ictnlp/AlignX

---

## 💡 一句话要点

**AlignX：通过多语言表示对齐提升多语言大语言模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言大语言模型` `跨语言对齐` `表示学习` `指令微调` `多语言语义对齐`

## 📋 核心要点

1. 多语言LLM在非主流语言上的性能和跨语言对齐不足，直接微调难以有效提升。
2. AlignX通过两阶段框架，首先对齐多语言表示，然后进行多语言指令微调，提升模型多语言能力。
3. 实验表明AlignX能有效提升LLM的多语言通用和跨语言生成能力，并改善跨语言对齐。

## 📝 摘要（中文）

多语言大型语言模型（LLM）具有令人印象深刻的多语言理解和生成能力。然而，对于非主流语言，它们的性能和跨语言对齐通常滞后。一个常见的解决方案是在大规模且更平衡的多语言语料库上微调LLM，但这种方法通常导致不精确的对齐和次优的知识转移，难以在各种语言中实现有限的改进。在本文中，我们提出了AlignX来弥合多语言性能差距，这是一个两阶段的表示级别框架，用于增强预训练LLM的多语言性能。在第一阶段，我们通过多语言语义对齐和语言特征集成来对齐多语言表示。在第二阶段，我们通过多语言指令微调来激发LLM的多语言能力。在几个预训练LLM上的实验结果表明，我们的方法增强了LLM的多语言通用和跨语言生成能力。进一步的分析表明，AlignX使多语言表示更接近，并改善了跨语言对齐。

## 🔬 方法详解

**问题定义**：多语言大语言模型在处理非主流语言时，性能往往不如处理主流语言，且跨语言对齐效果较差。直接在多语言语料库上进行微调虽然是一种常见方法，但容易导致对齐不精确和知识迁移效果不佳，难以显著提升所有语言的性能。

**核心思路**：AlignX的核心思路是通过表示级别的对齐来提升多语言LLM的性能。它分为两个阶段：首先，对齐不同语言的表示空间，使得语义相似的句子在不同语言中具有相似的表示；其次，通过多语言指令微调，进一步激发模型的多语言能力，使其更好地理解和生成不同语言的文本。

**技术框架**：AlignX包含两个主要阶段：多语言表示对齐和多语言指令微调。在多语言表示对齐阶段，模型首先通过多语言语义对齐模块，学习将不同语言的句子映射到统一的语义空间。然后，通过语言特征集成模块，将语言相关的特征融入到表示中，以区分不同语言的特性。在多语言指令微调阶段，模型使用多语言指令数据进行微调，以提升其多语言理解和生成能力。

**关键创新**：AlignX的关键创新在于其表示级别的对齐方法。与直接微调相比，AlignX更加注重对齐不同语言的表示空间，从而更好地实现跨语言知识迁移。此外，AlignX还引入了语言特征集成模块，使得模型能够更好地理解不同语言的特性。

**关键设计**：在多语言语义对齐模块中，可以使用对比学习损失来训练模型，使得语义相似的句子在不同语言中具有相似的表示。语言特征集成模块可以使用简单的线性层或更复杂的神经网络来将语言相关的特征融入到表示中。在多语言指令微调阶段，需要精心设计指令数据，以覆盖各种多语言任务，例如翻译、问答、摘要等。

## 📊 实验亮点

实验结果表明，AlignX能够显著提升LLM的多语言通用和跨语言生成能力。具体而言，在多个预训练LLM上进行了实验，结果显示AlignX在各种多语言任务上都取得了显著的性能提升，并且能够有效改善跨语言对齐效果。具体提升幅度未知，需要查阅原论文。

## 🎯 应用场景

AlignX可应用于各种需要多语言理解和生成的场景，例如机器翻译、跨语言信息检索、多语言对话系统等。该研究有助于提升多语言LLM在非主流语言上的性能，促进全球范围内的信息交流和知识共享，并为构建更加公平和包容的AI系统奠定基础。

## 📄 摘要（原文）

> Multilingual large language models (LLMs) possess impressive multilingual understanding and generation capabilities. However, their performance and cross-lingual alignment often lag for non-dominant languages. A common solution is to fine-tune LLMs on large-scale and more balanced multilingual corpus, but such approaches often lead to imprecise alignment and suboptimal knowledge transfer, struggling with limited improvements across languages. In this paper, we propose AlignX to bridge the multilingual performance gap, which is a two-stage representation-level framework for enhancing multilingual performance of pre-trained LLMs. In the first stage, we align multilingual representations with multilingual semantic alignment and language feature integration. In the second stage, we stimulate the multilingual capability of LLMs via multilingual instruction fine-tuning. Experimental results on several pre-trained LLMs demonstrate that our approach enhances LLMs' multilingual general and cross-lingual generation capability. Further analysis indicates that AlignX brings the multilingual representations closer and improves the cross-lingual alignment.

