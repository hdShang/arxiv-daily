---
layout: default
title: NeuralRemaster: Phase-Preserving Diffusion for Structure-Aligned Generation
---

# NeuralRemaster: Phase-Preserving Diffusion for Structure-Aligned Generation

**arXiv**: [2512.05106v1](https://arxiv.org/abs/2512.05106) | [PDF](https://arxiv.org/pdf/2512.05106.pdf)

**作者**: Yu Zeng, Charles Ochoa, Mingyuan Zhou, Vishal M. Patel, Vitor Guizilini, Rowan McAllister

---

## 💡 一句话要点

**提出相位保持扩散以解决标准扩散破坏空间结构的问题，适用于结构对齐生成任务。**

**关键词**: `相位保持扩散` `结构对齐生成` `图像到图像翻译` `视频生成` `频率选择性噪声` `模拟到真实增强`

## 📋 核心要点

1. 标准扩散使用高斯噪声破坏相位，导致空间结构丢失，不适合几何一致性任务。
2. 引入相位保持扩散，保留输入相位并随机化幅度，无需修改架构或增加参数。
3. 提出频率选择性结构化噪声，通过单一频率截止参数控制结构刚性，实验显示在CARLA模拟器中提升规划器性能50%。

## 📄 摘要（原文）

> Standard diffusion corrupts data using Gaussian noise whose Fourier coefficients have random magnitudes and random phases. While effective for unconditional or text-to-image generation, corrupting phase components destroys spatial structure, making it ill-suited for tasks requiring geometric consistency, such as re-rendering, simulation enhancement, and image-to-image translation. We introduce Phase-Preserving Diffusion φ-PD, a model-agnostic reformulation of the diffusion process that preserves input phase while randomizing magnitude, enabling structure-aligned generation without architectural changes or additional parameters. We further propose Frequency-Selective Structured (FSS) noise, which provides continuous control over structural rigidity via a single frequency-cutoff parameter. φ-PD adds no inference-time cost and is compatible with any diffusion model for images or videos. Across photorealistic and stylized re-rendering, as well as sim-to-real enhancement for driving planners, φ-PD produces controllable, spatially aligned results. When applied to the CARLA simulator, φ-PD improves CARLA-to-Waymo planner performance by 50\%. The method is complementary to existing conditioning approaches and broadly applicable to image-to-image and video-to-video generation. Videos, additional examples, and code are available on our \href{https://yuzeng-at-tri.github.io/ppd-page/}{project page}.

