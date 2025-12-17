---
layout: default
title: 3M-TI: High-Quality Mobile Thermal Imaging via Calibration-free Multi-Camera Cross-Modal Diffusion
---

# 3M-TI: High-Quality Mobile Thermal Imaging via Calibration-free Multi-Camera Cross-Modal Diffusion

**arXiv**: [2511.19117v1](https://arxiv.org/abs/2511.19117) | [PDF](https://arxiv.org/pdf/2511.19117.pdf)

**作者**: Minchong Chen, Xiaoyun Yuan, Junzhe Wan, Jianing Zhang, Jun Zhang

---

## 💡 一句话要点

**提出3M-TI框架以解决移动热成像分辨率低和纹理模糊问题**

**关键词**: `热成像超分辨率` `跨模态扩散` `移动视觉` `无校准对齐` `下游任务增强`

## 📋 核心要点

1. 移动热传感器小型化导致图像分辨率低和纹理模糊，现有方法依赖校准或信息不足
2. 引入跨模态自注意力模块，在扩散过程中对齐热和RGB特征，无需相机校准
3. 在真实移动设备和基准测试中实现SOTA性能，提升下游任务如检测和分割效果

## 📄 摘要（原文）

> The miniaturization of thermal sensors for mobile platforms inherently limits their spatial resolution and textural fidelity, leading to blurry and less informative images. Existing thermal super-resolution (SR) methods can be grouped into single-image and RGB-guided approaches: the former struggles to recover fine structures from limited information, while the latter relies on accurate and laborious cross-camera calibration, which hinders practical deployment and robustness. Here, we propose 3M-TI, a calibration-free Multi-camera cross-Modality diffusion framework for Mobile Thermal Imaging. At its core, 3M-TI integrates a cross-modal self-attention module (CSM) into the diffusion UNet, replacing the original self-attention layers to adaptively align thermal and RGB features throughout the denoising process, without requiring explicit camera calibration. This design enables the diffusion network to leverage its generative prior to enhance spatial resolution, structural fidelity, and texture detail in the super-resolved thermal images. Extensive evaluations on real-world mobile thermal cameras and public benchmarks validate our superior performance, achieving state-of-the-art results in both visual quality and quantitative metrics. More importantly, the thermal images enhanced by 3M-TI lead to substantial gains in critical downstream tasks like object detection and segmentation, underscoring its practical value for robust mobile thermal perception systems. More materials: https://github.com/work-submit/3MTI.

