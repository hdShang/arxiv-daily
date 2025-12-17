---
layout: default
title: MoCapAnything: Unified 3D Motion Capture for Arbitrary Skeletons from Monocular Videos
---

# MoCapAnything: Unified 3D Motion Capture for Arbitrary Skeletons from Monocular Videos

**arXiv**: [2512.10881v1](https://arxiv.org/abs/2512.10881) | [PDF](https://arxiv.org/pdf/2512.10881.pdf)

**作者**: Kehong Gong, Zhengyu Wen, Weixia He, Mingxi Xu, Qi Wang, Ning Zhang, Zhengyu Li, Dongze Lian, Wei Zhao, Xiaoyu He, Mingyuan Zhang

---

## 💡 一句话要点

**提出MoCapAnything框架，通过单目视频和任意骨骼资产实现类别无关的3D运动捕捉。**

**关键词**: `3D运动捕捉` `单目视频` `类别无关` `逆运动学` `骨骼动画` `跨物种重定向`

## 📋 核心要点

1. 核心问题：现有运动捕捉流程通常针对特定物种或模板，缺乏通用性。
2. 方法要点：采用参考引导的分解框架，预测3D关节轨迹并通过约束感知逆运动学恢复资产特定旋转。
3. 实验或效果：在基准测试和野外视频中生成高质量骨骼动画，支持跨物种重定向。

## 📄 摘要（原文）

> Motion capture now underpins content creation far beyond digital humans, yet most existing pipelines remain species- or template-specific. We formalize this gap as Category-Agnostic Motion Capture (CAMoCap): given a monocular video and an arbitrary rigged 3D asset as a prompt, the goal is to reconstruct a rotation-based animation such as BVH that directly drives the specific asset. We present MoCapAnything, a reference-guided, factorized framework that first predicts 3D joint trajectories and then recovers asset-specific rotations via constraint-aware inverse kinematics. The system contains three learnable modules and a lightweight IK stage: (1) a Reference Prompt Encoder that extracts per-joint queries from the asset's skeleton, mesh, and rendered images; (2) a Video Feature Extractor that computes dense visual descriptors and reconstructs a coarse 4D deforming mesh to bridge the gap between video and joint space; and (3) a Unified Motion Decoder that fuses these cues to produce temporally coherent trajectories. We also curate Truebones Zoo with 1038 motion clips, each providing a standardized skeleton-mesh-render triad. Experiments on both in-domain benchmarks and in-the-wild videos show that MoCapAnything delivers high-quality skeletal animations and exhibits meaningful cross-species retargeting across heterogeneous rigs, enabling scalable, prompt-driven 3D motion capture for arbitrary assets. Project page: https://animotionlab.github.io/MoCapAnything/

