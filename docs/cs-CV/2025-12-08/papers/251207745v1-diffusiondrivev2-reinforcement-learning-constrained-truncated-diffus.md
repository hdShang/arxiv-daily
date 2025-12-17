---
layout: default
title: DiffusionDriveV2: Reinforcement Learning-Constrained Truncated Diffusion Modeling in End-to-End Autonomous Driving
---

# DiffusionDriveV2: Reinforcement Learning-Constrained Truncated Diffusion Modeling in End-to-End Autonomous Driving

**arXiv**: [2512.07745v1](https://arxiv.org/abs/2512.07745) | [PDF](https://arxiv.org/pdf/2512.07745.pdf)

**作者**: Jialv Zou, Shaoyu Chen, Bencheng Liao, Zhiyu Zheng, Yuehao Song, Lefei Zhang, Qian Zhang, Wenyu Liu, Xinggang Wang

---

## 💡 一句话要点

**提出DiffusionDriveV2，利用强化学习约束截断扩散模型，解决端到端自动驾驶中多样性与高质量轨迹生成的困境。**

**关键词**: `端到端自动驾驶` `扩散模型` `强化学习` `轨迹生成` `模式崩溃` `截断建模`

## 📋 核心要点

1. 核心问题：生成扩散模型在端到端自动驾驶中易出现模式崩溃，导致保守和同质化行为，难以平衡多样性与一致高质量。
2. 方法要点：采用尺度自适应乘性噪声促进探索，结合锚内GRPO和锚间截断GRPO管理优势估计，避免不同意图间不当比较。
3. 实验或效果：在NAVSIM数据集上取得领先性能，验证了方法在多样性与高质量间的优化平衡，代码将开源。

## 📄 摘要（原文）

> Generative diffusion models for end-to-end autonomous driving often suffer from mode collapse, tending to generate conservative and homogeneous behaviors. While DiffusionDrive employs predefined anchors representing different driving intentions to partition the action space and generate diverse trajectories, its reliance on imitation learning lacks sufficient constraints, resulting in a dilemma between diversity and consistent high quality. In this work, we propose DiffusionDriveV2, which leverages reinforcement learning to both constrain low-quality modes and explore for superior trajectories. This significantly enhances the overall output quality while preserving the inherent multimodality of its core Gaussian Mixture Model. First, we use scale-adaptive multiplicative noise, ideal for trajectory planning, to promote broad exploration. Second, we employ intra-anchor GRPO to manage advantage estimation among samples generated from a single anchor, and inter-anchor truncated GRPO to incorporate a global perspective across different anchors, preventing improper advantage comparisons between distinct intentions (e.g., turning vs. going straight), which can lead to further mode collapse. DiffusionDriveV2 achieves 91.2 PDMS on the NAVSIM v1 dataset and 85.5 EPDMS on the NAVSIM v2 dataset in closed-loop evaluation with an aligned ResNet-34 backbone, setting a new record. Further experiments validate that our approach resolves the dilemma between diversity and consistent high quality for truncated diffusion models, achieving the best trade-off. Code and model will be available at https://github.com/hustvl/DiffusionDriveV2

