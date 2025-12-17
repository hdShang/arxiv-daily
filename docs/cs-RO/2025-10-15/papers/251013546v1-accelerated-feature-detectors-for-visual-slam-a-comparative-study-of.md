---
layout: default
title: Accelerated Feature Detectors for Visual SLAM: A Comparative Study of FPGA vs GPU
---

# Accelerated Feature Detectors for Visual SLAM: A Comparative Study of FPGA vs GPU

**arXiv**: [2510.13546v1](https://arxiv.org/abs/2510.13546) | [PDF](https://arxiv.org/pdf/2510.13546.pdf)

**作者**: Ruiqi Ye, Mikel Luján

---

## 💡 一句话要点

**比较FPGA与GPU在视觉SLAM中加速特征检测的性能与能效**

**关键词**: `视觉SLAM` `特征检测` `硬件加速` `FPGA` `GPU` `能效优化`

## 📋 核心要点

1. 视觉SLAM中特征检测模块耗时高，需在功耗受限平台优化
2. 对比GPU与FPGA加速FAST、Harris和SuperPoint特征检测器
3. FPGA在SuperPoint上表现更优，GPU在非学习型检测器及精度上占优

## 📄 摘要（原文）

> Feature detection is a common yet time-consuming module in Simultaneous
> Localization and Mapping (SLAM) implementations, which are increasingly
> deployed on power-constrained platforms, such as drones. Graphics Processing
> Units (GPUs) have been a popular accelerator for computer vision in general,
> and feature detection and SLAM in particular.
>   On the other hand, System-on-Chips (SoCs) with integrated Field Programmable
> Gate Array (FPGA) are also widely available. This paper presents the first
> study of hardware-accelerated feature detectors considering a Visual SLAM
> (V-SLAM) pipeline. We offer new insights by comparing the best GPU-accelerated
> FAST, Harris, and SuperPoint implementations against the FPGA-accelerated
> counterparts on modern SoCs (Nvidia Jetson Orin and AMD Versal).
>   The evaluation shows that when using a non-learning-based feature detector
> such as FAST and Harris, their GPU implementations, and the GPU-accelerated
> V-SLAM can achieve better run-time performance and energy efficiency than the
> FAST and Harris FPGA implementations as well as the FPGA-accelerated V-SLAM.
> However, when considering a learning-based detector such as SuperPoint, its
> FPGA implementation can achieve better run-time performance and energy
> efficiency (up to 3.1$\times$ and 1.4$\times$ improvements, respectively) than
> the GPU implementation. The FPGA-accelerated V-SLAM can also achieve comparable
> run-time performance compared to the GPU-accelerated V-SLAM, with better FPS in
> 2 out of 5 dataset sequences. When considering the accuracy, the results show
> that the GPU-accelerated V-SLAM is more accurate than the FPGA-accelerated
> V-SLAM in general. Last but not least, the use of hardware acceleration for
> feature detection could further improve the performance of the V-SLAM pipeline
> by having the global bundle adjustment module invoked less frequently without
> sacrificing accuracy.

