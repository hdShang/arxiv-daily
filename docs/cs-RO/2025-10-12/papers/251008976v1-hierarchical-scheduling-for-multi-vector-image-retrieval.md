---
layout: default
title: Hierarchical Scheduling for Multi-Vector Image Retrieval
---

# Hierarchical Scheduling for Multi-Vector Image Retrieval

**arXiv**: [2510.08976v1](https://arxiv.org/abs/2510.08976) | [PDF](https://arxiv.org/pdf/2510.08976.pdf)

**作者**: Maoliang Li, Ke Li, Yaoyang Liu, Jiayu Chen, Zihao Zheng, Yinjun Wu, Xiang Chen

---

## 💡 一句话要点

**提出分层调度框架HiMIR以提升多向量图像检索的准确性和效率**

**关键词**: `多向量图像检索` `分层调度` `检索增强生成` `相似性一致性` `计算效率优化`

## 📋 核心要点

1. 核心问题：传统检索方法准确率低，多向量检索存在对齐不足和冗余计算问题
2. 方法要点：采用分层范式增强查询与图像对象对齐，利用一致性减少冗余匹配
3. 实验效果：在准确率显著提升的同时，计算量减少高达3.5倍

## 📄 摘要（原文）

> To effectively leverage user-specific data, retrieval augmented generation
> (RAG) is employed in multimodal large language model (MLLM) applications.
> However, conventional retrieval approaches often suffer from limited retrieval
> accuracy. Recent advances in multi-vector retrieval (MVR) improve accuracy by
> decomposing queries and matching against segmented images. They still suffer
> from sub-optimal accuracy and efficiency, overlooking alignment between the
> query and varying image objects and redundant fine-grained image segments. In
> this work, we present an efficient scheduling framework for image retrieval -
> HiMIR. First, we introduce a novel hierarchical paradigm, employing multiple
> intermediate granularities for varying image objects to enhance alignment.
> Second, we minimize redundancy in retrieval by leveraging cross-hierarchy
> similarity consistency and hierarchy sparsity to minimize unnecessary matching
> computation. Furthermore, we configure parameters for each dataset
> automatically for practicality across diverse scenarios. Our empirical study
> shows that, HiMIR not only achieves substantial accuracy improvements but also
> reduces computation by up to 3.5 times over the existing MVR system.

