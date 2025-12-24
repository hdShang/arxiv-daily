---
layout: default
title: "CLaMR: Contextualized Late-Interaction for Multimodal Content Retrieval"
---

# CLaMR: Contextualized Late-Interaction for Multimodal Content Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06144" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06144v1</a>
  <a href="https://arxiv.org/pdf/2506.06144.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06144v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06144v1', 'CLaMR: Contextualized Late-Interaction for Multimodal Content Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: David Wan, Han Wang, Elias Stengel-Eskin, Jaemin Cho, Mohit Bansal

**分类**: cs.CV, cs.CL, cs.IR

**发布日期**: 2025-06-06

**备注**: 18 pages. Code and data: https://github.com/meetdavidwan/clamr

---

## 💡 一句话要点

**提出CLaMR以解决多模态视频内容检索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索` `视频理解` `动态模态选择` `合成数据集` `模态感知损失` `长视频问答` `信息检索`

## 📋 核心要点

1. 现有多模态视频检索方法通常将不同模态视为独立来源，导致检索结果噪声大且效果不佳。
2. CLaMR通过统一编码多模态数据，利用动态模态选择机制，提升检索的相关性和准确性。
3. 在MultiVENT 2.0++和MSRVTT测试集上，CLaMR在nDCG@10上分别比最佳单模态和多模态检索器提升了25.6和35.4。

## 📝 摘要（中文）

在线视频内容具有丰富的多模态特性，通常包括视觉、语音、环境音频和屏幕文本。现有的检索系统往往将这些模态视为独立的检索源，导致检索效果不佳。本文提出CLaMR，一个多模态的晚期交互检索器，能够联合索引视频帧、转录语音、屏幕文本和元数据。CLaMR通过统一的多模态骨干网络进行编码，以增强上下文理解，并通过引入MultiVENT 2.0++合成数据集和模态感知损失函数来提升动态模态选择能力。实验结果表明，CLaMR在多个基准数据集上显著优于现有检索器。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态视频内容检索中模态独立处理导致的噪声和效果不佳的问题。现有方法未能有效利用模态间的关联性，影响了检索的准确性。

**核心思路**：CLaMR通过联合编码视频帧、转录语音、屏幕文本和元数据，利用统一的多模态骨干网络来增强上下文理解，并通过动态模态选择机制来提升检索效果。

**技术框架**：CLaMR的整体架构包括数据预处理、模态编码、动态模态选择和检索模块。首先，输入的多模态数据经过统一编码，然后根据查询动态选择最相关的模态进行检索。

**关键创新**：CLaMR的主要创新在于引入了MultiVENT 2.0++合成数据集和模态感知损失函数，前者为多模态检索提供了丰富的训练数据，后者则优化了模态使用的学习过程。

**关键设计**：在损失函数设计上，CLaMR结合了标准对比损失和模态感知损失，以确保模型能够有效学习各模态的使用。同时，网络结构采用了先进的多模态骨干网络，以提升特征提取的能力。

## 📊 实验亮点

CLaMR在多个基准测试集上表现优异，特别是在MultiVENT 2.0++上，CLaMR的nDCG@10比最佳单模态检索器提升了25.6，比最佳多模态检索器提升了35.4。此外，在长视频问答任务中，CLaMR在Video-MME上比LanguageBind提升了3.50%，在LongVideoBench上比密集采样提升了1.42%。

## 🎯 应用场景

CLaMR的研究成果在多模态视频检索领域具有广泛的应用潜力，尤其是在长视频问答、视频内容推荐和信息检索等场景中。通过提升检索的准确性和相关性，CLaMR能够为用户提供更为精准的内容推荐，进而改善用户体验。未来，该技术还可能扩展到其他多模态数据处理领域，如图像与文本的联合检索。

## 📄 摘要（原文）

> Online video web content is richly multimodal: a single video blends vision, speech, ambient audio, and on-screen text. Retrieval systems typically treat these modalities as independent retrieval sources, which can lead to noisy and subpar retrieval. We explore multimodal video content retrieval, where relevance can be scored from one particular modality or jointly across multiple modalities simultaneously. Consequently, an effective retriever must dynamically choose which modality (or set of modalities) best addresses the query. We introduce CLaMR, a multimodal, late-interaction retriever that jointly indexes 4 modalities: video frames, transcribed speech, on-screen text, and metadata. CLaMR jointly encodes all modalities with a unified multimodal backbone for improved contextualization and is trained to enhance dynamic modality selection via two key innovations. First, given the lack of training data for multimodal retrieval, we introduce MultiVENT 2.0++, a large-scale synthetic training dataset built on MultiVENT 2.0 (event-centric videos in various languages paired with queries) with modality-targeted queries. Next, we propose a modality-aware loss that jointly trains according to a standard contrastive objective alongside an objective for learning correct modality usage. On the test sets of MultiVENT 2.0++ and MSRVTT, conventional aggregation strategies, such as averaging similarities for baseline retrievers, degrade performance by introducing noise from irrelevant modalities. In contrast, CLaMR consistently outperforms existing retrievers: on MultiVENT 2.0++, CLaMR improves nDCG@10 by 25.6 over the best single-modality retriever and by 35.4 over the best multi-modality retriever. We illustrate CLaMR's downstream utility on long-video QA, retrieving relevant frames and obtaining a 3.50% boost over LanguageBind on Video-MME and 1.42% over dense sampling on LongVideoBench.

