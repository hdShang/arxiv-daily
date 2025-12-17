---
layout: default
title: The Best of the Two Worlds: Harmonizing Semantic and Hash IDs for Sequential Recommendation
---

# The Best of the Two Worlds: Harmonizing Semantic and Hash IDs for Sequential Recommendation

**arXiv**: [2512.10388v1](https://arxiv.org/abs/2512.10388) | [PDF](https://arxiv.org/pdf/2512.10388.pdf)

**作者**: Ziwei Liu, Yejing Wang, Qidong Liu, Zijian Zhang, Chong Chen, Wei Huang, Xiangyu Zhao

---

## 💡 一句话要点

**提出H2Rec框架，通过协调语义ID与哈希ID以解决序列推荐中头尾项目性能权衡问题。**

**关键词**: `序列推荐` `语义ID` `哈希ID` `长尾问题` `双分支建模` `知识对齐`

## 📋 核心要点

1. 核心问题：传统哈希ID易受长尾问题影响，语义ID虽能共享代码但面临协作压倒现象，导致头尾项目性能摇摆。
2. 方法要点：设计双分支建模架构，同时捕获语义ID的多粒度语义和哈希ID的独特协作身份，并引入双级对齐策略促进知识转移。
3. 实验或效果：在三个真实数据集上实验显示，H2Rec有效平衡头尾项目推荐质量，超越现有基线。

## 📄 摘要（原文）

> Conventional Sequential Recommender Systems (SRS) typically assign unique Hash IDs (HID) to construct item embeddings. These HID embeddings effectively learn collaborative information from historical user-item interactions, making them vulnerable to situations where most items are rarely consumed (the long-tail problem). Recent methods that incorporate auxiliary information often suffer from noisy collaborative sharing caused by co-occurrence signals or semantic homogeneity caused by flat dense embeddings. Semantic IDs (SIDs), with their capability of code sharing and multi-granular semantic modeling, provide a promising alternative. However, the collaborative overwhelming phenomenon hinders the further development of SID-based methods. The quantization mechanisms commonly compromise the uniqueness of identifiers required for modeling head items, creating a performance seesaw between head and tail items. To address this dilemma, we propose \textbf{\name}, a novel framework that harmonizes the SID and HID. Specifically, we devise a dual-branch modeling architecture that enables the model to capture both the multi-granular semantics within SID while preserving the unique collaborative identity of HID. Furthermore, we introduce a dual-level alignment strategy that bridges the two representations, facilitating knowledge transfer and supporting robust preference modeling. Extensive experiments on three real-world datasets show that \name~ effectively balances recommendation quality for both head and tail items while surpassing the existing baselines. The implementation code can be found online\footnote{https://github.com/ziwliu8/H2Rec}.

