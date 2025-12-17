---
layout: default
title: QUILL: An Algorithm-Architecture Co-Design for Cache-Local Deformable Attention
---

# QUILL: An Algorithm-Architecture Co-Design for Cache-Local Deformable Attention

**arXiv**: [2511.13679v1](https://arxiv.org/abs/2511.13679) | [PDF](https://arxiv.org/pdf/2511.13679.pdf)

**作者**: Hyunwoo Oh, Hanning Chen, Sanggeon Yun, Yang Ni, Wenjun Huang, Tamoghno Das, Suyeon Jang, Mohsen Imani

---

## 💡 一句话要点

**提出QUILL算法-架构协同设计，通过缓存局部变形注意力提升检测效率**

**关键词**: `变形注意力` `硬件加速器` `缓存优化` `算法-架构协同设计` `目标检测` `能效提升`

## 📋 核心要点

1. 变形Transformer在检测中性能领先，但存在内存访问不规则和算术强度低的问题
2. 核心方法包括基于距离的无序查询排序和区域预取，实现单次融合计算
3. 实验显示吞吐量提升最高7.29倍，能效提高47.3倍，精度损失小于0.9 AP

## 📄 摘要（原文）

> Deformable transformers deliver state-of-the-art detection but map poorly to hardware due to irregular memory access and low arithmetic intensity. We introduce QUILL, a schedule-aware accelerator that turns deformable attention into cache-friendly, single-pass work. At its core, Distance-based Out-of-Order Querying (DOOQ) orders queries by spatial proximity; the look-ahead drives a region prefetch into an alternate buffer--forming a schedule-aware prefetch loop that overlaps memory and compute. A fused MSDeformAttn engine executes interpolation, Softmax, aggregation, and the final projection (W''m) in one pass without spilling intermediates, while small tensors are kept on-chip and surrounding dense layers run on integrated GEMMs. Implemented as RTL and evaluated end-to-end, QUILL achieves up to 7.29x higher throughput and 47.3x better energy efficiency than an RTX 4090, and exceeds prior accelerators by 3.26-9.82x in throughput and 2.01-6.07x in energy efficiency. With mixed-precision quantization, accuracy tracks FP32 within <=0.9 AP across Deformable and Sparse DETR variants. By converting sparsity into locality--and locality into utilization--QUILL delivers consistent, end-to-end speedups.

