---
layout: default
title: Fast Marker Detection for UV-Based Visual Relative Localisation in Agile UAV Swarms
---

# Fast Marker Detection for UV-Based Visual Relative Localisation in Agile UAV Swarms

**arXiv**: [2510.19663v1](https://arxiv.org/abs/2510.19663) | [PDF](https://arxiv.org/pdf/2510.19663.pdf)

**作者**: Vojtěch Vrba, Viktor Walter, Petr Štěpán, Martin Saska

---

## 💡 一句话要点

**提出快速标记检测方法以支持敏捷无人机群的视觉相对定位**

**关键词**: `标记检测` `视觉相对定位` `无人机群` `实时系统` `硬件加速`

## 📋 核心要点

1. 核心问题：敏捷无人机群中实时视觉相对定位需要快速检测孤立标记。
2. 方法要点：优化CPU程序、GPU着色器和FPGA流架构，加速处理速度。
3. 实验或效果：CPU和GPU方案处理速度提升2-3个数量级，FPGA最小化延迟。

## 📄 摘要（原文）

> A novel approach for the fast onboard detection of isolated markers for
> visual relative localisation of multiple teammates in agile UAV swarms is
> introduced in this paper. As the detection forms a key component of real-time
> localisation systems, a three-fold innovation is presented, consisting of an
> optimised procedure for CPUs, a GPU shader program, and a functionally
> equivalent FPGA streaming architecture. For the proposed CPU and GPU solutions,
> the mean processing time per pixel of input camera frames was accelerated by
> two to three orders of magnitude compared to the state of the art. For the
> localisation task, the proposed FPGA architecture offered the most significant
> overall acceleration by minimising the total delay from camera exposure to
> detection results. Additionally, the proposed solutions were evaluated on
> various 32-bit and 64-bit embedded platforms to demonstrate their efficiency,
> as well as their feasibility for applications using low-end UAVs and MAVs.
> Thus, it has become a crucial enabling technology for agile UAV swarming.

