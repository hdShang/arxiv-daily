---
layout: default
title: "GraphLAMA: Enabling Efficient Adaptation of Graph Language Models with Limited Annotations"
---

# GraphLAMA: Enabling Efficient Adaptation of Graph Language Models with Limited Annotations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21559" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21559v1</a>
  <a href="https://arxiv.org/pdf/2506.21559.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21559v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21559v1', 'GraphLAMA: Enabling Efficient Adaptation of Graph Language Models with Limited Annotations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junze Chen, Cheng Yang, Shujie Li, Zhiqiang Zhang, Yawen Li, Junping Du, Chuan Shi

**分类**: cs.CL

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出GraphLAMA以解决图语言模型适应性不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图语言模型` `参数适应` `图神经网络` `上下文学习` `指令调优` `少样本学习` `推理速度`

## 📋 核心要点

1. 现有的图语言模型在处理未见任务时，存在有效性和效率的不足，尤其是在上下文学习和指令调优方面。
2. 本文提出GraphLAMA方法，通过引入参数适应阶段，仅需少量标注示例即可高效调整图语言模型，提升预测性能。
3. 实验表明，GraphLAMA在节点分类和摘要生成任务中实现了4.91%的准确率提升，推理速度提高了10倍。

## 📝 摘要（中文）

大型语言模型（LLMs）在多个领域展现出强大的能力，最近被整合用于图分析，形成图语言模型（GLMs）。一些GLMs能够通过自然语言描述解释未见任务，并通过少量示例进行学习，称为上下文学习（ICL）。然而，ICL在图上的有效性和效率存在问题，而指令调优需要大量标注数据，难以获取。为此，本文提出GraphLAMA方法，通过引入额外的参数适应阶段，仅需少量标注示例即可高效调整GLMs，以提高预测准确性和推理速度。实验结果表明，GraphLAMA在少/零样本节点分类和摘要生成任务中表现出色，准确率提升4.91%，推理速度在5-shot设置下可提高10倍。

## 🔬 方法详解

**问题定义**：本文旨在解决图语言模型在面对未见任务时的适应性不足和效率低下的问题。现有方法在上下文学习中参数固定，且指令调优需要大量标注数据，难以在实际场景中应用。

**核心思路**：GraphLAMA通过引入额外的参数适应阶段，允许模型在仅有少量标注示例的情况下进行高效调整，从而提高预测准确性和推理速度。

**技术框架**：GraphLAMA的整体架构包括预训练阶段和适应阶段。在预训练阶段，除了LLM的参数外，模型的其他参数会针对不同任务进行训练，以捕捉通用知识。在适应阶段，仅更新少量预训练参数，基于少量示例进行调整。

**关键创新**：GraphLAMA的主要创新在于其参数适应机制，使得图语言模型能够在少量标注数据的情况下高效适应新任务，与传统的上下文学习和指令调优方法有本质区别。

**关键设计**：模型采用图神经网络（GNN）作为骨干网络，设计了多个组件将节点转换为LLM标记的表示空间。任务指令则通过节点和语言标记的混合表示。

## 📊 实验亮点

在实验中，GraphLAMA在少样本和零样本节点分类及摘要生成任务中表现优异，准确率提升4.91%。与上下文学习相比，其推理速度在5-shot设置下提高了10倍，展现出显著的性能优势。

## 🎯 应用场景

GraphLAMA的研究成果可广泛应用于图数据分析、社交网络分析、知识图谱构建等领域。其高效的适应能力和快速推理速度使得在实际应用中能够更好地处理动态变化的任务需求，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated their strong capabilities in various domains, and have been recently integrated for graph analysis as graph language models (GLMs). With LLMs as the predictor, some GLMs can interpret unseen tasks described by natural language, and learn from a few examples in the prompts without parameter tuning, known as in-context learning (ICL). Another subset of GLMs utilizes abundant training labels to enhance model performance, known as instruction tuning. However, we argue that ICL on graphs has effectiveness issues due to fixed parameters and efficiency issues due to long context. Meanwhile, the large amount of labeled data required for instruction tuning can be difficult to obtain in real-world scenarios. To this end, we aim to introduce an extra parameter adaptation stage that can efficiently tailor GLMs to an unseen graph and task with only a few labeled examples, in exchange for better prediction accuracy and faster inference speed. For implementation, in this paper we propose GraphLAMA method, with its model backbone and learning schemes specialized for efficient tuning and inference. Specifically, for model backbone, we use a graph neural network (GNN) with several well-designed components to transform nodes into the representation space of LLM tokens. Task instructions can then be represented as a mixture of node and language tokens. In the pre-training stage, model parameters except the LLM will be trained with different tasks to capture general knowledge. In the adaptation stage, only a few pre-trained parameters will be updated based on few-shot examples. Extensive experiments on few/zero-shot node classification and summary generation show that our proposed GraphLAMA achieves state-of-the-art performance with 4.91% absolution improvement in accuracy. Compared with ICL, our inference speed can be 10 times faster under 5-shot setting.

