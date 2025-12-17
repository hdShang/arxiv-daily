---
layout: default
title: PhysCorr: Dual-Reward DPO for Physics-Constrained Text-to-Video Generation with Automated Preference Selection
---

# PhysCorr: Dual-Reward DPO for Physics-Constrained Text-to-Video Generation with Automated Preference Selection

**arXiv**: [2511.03997v1](https://arxiv.org/abs/2511.03997) | [PDF](https://arxiv.org/pdf/2511.03997.pdf)

**作者**: Peiyao Wang, Weining Wang, Qi Li

---

## 💡 一句话要点

**提出PhysCorr框架以解决文本到视频生成中的物理一致性问题**

**关键词**: `文本到视频生成` `物理一致性` `奖励模型` `直接偏好优化` `视频扩散模型`

## 📋 核心要点

1. 核心问题：生成视频常违反物理原理，如物体动态不合理，影响AI和机器人应用。
2. 方法要点：引入PhysicsRM奖励模型和PhyDPO优化管道，提升物理一致性。
3. 实验或效果：在多个基准测试中显著改善物理真实感，保持视觉保真度。

## 📄 摘要（原文）

> Recent advances in text-to-video generation have achieved impressive
> perceptual quality, yet generated content often violates fundamental principles
> of physical plausibility - manifesting as implausible object dynamics,
> incoherent interactions, and unrealistic motion patterns. Such failures hinder
> the deployment of video generation models in embodied AI, robotics, and
> simulation-intensive domains. To bridge this gap, we propose PhysCorr, a
> unified framework for modeling, evaluating, and optimizing physical consistency
> in video generation. Specifically, we introduce PhysicsRM, the first
> dual-dimensional reward model that quantifies both intra-object stability and
> inter-object interactions. On this foundation, we develop PhyDPO, a novel
> direct preference optimization pipeline that leverages contrastive feedback and
> physics-aware reweighting to guide generation toward physically coherent
> outputs. Our approach is model-agnostic and scalable, enabling seamless
> integration into a wide range of video diffusion and transformer-based
> backbones. Extensive experiments across multiple benchmarks demonstrate that
> PhysCorr achieves significant improvements in physical realism while preserving
> visual fidelity and semantic alignment. This work takes a critical step toward
> physically grounded and trustworthy video generation.

