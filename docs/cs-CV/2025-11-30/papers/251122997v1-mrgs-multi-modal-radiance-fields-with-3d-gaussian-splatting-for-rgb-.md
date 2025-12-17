---
layout: default
title: MrGS: Multi-modal Radiance Fields with 3D Gaussian Splatting for RGB-Thermal Novel View Synthesis
---

# MrGS: Multi-modal Radiance Fields with 3D Gaussian Splatting for RGB-Thermal Novel View Synthesis

**arXiv**: [2511.22997v1](https://arxiv.org/abs/2511.22997) | [PDF](https://arxiv.org/pdf/2511.22997.pdf)

**作者**: Minseong Kweon, Janghyun Kim, Ukcheol Shin, Jinsun Park

---

## 💡 一句话要点

**提出MrGS基于3D高斯泼溅的多模态辐射场，用于RGB-热红外新视角合成**

**关键词**: `多模态渲染` `3D高斯泼溅` `热红外成像` `辐射场` `新视角合成` `物理建模`

## 📋 核心要点

1. 核心问题：现有方法忽视热红外图像特性，如热传导和朗伯反射，导致多模态渲染性能不足。
2. 方法要点：通过正交特征提取从单一外观特征获取RGB和热信息，并基于朗伯反射程度采用视图依赖或独立嵌入策略。
3. 实验或效果：实验显示MrGS实现高保真RGB-T场景重建，同时减少高斯数量。

## 📄 摘要（原文）

> Recent advances in Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (3DGS) have achieved considerable performance in RGB scene reconstruction. However, multi-modal rendering that incorporates thermal infrared imagery remains largely underexplored. Existing approaches tend to neglect distinctive thermal characteristics, such as heat conduction and the Lambertian property. In this study, we introduce MrGS, a multi-modal radiance field based on 3DGS that simultaneously reconstructs both RGB and thermal 3D scenes. Specifically, MrGS derives RGB- and thermal-related information from a single appearance feature through orthogonal feature extraction and employs view-dependent or view-independent embedding strategies depending on the degree of Lambertian reflectance exhibited by each modality. Furthermore, we leverage two physics-based principles to effectively model thermal-domain phenomena. First, we integrate Fourier's law of heat conduction prior to alpha blending to model intensity interpolation caused by thermal conduction between neighboring Gaussians. Second, we apply the Stefan-Boltzmann law and the inverse-square law to formulate a depth-aware thermal radiation map that imposes additional geometric constraints on thermal rendering. Experimental results demonstrate that the proposed MrGS achieves high-fidelity RGB-T scene reconstruction while reducing the number of Gaussians.

