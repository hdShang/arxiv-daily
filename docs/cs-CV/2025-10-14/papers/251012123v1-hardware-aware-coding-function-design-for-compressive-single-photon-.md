---
layout: default
title: Hardware-aware Coding Function Design for Compressive Single-Photon 3D Cameras
---

# Hardware-aware Coding Function Design for Compressive Single-Photon 3D Cameras

**arXiv**: [2510.12123v1](https://arxiv.org/abs/2510.12123) | [PDF](https://arxiv.org/pdf/2510.12123.pdf)

**作者**: David Parra, Felipe Gutierrez-Barragan, Trevor Seets, Andreas Velten

---

## 💡 一句话要点

**提出硬件感知编码函数设计以优化压缩单光子3D相机性能**

**关键词**: `单光子3D成像` `压缩直方图` `硬件约束优化` `编码函数设计` `梯度下降优化`

## 📋 核心要点

1. 单光子3D相机受硬件限制影响性能，如带宽和峰值功率
2. 采用约束优化方法联合优化照明和编码矩阵，适应硬件约束
3. 仿真显示在带宽和峰值功率约束下优于传统编码设计

## 📄 摘要（原文）

> Single-photon cameras are becoming increasingly popular in time-of-flight 3D
> imaging because they can time-tag individual photons with extreme resolution.
> However, their performance is susceptible to hardware limitations, such as
> system bandwidth, maximum laser power, sensor data rates, and in-sensor memory
> and compute resources. Compressive histograms were recently introduced as a
> solution to the challenge of data rates through an online in-sensor compression
> of photon timestamp data. Although compressive histograms work within limited
> in-sensor memory and computational resources, they underperform when subjected
> to real-world illumination hardware constraints. To address this, we present a
> constrained optimization approach for designing practical coding functions for
> compressive single-photon 3D imaging. Using gradient descent, we jointly
> optimize an illumination and coding matrix (i.e., the coding functions) that
> adheres to hardware constraints. We show through extensive simulations that our
> coding functions consistently outperform traditional coding designs under both
> bandwidth and peak power constraints. This advantage is particularly pronounced
> in systems constrained by peak power. Finally, we show that our approach adapts
> to arbitrary parameterized impulse responses by evaluating it on a real-world
> system with a non-ideal impulse response function.

