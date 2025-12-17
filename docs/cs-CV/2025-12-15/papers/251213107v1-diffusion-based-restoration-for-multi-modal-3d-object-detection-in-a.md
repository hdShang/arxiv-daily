---
layout: default
title: Diffusion-Based Restoration for Multi-Modal 3D Object Detection in Adverse Weather
---

# Diffusion-Based Restoration for Multi-Modal 3D Object Detection in Adverse Weather

**arXiv**: [2512.13107v1](https://arxiv.org/abs/2512.13107) | [PDF](https://arxiv.org/pdf/2512.13107.pdf)

**作者**: Zhijian He, Feifei Liu, Yuwei Li, Zhanpeng Liu, Jintao Cheng, Xieyuanli Chen, Xiaoyu Tang

---

## 💡 一句话要点

**提出DiffFusion框架，通过扩散模型恢复和自适应跨模态融合，增强恶劣天气下多模态3D目标检测的鲁棒性。**

**关键词**: `多模态3D目标检测` `扩散模型` `恶劣天气鲁棒性` `跨模态融合` `BEV对齐` `零样本泛化`

## 📋 核心要点

1. 核心问题：恶劣天气导致多模态数据失真和模态间错位，限制3D目标检测的可靠性。
2. 方法要点：使用Diffusion-IR恢复图像，PCR补偿LiDAR数据，BAFAM模块实现动态融合和BEV对齐。
3. 实验或效果：在三个公开数据集上实现最先进的鲁棒性，并在DENSE数据集上验证零样本泛化能力。

## 📄 摘要（原文）

> Multi-modal 3D object detection is important for reliable perception in robotics and autonomous driving. However, its effectiveness remains limited under adverse weather conditions due to weather-induced distortions and misalignment between different data modalities. In this work, we propose DiffFusion, a novel framework designed to enhance robustness in challenging weather through diffusion-based restoration and adaptive cross-modal fusion. Our key insight is that diffusion models possess strong capabilities for denoising and generating data that can adapt to various weather conditions. Building on this, DiffFusion introduces Diffusion-IR restoring images degraded by weather effects and Point Cloud Restoration (PCR) compensating for corrupted LiDAR data using image object cues. To tackle misalignments between two modalities, we develop Bidirectional Adaptive Fusion and Alignment Module (BAFAM). It enables dynamic multi-modal fusion and bidirectional bird's-eye view (BEV) alignment to maintain consistent spatial correspondence. Extensive experiments on three public datasets show that DiffFusion achieves state-of-the-art robustness under adverse weather while preserving strong clean-data performance. Zero-shot results on the real-world DENSE dataset further validate its generalization. The implementation of our DiffFusion will be released as open-source.

