---
layout: default
title: LiNeXt: Revisiting LiDAR Completion with Efficient Non-Diffusion Architectures
---

# LiNeXt: Revisiting LiDAR Completion with Efficient Non-Diffusion Architectures

**arXiv**: [2511.10209v1](https://arxiv.org/abs/2511.10209) | [PDF](https://arxiv.org/pdf/2511.10209.pdf)

**作者**: Wenzhe He, Xiaojun Chen, Ruiqi Wang, Ruihui Li, Huilong Pi, Jiapeng Zhang, Zhuo Tang, Kenli Li

---

## 💡 一句话要点

**提出LiNeXt非扩散网络以高效解决LiDAR点云补全问题**

**关键词**: `LiDAR点云补全` `非扩散架构` `实时感知` `距离感知采样` `轻量网络`

## 📋 核心要点

1. 核心问题：扩散模型在LiDAR补全中计算开销大，难以实时应用。
2. 方法要点：使用N2C模块单次去噪和Refine模块精炼，结合距离感知策略。
3. 实验效果：在SemanticKITTI上，推理速度提升199.8倍，Chamfer距离降低50.7%。

## 📄 摘要（原文）

> 3D LiDAR scene completion from point clouds is a fundamental component of perception systems in autonomous vehicles. Previous methods have predominantly employed diffusion models for high-fidelity reconstruction. However, their multi-step iterative sampling incurs significant computational overhead, limiting its real-time applicability. To address this, we propose LiNeXt-a lightweight, non-diffusion network optimized for rapid and accurate point cloud completion. Specifically, LiNeXt first applies the Noise-to-Coarse (N2C) Module to denoise the input noisy point cloud in a single pass, thereby obviating the multi-step iterative sampling of diffusion-based methods. The Refine Module then takes the coarse point cloud and its intermediate features from the N2C Module to perform more precise refinement, further enhancing structural completeness. Furthermore, we observe that LiDAR point clouds exhibit a distance-dependent spatial distribution, being densely sampled at proximal ranges and sparsely sampled at distal ranges. Accordingly, we propose the Distance-aware Selected Repeat strategy to generate a more uniformly distributed noisy point cloud. On the SemanticKITTI dataset, LiNeXt achieves a 199.8x speedup in inference, reduces Chamfer Distance by 50.7%, and uses only 6.1% of the parameters compared with LiDiff. These results demonstrate the superior efficiency and effectiveness of LiNeXt for real-time scene completion.

