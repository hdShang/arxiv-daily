---
layout: default
title: DualCamCtrl: Dual-Branch Diffusion Model for Geometry-Aware Camera-Controlled Video Generation
---

# DualCamCtrl: Dual-Branch Diffusion Model for Geometry-Aware Camera-Controlled Video Generation

**arXiv**: [2511.23127v1](https://arxiv.org/abs/2511.23127) | [PDF](https://arxiv.org/pdf/2511.23127.pdf)

**作者**: Hongfei Zhang, Kanghao Chen, Zixin Zhang, Harold Haodong Chen, Yuanhuiyi Lyu, Yuqi Zhang, Shuai Yang, Kun Zhou, Yingcong Chen

---

## 💡 一句话要点

**提出DualCamCtrl双分支扩散模型，通过RGB-深度序列互生成实现几何感知的相机控制视频生成。**

**关键词**: `相机控制视频生成` `扩散模型` `几何感知` `RGB-深度融合` `语义引导对齐`

## 📋 核心要点

1. 核心问题：现有相机控制视频生成方法缺乏场景理解和几何感知，导致相机轨迹一致性不足。
2. 方法要点：引入双分支框架生成相机一致的RGB和深度序列，并设计语义引导互对齐机制进行模态融合。
3. 实验或效果：在实验中减少相机运动误差超过40%，生成视频更忠实于指定相机轨迹。

## 📄 摘要（原文）

> This paper presents DualCamCtrl, a novel end-to-end diffusion model for camera-controlled video generation. Recent works have advanced this field by representing camera poses as ray-based conditions, yet they often lack sufficient scene understanding and geometric awareness. DualCamCtrl specifically targets this limitation by introducing a dual-branch framework that mutually generates camera-consistent RGB and depth sequences. To harmonize these two modalities, we further propose the Semantic Guided Mutual Alignment (SIGMA) mechanism, which performs RGB-depth fusion in a semantics-guided and mutually reinforced manner. These designs collectively enable DualCamCtrl to better disentangle appearance and geometry modeling, generating videos that more faithfully adhere to the specified camera trajectories. Additionally, we analyze and reveal the distinct influence of depth and camera poses across denoising stages and further demonstrate that early and late stages play complementary roles in forming global structure and refining local details. Extensive experiments demonstrate that DualCamCtrl achieves more consistent camera-controlled video generation, with over 40\% reduction in camera motion errors compared with prior methods. Our project page: https://soyouthinkyoucantell.github.io/dualcamctrl\-page/

