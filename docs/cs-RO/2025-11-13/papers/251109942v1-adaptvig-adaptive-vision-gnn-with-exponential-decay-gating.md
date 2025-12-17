---
layout: default
title: AdaptViG: Adaptive Vision GNN with Exponential Decay Gating
---

# AdaptViG: Adaptive Vision GNN with Exponential Decay Gating

**arXiv**: [2511.09942v1](https://arxiv.org/abs/2511.09942) | [PDF](https://arxiv.org/pdf/2511.09942.pdf)

**作者**: Mustafa Munir, Md Mostafijur Rahman, Radu Marculescu

---

## 💡 一句话要点

**提出AdaptViG自适应视觉图神经网络，通过指数衰减门控解决图构建计算效率问题**

**关键词**: `视觉图神经网络` `自适应图卷积` `指数衰减门控` `计算效率优化` `混合策略` `下游任务性能`

## 📋 核心要点

1. 视觉图神经网络图构建阶段计算量大，影响模型效率
2. 引入自适应图卷积，结合静态轴向支架和动态指数衰减门控机制
3. 在ImageNet达82.6%准确率，参数和计算量大幅减少，下游任务性能领先

## 📄 摘要（原文）

> Vision Graph Neural Networks (ViGs) offer a new direction for advancements in vision architectures. While powerful, ViGs often face substantial computational challenges stemming from their graph construction phase, which can hinder their efficiency. To address this issue we propose AdaptViG, an efficient and powerful hybrid Vision GNN that introduces a novel graph construction mechanism called Adaptive Graph Convolution. This mechanism builds upon a highly efficient static axial scaffold and a dynamic, content-aware gating strategy called Exponential Decay Gating. This gating mechanism selectively weighs long-range connections based on feature similarity. Furthermore, AdaptViG employs a hybrid strategy, utilizing our efficient gating mechanism in the early stages and a full Global Attention block in the final stage for maximum feature aggregation. Our method achieves a new state-of-the-art trade-off between accuracy and efficiency among Vision GNNs. For instance, our AdaptViG-M achieves 82.6% top-1 accuracy, outperforming ViG-B by 0.3% while using 80% fewer parameters and 84% fewer GMACs. On downstream tasks, AdaptViG-M obtains 45.8 mIoU, 44.8 APbox, and 41.1 APmask, surpassing the much larger EfficientFormer-L7 by 0.7 mIoU, 2.2 APbox, and 2.1 APmask, respectively, with 78% fewer parameters.

