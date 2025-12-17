---
layout: default
title: SEE4D: Pose-Free 4D Generation via Auto-Regressive Video Inpainting
---

# SEE4D: Pose-Free 4D Generation via Auto-Regressive Video Inpainting

**arXiv**: [2510.26796v1](https://arxiv.org/abs/2510.26796) | [PDF](https://arxiv.org/pdf/2510.26796.pdf)

**作者**: Dongyue Lu, Ao Liang, Tianxin Huang, Xiao Fu, Yuyang Zhao, Baorui Ma, Liang Pan, Wei Yin, Lingdong Kong, Wei Tsang Ooi, Ziwei Liu

---

## 💡 一句话要点

**提出SEE4D方法，通过自回归视频修复实现无姿态4D生成，从随意视频合成时空内容。**

**关键词**: `4D生成` `视频修复` `无姿态学习` `虚拟相机` `自回归推理` `时空建模`

## 📋 核心要点

1. 核心问题：现有视频到4D方法依赖手动标注相机姿态，成本高且对野外视频脆弱。
2. 方法要点：使用固定虚拟相机库和视图条件视频修复模型，分离相机控制与场景建模。
3. 实验或效果：在跨视图视频生成和稀疏重建基准上，实现优于姿态或轨迹条件基线的性能。

## 📄 摘要（原文）

> Immersive applications call for synthesizing spatiotemporal 4D content from
> casual videos without costly 3D supervision. Existing video-to-4D methods
> typically rely on manually annotated camera poses, which are labor-intensive
> and brittle for in-the-wild footage. Recent warp-then-inpaint approaches
> mitigate the need for pose labels by warping input frames along a novel camera
> trajectory and using an inpainting model to fill missing regions, thereby
> depicting the 4D scene from diverse viewpoints. However, this
> trajectory-to-trajectory formulation often entangles camera motion with scene
> dynamics and complicates both modeling and inference. We introduce SEE4D, a
> pose-free, trajectory-to-camera framework that replaces explicit trajectory
> prediction with rendering to a bank of fixed virtual cameras, thereby
> separating camera control from scene modeling. A view-conditional video
> inpainting model is trained to learn a robust geometry prior by denoising
> realistically synthesized warped images and to inpaint occluded or missing
> regions across virtual viewpoints, eliminating the need for explicit 3D
> annotations. Building on this inpainting core, we design a spatiotemporal
> autoregressive inference pipeline that traverses virtual-camera splines and
> extends videos with overlapping windows, enabling coherent generation at
> bounded per-step complexity. We validate See4D on cross-view video generation
> and sparse reconstruction benchmarks. Across quantitative metrics and
> qualitative assessments, our method achieves superior generalization and
> improved performance relative to pose- or trajectory-conditioned baselines,
> advancing practical 4D world modeling from casual videos.

