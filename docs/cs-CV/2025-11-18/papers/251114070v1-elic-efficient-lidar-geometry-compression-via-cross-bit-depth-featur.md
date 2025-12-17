---
layout: default
title: ELiC: Efficient LiDAR Geometry Compression via Cross-Bit-depth Feature Propagation and Bag-of-Encoders
---

# ELiC: Efficient LiDAR Geometry Compression via Cross-Bit-depth Feature Propagation and Bag-of-Encoders

**arXiv**: [2511.14070v1](https://arxiv.org/abs/2511.14070) | [PDF](https://arxiv.org/pdf/2511.14070.pdf)

**作者**: Junsik Kim, Gun Bang, Soowoong Kim

---

## 💡 一句话要点

**提出ELiC框架以高效压缩LiDAR几何数据，实现实时处理**

**关键词**: `LiDAR几何压缩` `跨位深特征传播` `Bag-of-Encoders` `Morton层次结构` `实时处理`

## 📋 核心要点

1. 核心问题：现有分层压缩方法独立处理不同位深，重复估计局部上下文，效率低
2. 方法要点：跨位深特征传播重用特征，Bag-of-Encoders自适应选择编码网络
3. 实验效果：在Ford和SemanticKITTI数据集上实现SOTA压缩，保持实时吞吐

## 📄 摘要（原文）

> Hierarchical LiDAR geometry compression encodes voxel occupancies from low to high bit-depths, yet prior methods treat each depth independently and re-estimate local context from coordinates at every level, limiting compression efficiency. We present ELiC, a real-time framework that combines cross-bit-depth feature propagation, a Bag-of-Encoders (BoE) selection scheme, and a Morton-order-preserving hierarchy. Cross-bit-depth propagation reuses features extracted at denser, lower depths to support prediction at sparser, higher depths. BoE selects, per depth, the most suitable coding network from a small pool, adapting capacity to observed occupancy statistics without training a separate model for each level. The Morton hierarchy maintains global Z-order across depth transitions, eliminating per-level sorting and reducing latency. Together these components improve entropy modeling and computation efficiency, yielding state-of-the-art compression at real-time throughput on Ford and SemanticKITTI. Code and models will be released upon publication.

