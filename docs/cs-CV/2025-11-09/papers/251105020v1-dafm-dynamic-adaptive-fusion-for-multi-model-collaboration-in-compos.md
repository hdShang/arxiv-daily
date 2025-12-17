---
layout: default
title: DAFM: Dynamic Adaptive Fusion for Multi-Model Collaboration in Composed Image Retrieval
---

# DAFM: Dynamic Adaptive Fusion for Multi-Model Collaboration in Composed Image Retrieval

**arXiv**: [2511.05020v1](https://arxiv.org/abs/2511.05020) | [PDF](https://arxiv.org/pdf/2511.05020.pdf)

**作者**: Yawei Cai, Jiapeng Mi, Nan Ji, Haotian Rong, Yawei Zhang, Zhangti Li, Wenbin Guo, Rensong Xie

---

## 💡 一句话要点

**提出动态自适应融合方法以解决组合图像检索中单模型融合不足问题**

**关键词**: `组合图像检索` `动态融合` `多模型协作` `异构模型` `检索精度` `自适应权重`

## 📋 核心要点

1. 核心问题：单模型在组合图像检索中难以同时处理全局与细节，且缺乏动态权重分配导致嵌入偏差
2. 方法要点：利用异构模型互补优势，动态调整模型贡献，提升融合鲁棒性和检索精度
3. 实验或效果：在CIRR和FashionIQ基准上Recall@10达93.21，平均Rmean提升最高4.5%

## 📄 摘要（原文）

> Composed Image Retrieval (CIR) is a cross-modal task that aims to retrieve
> target images from large-scale databases using a reference image and a
> modification text. Most existing methods rely on a single model to perform
> feature fusion and similarity matching. However, this paradigm faces two major
> challenges. First, one model alone can't see the whole picture and the tiny
> details at the same time; it has to handle different tasks with the same
> weights, so it often misses the small but important links between image and
> text. Second, the absence of dynamic weight allocation prevents adaptive
> leveraging of complementary model strengths, so the resulting embedding drifts
> away from the target and misleads the nearest-neighbor search in CIR. To
> address these limitations, we propose Dynamic Adaptive Fusion (DAFM) for
> multi-model collaboration in CIR. Rather than optimizing a single method in
> isolation, DAFM exploits the complementary strengths of heterogeneous models
> and adaptively rebalances their contributions. This not only maximizes
> retrieval accuracy but also ensures that the performance gains are independent
> of the fusion order, highlighting the robustness of our approach. Experiments
> on the CIRR and FashionIQ benchmarks demonstrate consistent improvements. Our
> method achieves a Recall@10 of 93.21 and an Rmean of 84.43 on CIRR, and an
> average Rmean of 67.48 on FashionIQ, surpassing recent strong baselines by up
> to 4.5%. These results confirm that dynamic multi-model collaboration provides
> an effective and general solution for CIR.

