---
layout: default
title: H3Former: Hypergraph-based Semantic-Aware Aggregation via Hyperbolic Hierarchical Contrastive Loss for Fine-Grained Visual Classification
---

# H3Former: Hypergraph-based Semantic-Aware Aggregation via Hyperbolic Hierarchical Contrastive Loss for Fine-Grained Visual Classification

**arXiv**: [2511.10260v1](https://arxiv.org/abs/2511.10260) | [PDF](https://arxiv.org/pdf/2511.10260.pdf)

**作者**: Yongji Zhang, Siqi Li, Kuiyang Huang, Yue Gao, Yu Jiang

---

## 💡 一句话要点

**提出H3Former框架以解决细粒度视觉分类中的语义冗余和依赖捕获问题**

**关键词**: `细粒度视觉分类` `超图卷积` `语义聚合` `双曲嵌入` `对比学习` `区域级建模`

## 📋 核心要点

1. 细粒度视觉分类存在类间差异细微和类内变化大的核心挑战
2. 方法结合超图语义聚合和双曲层次对比损失，提升特征表示
3. 在四个标准基准测试中验证了框架的优越性能

## 📄 摘要（原文）

> Fine-Grained Visual Classification (FGVC) remains a challenging task due to subtle inter-class differences and large intra-class variations. Existing approaches typically rely on feature-selection mechanisms or region-proposal strategies to localize discriminative regions for semantic analysis. However, these methods often fail to capture discriminative cues comprehensively while introducing substantial category-agnostic redundancy. To address these limitations, we propose H3Former, a novel token-to-region framework that leverages high-order semantic relations to aggregate local fine-grained representations with structured region-level modeling. Specifically, we propose the Semantic-Aware Aggregation Module (SAAM), which exploits multi-scale contextual cues to dynamically construct a weighted hypergraph among tokens. By applying hypergraph convolution, SAAM captures high-order semantic dependencies and progressively aggregates token features into compact region-level representations. Furthermore, we introduce the Hyperbolic Hierarchical Contrastive Loss (HHCL), which enforces hierarchical semantic constraints in a non-Euclidean embedding space. The HHCL enhances inter-class separability and intra-class consistency while preserving the intrinsic hierarchical relationships among fine-grained categories. Comprehensive experiments conducted on four standard FGVC benchmarks validate the superiority of our H3Former framework.

