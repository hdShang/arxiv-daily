---
layout: default
title: Physics-Informed Video Flare Synthesis and Removal Leveraging Motion Independence between Flare and Scene
---

# Physics-Informed Video Flare Synthesis and Removal Leveraging Motion Independence between Flare and Scene

**arXiv**: [2512.11327v1](https://arxiv.org/abs/2512.11327) | [PDF](https://arxiv.org/pdf/2512.11327.pdf)

**作者**: Junqiao Wang, Yuanfei Huang, Hua Huang

---

## 💡 一句话要点

**提出物理引导的视频光晕合成与去除方法，利用光晕与场景运动独立性提升视频恢复性能。**

**关键词**: `视频光晕去除` `物理引导合成` `时空建模` `注意力机制` `Mamba网络` `光晕数据集`

## 📋 核心要点

1. 核心问题：视频光晕去除因光晕、光源和场景运动独立而复杂，导致闪烁和伪影。
2. 方法要点：设计物理引导的动态光晕合成流程和基于注意力与Mamba的视频去除网络，无需多帧对齐。
3. 实验或效果：构建首个视频光晕数据集，实验显示在真实和合成视频上优于现有方法，保持时空一致性。

## 📄 摘要（原文）

> Lens flare is a degradation phenomenon caused by strong light sources. Existing researches on flare removal have mainly focused on images, while the spatiotemporal characteristics of video flare remain largely unexplored. Video flare synthesis and removal pose significantly greater challenges than in image, owing to the complex and mutually independent motion of flare, light sources, and scene content. This motion independence further affects restoration performance, often resulting in flicker and artifacts. To address this issue, we propose a physics-informed dynamic flare synthesis pipeline, which simulates light source motion using optical flow and models the temporal behaviors of both scattering and reflective flares. Meanwhile, we design a video flare removal network that employs an attention module to spatially suppress flare regions and incorporates a Mamba-based temporal modeling component to capture long range spatio-temporal dependencies. This motion-independent spatiotemporal representation effectively eliminates the need for multi-frame alignment, alleviating temporal aliasing between flares and scene content and thereby improving video flare removal performance. Building upon this, we construct the first video flare dataset to comprehensively evaluate our method, which includes a large set of synthetic paired videos and additional real-world videos collected from the Internet to assess generalization capability. Extensive experiments demonstrate that our method consistently outperforms existing video-based restoration and image-based flare removal methods on both real and synthetic videos, effectively removing dynamic flares while preserving light source integrity and maintaining spatiotemporal consistency of scene.

