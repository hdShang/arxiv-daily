---
layout: default
title: WaterFlow: Explicit Physics-Prior Rectified Flow for Underwater Saliency Mask Generation
---

# WaterFlow: Explicit Physics-Prior Rectified Flow for Underwater Saliency Mask Generation

**arXiv**: [2510.12605v1](https://arxiv.org/abs/2510.12605) | [PDF](https://arxiv.org/pdf/2510.12605.pdf)

**作者**: Runting Li, Shijie Lian, Hua Li, Yutong Li, Wenhui Wu, Sam Kwong

---

## 💡 一句话要点

**提出WaterFlow框架，利用显式物理先验和整流流解决水下显著目标检测问题**

**关键词**: `水下显著目标检测` `整流流框架` `物理先验` `时序建模` `图像质量退化`

## 📋 核心要点

1. 核心问题：水下图像质量退化和领域差距，现有方法忽略物理成像原理或简单消除干扰
2. 方法要点：引入水下物理成像信息作为显式先验，结合整流流框架和时序维度建模
3. 实验或效果：在USOD10K数据集上S_m指标提升0.072，显示方法有效性和优越性

## 📄 摘要（原文）

> Underwater Salient Object Detection (USOD) faces significant challenges,
> including underwater image quality degradation and domain gaps. Existing
> methods tend to ignore the physical principles of underwater imaging or simply
> treat degradation phenomena in underwater images as interference factors that
> must be eliminated, failing to fully exploit the valuable information they
> contain. We propose WaterFlow, a rectified flow-based framework for underwater
> salient object detection that innovatively incorporates underwater physical
> imaging information as explicit priors directly into the network training
> process and introduces temporal dimension modeling, significantly enhancing the
> model's capability for salient object identification. On the USOD10K dataset,
> WaterFlow achieves a 0.072 gain in S_m, demonstrating the effectiveness and
> superiority of our method. The code will be published after the acceptance.

