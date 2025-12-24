---
layout: default
title: "MLP Memory: A Retriever-Pretrained Memory for Large Language Models"
---

# MLP Memory: A Retriever-Pretrained Memory for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01832" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01832v3</a>
  <a href="https://arxiv.org/pdf/2508.01832.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01832v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01832v3', 'MLP Memory: A Retriever-Pretrained Memory for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rubin Wei, Jiaqi Cao, Jiarui Wang, Jushi Kai, Qipeng Guo, Bowen Zhou, Zhouhan Lin

**分类**: cs.CL

**发布日期**: 2025-08-03 (更新: 2025-10-23)

---

## 💡 一句话要点

**提出MLP Memory以解决大语言模型知识获取效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `知识获取` `参数化学习` `多层感知机` `推理效率` `信息检索` `问答系统`

## 📋 核心要点

1. 现有方法在增强大语言模型的知识获取效率时存在推理延迟高和集成浅的问题。
2. 本文提出的MLP Memory通过预训练多层感知机来内部化检索模式，无需显式文档访问。
3. 实验结果显示，MLP Memory在多个基准上显著提升了性能，同时加快了推理速度。

## 📝 摘要（中文）

现代增强大语言模型的事实准确性和知识利用的方法面临基本的权衡：非参数检索增强生成（RAG）提供灵活的外部知识访问，但推理延迟高且集成浅，而参数微调方法如LoRA则存在灾难性遗忘和能力下降的风险。本文提出MLP Memory，一个轻量级的参数模块，能够在没有显式文档访问的情况下学习检索模式。通过预训练一个多层感知机（MLP）来模仿kNN检索器在整个预训练数据集上的行为，我们创建了一个可微分的记忆组件，以完全参数化的形式捕获基于检索的知识访问的优势。我们的架构通过简单的概率插值将预训练的MLP Memory与Transformer解码器集成，在WikiText-103和Web数据集上分别实现了17.5%和24.1%的扩展增益，并在五个问答基准上实现了12.3%的相对提升，在九个通用NLP任务上实现了5.2分的绝对增益，同时在HaluEval上减少了多达10分的幻觉。此外，MLP Memory的推理速度比RAG快2.5倍且准确性更高。我们的研究表明，参数化学习检索模式弥合了高效推理与有效知识访问之间的差距，为RAG和微调方法提供了实用的替代方案。

## 🔬 方法详解

**问题定义**：本文旨在解决现有增强大语言模型的知识获取方法在推理效率和知识集成方面的不足，特别是RAG方法的高延迟和微调方法的灾难性遗忘问题。

**核心思路**：论文提出的MLP Memory通过预训练一个多层感知机（MLP），模仿kNN检索器的行为，从而在不依赖外部文档的情况下，学习到有效的检索模式。

**技术框架**：整体架构包括一个预训练的MLP Memory模块，该模块与Transformer解码器通过概率插值进行集成。预训练阶段使用整个数据集来训练MLP，使其能够捕获检索模式。

**关键创新**：最重要的创新在于将检索模式的学习转化为参数化的形式，避免了传统方法中的高延迟和灾难性遗忘，提供了一种新的知识访问方式。

**关键设计**：在设计中，MLP的结构和损失函数经过精心选择，以确保其能够有效模仿kNN检索器的行为，具体参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，MLP Memory在WikiText-103和Web数据集上分别实现了17.5%和24.1%的性能提升，并在五个问答基准上相对提升12.3%。此外，推理速度比RAG快2.5倍，同时减少了多达10分的幻觉现象，展现出显著的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、问答系统和信息检索等。通过提高知识获取的效率，MLP Memory能够在实际应用中显著提升大语言模型的性能，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Modern approaches to enhancing Large Language Models' factual accuracy and knowledge utilization face a fundamental trade-off: non-parametric retrieval-augmented generation (RAG) provides flexible access to external knowledge but suffers from high inference latency and shallow integration, while parametric fine-tuning methods like LoRA risk catastrophic forgetting and degraded general capabilities. In this work, we propose MLP Memory, a lightweight parametric module that learns to internalize retrieval patterns without explicit document access. By pretraining an MLP to imitate a $k$NN retriever's behavior on the entire pretraining dataset, we create a differentiable memory component that captures the benefits of retrieval-based knowledge access in a fully parametric form. Our architecture integrates this pretrained MLP Memory with Transformer decoders through simple probability interpolation, yielding 17.5\% and 24.1\% scaling gains on WikiText-103 and Web datasets, respectively. It further achieves 12.3\% relative improvement on five question-answering benchmarks and 5.2 points absolute gain across nine general NLP tasks, while reducing hallucinations by up to 10 points on HaluEval. Moreover, MLP Memory delivers 2.5$\times$ faster inference than RAG with superior accuracy. Our findings show that learning retrieval patterns parametrically bridges the gap between efficient inference and effective knowledge access, offering a practical alternative to both RAG and fine-tuning approaches.

