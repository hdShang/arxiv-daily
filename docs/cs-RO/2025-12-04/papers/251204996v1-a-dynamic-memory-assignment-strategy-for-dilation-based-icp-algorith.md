---
layout: default
title: A dynamic memory assignment strategy for dilation-based ICP algorithm on embedded GPUs
---

# A dynamic memory assignment strategy for dilation-based ICP algorithm on embedded GPUs

**arXiv**: [2512.04996v1](https://arxiv.org/abs/2512.04996) | [PDF](https://arxiv.org/pdf/2512.04996.pdf)

**作者**: Qiong Chang, Weimin Wang, Junpei Zhong, Jun Miyazaki

---

## 💡 一句话要点

**提出动态内存分配策略以优化VANICP在嵌入式GPU上的内存使用**

**关键词**: `点云配准` `嵌入式GPU` `内存优化` `膨胀操作` `动态内存分配`

## 📋 核心要点

1. VANICP算法在嵌入式GPU上内存需求高，限制部署
2. 基于膨胀操作设计GPU动态内存分配策略，减少内存占用
3. 实验显示内存消耗降低超97%，性能保持原水平

## 📄 摘要（原文）

> This paper proposes a memory-efficient optimization strategy for the high-performance point cloud registration algorithm VANICP, enabling lightweight execution on embedded GPUs with constrained hardware resources. VANICP is a recently published acceleration framework that significantly improves the computational efficiency of point-cloud-based applications. By transforming the global nearest neighbor search into a localized process through a dilation-based information propagation mechanism, VANICP greatly reduces the computational complexity of the NNS. However, its original implementation demands a considerable amount of memory, which restricts its deployment in resource-constrained environments such as embedded systems. To address this issue, we propose a GPU-oriented dynamic memory assignment strategy that optimizes the memory usage of the dilation operation. Furthermore, based on this strategy, we construct an enhanced version of the VANICP framework that achieves over 97% reduction in memory consumption while preserving the original performance. Source code is published on: https://github.com/changqiong/VANICP4Em.git.

