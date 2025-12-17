---
layout: default
title: Prototype-Based Semantic Consistency Alignment for Domain Adaptive Retrieval
---

# Prototype-Based Semantic Consistency Alignment for Domain Adaptive Retrieval

**arXiv**: [2512.04524v1](https://arxiv.org/abs/2512.04524) | [PDF](https://arxiv.org/pdf/2512.04524.pdf)

**作者**: Tianle Hu, Weijun Lv, Na Han, Xiaozhao Fang, Jie Wen, Jiaxing Li, Guoxu Zhou

---

## 💡 一句话要点

**提出基于原型的语义一致性对齐方法，以解决领域自适应检索中的语义对齐与哈希编码质量问题。**

**关键词**: `领域自适应检索` `语义对齐` `原型学习` `哈希编码` `伪标签可靠性` `特征重构`

## 📋 核心要点

1. 核心问题：现有方法忽视类级语义对齐，过度依赖样本对对齐，且伪标签可靠性不足，影响哈希编码质量。
2. 方法要点：采用两阶段框架，第一阶段通过正交原型实现类级语义对齐，结合几何邻近性加权伪标签置信度；第二阶段在重构特征上应用量化函数生成跨域统一哈希码。
3. 实验或效果：在多个数据集上验证了PSCA的优越性能，提升了检索效果。

## 📄 摘要（原文）

> Domain adaptive retrieval aims to transfer knowledge from a labeled source domain to an unlabeled target domain, enabling effective retrieval while mitigating domain discrepancies. However, existing methods encounter several fundamental limitations: 1) neglecting class-level semantic alignment and excessively pursuing pair-wise sample alignment; 2) lacking either pseudo-label reliability consideration or geometric guidance for assessing label correctness; 3) directly quantizing original features affected by domain shift, undermining the quality of learned hash codes. In view of these limitations, we propose Prototype-Based Semantic Consistency Alignment (PSCA), a two-stage framework for effective domain adaptive retrieval. In the first stage, a set of orthogonal prototypes directly establishes class-level semantic connections, maximizing inter-class separability while gathering intra-class samples. During the prototype learning, geometric proximity provides a reliability indicator for semantic consistency alignment through adaptive weighting of pseudo-label confidences. The resulting membership matrix and prototypes facilitate feature reconstruction, ensuring quantization on reconstructed rather than original features, thereby improving subsequent hash coding quality and seamlessly connecting both stages. In the second stage, domain-specific quantization functions process the reconstructed features under mutual approximation constraints, generating unified binary hash codes across domains. Extensive experiments validate PSCA's superior performance across multiple datasets.

