---
layout: default
title: A Simple and Effective Framework for Symmetric Consistent Indexing in Large-Scale Dense Retrieval
---

# A Simple and Effective Framework for Symmetric Consistent Indexing in Large-Scale Dense Retrieval

**arXiv**: [2512.13074v1](https://arxiv.org/abs/2512.13074) | [PDF](https://arxiv.org/pdf/2512.13074.pdf)

**作者**: Huimu Wang, Yiming Qiu, Xingzhi Yao, Zhiguo Chen, Guoyu Tang, Songlin Wang, Sulong Xu, Mingming Li

---

## 💡 一句话要点

**提出对称一致索引框架以解决大规模稠密检索中的表示空间错位与索引不一致问题**

**关键词**: `稠密检索` `对称表示对齐` `一致索引` `双塔架构` `语义ID生成` `大规模信息检索`

## 📋 核心要点

1. 核心问题：双塔编码架构导致表示空间错位和检索索引不一致，影响匹配精度和长尾查询性能
2. 方法要点：通过对称表示对齐模块和双塔协同一致索引模块，统一表示空间并保持训练到推理的一致性
3. 实验或效果：在公开和电商数据集上验证有效性，支持十亿级部署且开销小

## 📄 摘要（原文）

> Dense retrieval has become the industry standard in large-scale information retrieval systems due to its high efficiency and competitive accuracy. Its core relies on a coarse-to-fine hierarchical architecture that enables rapid candidate selection and precise semantic matching, achieving millisecond-level response over billion-scale corpora. This capability makes it essential not only in traditional search and recommendation scenarios but also in the emerging paradigm of generative recommendation driven by large language models, where semantic IDs-themselves a form of coarse-to-fine representation-play a foundational role. However, the widely adopted dual-tower encoding architecture introduces inherent challenges, primarily representational space misalignment and retrieval index inconsistency, which degrade matching accuracy, retrieval stability, and performance on long-tail queries. These issues are further magnified in semantic ID generation, ultimately limiting the performance ceiling of downstream generative models.
>   To address these challenges, this paper proposes a simple and effective framework named SCI comprising two synergistic modules: a symmetric representation alignment module that employs an innovative input-swapping mechanism to unify the dual-tower representation space without adding parameters, and an consistent indexing with dual-tower synergy module that redesigns retrieval paths using a dual-view indexing strategy to maintain consistency from training to inference. The framework is systematic, lightweight, and engineering-friendly, requiring minimal overhead while fully supporting billion-scale deployment. We provide theoretical guarantees for our approach, with its effectiveness validated by results across public datasets and real-world e-commerce datasets.

