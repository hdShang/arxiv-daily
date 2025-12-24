---
layout: default
title: "ScaleRTL: Scaling LLMs with Reasoning Data and Test-Time Compute for Accurate RTL Code Generation"
---

# ScaleRTL: Scaling LLMs with Reasoning Data and Test-Time Compute for Accurate RTL Code Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05566" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05566v2</a>
  <a href="https://arxiv.org/pdf/2506.05566.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05566v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05566v2', 'ScaleRTL: Scaling LLMs with Reasoning Data and Test-Time Compute for Accurate RTL Code Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenhui Deng, Yun-Da Tsai, Guan-Ting Liu, Zhongzhi Yu, Haoxing Ren

**分类**: cs.AR, cs.AI

**发布日期**: 2025-06-05 (更新: 2025-07-15)

**备注**: Accepted to MLCAD 2025

---

## 💡 一句话要点

**提出ScaleRTL以解决RTL代码生成中的数据瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `RTL代码生成` `推理能力` `测试时计算` `数据集策划`

## 📋 核心要点

1. 现有方法在RTL代码生成中面临高质量训练数据稀缺的问题，限制了LLMs的有效性。
2. ScaleRTL通过策划长链推理轨迹和测试时计算扩展，解决了数据瓶颈和推理能力不足的问题。
3. 实验结果表明，ScaleRTL在VerilogEval和RTLLM上达到了最先进的性能，分别超越18个基线模型18.4%和12.7%。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进步使其在软件编码基准测试中接近人类表现，但在RTL代码生成方面的有效性仍然有限，主要由于高质量训练数据的稀缺。尽管之前的研究对LLMs进行了微调以适应RTL任务，但未能从根本上克服数据瓶颈，并且由于缺乏推理能力，无法支持测试时的扩展。本文提出了ScaleRTL，这是首个针对RTL编码的推理LLM，能够同时扩展高质量推理数据和测试时计算。我们特别策划了一套多样化的长链推理轨迹，平均每个轨迹包含56K个标记，形成了一个包含35亿个标记的数据集，捕捉了丰富的RTL知识。对这一语料库进行微调后，ScaleRTL能够进行深度RTL推理，并通过一种新颖的测试时扩展策略进一步提升性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在RTL代码生成中的数据瓶颈问题。现有方法虽然经过微调，但仍无法有效利用高质量的推理数据，且缺乏在测试时的推理扩展能力。

**核心思路**：ScaleRTL的核心思路是通过策划丰富的推理数据集和引入测试时计算扩展，来提升模型在RTL编码任务中的推理能力。这样的设计使得模型能够在生成代码时进行深度推理和自我修正。

**技术框架**：ScaleRTL的整体架构包括数据集策划、模型微调和测试时推理扩展三个主要模块。首先，策划出包含丰富推理信息的数据集；其次，对通用推理模型进行微调；最后，通过迭代反思和自我修正来扩展推理过程。

**关键创新**：ScaleRTL的主要创新在于其推理能力的引入和测试时计算的扩展，这与现有方法的静态推理方式形成了鲜明对比。通过这种方式，ScaleRTL能够在生成代码时进行更深层次的推理和自我校正。

**关键设计**：在模型微调过程中，ScaleRTL使用了包含35亿个标记的多样化数据集，并设计了特定的损失函数以优化推理过程。此外，模型的网络结构经过调整，以适应长链推理的需求。通过这些设计，ScaleRTL在性能上显著提升。

## 📊 实验亮点

ScaleRTL在VerilogEval和RTLLM上实现了最先进的性能，分别超越18个竞争基线模型18.4%和12.7%。这些实验结果表明，ScaleRTL在处理复杂RTL编码任务时具有显著的优势，验证了其推理能力和测试时扩展策略的有效性。

## 🎯 应用场景

ScaleRTL的研究成果在多个领域具有广泛的应用潜力，尤其是在集成电路设计和硬件描述语言的自动生成方面。随着对高效RTL代码生成需求的增加，ScaleRTL能够为工程师提供更高效的工具，提升设计效率和准确性。未来，该技术可能会推动自动化设计工具的发展，进一步降低人力成本和错误率。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have enabled near-human performance on software coding benchmarks, but their effectiveness in RTL code generation remains limited due to the scarcity of high-quality training data. While prior efforts have fine-tuned LLMs for RTL tasks, they do not fundamentally overcome the data bottleneck and lack support for test-time scaling due to their non-reasoning nature. In this work, we introduce ScaleRTL, the first reasoning LLM for RTL coding that scales up both high-quality reasoning data and test-time compute. Specifically, we curate a diverse set of long chain-of-thought reasoning traces averaging 56K tokens each, resulting in a dataset of 3.5B tokens that captures rich RTL knowledge. Fine-tuning a general-purpose reasoning model on this corpus yields ScaleRTL that is capable of deep RTL reasoning. Subsequently, we further enhance the performance of ScaleRTL through a novel test-time scaling strategy that extends the reasoning process via iteratively reflecting on and self-correcting previous reasoning steps. Experimental results show that ScaleRTL achieves state-of-the-art performance on VerilogEval and RTLLM, outperforming 18 competitive baselines by up to 18.4% on VerilogEval and 12.7% on RTLLM.

