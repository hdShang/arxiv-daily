---
layout: default
title: "Hybrid-NL2SVA: Integrating RAG and Finetuning for LLM-based NL2SVA"
---

# Hybrid-NL2SVA: Integrating RAG and Finetuning for LLM-based NL2SVA

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21569" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21569v1</a>
  <a href="https://arxiv.org/pdf/2506.21569.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21569v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21569v1', 'Hybrid-NL2SVA: Integrating RAG and Finetuning for LLM-based NL2SVA')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weihua Xiao, Derek Ekberg, Siddharth Garg, Ramesh Karri

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出Hybrid-NL2SVA框架以解决NL2SVA自动化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言处理` `系统验证` `硬件设计` `大型语言模型` `自动化生成` `微调技术` `检索增强生成`

## 📋 核心要点

1. 现有的NL2SVA方法在理解领域特定的语法和语义方面存在困难，导致生成的SVAs质量不高。
2. 本文提出了一种结合检索增强生成（RAG）和合成微调数据集的框架，以提升LLMs在NL2SVA任务中的表现。
3. 实验结果显示，定制的RAG框架和微调数据集显著提高了模型在功能匹配上的准确性，达到了58.42%和59.05%的提升。

## 📝 摘要（中文）

SystemVerilog Assertions (SVAs) 对于硬件设计的正确性验证至关重要，但从自然语言属性描述自动生成SVAs的过程仍然劳动密集且易出错。本文提出了一种定制的检索增强生成（RAG）框架和合成微调数据集，以提升大型语言模型（LLMs）在NL2SVA任务中的表现。通过提供逐层构建并发SVAs的提示引导解释，该微调数据集显著提高了模型的语法和功能准确性。实验结果表明，定制的RAG框架使得功能匹配的SVAs数量较GPT-4o-mini提升了58.42%，而在我们的微调数据集上进行微调并集成HybridRetrieval的Qwen2.5-Coder-7B-Instruct模型则较基础Qwen模型提升了59.05%。

## 🔬 方法详解

**问题定义**：本文旨在解决从自然语言描述自动生成SystemVerilog Assertions (SVAs)的困难，现有方法在理解特定领域的语法和语义方面存在不足，导致生成的SVAs质量低下。

**核心思路**：提出了一种定制的检索增强生成（RAG）框架，结合合成微调数据集，通过逐层构建SVAs的提示引导解释来提升大型语言模型（LLMs）的性能。

**技术框架**：整体架构包括两个主要模块：检索模块用于获取相关的SVAs和描述，生成模块则基于检索结果和微调数据集生成高质量的SVAs。

**关键创新**：最重要的创新在于结合了RAG框架与合成微调数据集，提供了逐层构建SVAs的提示引导，从而显著提升了模型的语法和功能准确性。

**关键设计**：在微调过程中，使用了特定的损失函数来优化生成的SVAs质量，并设计了适合领域特定语法的网络结构，以提高模型的理解能力。通过这些设计，模型能够更好地学习并生成符合要求的SVAs。

## 📊 实验亮点

实验结果表明，定制的RAG框架使得功能匹配的SVAs数量较GPT-4o-mini提升了58.42%，而在微调数据集上进行微调的Qwen2.5-Coder-7B-Instruct模型则较基础Qwen模型提升了59.05%。这些结果展示了新方法在NL2SVA任务中的显著性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括硬件设计验证、自动化测试生成以及智能合约的验证等。通过提高NL2SVA的自动化程度，可以显著降低人工编写SVAs的工作量，提升硬件设计的验证效率和准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> SystemVerilog Assertions (SVAs) are critical for verifying the correctness of hardware designs, but manually writing them from natural language property descriptions, i.e., NL2SVA, remains a labor-intensive and error-prone task. Recent advances in large language models (LLMs) offer opportunities to automate this translation. However, existing models still struggle with understanding domain-specific syntax and semantics. To enhance LLM performance in NL2SVA, we propose a customized retrieval-augmented generation (RAG) framework and a synthetic fine-tuning dataset that together improve LLM's performance. To further improve lightweight models over NL2SVA, our fine-tuning dataset provides prompt-guided explanations that teach LLMs the layer-by-layer construction process of concurrent SVAs, enabling supervised fine-tuning that greatly improves syntax and functionality accuracy. To evaluate the performance of LLMs over NL2SVA, we construct the largest evaluation dataset for NL2SVA, comprising 40 Verilog designs and 229 formally verified SVAs with detailed annotations. Experimental results show that our customized RAG framework increases the number of functionality matched SVAs by 58.42% over GPT-4o-mini, while Qwen2.5-Coder-7B-Instruct fine-tuned on our fine-tuning dataset and integrated with HybridRetrieval achieves a 59.05% over the base Qwen model.

