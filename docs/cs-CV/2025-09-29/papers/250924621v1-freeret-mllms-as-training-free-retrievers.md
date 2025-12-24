---
layout: default
title: "FreeRet: MLLMs as Training-Free Retrievers"
---

# FreeRet: MLLMs as Training-Free Retrievers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24621" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24621v1</a>
  <a href="https://arxiv.org/pdf/2509.24621.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24621v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24621v1', 'FreeRet: MLLMs as Training-Free Retrievers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhan Zhu, Xiangyu Zeng, Chenting Wang, Xinhao Li, Yicheng Xu, Ziang Yan, Yi Wang, Limin Wang

**分类**: cs.CV

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**FreeRet：无需训练，利用MLLM实现强大的多模态检索**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索` `大型语言模型` `零样本学习` `语义嵌入` `重排序`

## 📋 核心要点

1. 现有MLLM检索方法需要大量训练，将其转化为对比编码器，成本高昂且效率低下。
2. FreeRet框架无需额外训练，通过语义嵌入和推理重排序，将MLLM转化为强大的检索器。
3. 实验表明，FreeRet在多个基准测试中显著优于训练模型，且具有良好的泛化性和可扩展性。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)正成为混合模态检索的多功能基础。然而，它们通常需要大量的后训练才能转化为用于检索的对比编码器。本文探讨了：现成的MLLM是否可以在没有额外训练的情况下作为强大的检索器？我们提出了FreeRet，一个即插即用的框架，可以将任何MLLM转化为两阶段检索器。FreeRet首先直接从模型中导出语义相关的嵌入，用于快速候选搜索，然后利用其推理能力进行精确的重排序。该框架贡献了三个方面的进展：绕过词汇对齐层以获得语义忠实的嵌入，使用显式先验调节表示生成，以及通过中性选择框架减轻重排序中的框架效应。在涵盖46个数据集的MMEB和MMEB-V2基准测试中，FreeRet显著优于在数百万个pair上训练的模型。除了基准测试之外，FreeRet是模型无关的，可以在MLLM系列和大小之间无缝扩展，保留其生成能力，支持任意模态组合，并将检索、重排序和生成统一到单个模型中的端到端RAG中。我们的研究结果表明，经过精心利用的预训练MLLM可以在没有训练的情况下作为强大的检索引擎，从而弥补了它们作为通用模型的一个关键差距。

## 🔬 方法详解

**问题定义**：现有的多模态检索方法通常依赖于对比学习，需要大量的训练数据和计算资源来将MLLM转化为对比编码器。这些方法不仅训练成本高昂，而且可能限制了MLLM的通用性和灵活性。此外，词汇对齐层可能会引入噪声，影响检索的准确性。

**核心思路**：FreeRet的核心思路是直接利用预训练MLLM的语义理解和推理能力，无需额外的训练。通过绕过词汇对齐层，获得更准确的语义嵌入，并利用MLLM的推理能力进行重排序，从而提高检索的准确性和效率。

**技术框架**：FreeRet是一个两阶段检索框架。第一阶段是候选检索，利用从MLLM中提取的语义嵌入进行快速搜索。具体来说，通过特定的prompt，引导MLLM生成文本描述，然后提取该文本描述的嵌入向量作为图像/视频的表示。第二阶段是重排序，利用MLLM的推理能力对候选结果进行排序，通过设计中性的prompt，减轻框架效应的影响。

**关键创新**：FreeRet的关键创新在于：1) 无需训练，直接利用预训练MLLM的检索能力；2) 绕过词汇对齐层，获得更准确的语义嵌入；3) 使用显式先验调节表示生成，提高嵌入的质量；4) 通过中性选择框架减轻重排序中的框架效应。与现有方法相比，FreeRet更加高效、灵活和通用。

**关键设计**：FreeRet的关键设计包括：1) 使用特定的prompt引导MLLM生成文本描述，从而提取语义嵌入；2) 设计中性的prompt，减轻重排序中的框架效应；3) 使用余弦相似度作为相似性度量；4) 在重排序阶段，使用MLLM对候选结果进行打分，并根据得分进行排序。

## 📊 实验亮点

FreeRet在MMEB和MMEB-V2基准测试中取得了显著的性能提升，超越了在数百万个pair上训练的模型。例如，在某些数据集上，FreeRet的性能提升超过了10%。此外，FreeRet具有良好的泛化性和可扩展性，可以应用于不同的MLLM模型和不同的模态组合，展示了其强大的检索能力。

## 🎯 应用场景

FreeRet可广泛应用于多模态信息检索、图像/视频搜索、问答系统、推荐系统等领域。它能够降低多模态检索的训练成本，提高检索效率和准确性，并支持任意模态组合，具有重要的实际应用价值和广阔的未来发展前景。例如，可以应用于电商平台的商品搜索，新闻媒体的视频检索，以及智能客服的知识库检索等。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) are emerging as versatile foundations for mixed-modality retrieval. Yet, they often require heavy post-hoc training to convert them into contrastive encoders for retrieval. This work asks: Can off-the-shelf MLLMs serve as powerful retrievers without additional training? We present FreeRet, a plug-and-play framework that turns any MLLM into a two-stage retriever. FreeRet first derives semantically grounded embeddings directly from the model for fast candidate search, and then exploits its reasoning ability for precise reranking. The framework contributes three advances: bypassing lexical alignment layers to obtain semantically faithful embeddings, conditioning representation generation with explicit priors, and mitigating framing effect in reranking via neutral choice framing. On the MMEB and MMEB-V2 benchmarks spanning 46 datasets, FreeRet substantially outperforms models trained on millions of pairs. Beyond benchmarks, FreeRet is model-agnostic and scales seamlessly across MLLM families and sizes, preserves their generative abilities, supports arbitrary modality combinations, and unifies retrieval, reranking, and generation into end-to-end RAG within a single model. Our findings demonstrate that pretrained MLLMs, when carefully harnessed, can serve as strong retrieval engines without training, closing a critical gap in their role as generalists.

