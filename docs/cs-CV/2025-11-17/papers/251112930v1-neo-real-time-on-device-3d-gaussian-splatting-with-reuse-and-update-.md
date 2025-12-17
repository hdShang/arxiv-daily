---
layout: default
title: Neo: Real-Time On-Device 3D Gaussian Splatting with Reuse-and-Update Sorting Acceleration
---

# Neo: Real-Time On-Device 3D Gaussian Splatting with Reuse-and-Update Sorting Acceleration

**arXiv**: [2511.12930v1](https://arxiv.org/abs/2511.12930) | [PDF](https://arxiv.org/pdf/2511.12930.pdf)

**作者**: Changhun Oh, Seongryong Oh, Jinwoo Hwang, Yoonsung Kim, Hardik Sharma, Jongse Park

---

## 💡 一句话要点

**提出重用更新排序算法以加速移动设备实时3D高斯泼溅渲染**

**关键词**: `3D高斯泼溅` `实时渲染` `移动设备加速` `排序算法优化` `内存带宽优化`

## 📋 核心要点

1. 3D高斯泼溅渲染中排序阶段是内存带宽瓶颈，限制实时性能
2. 引入重用更新排序算法，利用帧间高斯顺序冗余减少计算和带宽
3. 实验显示吞吐量提升最高10倍，DRAM流量降低94.5%

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) rendering in real-time on resource-constrained devices is essential for delivering immersive augmented and virtual reality (AR/VR) experiences. However, existing solutions struggle to achieve high frame rates, especially for high-resolution rendering. Our analysis identifies the sorting stage in the 3DGS rendering pipeline as the major bottleneck due to its high memory bandwidth demand. This paper presents Neo, which introduces a reuse-and-update sorting algorithm that exploits temporal redundancy in Gaussian ordering across consecutive frames, and devises a hardware accelerator optimized for this algorithm. By efficiently tracking and updating Gaussian depth ordering instead of re-sorting from scratch, Neo significantly reduces redundant computations and memory bandwidth pressure. Experimental results show that Neo achieves up to 10.0x and 5.6x higher throughput than state-of-the-art edge GPU and ASIC solution, respectively, while reducing DRAM traffic by 94.5% and 81.3%. These improvements make high-quality and low-latency on-device 3D rendering more practical.

