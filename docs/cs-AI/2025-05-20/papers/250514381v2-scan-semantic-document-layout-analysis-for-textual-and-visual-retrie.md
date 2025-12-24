---
layout: default
title: SCAN: Semantic Document Layout Analysis for Textual and Visual Retrieval-Augmented Generation
---

# SCAN: Semantic Document Layout Analysis for Textual and Visual Retrieval-Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14381" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14381v2</a>
  <a href="https://arxiv.org/pdf/2505.14381.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14381v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14381v2', 'SCAN: Semantic Document Layout Analysis for Textual and Visual Retrieval-Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuyang Dong, Nobuhiro Ueda, Krisztián Boros, Daiki Ito, Takuya Sera, Masafumi Oyamada

**分类**: cs.AI

**发布日期**: 2025-05-20 (更新: 2025-12-11)

---

## 💡 一句话要点

**提出SCAN以解决丰富文档的检索增强生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文档分析` `检索增强生成` `视觉语言模型` `语义分析` `信息提取`

## 📋 核心要点

1. 现有方法在处理丰富文档时面临信息量大、上下文保留与处理效率之间的平衡挑战。
2. SCAN通过粗粒度语义分析，将文档划分为连贯区域，从而提高文本和视觉RAG系统的性能。
3. 实验结果显示，SCAN在文本RAG和视觉RAG性能上分别提升了9.4分和10.4分，优于传统方法。

## 📝 摘要（中文）

随着大型语言模型（LLMs）和视觉语言模型（VLMs）的广泛应用，针对检索增强生成（RAG）和视觉RAG的文档分析技术受到越来越多的关注。尽管VLMs在RAG性能上表现优越，但处理丰富文档仍然是一大挑战。本文提出了SCAN（语义文档布局分析），一种新颖的方法，旨在增强处理视觉丰富文档的文本和视觉RAG系统。SCAN通过粗粒度语义方法将文档划分为连贯区域，平衡了上下文保留与处理效率。实验结果表明，SCAN在英语和日语数据集上显著提升了文本RAG性能（最高提升9.4分）和视觉RAG性能（最高提升10.4分），超越了传统方法和商业文档处理解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决在处理丰富文档时，现有方法无法有效平衡上下文保留与处理效率的问题，导致RAG性能受限。

**核心思路**：SCAN采用粗粒度语义分析，将文档划分为连贯的区域，确保在处理时能够保留必要的上下文信息，同时提高处理效率。这样的设计使得模型能够更好地理解文档结构和内容。

**技术框架**：SCAN的整体架构包括文档组件识别、语义区域划分和基于VLM的生成模块。首先，通过对象检测模型对文档进行细致标注，然后将文档划分为多个语义区域，最后利用VLM进行生成任务。

**关键创新**：SCAN的主要创新在于其粗粒度语义分析方法，能够有效识别文档中的连贯区域，与传统方法相比，显著提升了RAG系统的性能。

**关键设计**：在模型训练中，SCAN通过对标注数据集进行微调，采用特定的损失函数和网络结构，以优化文档组件的识别和语义区域的划分。

## 📊 实验亮点

实验结果表明，SCAN在英语和日语数据集上，文本RAG性能提升最高达9.4分，视觉RAG性能提升最高达10.4分，显著优于传统方法和商业解决方案，展示了其在实际应用中的有效性。

## 🎯 应用场景

SCAN的研究成果在多个领域具有广泛的应用潜力，包括文档检索、信息提取和智能问答系统。通过提升对丰富文档的理解能力，SCAN能够为用户提供更准确的信息检索和生成服务，推动文档处理技术的进步。

## 📄 摘要（原文）

> With the increasing adoption of Large Language Models (LLMs) and Vision-Language Models (VLMs), rich document analysis technologies for applications like Retrieval-Augmented Generation (RAG) and visual RAG are gaining significant attention. Recent research indicates that using VLMs yields better RAG performance, but processing rich documents remains a challenge since a single page contains large amounts of information. In this paper, we present SCAN (SemantiC Document Layout ANalysis), a novel approach that enhances both textual and visual Retrieval-Augmented Generation (RAG) systems that work with visually rich documents. It is a VLM-friendly approach that identifies document components with appropriate semantic granularity, balancing context preservation with processing efficiency. SCAN uses a coarse-grained semantic approach that divides documents into coherent regions covering contiguous components. We trained the SCAN model by fine-tuning object detection models on an annotated dataset. Our experimental results across English and Japanese datasets demonstrate that applying SCAN improves end-to-end textual RAG performance by up to 9.4 points and visual RAG performance by up to 10.4 points, outperforming conventional approaches and even commercial document processing solutions.

