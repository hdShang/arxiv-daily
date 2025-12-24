---
layout: default
title: "Scaling Legal AI: Benchmarking Mamba and Transformers for Statutory Classification and Case Law Retrieval"
---

# Scaling Legal AI: Benchmarking Mamba and Transformers for Statutory Classification and Case Law Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00141" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00141v1</a>
  <a href="https://arxiv.org/pdf/2509.00141.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00141v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00141v1', 'Scaling Legal AI: Benchmarking Mamba and Transformers for Statutory Classification and Case Law Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anuraj Maurya

**分类**: cs.CY, cs.AI, cs.LG

**发布日期**: 2025-08-29

---

## 💡 一句话要点

**提出Mamba模型以解决法律AI的长文档处理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `法律AI` `长文档处理` `状态空间模型` `Transformer` `自然语言处理` `案例检索` `文档分类` `机器学习`

## 📋 核心要点

1. 现有的Transformer模型在处理长文档时效率低下，尤其是在法律领域的应用中，导致分类和检索性能受限。
2. 本文提出Mamba模型，利用线性时间选择机制，旨在提高法律文档处理的效率和可扩展性。
3. 实验结果显示，Mamba能够处理的文档长度是Transformer的几倍，同时在分类和检索任务中表现优异。

## 📝 摘要（中文）

随着法定文献和司法判决的快速增长，迫切需要可扩展的法律AI系统来处理极长上下文的分类和检索任务。当前基于Transformer的架构（如Longformer和DeBERTa）在法律自然语言处理基准中占据主导地位，但由于其二次注意力成本，效率和可扩展性受到限制。本文首次对Mamba这一具有线性时间选择机制的状态空间模型（SSM）进行全面基准测试，评估其在法定分类和案例检索中的表现。实验结果表明，Mamba在处理比Transformer长得多的法律文档时，能够保持或超越检索和分类性能，同时引入了新的法律NLP基准套件，支持可重复性研究。

## 🔬 方法详解

**问题定义**：本文旨在解决现有法律AI系统在处理长文档时的效率和可扩展性问题，尤其是Transformer模型在二次注意力机制下的性能瓶颈。

**核心思路**：论文提出Mamba模型，采用状态空间模型（SSM）和线性时间选择机制，以提高对长文档的处理能力，旨在在保持性能的同时降低计算复杂度。

**技术框架**：Mamba模型的整体架构包括输入层、状态空间模块和输出层，能够有效地处理长上下文信息。模型通过选择性机制来聚焦于重要信息，从而提高处理效率。

**关键创新**：Mamba的主要创新在于其线性时间复杂度的选择机制，与传统的Transformer模型相比，显著降低了计算成本，使得处理长文档成为可能。

**关键设计**：Mamba模型的设计包括优化的参数设置和损失函数，采用了适应性学习率和正则化技术，以确保模型在长文档处理中的稳定性和准确性。具体的网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，Mamba模型在处理法律文档时的效率显著高于传统的Transformer模型，能够处理的文档长度是其几倍，同时在准确性、召回率和其他评估指标上保持或超越了现有基线，展示了其在法律NLP领域的强大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括法律文书的自动分类、司法判决的预测以及案例检索等。Mamba模型的高效性和可扩展性使其在法律分析、司法决策支持和政策研究中具有重要的实际价值，未来可能推动法律AI技术的广泛应用。

## 📄 摘要（原文）

> The rapid growth of statutory corpora and judicial decisions requires scalable legal AI systems capable of classification and retrieval over extremely long contexts. Transformer-based architectures (e.g., Longformer, DeBERTa) dominate current legal NLP benchmarks but struggle with quadratic attention costs, limiting efficiency and scalability. In this work, we present the first comprehensive benchmarking of Mamba, a state-space model (SSM) with linear-time selective mechanisms, against leading transformer models for statutory classification and case law retrieval. We evaluate models on open-source legal corpora including LexGLUE, EUR-Lex, and ILDC, covering statutory tagging, judicial outcome prediction, and case retrieval tasks. Metrics include accuracy, recall at k, mean reciprocal rank (MRR), and normalized discounted cumulative gain (nDCG), alongside throughput measured in tokens per second and maximum context length. Results show that Mamba's linear scaling enables processing of legal documents several times longer than transformers, while maintaining or surpassing retrieval and classification performance. This study introduces a new legal NLP benchmark suite for long-context modeling, along with open-source code and datasets to support reproducibility. Our findings highlight trade-offs between state-space models and transformers, providing guidance for deploying scalable legal AI in statutory analysis, judicial decision support, and policy research.

