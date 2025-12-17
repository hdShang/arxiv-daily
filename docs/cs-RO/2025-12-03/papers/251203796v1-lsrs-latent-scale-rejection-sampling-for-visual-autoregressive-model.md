---
layout: default
title: LSRS: Latent Scale Rejection Sampling for Visual Autoregressive Modeling
---

# LSRS: Latent Scale Rejection Sampling for Visual Autoregressive Modeling

**arXiv**: [2512.03796v1](https://arxiv.org/abs/2512.03796) | [PDF](https://arxiv.org/pdf/2512.03796.pdf)

**作者**: Hong-Kai Zheng, Piji Li

---

## 💡 一句话要点

**提出LSRS方法以解决视觉自回归模型中并行采样导致的结构错误问题**

**关键词**: `视觉自回归建模` `图像生成` `拒绝采样` `潜在尺度优化` `推理加速`

## 📋 核心要点

1. 视觉自回归模型在尺度内并行采样可能引发结构错误，影响生成质量
2. LSRS通过轻量评分模型在推理时渐进优化潜在尺度中的token图，选择高质量候选
3. 实验显示LSRS显著提升VAR生成质量，如VAR-d30模型FID从1.95降至1.78，推理时间仅增1%

## 📄 摘要（原文）

> Visual Autoregressive (VAR) modeling approach for image generation proposes autoregressive processing across hierarchical scales, decoding multiple tokens per scale in parallel. This method achieves high-quality generation while accelerating synthesis. However, parallel token sampling within a scale may lead to structural errors, resulting in suboptimal generated images. To mitigate this, we propose Latent Scale Rejection Sampling (LSRS), a method that progressively refines token maps in the latent scale during inference to enhance VAR models. Our method uses a lightweight scoring model to evaluate multiple candidate token maps sampled at each scale, selecting the high-quality map to guide subsequent scale generation. By prioritizing early scales critical for structural coherence, LSRS effectively mitigates autoregressive error accumulation while maintaining computational efficiency. Experiments demonstrate that LSRS significantly improves VAR's generation quality with minimal additional computational overhead. For the VAR-d30 model, LSRS increases the inference time by merely 1% while reducing its FID score from 1.95 to 1.78. When the inference time is increased by 15%, the FID score can be further reduced to 1.66. LSRS offers an efficient test-time scaling solution for enhancing VAR-based generation.

