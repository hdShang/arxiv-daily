---
layout: default
title: DreamPose3D: Hallucinative Diffusion with Prompt Learning for 3D Human Pose Estimation
---

# DreamPose3D: Hallucinative Diffusion with Prompt Learning for 3D Human Pose Estimation

**arXiv**: [2511.09502v1](https://arxiv.org/abs/2511.09502) | [PDF](https://arxiv.org/pdf/2511.09502.pdf)

**作者**: Jerrin Bright, Yuhao Chen, John S. Zelek

---

## 💡 一句话要点

**提出DreamPose3D扩散框架，结合动作提示与时间想象解决3D人体姿态估计中的模糊运动问题**

**关键词**: `3D人体姿态估计` `扩散模型` `动作提示学习` `时间一致性` `关节亲和力编码` `幻觉姿态解码`

## 📋 核心要点

1. 核心问题：现有方法依赖几何线索独立预测3D姿态，难以处理模糊运动和泛化到真实场景。
2. 方法要点：使用动作提示条件化去噪过程，引入关节亲和力编码器，并采用幻觉姿态解码器预测时间一致序列。
3. 实验或效果：在Human3.6M和MPI-3DHP数据集上达到SOTA，并在广播棒球数据上验证鲁棒性。

## 📄 摘要（原文）

> Accurate 3D human pose estimation remains a critical yet unresolved challenge, requiring both temporal coherence across frames and fine-grained modeling of joint relationships. However, most existing methods rely solely on geometric cues and predict each 3D pose independently, which limits their ability to resolve ambiguous motions and generalize to real-world scenarios. Inspired by how humans understand and anticipate motion, we introduce DreamPose3D, a diffusion-based framework that combines action-aware reasoning with temporal imagination for 3D pose estimation. DreamPose3D dynamically conditions the denoising process using task-relevant action prompts extracted from 2D pose sequences, capturing high-level intent. To model the structural relationships between joints effectively, we introduce a representation encoder that incorporates kinematic joint affinity into the attention mechanism. Finally, a hallucinative pose decoder predicts temporally coherent 3D pose sequences during training, simulating how humans mentally reconstruct motion trajectories to resolve ambiguity in perception. Extensive experiments on benchmarked Human3.6M and MPI-3DHP datasets demonstrate state-of-the-art performance across all metrics. To further validate DreamPose3D's robustness, we tested it on a broadcast baseball dataset, where it demonstrated strong performance despite ambiguous and noisy 2D inputs, effectively handling temporal consistency and intent-driven motion variations.

