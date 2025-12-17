---
layout: default
title: Text-based Aerial-Ground Person Retrieval
---

# Text-based Aerial-Ground Person Retrieval

**arXiv**: [2511.08369v1](https://arxiv.org/abs/2511.08369) | [PDF](https://arxiv.org/pdf/2511.08369.pdf)

**作者**: Xinyu Zhou, Yu Wu, Jiayao Ma, Wenhao Wang, Min Cao, Mang Ye

---

## 💡 一句话要点

**提出TAG-PR任务和TAG-CLIP框架，以解决基于文本的空中-地面行人检索中的视角差异问题。**

**关键词**: `文本行人检索` `多视角图像检索` `跨模态对齐` `数据集构建` `混合专家模型`

## 📋 核心要点

1. 核心问题：空中与地面视图间存在大视角差异，增加了文本描述检索行人图像的难度。
2. 方法要点：使用分层路由专家模块和视角解耦策略，学习视图特定和视图无关特征。
3. 实验或效果：在TAG-PEDES数据集和现有基准上评估，框架有效提升检索性能。

## 📄 摘要（原文）

> This work introduces Text-based Aerial-Ground Person Retrieval (TAG-PR), which aims to retrieve person images from heterogeneous aerial and ground views with textual descriptions. Unlike traditional Text-based Person Retrieval (T-PR), which focuses solely on ground-view images, TAG-PR introduces greater practical significance and presents unique challenges due to the large viewpoint discrepancy across images. To support this task, we contribute: (1) TAG-PEDES dataset, constructed from public benchmarks with automatically generated textual descriptions, enhanced by a diversified text generation paradigm to ensure robustness under view heterogeneity; and (2) TAG-CLIP, a novel retrieval framework that addresses view heterogeneity through a hierarchically-routed mixture of experts module to learn view-specific and view-agnostic features and a viewpoint decoupling strategy to decouple view-specific features for better cross-modal alignment. We evaluate the effectiveness of TAG-CLIP on both the proposed TAG-PEDES dataset and existing T-PR benchmarks. The dataset and code are available at https://github.com/Flame-Chasers/TAG-PR.

