---
layout: default
title: 3DAlign-DAER: Dynamic Attention Policy and Efficient Retrieval Strategy for Fine-grained 3D-Text Alignment at Scale
---

# 3DAlign-DAER: Dynamic Attention Policy and Efficient Retrieval Strategy for Fine-grained 3D-Text Alignment at Scale

**arXiv**: [2511.13211v1](https://arxiv.org/abs/2511.13211) | [PDF](https://arxiv.org/pdf/2511.13211.pdf)

**作者**: Yijia Fan, Jusheng Zhang, Kaitong Cai, Jing Yang, Jian Wang, Keze Wang

---

## 💡 一句话要点

**提出3DAlign-DAER框架，通过动态注意力策略和高效检索策略解决大规模细粒度3D-文本对齐问题。**

**关键词**: `3D-文本对齐` `动态注意力策略` `高效检索` `分层注意力融合` `蒙特卡洛树搜索` `大规模数据集`

## 📋 核心要点

1. 现有方法难以对齐细粒度文本语义与3D几何结构，且在大规模数据库中性能下降。
2. 动态注意力策略使用分层注意力融合和蒙特卡洛树搜索优化细粒度对齐。
3. 高效检索策略在大规模嵌入空间实现分层搜索，实验显示在准确性和效率上优于传统方法。

## 📄 摘要（原文）

> Despite recent advancements in 3D-text cross-modal alignment, existing state-of-the-art methods still struggle to align fine-grained textual semantics with detailed geometric structures, and their alignment performance degrades significantly when scaling to large-scale 3D databases. To overcome this limitation, we introduce 3DAlign-DAER, a unified framework designed to align text and 3D geometry via the proposed dynamic attention policy and the efficient retrieval strategy, capturing subtle correspondences for diverse cross-modal retrieval and classification tasks. Specifically, during the training, our proposed dynamic attention policy (DAP) employs the Hierarchical Attention Fusion (HAF) module to represent the alignment as learnable fine-grained token-to-point attentions. To optimize these attentions across different tasks and geometric hierarchies, our DAP further exploits the Monte Carlo tree search to dynamically calibrate HAF attention weights via a hybrid reward signal and further enhances the alignment between textual descriptions and local 3D geometry. During the inference, our 3DAlign-DAER introduces an Efficient Retrieval Strategy (ERS) to leverage efficient hierarchical searching in the large-scale embedding spaces, outperforming traditional methods (e.g., KNN) in accuracy and efficiency. Furthermore, to facilitate text-3D alignment research and train our 3DAlign-DAER, we construct Align3D-2M, a large-scale dataset featuring 2M text-3D pairs, to provide sufficient fine-grained cross-modal annotations. Extensive and comprehensive experiments demonstrate the superior performance of our 3DAlign-DAER on diverse benchmarks. We will release our codes, models, and datasets.

