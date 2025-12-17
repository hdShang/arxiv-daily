---
layout: default
title: Feedforward 3D Editing via Text-Steerable Image-to-3D
---

# Feedforward 3D Editing via Text-Steerable Image-to-3D

**arXiv**: [2512.13678v1](https://arxiv.org/abs/2512.13678) | [PDF](https://arxiv.org/pdf/2512.13678.pdf)

**作者**: Ziqi Ma, Hongqiao Chen, Yisong Yue, Georgia Gkioxari

---

## 💡 一句话要点

**提出Steer3D方法，通过文本引导实现图像到3D生成模型的快速编辑**

**关键词**: `图像到3D生成` `文本引导编辑` `前馈式方法` `流匹配训练` `直接偏好优化` `数据引擎`

## 📋 核心要点

1. 核心问题：AI生成3D资产难以用语言轻松编辑，限制实际应用。
2. 方法要点：基于ControlNet适配图像到3D生成，实现前馈式文本引导，结合流匹配训练和DPO优化。
3. 实验或效果：相比竞品，更忠实遵循语言指令，保持原始3D资产一致性，速度提升2.4至28.5倍。

## 📄 摘要（原文）

> Recent progress in image-to-3D has opened up immense possibilities for design, AR/VR, and robotics. However, to use AI-generated 3D assets in real applications, a critical requirement is the capability to edit them easily. We present a feedforward method, Steer3D, to add text steerability to image-to-3D models, which enables editing of generated 3D assets with language. Our approach is inspired by ControlNet, which we adapt to image-to-3D generation to enable text steering directly in a forward pass. We build a scalable data engine for automatic data generation, and develop a two-stage training recipe based on flow-matching training and Direct Preference Optimization (DPO). Compared to competing methods, Steer3D more faithfully follows the language instruction and maintains better consistency with the original 3D asset, while being 2.4x to 28.5x faster. Steer3D demonstrates that it is possible to add a new modality (text) to steer the generation of pretrained image-to-3D generative models with 100k data. Project website: https://glab-caltech.github.io/steer3d/

