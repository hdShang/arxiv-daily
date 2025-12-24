---
layout: default
title: "Towards LLM-Centric Multimodal Fusion: A Survey on Integration Strategies and Techniques"
---

# Towards LLM-Centric Multimodal Fusion: A Survey on Integration Strategies and Techniques

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04788" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04788v1</a>
  <a href="https://arxiv.org/pdf/2506.04788.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04788v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04788v1', 'Towards LLM-Centric Multimodal Fusion: A Survey on Integration Strategies and Techniques')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jisu An, Junseok Lee, Jeoungeun Lee, Yongseok Son

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-05

**备注**: 18 pages, 3 figures, 3 tables

---

## 💡 一句话要点

**提出LLM中心的多模态融合框架以解决现有整合策略的不足**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大型语言模型` `模态整合` `表示学习` `训练策略` `分类框架` `人工智能` `系统分析`

## 📋 核心要点

1. 现有多模态大型语言模型的整合策略缺乏系统性理解，导致不同模态的连接性不足。
2. 论文提出了一种基于LLM的分类框架，系统分析模态整合的架构、表示学习和训练策略。
3. 通过对125个MLLM的研究，识别出新兴模式，为未来的多模态整合提供了指导。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）的快速发展改变了人工智能的格局。这些模型将预训练的LLM与各种模态编码器结合，要求系统理解不同模态如何连接到语言主干。本文对当前方法进行了LLM中心的分析，探讨了将多样化模态输入转化并对齐到语言嵌入空间的方法，填补了现有文献中的重要空白。我们提出了基于三个关键维度的MLLM分类框架，分别是模态整合的架构策略、表示学习技术的分类以及训练范式的分析。通过对2021至2025年间开发的125个MLLM进行研究，我们识别出该领域的新兴模式，为研究人员提供了当前整合技术的结构化概述，旨在指导未来基于预训练基础的更强大的多模态整合策略的开发。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大型语言模型（MLLMs）中不同模态如何有效整合的问题。现有方法在模态连接性和整合策略上存在不足，缺乏系统性分析。

**核心思路**：论文的核心思路是提出一个LLM中心的分类框架，系统性地分析模态整合的架构、表示学习和训练策略，以填补文献中的空白。

**技术框架**：整体架构包括三个主要模块：模态整合架构策略、表示学习技术分类（联合表示与协调表示）以及训练范式（训练策略与目标函数）。

**关键创新**：最重要的技术创新点在于提出了一个结构化的分类框架，系统性地分析了当前的整合技术，识别出新兴模式，与现有方法相比，提供了更全面的视角。

**关键设计**：在设计中，论文详细讨论了模态整合的具体机制、融合层次、损失函数的选择以及网络结构的设计，以确保不同模态的有效对齐与整合。

## 📊 实验亮点

通过对125个MLLM的分析，论文识别出多模态整合的新兴模式，提供了结构化的分类框架。这一框架为未来的研究提供了重要的指导，促进了多模态技术的进一步发展。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动驾驶、医疗影像分析等多模态任务。通过提供更强大的多模态整合策略，未来的模型能够更好地理解和处理来自不同来源的信息，从而提升人工智能系统的智能水平和应用效果。

## 📄 摘要（原文）

> The rapid progress of Multimodal Large Language Models(MLLMs) has transformed the AI landscape. These models combine pre-trained LLMs with various modality encoders. This integration requires a systematic understanding of how different modalities connect to the language backbone. Our survey presents an LLM-centric analysis of current approaches. We examine methods for transforming and aligning diverse modal inputs into the language embedding space. This addresses a significant gap in existing literature. We propose a classification framework for MLLMs based on three key dimensions. First, we examine architectural strategies for modality integration. This includes both the specific integration mechanisms and the fusion level. Second, we categorize representation learning techniques as either joint or coordinate representations. Third, we analyze training paradigms, including training strategies and objective functions. By examining 125 MLLMs developed between 2021 and 2025, we identify emerging patterns in the field. Our taxonomy provides researchers with a structured overview of current integration techniques. These insights aim to guide the development of more robust multimodal integration strategies for future models built on pre-trained foundations.

