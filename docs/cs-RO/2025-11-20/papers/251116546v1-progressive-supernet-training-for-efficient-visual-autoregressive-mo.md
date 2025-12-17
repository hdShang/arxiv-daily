---
layout: default
title: Progressive Supernet Training for Efficient Visual Autoregressive Modeling
---

# Progressive Supernet Training for Efficient Visual Autoregressive Modeling

**arXiv**: [2511.16546v1](https://arxiv.org/abs/2511.16546) | [PDF](https://arxiv.org/pdf/2511.16546.pdf)

**作者**: Xiaoyue Chen, Yuling Shi, Kaiyuan Li, Huandong Wang, Yong Li, Xiaodong Gu, Xinlei Chen, Mingbao Lin

---

## 💡 一句话要点

**提出VARiant渐进超网训练以解决视觉自回归模型内存开销问题**

**关键词**: `视觉自回归建模` `渐进训练` `权重共享` `内存优化` `多尺度生成` `模型压缩`

## 📋 核心要点

1. 视觉自回归模型多尺度生成因KV缓存累积导致高内存开销，限制部署
2. 利用尺度-深度非对称依赖，通过权重共享子网实现灵活深度调整
3. 实验显示VARiant在ImageNet上显著降低内存和加速，保持生成质量

## 📄 摘要（原文）

> Visual Auto-Regressive (VAR) models significantly reduce inference steps through the "next-scale" prediction paradigm. However, progressive multi-scale generation incurs substantial memory overhead due to cumulative KV caching, limiting practical deployment.
>   We observe a scale-depth asymmetric dependency in VAR: early scales exhibit extreme sensitivity to network depth, while later scales remain robust to depth reduction. Inspired by this, we propose VARiant: by equidistant sampling, we select multiple subnets ranging from 16 to 2 layers from the original 30-layer VAR-d30 network. Early scales are processed by the full network, while later scales utilize subnet. Subnet and the full network share weights, enabling flexible depth adjustment within a single model.
>   However, weight sharing between subnet and the entire network can lead to optimization conflicts. To address this, we propose a progressive training strategy that breaks through the Pareto frontier of generation quality for both subnets and the full network under fixed-ratio training, achieving joint optimality.
>   Experiments on ImageNet demonstrate that, compared to the pretrained VAR-d30 (FID 1.95), VARiant-d16 and VARiant-d8 achieve nearly equivalent quality (FID 2.05/2.12) while reducing memory consumption by 40-65%. VARiant-d2 achieves 3.5 times speedup and 80% memory reduction at moderate quality cost (FID 2.97). In terms of deployment, VARiant's single-model architecture supports zero-cost runtime depth switching and provides flexible deployment options from high quality to extreme efficiency, catering to diverse application scenarios.

