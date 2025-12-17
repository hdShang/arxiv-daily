---
layout: default
title: FMA-Net++: Motion- and Exposure-Aware Real-World Joint Video Super-Resolution and Deblurring
---

# FMA-Net++: Motion- and Exposure-Aware Real-World Joint Video Super-Resolution and Deblurring

**arXiv**: [2512.04390v1](https://arxiv.org/abs/2512.04390) | [PDF](https://arxiv.org/pdf/2512.04390.pdf)

**作者**: Geunhyuk Youk, Jihyong Oh, Munchurl Kim

---

## 💡 一句话要点

**提出FMA-Net++框架，以解决真实视频中运动与动态曝光耦合的联合超分辨率与去模糊问题。**

**关键词**: `视频恢复` `运动与曝光耦合` `联合超分辨率去模糊` `序列级架构` `动态滤波` `合成数据训练`

## 📋 核心要点

1. 核心问题：真实视频恢复面临运动与动态曝光耦合的复杂退化，现有方法常忽略此挑战。
2. 方法要点：采用序列级架构，通过曝光时间感知调制和流引导动态滤波，解耦退化学习与恢复。
3. 实验或效果：在REDS-ME等新基准上实现最优精度与时间一致性，并提升推理速度。

## 📄 摘要（原文）

> Real-world video restoration is plagued by complex degradations from motion coupled with dynamically varying exposure - a key challenge largely overlooked by prior works and a common artifact of auto-exposure or low-light capture. We present FMA-Net++, a framework for joint video super-resolution and deblurring that explicitly models this coupled effect of motion and dynamically varying exposure. FMA-Net++ adopts a sequence-level architecture built from Hierarchical Refinement with Bidirectional Propagation blocks, enabling parallel, long-range temporal modeling. Within each block, an Exposure Time-aware Modulation layer conditions features on per-frame exposure, which in turn drives an exposure-aware Flow-Guided Dynamic Filtering module to infer motion- and exposure-aware degradation kernels. FMA-Net++ decouples degradation learning from restoration: the former predicts exposure- and motion-aware priors to guide the latter, improving both accuracy and efficiency. To evaluate under realistic capture conditions, we introduce REDS-ME (multi-exposure) and REDS-RE (random-exposure) benchmarks. Trained solely on synthetic data, FMA-Net++ achieves state-of-the-art accuracy and temporal consistency on our new benchmarks and GoPro, outperforming recent methods in both restoration quality and inference speed, and generalizes well to challenging real-world videos.

