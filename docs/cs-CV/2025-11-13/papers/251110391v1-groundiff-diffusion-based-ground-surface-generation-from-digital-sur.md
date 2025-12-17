---
layout: default
title: GrounDiff: Diffusion-Based Ground Surface Generation from Digital Surface Models
---

# GrounDiff: Diffusion-Based Ground Surface Generation from Digital Surface Models

**arXiv**: [2511.10391v1](https://arxiv.org/abs/2511.10391) | [PDF](https://arxiv.org/pdf/2511.10391.pdf)

**作者**: Oussema Dhaouadi, Johannes Meier, Jacques Kaiser, Daniel Cremers

---

## 💡 一句话要点

**提出GrounDiff扩散模型从数字表面模型生成地面表面**

**关键词**: `数字地形模型生成` `扩散模型` `地面表面重建` `深度学习` `遥感数据处理`

## 📋 核心要点

1. 核心问题：数字地形模型无法直接测量，需从数字表面模型生成，传统方法依赖手动调参。
2. 方法要点：基于扩散模型迭代去除非地面结构，引入门控设计和置信引导生成。
3. 实验效果：在多个数据集上优于深度学习方法，RMSE降低最高达93%。

## 📄 摘要（原文）

> Digital Terrain Models (DTMs) represent the bare-earth elevation and are important in numerous geospatial applications. Such data models cannot be directly measured by sensors and are typically generated from Digital Surface Models (DSMs) derived from LiDAR or photogrammetry. Traditional filtering approaches rely on manually tuned parameters, while learning-based methods require well-designed architectures, often combined with post-processing. To address these challenges, we introduce Ground Diffusion (GrounDiff), the first diffusion-based framework that iteratively removes non-ground structures by formulating the problem as a denoising task. We incorporate a gated design with confidence-guided generation that enables selective filtering. To increase scalability, we further propose Prior-Guided Stitching (PrioStitch), which employs a downsampled global prior automatically generated using GrounDiff to guide local high-resolution predictions. We evaluate our method on the DSM-to-DTM translation task across diverse datasets, showing that GrounDiff consistently outperforms deep learning-based state-of-the-art methods, reducing RMSE by up to 93% on ALS2DTM and up to 47% on USGS benchmarks. In the task of road reconstruction, which requires both high precision and smoothness, our method achieves up to 81% lower distance error compared to specialized techniques on the GeRoD benchmark, while maintaining competitive surface smoothness using only DSM inputs, without task-specific optimization. Our variant for road reconstruction, GrounDiff+, is specifically designed to produce even smoother surfaces, further surpassing state-of-the-art methods. The project page is available at https://deepscenario.github.io/GrounDiff/.

