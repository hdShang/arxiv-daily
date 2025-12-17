---
layout: default
title: Development and Testing for Perception Based Autonomous Landing of a Long-Range QuadPlane
---

# Development and Testing for Perception Based Autonomous Landing of a Long-Range QuadPlane

**arXiv**: [2512.09343v1](https://arxiv.org/abs/2512.09343) | [PDF](https://arxiv.org/pdf/2512.09343.pdf)

**作者**: Ashik E Rasul, Humaira Tasnim, Ji Yu Kim, Young Hyun Lim, Scott Schmitz, Bruce W. Jo, Hyung-Jin Yoon

---

## 💡 一句话要点

**提出轻量级四轴固定翼系统，用于动态无GPS环境下的高效视觉自主着陆与视觉惯性里程计。**

**关键词**: `四轴固定翼` `视觉自主着陆` `视觉惯性里程计` `边缘AI` `非结构化环境` `长程无人机`

## 📋 核心要点

1. 核心问题：长程四轴固定翼在无GPS或杂乱环境中，面临着陆区非结构化、边缘AI资源受限及高惯性飞行特性的挑战。
2. 方法要点：开发轻量级硬件平台与优化部署框架，结合深度神经网络学习着陆特征，实现实时检测与控制。
3. 实验或效果：未知具体实验数据，但系统为动态无GPS环境中的自主着陆部署奠定了基础。

## 📄 摘要（原文）

> QuadPlanes combine the range efficiency of fixed-wing aircraft with the maneuverability of multi-rotor platforms for long-range autonomous missions. In GPS-denied or cluttered urban environments, perception-based landing is vital for reliable operation. Unlike structured landing zones, real-world sites are unstructured and highly variable, requiring strong generalization capabilities from the perception system. Deep neural networks (DNNs) provide a scalable solution for learning landing site features across diverse visual and environmental conditions. While perception-driven landing has been shown in simulation, real-world deployment introduces significant challenges. Payload and volume constraints limit high-performance edge AI devices like the NVIDIA Jetson Orin Nano, which are crucial for real-time detection and control. Accurate pose estimation during descent is necessary, especially in the absence of GPS, and relies on dependable visual-inertial odometry. Achieving this with limited edge AI resources requires careful optimization of the entire deployment framework. The flight characteristics of large QuadPlanes further complicate the problem. These aircraft exhibit high inertia, reduced thrust vectoring, and slow response times further complicate stable landing maneuvers. This work presents a lightweight QuadPlane system for efficient vision-based autonomous landing and visual-inertial odometry, specifically developed for long-range QuadPlane operations such as aerial monitoring. It describes the hardware platform, sensor configuration, and embedded computing architecture designed to meet demanding real-time, physical constraints. This establishes a foundation for deploying autonomous landing in dynamic, unstructured, GPS-denied environments.

