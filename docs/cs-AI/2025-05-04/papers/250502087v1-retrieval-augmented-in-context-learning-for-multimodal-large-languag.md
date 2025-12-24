---
layout: default
title: Retrieval-augmented in-context learning for multimodal large language models in disease classification
---

# Retrieval-augmented in-context learning for multimodal large language models in disease classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02087" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02087v1</a>
  <a href="https://arxiv.org/pdf/2505.02087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02087v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02087v1', 'Retrieval-augmented in-context learning for multimodal large language models in disease classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zaifu Zhan, Shuang Zhou, Xiaoshan Zhou, Yongkang Xiao, Jun Wang, Jiawen Deng, He Zhu, Yu Hou, Rui Zhang

**分类**: cs.AI

**发布日期**: 2025-05-04

**备注**: 17 Pages, 1 figure, 7 tables

---

## 💡 一句话要点

**提出RAICL框架以提升多模态大语言模型在疾病分类中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `疾病分类` `上下文学习` `检索增强生成` `深度学习` `医疗影像分析` `大语言模型`

## 📋 核心要点

1. 现有方法在多模态疾病分类中面临示例选择不当和上下文学习效果不足的挑战。
2. 论文提出的RAICL框架通过动态检索相似示例，结合RAG和ICL，提升多模态学习效果。
3. 实验结果显示，RAICL在TCGA和IU胸部X光数据集上的分类准确率分别提升至0.8368和0.8658，表现出显著的性能改进。

## 📝 摘要（中文）

本研究旨在动态检索信息丰富的示例，增强多模态大语言模型（MLLMs）在疾病分类中的上下文学习。我们提出了检索增强的上下文学习（RAICL）框架，结合了检索增强生成（RAG）和上下文学习（ICL），自适应选择具有相似疾病模式的示例，从而提高MLLMs的学习效果。通过在真实的多模态数据集（TCGA和IU胸部X光）上进行评估，RAICL在多个MLLMs上表现出一致的分类性能提升，证明了其有效性和可扩展性。

## 🔬 方法详解

**问题定义**：本研究旨在解决多模态大语言模型在疾病分类中的上下文学习效果不足，现有方法在示例选择上存在局限性，导致分类性能不佳。

**核心思路**：RAICL框架通过动态检索与任务相关的示例，结合检索增强生成（RAG）和上下文学习（ICL），使模型能够更有效地利用已有知识进行学习。

**技术框架**：RAICL的整体架构包括多个模块：首先，使用不同编码器（如ResNet、BERT、BioBERT和ClinicalBERT）生成嵌入；其次，基于相似度度量检索合适的示例；最后，构建优化的对话提示以增强上下文学习。

**关键创新**：RAICL的主要创新在于其自适应示例检索机制，能够根据疾病模式选择最相关的示例，从而显著提升学习效果，与传统方法相比具有更高的灵活性和准确性。

**关键设计**：在实验中，使用了多种相似度度量（如欧几里得距离和余弦相似度），并发现欧几里得距离在准确率上表现最佳，而余弦相似度在宏观F1分数上更具优势。

## 📊 实验亮点

RAICL在TCGA数据集上的准确率从0.7854提升至0.8368，在IU胸部X光数据集上从0.7924提升至0.8658，显示出多模态输入相较于单模态输入的显著优势，且随着检索示例数量的增加，性能持续提升。

## 🎯 应用场景

该研究的RAICL框架具有广泛的应用潜力，尤其在医疗影像分析和疾病诊断中，可以帮助医生更准确地分类和识别疾病。未来，该方法还可扩展到其他领域的多模态学习任务，提升智能系统的决策能力。

## 📄 摘要（原文）

> Objectives: We aim to dynamically retrieve informative demonstrations, enhancing in-context learning in multimodal large language models (MLLMs) for disease classification.
>   Methods: We propose a Retrieval-Augmented In-Context Learning (RAICL) framework, which integrates retrieval-augmented generation (RAG) and in-context learning (ICL) to adaptively select demonstrations with similar disease patterns, enabling more effective ICL in MLLMs. Specifically, RAICL examines embeddings from diverse encoders, including ResNet, BERT, BioBERT, and ClinicalBERT, to retrieve appropriate demonstrations, and constructs conversational prompts optimized for ICL. We evaluated the framework on two real-world multi-modal datasets (TCGA and IU Chest X-ray), assessing its performance across multiple MLLMs (Qwen, Llava, Gemma), embedding strategies, similarity metrics, and varying numbers of demonstrations.
>   Results: RAICL consistently improved classification performance. Accuracy increased from 0.7854 to 0.8368 on TCGA and from 0.7924 to 0.8658 on IU Chest X-ray. Multi-modal inputs outperformed single-modal ones, with text-only inputs being stronger than images alone. The richness of information embedded in each modality will determine which embedding model can be used to get better results. Few-shot experiments showed that increasing the number of retrieved examples further enhanced performance. Across different similarity metrics, Euclidean distance achieved the highest accuracy while cosine similarity yielded better macro-F1 scores. RAICL demonstrated consistent improvements across various MLLMs, confirming its robustness and versatility.
>   Conclusions: RAICL provides an efficient and scalable approach to enhance in-context learning in MLLMs for multimodal disease classification.

