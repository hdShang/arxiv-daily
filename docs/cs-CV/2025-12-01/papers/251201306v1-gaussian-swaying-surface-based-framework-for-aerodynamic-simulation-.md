---
layout: default
title: Gaussian Swaying: Surface-Based Framework for Aerodynamic Simulation with 3D Gaussians
---

# Gaussian Swaying: Surface-Based Framework for Aerodynamic Simulation with 3D Gaussians

**arXiv**: [2512.01306v1](https://arxiv.org/abs/2512.01306) | [PDF](https://arxiv.org/pdf/2512.01306.pdf)

**作者**: Hongru Yan, Xiang Zhang, Zeyuan Chen, Fangyin Wei, Zhuowen Tu

---

## 💡 一句话要点

**提出Gaussian Swaying框架，基于3D高斯实现高效精细的气动表面模拟与渲染统一。**

**关键词**: `气动模拟` `3D高斯` `表面建模` `统一渲染` `高效计算`

## 📋 核心要点

1. 核心问题：传统网格或粒子方法在气动模拟中效率低或细节不足，影响自然运动真实性。
2. 方法要点：使用3D高斯连续建模表面，统一模拟与渲染于高斯补丁，支持力计算和轻量着色。
3. 实验或效果：在合成和真实数据集上，通过多指标验证达到先进性能与效率，可扩展用于真实场景。

## 📄 摘要（原文）

> Branches swaying in the breeze, flags rippling in the wind, and boats rocking on the water all show how aerodynamics shape natural motion -- an effect crucial for realism in vision and graphics. In this paper, we present Gaussian Swaying, a surface-based framework for aerodynamic simulation using 3D Gaussians. Unlike mesh-based methods that require costly meshing, or particle-based approaches that rely on discrete positional data, Gaussian Swaying models surfaces continuously with 3D Gaussians, enabling efficient and fine-grained aerodynamic interaction. Our framework unifies simulation and rendering on the same representation: Gaussian patches, which support force computation for dynamics while simultaneously providing normals for lightweight shading. Comprehensive experiments on both synthetic and real-world datasets across multiple metrics demonstrate that Gaussian Swaying achieves state-of-the-art performance and efficiency, offering a scalable approach for realistic aerodynamic scene simulation.

