---
layout: default
title: MUSE: A Simple Yet Effective Multimodal Search-Based Framework for Lifelong User Interest Modeling
---

# MUSE: A Simple Yet Effective Multimodal Search-Based Framework for Lifelong User Interest Modeling

**arXiv**: [2512.07216v1](https://arxiv.org/abs/2512.07216) | [PDF](https://arxiv.org/pdf/2512.07216.pdf)

**作者**: Bin Wu, Feifan Yang, Zhangming Chan, Yu-Ran Gu, Jiawei Feng, Chao Yi, Xiang-Rong Sheng, Han Zhu, Jian Xu, Mang Ye, Bo Zheng

---

## 💡 一句话要点

**提出MUSE框架，通过两阶段多模态搜索解决推荐系统中终身用户兴趣建模的泛化与语义表达问题。**

**关键词**: `终身用户兴趣建模` `多模态搜索` `推荐系统` `行为序列建模` `工业部署`

## 📋 核心要点

1. 核心问题：现有方法依赖ID特征，在长尾物品上泛化差且语义表达有限。
2. 方法要点：在GSU阶段使用轻量余弦相似度，在ESU阶段结合多模态序列建模与ID-多模态融合。
3. 实验或效果：部署于淘宝广告系统，支持10万长度行为序列建模，显著提升指标且在线延迟可忽略。

## 📄 摘要（原文）

> Lifelong user interest modeling is crucial for industrial recommender systems, yet existing approaches rely predominantly on ID-based features, suffering from poor generalization on long-tail items and limited semantic expressiveness. While recent work explores multimodal representations for behavior retrieval in the General Search Unit (GSU), they often neglect multimodal integration in the fine-grained modeling stage -- the Exact Search Unit (ESU). In this work, we present a systematic analysis of how to effectively leverage multimodal signals across both stages of the two-stage lifelong modeling framework. Our key insight is that simplicity suffices in the GSU: lightweight cosine similarity with high-quality multimodal embeddings outperforms complex retrieval mechanisms. In contrast, the ESU demands richer multimodal sequence modeling and effective ID-multimodal fusion to unlock its full potential. Guided by these principles, we propose MUSE, a simple yet effective multimodal search-based framework. MUSE has been deployed in Taobao display advertising system, enabling 100K-length user behavior sequence modeling and delivering significant gains in top-line metrics with negligible online latency overhead. To foster community research, we share industrial deployment practices and open-source the first large-scale dataset featuring ultra-long behavior sequences paired with high-quality multimodal embeddings. Our code and data is available at https://taobao-mm.github.io.

