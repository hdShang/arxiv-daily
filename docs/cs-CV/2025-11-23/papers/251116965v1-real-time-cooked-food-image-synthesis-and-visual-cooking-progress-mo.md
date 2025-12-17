---
layout: default
title: Real-Time Cooked Food Image Synthesis and Visual Cooking Progress Monitoring on Edge Devices
---

# Real-Time Cooked Food Image Synthesis and Visual Cooking Progress Monitoring on Edge Devices

**arXiv**: [2511.16965v1](https://arxiv.org/abs/2511.16965) | [PDF](https://arxiv.org/pdf/2511.16965.pdf)

**作者**: Jigyasa Gupta, Soumya Goyal, Anil Kumar, Ishan Jindal

---

## 💡 一句话要点

**提出边缘设备上基于烹饪状态引导的生成器以合成真实熟食图像并监控烹饪进度**

**关键词**: `图像合成` `边缘计算` `烹饪进度监控` `生成对抗网络` `领域特定度量`

## 📋 核心要点

1. 核心问题：边缘设备上合成真实熟食图像困难，现有方法不真实或资源消耗大
2. 方法要点：引入烹饪状态引导生成器，结合食谱和烹饪状态条件生成图像
3. 实验或效果：在数据集上FID分数显著降低，改进30%至60%

## 📄 摘要（原文）

> Synthesizing realistic cooked food images from raw inputs on edge devices is a challenging generative task, requiring models to capture complex changes in texture, color and structure during cooking. Existing image-to-image generation methods often produce unrealistic results or are too resource-intensive for edge deployment. We introduce the first oven-based cooking-progression dataset with chef-annotated doneness levels and propose an edge-efficient recipe and cooking state guided generator that synthesizes realistic food images conditioned on raw food image. This formulation enables user-preferred visual targets rather than fixed presets. To ensure temporal consistency and culinary plausibility, we introduce a domain-specific \textit{Culinary Image Similarity (CIS)} metric, which serves both as a training loss and a progress-monitoring signal. Our model outperforms existing baselines with significant reductions in FID scores (30\% improvement on our dataset; 60\% on public datasets)

