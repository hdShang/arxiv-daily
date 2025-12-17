---
layout: default
title: RL-AD-Net: Reinforcement Learning Guided Adaptive Displacement in Latent Space for Refined Point Cloud Completion
---

# RL-AD-Net: Reinforcement Learning Guided Adaptive Displacement in Latent Space for Refined Point Cloud Completion

**arXiv**: [2511.17054v1](https://arxiv.org/abs/2511.17054) | [PDF](https://arxiv.org/pdf/2511.17054.pdf)

**作者**: Bhanu Pratap Paregi, Vaibhav Kumar

---

## 💡 一句话要点

**提出RL-AD-Net，通过强化学习在潜在空间调整点云补全，提升几何一致性。**

**关键词**: `点云补全` `强化学习` `潜在空间优化` `几何一致性` `模型无关框架`

## 📋 核心要点

1. 点云补全模型常产生局部几何不一致问题。
2. 使用强化学习在预训练自编码器潜在空间微调全局特征向量。
3. 实验显示在随机裁剪场景下，RL-AD-Net优于基线模型。

## 📄 摘要（原文）

> Recent point cloud completion models, including transformer-based, denoising-based, and other state-of-the-art approaches, generate globally plausible shapes from partial inputs but often leave local geometric inconsistencies. We propose RL-AD-Net, a reinforcement learning (RL) refinement framework that operates in the latent space of a pretrained point autoencoder. The autoencoder encodes completions into compact global feature vectors (GFVs), which are selectively adjusted by an RL agent to improve geometric fidelity. To ensure robustness, a lightweight non-parametric PointNN selector evaluates the geometric consistency of both the original completion and the RL-refined output, retaining the better reconstruction. When ground truth is available, both Chamfer Distance and geometric consistency metrics guide refinement. Training is performed separately per category, since the unsupervised and dynamic nature of RL makes convergence across highly diverse categories challenging. Nevertheless, the framework can be extended to multi-category refinement in future work. Experiments on ShapeNetCore-2048 demonstrate that while baseline completion networks perform reasonable under their training-style cropping, they struggle in random cropping scenarios. In contrast, RL-AD-Net consistently delivers improvements across both settings, highlighting the effectiveness of RL-guided ensemble refinement. The approach is lightweight, modular, and model-agnostic, making it applicable to a wide range of completion networks without requiring retraining.

