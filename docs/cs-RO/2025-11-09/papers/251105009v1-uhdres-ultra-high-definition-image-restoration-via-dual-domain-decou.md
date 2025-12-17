---
layout: default
title: UHDRes: Ultra-High-Definition Image Restoration via Dual-Domain Decoupled Spectral Modulation
---

# UHDRes: Ultra-High-Definition Image Restoration via Dual-Domain Decoupled Spectral Modulation

**arXiv**: [2511.05009v1](https://arxiv.org/abs/2511.05009) | [PDF](https://arxiv.org/pdf/2511.05009.pdf)

**作者**: S. Zhao, W. Lu, B. Wang, T. Wang, K. Zhang, H. Zhao

---

## 💡 一句话要点

**提出UHDRes框架，通过双域解耦谱调制解决超高清图像恢复问题**

**关键词**: `超高清图像恢复` `双域解耦谱调制` `轻量级网络` `频率域处理` `空间域细化`

## 📋 核心要点

1. 超高清图像因高分辨率和计算需求，面临模糊、雾霾等退化挑战
2. 采用轻量级双域解耦谱调制，显式增强振幅谱，隐式恢复相位
3. 在五个基准测试中，以40万参数实现最优性能，降低推理延迟和内存使用

## 📄 摘要（原文）

> Ultra-high-definition (UHD) images often suffer from severe degradations such
> as blur, haze, rain, or low-light conditions, which pose significant challenges
> for image restoration due to their high resolution and computational demands.
> In this paper, we propose UHDRes, a novel lightweight dual-domain decoupled
> spectral modulation framework for UHD image restoration. It explicitly models
> the amplitude spectrum via lightweight spectrum-domain modulation, while
> restoring phase implicitly through spatial-domain refinement. We introduce the
> spatio-spectral fusion mechanism, which first employs a multi-scale context
> aggregator to extract local and global spatial features, and then performs
> spectral modulation in a decoupled manner. It explicitly enhances amplitude
> features in the frequency domain while implicitly restoring phase information
> through spatial refinement. Additionally, a shared gated feed-forward network
> is designed to efficiently promote feature interaction through shared-parameter
> convolutions and adaptive gating mechanisms. Extensive experimental comparisons
> on five public UHD benchmarks demonstrate that our UHDRes achieves the
> state-of-the-art restoration performance with only 400K parameters, while
> significantly reducing inference latency and memory usage. The codes and models
> are available at https://github.com/Zhao0100/UHDRes.

