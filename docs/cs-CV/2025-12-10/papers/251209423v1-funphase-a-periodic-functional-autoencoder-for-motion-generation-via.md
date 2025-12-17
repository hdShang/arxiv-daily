---
layout: default
title: FunPhase: A Periodic Functional Autoencoder for Motion Generation via Phase Manifolds
---

# FunPhase: A Periodic Functional Autoencoder for Motion Generation via Phase Manifolds

**arXiv**: [2512.09423v1](https://arxiv.org/abs/2512.09423) | [PDF](https://arxiv.org/pdf/2512.09423.pdf)

**作者**: Marco Pegoraro, Evan Atherton, Bruno Roy, Aliasghar Khani, Arianna Rampini

---

## 💡 一句话要点

**提出FunPhase周期性功能自编码器，通过相位流形实现运动生成，解决时空耦合与可扩展性问题。**

**关键词**: `运动生成` `相位流形` `功能自编码器` `时空耦合` `超分辨率` `运动补全`

## 📋 核心要点

1. 核心问题：自然身体运动学习因空间几何与时间动态强耦合而具挑战性，现有相位流形方法缺乏可扩展性。
2. 方法要点：引入功能周期性自编码器，学习运动相位流形，用函数空间解码替代离散解码，支持任意时间分辨率采样。
3. 实验或效果：在重建误差上优于先前周期性自编码器基线，泛化于不同骨架和数据集，性能与先进运动生成方法相当。

## 📄 摘要（原文）

> Learning natural body motion remains challenging due to the strong coupling between spatial geometry and temporal dynamics. Embedding motion in phase manifolds, latent spaces that capture local periodicity, has proven effective for motion prediction; however, existing approaches lack scalability and remain confined to specific settings. We introduce FunPhase, a functional periodic autoencoder that learns a phase manifold for motion and replaces discrete temporal decoding with a function-space formulation, enabling smooth trajectories that can be sampled at arbitrary temporal resolutions. FunPhase supports downstream tasks such as super-resolution and partial-body motion completion, generalizes across skeletons and datasets, and unifies motion prediction and generation within a single interpretable manifold. Our model achieves substantially lower reconstruction error than prior periodic autoencoder baselines while enabling a broader range of applications and performing on par with state-of-the-art motion generation methods.

