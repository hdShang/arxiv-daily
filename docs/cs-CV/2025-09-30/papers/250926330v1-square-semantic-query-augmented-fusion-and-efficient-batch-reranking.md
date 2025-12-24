---
layout: default
title: "SQUARE: Semantic Query-Augmented Fusion and Efficient Batch Reranking for Training-free Zero-Shot Composed Image Retrieval"
---

# SQUARE: Semantic Query-Augmented Fusion and Efficient Batch Reranking for Training-free Zero-Shot Composed Image Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26330" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26330v1</a>
  <a href="https://arxiv.org/pdf/2509.26330.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26330v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26330v1', 'SQUARE: Semantic Query-Augmented Fusion and Efficient Batch Reranking for Training-free Zero-Shot Composed Image Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ren-Di Wu, Yu-Yen Lin, Huei-Fang Yang

**分类**: cs.CV, cs.IR

**发布日期**: 2025-09-30

**备注**: 20 pages, 9 figures

---

## 💡 一句话要点

**提出SQUARE框架，通过语义增强和高效重排序实现免训练零样本组合图像检索**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `组合图像检索` `零样本学习` `多模态大语言模型` `语义增强` `批重排序`

## 📋 核心要点

1. 零样本组合图像检索旨在根据参考图像和文本修改检索目标图像，现有方法难以准确捕捉用户意图。
2. SQUARE框架利用MLLM生成目标图像的描述，增强查询嵌入，并使用高效批重排序策略提升检索精度。
3. 实验表明，SQUARE在多个CIR基准上表现出色，即使使用轻量级预训练模型也能保持高性能。

## 📝 摘要（中文）

本文提出SQUARE，一种新颖的两阶段免训练框架，利用多模态大语言模型(MLLM)来增强零样本组合图像检索(ZS-CIR)。在语义查询增强融合(SQAF)阶段，我们使用MLLM生成的关于目标图像的描述来丰富从视觉-语言模型(VLM)（如CLIP）导出的查询嵌入。这些描述提供高层次的语义指导，使查询能够更好地捕捉用户的意图并提高全局检索质量。在高效批重排序(EBR)阶段，将排名靠前的候选图像以带有视觉标记的图像网格形式呈现给MLLM，MLLM对所有候选图像执行联合视觉-语义推理。我们的重排序策略在单次传递中运行，并产生更准确的排名。实验表明，SQUARE以其简单性和有效性，在四个标准CIR基准上实现了强大的性能。值得注意的是，即使使用轻量级预训练模型，它也能保持高性能，证明了其潜在的适用性。

## 🔬 方法详解

**问题定义**：组合图像检索(CIR)旨在根据给定的参考图像和文本描述，检索出既包含参考图像的视觉内容，又符合文本描述修改的目标图像。现有的免训练零样本CIR方法，虽然不需要特定任务的训练数据，但难以准确捕捉用户的意图，导致检索效果不佳。

**核心思路**：SQUARE的核心思路是利用多模态大语言模型(MLLM)的强大语义理解和推理能力，来增强查询的表达能力，并对检索结果进行更精确的重排序。通过MLLM生成目标图像的语义描述，可以弥补视觉-语言模型(VLM)在理解复杂文本修改意图方面的不足。

**技术框架**：SQUARE框架包含两个主要阶段：语义查询增强融合(SQAF)和高效批重排序(EBR)。在SQAF阶段，首先使用VLM（如CLIP）提取参考图像和文本描述的特征，然后利用MLLM生成目标图像的描述，并将这些描述融入到查询嵌入中。在EBR阶段，将SQAF阶段检索出的Top-K个候选图像以图像网格的形式输入到MLLM中，MLLM对这些候选图像进行联合视觉-语义推理，并根据推理结果重新排序。

**关键创新**：SQUARE的关键创新在于利用MLLM来增强查询的语义表达能力，并进行高效的批重排序。传统的VLM在处理复杂的文本修改意图时存在局限性，而MLLM可以提供更丰富的语义信息，从而提高检索的准确性。此外，EBR阶段的联合视觉-语义推理可以更好地捕捉候选图像之间的关系，从而产生更准确的排名。

**关键设计**：在SQAF阶段，MLLM生成的描述被用来增强VLM提取的查询嵌入。具体来说，可以将MLLM生成的描述转换为文本嵌入，然后与VLM提取的图像和文本嵌入进行融合。融合的方式可以是简单的拼接，也可以是更复杂的注意力机制。在EBR阶段，图像网格的大小和视觉标记的设计会影响MLLM的推理效果。此外，如何设计损失函数来指导MLLM进行重排序也是一个关键的技术细节。具体参数设置和网络结构在论文中未明确说明，属于未知信息。

## 📊 实验亮点

SQUARE框架在四个标准CIR基准测试中表现出色，证明了其有效性。具体性能数据和对比基线在论文中未明确给出，属于未知信息。但论文强调，即使使用轻量级预训练模型，SQUARE也能保持高性能，表明其具有良好的泛化能力和实用价值。

## 🎯 应用场景

SQUARE框架可应用于电商、搜索引擎、图像编辑等领域。例如，在电商平台上，用户可以通过上传一张参考图片并添加文字描述（如“红色连衣裙”）来检索目标商品。在图像编辑领域，用户可以通过指定参考图像和修改描述（如“去除背景”）来生成新的图像。该研究的未来影响在于推动零样本组合图像检索技术的发展，降低对标注数据的依赖，并提高检索的准确性和效率。

## 📄 摘要（原文）

> Composed Image Retrieval (CIR) aims to retrieve target images that preserve the visual content of a reference image while incorporating user-specified textual modifications. Training-free zero-shot CIR (ZS-CIR) approaches, which require no task-specific training or labeled data, are highly desirable, yet accurately capturing user intent remains challenging. In this paper, we present SQUARE, a novel two-stage training-free framework that leverages Multimodal Large Language Models (MLLMs) to enhance ZS-CIR. In the Semantic Query-Augmented Fusion (SQAF) stage, we enrich the query embedding derived from a vision-language model (VLM) such as CLIP with MLLM-generated captions of the target image. These captions provide high-level semantic guidance, enabling the query to better capture the user's intent and improve global retrieval quality. In the Efficient Batch Reranking (EBR) stage, top-ranked candidates are presented as an image grid with visual marks to the MLLM, which performs joint visual-semantic reasoning across all candidates. Our reranking strategy operates in a single pass and yields more accurate rankings. Experiments show that SQUARE, with its simplicity and effectiveness, delivers strong performance on four standard CIR benchmarks. Notably, it maintains high performance even with lightweight pre-trained, demonstrating its potential applicability.

