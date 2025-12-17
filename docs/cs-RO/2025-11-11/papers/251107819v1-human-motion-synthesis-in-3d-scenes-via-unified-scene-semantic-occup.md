---
layout: default
title: Human Motion Synthesis in 3D Scenes via Unified Scene Semantic Occupancy
---

# Human Motion Synthesis in 3D Scenes via Unified Scene Semantic Occupancy

**arXiv**: [2511.07819v1](https://arxiv.org/abs/2511.07819) | [PDF](https://arxiv.org/pdf/2511.07819.pdf)

**作者**: Gong Jingyu, Tong Kunkun, Chen Zhuoran, Yuan Chuanhan, Chen Mingang, Zhang Zhizhong, Tan Xin, Xie Yuan

---

## 💡 一句话要点

**提出SSOMotion框架，利用统一场景语义占据实现3D场景中人体运动合成。**

**关键词**: `人体运动合成` `3D场景理解` `场景语义占据` `CLIP编码` `双向三平面分解`

## 📋 核心要点

1. 核心问题：现有方法依赖场景结构，但忽略语义理解，影响运动合成准确性。
2. 方法要点：采用双向三平面分解压缩场景语义占据，结合CLIP编码映射到统一特征空间。
3. 实验效果：在ShapeNet、PROX和Replica数据集上验证，性能领先且泛化能力强。

## 📄 摘要（原文）

> Human motion synthesis in 3D scenes relies heavily on scene comprehension, while current methods focus mainly on scene structure but ignore the semantic understanding. In this paper, we propose a human motion synthesis framework that take an unified Scene Semantic Occupancy (SSO) for scene representation, termed SSOMotion. We design a bi-directional tri-plane decomposition to derive a compact version of the SSO, and scene semantics are mapped to an unified feature space via CLIP encoding and shared linear dimensionality reduction. Such strategy can derive the fine-grained scene semantic structures while significantly reduce redundant computations. We further take these scene hints and movement direction derived from instructions for motion control via frame-wise scene query. Extensive experiments and ablation studies conducted on cluttered scenes using ShapeNet furniture, as well as scanned scenes from PROX and Replica datasets, demonstrate its cutting-edge performance while validating its effectiveness and generalization ability. Code will be publicly available at https://github.com/jingyugong/SSOMotion.

