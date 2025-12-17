---
layout: default
title: From Detection to Association: Learning Discriminative Object Embeddings for Multi-Object Tracking
---

# From Detection to Association: Learning Discriminative Object Embeddings for Multi-Object Tracking

**arXiv**: [2512.02392v1](https://arxiv.org/abs/2512.02392) | [PDF](https://arxiv.org/pdf/2512.02392.pdf)

**作者**: Yuqing Shao, Yuchen Yang, Rui Yu, Weilong Li, Xu Guo, Huaicheng Yan, Wei Wang, Xiao Sun

---

## 💡 一句话要点

**提出FDTA框架，通过空间、时间和身份适配器增强对象嵌入的判别性，以解决端到端多目标跟踪中关联准确率低的问题。**

**关键词**: `多目标跟踪` `端到端学习` `对象嵌入` `判别性特征` `对比学习` `时空连续性`

## 📋 核心要点

1. 核心问题：端到端多目标跟踪方法中，共享DETR架构生成的对象嵌入在帧间相似度过高，导致关联准确率不足。
2. 方法要点：引入FDTA框架，包含空间适配器（整合深度感知线索）、时间适配器（聚合历史信息）和身份适配器（基于质量感知对比学习），从三个互补角度优化对象嵌入。
3. 实验或效果：在DanceTrack、SportsMOT和BFT等多个挑战性基准测试中达到最先进性能，验证了增强判别性嵌入策略的有效性。

## 📄 摘要（原文）

> End-to-end multi-object tracking (MOT) methods have recently achieved remarkable progress by unifying detection and association within a single framework. Despite their strong detection performance, these methods suffer from relatively low association accuracy. Through detailed analysis, we observe that object embeddings produced by the shared DETR architecture display excessively high inter-object similarity, as it emphasizes only category-level discrimination within single frames. In contrast, tracking requires instance-level distinction across frames with spatial and temporal continuity, for which current end-to-end approaches insufficiently optimize object embeddings. To address this, we introduce FDTA (From Detection to Association), an explicit feature refinement framework that enhances object discriminativeness across three complementary perspectives. Specifically, we introduce a Spatial Adapter (SA) to integrate depth-aware cues for spatial continuity, a Temporal Adapter (TA) to aggregate historical information for temporal dependencies, and an Identity Adapter (IA) to leverage quality-aware contrastive learning for instance-level separability. Extensive experiments demonstrate that FDTA achieves state-of-the-art performance on multiple challenging MOT benchmarks, including DanceTrack, SportsMOT, and BFT, highlighting the effectiveness of our proposed discriminative embedding enhancement strategy. The code is available at https://github.com/Spongebobbbbbbbb/FDTA.

