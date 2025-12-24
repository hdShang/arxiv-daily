---
layout: default
title: "LiteLong: Resource-Efficient Long-Context Data Synthesis for LLMs"
---

# LiteLong: Resource-Efficient Long-Context Data Synthesis for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15568" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15568v1</a>
  <a href="https://arxiv.org/pdf/2509.15568.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15568v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15568v1', 'LiteLong: Resource-Efficient Long-Context Data Synthesis for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junlong Jia, Xing Wu, Chaochen Gao, Ziyang Chen, Zijia Lin, Zhongzhi Li, Weinong Wang, Haotian Xu, Donghui Jin, Debing Zhang, Binghui Guo

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-19

**备注**: work in progress

---

## 💡 一句话要点

**LiteLong：一种资源高效的长文本数据合成方法，用于训练大型语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本数据合成` `大型语言模型` `多智能体辩论` `主题组织` `BM25检索`

## 📋 核心要点

1. 现有长文本数据合成方法计算效率低，难以满足大型语言模型训练的需求。
2. LiteLong通过结构化主题组织和多智能体辩论，高效合成高质量长文本数据。
3. 实验表明，LiteLong在长文本基准测试中表现出色，且易于与其他长依赖增强方法集成。

## 📝 摘要（中文）

高质量的长文本数据对于训练能够处理大量文档的大型语言模型至关重要。然而，现有的基于相关性聚合的合成方法面临计算效率的挑战。我们提出了LiteLong，一种资源高效的方法，通过结构化的主题组织和多智能体辩论来合成长文本数据。我们的方法利用BISAC图书分类系统提供全面的分层主题组织，然后采用多LLM辩论机制，在该结构内生成多样化、高质量的主题。对于每个主题，我们使用轻量级的BM25检索来获取相关文档，并将它们连接成128K token的训练样本。在HELMET和Ruler基准测试上的实验表明，LiteLong实现了具有竞争力的长文本性能，并且可以与其他长依赖增强方法无缝集成。LiteLong通过降低计算和数据工程成本，使高质量的长文本数据合成更易于访问，从而促进长文本语言训练的进一步研究。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型训练中，高质量长文本数据合成效率低下的问题。现有方法，如基于相关性聚合的方法，在处理长文本时需要大量的计算资源，使得长文本数据的获取成本很高。

**核心思路**：LiteLong的核心思路是通过结构化的主题组织和多智能体辩论来提高长文本数据合成的效率和质量。首先，利用BISAC图书分类系统构建分层主题结构，然后利用多个LLM进行辩论，生成多样且高质量的主题，最后基于这些主题检索相关文档并拼接成长文本数据。

**技术框架**：LiteLong的整体框架包含以下几个主要阶段：1) **主题组织**：利用BISAC图书分类系统构建分层主题结构。2) **主题生成**：使用多个LLM进行辩论，在主题结构内生成多样且高质量的主题。3) **文档检索**：对于每个生成的主题，使用轻量级的BM25检索算法获取相关文档。4) **数据合成**：将检索到的文档拼接成128K token的长文本训练样本。

**关键创新**：LiteLong的关键创新在于其资源高效的长文本数据合成方法。与传统的基于相关性聚合的方法相比，LiteLong通过结构化的主题组织和多智能体辩论，显著降低了计算成本和数据工程成本，同时保证了生成数据的质量和多样性。

**关键设计**：LiteLong的关键设计包括：1) 使用BISAC图书分类系统作为主题组织的先验知识，避免了从零开始构建主题结构的复杂性。2) 采用多LLM辩论机制，鼓励生成多样化的主题，避免了单一LLM生成主题的偏差。3) 使用轻量级的BM25检索算法，降低了文档检索的计算成本。4) 将长文本样本固定为128K token，方便后续的训练和评估。

## 📊 实验亮点

LiteLong在HELMET和Ruler基准测试中取得了具有竞争力的长文本性能，证明了其有效性。该方法能够与其他长依赖增强方法无缝集成，进一步提升模型性能。LiteLong降低了计算和数据工程成本，使得高质量长文本数据合成更易于访问。

## 🎯 应用场景

LiteLong可应用于各种需要长文本理解的大型语言模型训练场景，例如长文档摘要、问答系统、信息检索等。该方法降低了长文本数据合成的成本，使得更多研究者和开发者能够训练出具有优秀长文本处理能力的模型，从而推动相关领域的进步。

## 📄 摘要（原文）

> High-quality long-context data is essential for training large language models (LLMs) capable of processing extensive documents, yet existing synthesis approaches using relevance-based aggregation face challenges of computational efficiency. We present LiteLong, a resource-efficient method for synthesizing long-context data through structured topic organization and multi-agent debate. Our approach leverages the BISAC book classification system to provide a comprehensive hierarchical topic organization, and then employs a debate mechanism with multiple LLMs to generate diverse, high-quality topics within this structure. For each topic, we use lightweight BM25 retrieval to obtain relevant documents and concatenate them into 128K-token training samples. Experiments on HELMET and Ruler benchmarks demonstrate that LiteLong achieves competitive long-context performance and can seamlessly integrate with other long-dependency enhancement methods. LiteLong makes high-quality long-context data synthesis more accessible by reducing both computational and data engineering costs, facilitating further research in long-context language training.

