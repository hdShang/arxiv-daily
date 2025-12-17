---
layout: default
title: Coupled Physics-Gated Adaptation: Spatially Decoding Volumetric Photochemical Conversion in Complex 3D-Printed Objects
---

# Coupled Physics-Gated Adaptation: Spatially Decoding Volumetric Photochemical Conversion in Complex 3D-Printed Objects

**arXiv**: [2511.19913v1](https://arxiv.org/abs/2511.19913) | [PDF](https://arxiv.org/pdf/2511.19913.pdf)

**作者**: Maryam Eftekharifar, Churun Zhang, Jialiang Wei, Xudong Cao, Hossein Heidari

---

## 💡 一句话要点

**提出C-PGA框架以预测复杂3D打印物体的光化学转化状态**

**关键词**: `3D视觉预测` `多模态融合` `物理引导调制` `光化学转化` `体积属性估计`

## 📋 核心要点

1. 核心问题：从3D视觉数据预测非视觉体积物理属性，传统模型缺乏物理耦合偏置
2. 方法要点：使用几何和过程参数作为Query，通过FiLM动态门控和调制双3D视觉流
3. 实验或效果：基于最大光学打印数据集，实现虚拟化学表征，无需后打印测量

## 📄 摘要（原文）

> We present a framework that pioneers the prediction of photochemical conversion in complex three-dimensionally printed objects, introducing a challenging new computer vision task: predicting dense, non-visual volumetric physical properties from 3D visual data. This approach leverages the largest-ever optically printed 3D specimen dataset, comprising a large family of parametrically designed complex minimal surface structures that have undergone terminal chemical characterisation. Conventional vision models are ill-equipped for this task, as they lack an inductive bias for the coupled, non-linear interactions of optical physics (diffraction, absorption) and material physics (diffusion, convection) that govern the final chemical state. To address this, we propose Coupled Physics-Gated Adaptation (C-PGA), a novel multimodal fusion architecture. Unlike standard concatenation, C-PGA explicitly models physical coupling by using sparse geometrical and process parameters (e.g., surface transport, print layer height) as a Query to dynamically gate and adapt the dense visual features via feature-wise linear modulation (FiLM). This mechanism spatially modulates dual 3D visual streams-extracted by parallel 3D-CNNs processing raw projection stacks and their diffusion-diffraction corrected counterparts allowing the model to recalibrate its visual perception based on the physical context. This approach offers a breakthrough in virtual chemical characterisation, eliminating the need for traditional post-print measurements and enabling precise control over the chemical conversion state.

