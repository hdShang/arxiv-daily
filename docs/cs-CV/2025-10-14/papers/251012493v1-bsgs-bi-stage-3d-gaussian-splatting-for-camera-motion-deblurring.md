---
layout: default
title: BSGS: Bi-stage 3D Gaussian Splatting for Camera Motion Deblurring
---

# BSGS: Bi-stage 3D Gaussian Splatting for Camera Motion Deblurring

**arXiv**: [2510.12493v1](https://arxiv.org/abs/2510.12493) | [PDF](https://arxiv.org/pdf/2510.12493.pdf)

**作者**: An Zhao, Piaopiao Yu, Zhe Zhu, Mingqiang Wei

---

## 💡 一句话要点

**提出双阶段3D高斯泼溅方法以解决相机运动模糊下的3D场景重建问题**

**关键词**: `3D高斯泼溅` `相机运动去模糊` `双阶段优化` `梯度聚合` `场景重建` `刚性变换`

## 📋 核心要点

1. 核心问题：现有3DGS方法在相机运动模糊下重建质量受限，依赖精确相机位姿且易产生错误高斯基元。
2. 方法要点：采用双阶段优化，先粗略优化相机位姿，再全局刚性变换校正模糊失真。
3. 实验效果：综合实验验证方法有效性，优于现有先进技术，提升重建质量。

## 📄 摘要（原文）

> 3D Gaussian Splatting has exhibited remarkable capabilities in 3D scene
> reconstruction.However, reconstructing high-quality 3D scenes from
> motion-blurred images caused by camera motion poses a significant challenge.The
> performance of existing 3DGS-based deblurring methods are limited due to their
> inherent mechanisms, such as extreme dependence on the accuracy of camera poses
> and inability to effectively control erroneous Gaussian primitives
> densification caused by motion blur.To solve these problems, we introduce a
> novel framework, Bi-Stage 3D Gaussian Splatting, to accurately reconstruct 3D
> scenes from motion-blurred images.BSGS contains two stages. First, Camera Pose
> Refinement roughly optimizes camera poses to reduce motion-induced distortions.
> Second, with fixed rough camera poses, Global RigidTransformation further
> corrects motion-induced blur distortions.To alleviate multi-subframe gradient
> conflicts, we propose a subframe gradient aggregation strategy to optimize both
> stages.Furthermore, a space-time bi-stage optimization strategy is introduced
> to dynamically adjust primitive densification thresholds and prevent premature
> noisy Gaussian generation in blurred regions. Comprehensive experiments verify
> the effectiveness of our proposed deblurring method and show its superiority
> over the state of the arts.

