---
layout: default
title: Robust Shape from Focus via Multiscale Directional Dilated Laplacian and Recurrent Network
---

# Robust Shape from Focus via Multiscale Directional Dilated Laplacian and Recurrent Network

**arXiv**: [2512.10498v1](https://arxiv.org/abs/2512.10498) | [PDF](https://arxiv.org/pdf/2512.10498.pdf)

**作者**: Khurram Ashfaq, Muhammad Tariq Mahmood

---

## 💡 一句话要点

**提出基于多尺度方向性扩张拉普拉斯和循环网络的鲁棒聚焦形状恢复方法**

**关键词**: `聚焦形状恢复` `多尺度特征提取` `循环神经网络` `深度估计` `鲁棒性优化`

## 📋 核心要点

1. 聚焦形状恢复中深度学习方法存在两阶段处理导致伪影和噪声放大的问题
2. 采用传统多尺度方向性扩张拉普拉斯核提取鲁棒聚焦体积，结合轻量级GRU循环网络迭代优化深度估计
3. 在合成和真实数据集上验证了方法在精度和泛化性上优于现有技术

## 📄 摘要（原文）

> Shape-from-Focus (SFF) is a passive depth estimation technique that infers scene depth by analyzing focus variations in a focal stack. Most recent deep learning-based SFF methods typically operate in two stages: first, they extract focus volumes (a per pixel representation of focus likelihood across the focal stack) using heavy feature encoders; then, they estimate depth via a simple one-step aggregation technique that often introduces artifacts and amplifies noise in the depth map. To address these issues, we propose a hybrid framework. Our method computes multi-scale focus volumes traditionally using handcrafted Directional Dilated Laplacian (DDL) kernels, which capture long-range and directional focus variations to form robust focus volumes. These focus volumes are then fed into a lightweight, multi-scale GRU-based depth extraction module that iteratively refines an initial depth estimate at a lower resolution for computational efficiency. Finally, a learned convex upsampling module within our recurrent network reconstructs high-resolution depth maps while preserving fine scene details and sharp boundaries. Extensive experiments on both synthetic and real-world datasets demonstrate that our approach outperforms state-of-the-art deep learning and traditional methods, achieving superior accuracy and generalization across diverse focal conditions.

