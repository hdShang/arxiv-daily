---
layout: default
title: Taming Camera-Controlled Video Generation with Verifiable Geometry Reward
---

# Taming Camera-Controlled Video Generation with Verifiable Geometry Reward

**arXiv**: [2512.02870v1](https://arxiv.org/abs/2512.02870) | [PDF](https://arxiv.org/pdf/2512.02870.pdf)

**作者**: Zhaoqing Wang, Xiaobo Xia, Zhuolin Bie, Jinlin Liu, Dongdong Yu, Jia-Wang Bian, Changhu Wang

---

## 💡 一句话要点

**提出在线强化学习后训练框架，通过可验证几何奖励优化相机控制视频生成**

**关键词**: `相机控制视频生成` `强化学习后训练` `可验证几何奖励` `3D相机轨迹估计` `视频扩散模型`

## 📋 核心要点

1. 核心问题：现有相机控制视频生成方法主要依赖监督微调，强化学习后训练未充分探索。
2. 方法要点：设计可验证几何奖励，基于3D相机轨迹分段比较，提供密集反馈以指导模型优化。
3. 实验或效果：在线强化学习后训练在相机控制精度、几何一致性和视觉质量上优于监督微调基线。

## 📄 摘要（原文）

> Recent advances in video diffusion models have remarkably improved camera-controlled video generation, but most methods rely solely on supervised fine-tuning (SFT), leaving online reinforcement learning (RL) post-training largely underexplored. In this work, we introduce an online RL post-training framework that optimizes a pretrained video generator for precise camera control. To make RL effective in this setting, we design a verifiable geometry reward that delivers dense segment-level feedback to guide model optimization. Specifically, we estimate the 3D camera trajectories for both generated and reference videos, divide each trajectory into short segments, and compute segment-wise relative poses. The reward function then compares each generated-reference segment pair and assigns an alignment score as the reward signal, which helps alleviate reward sparsity and improve optimization efficiency. Moreover, we construct a comprehensive dataset featuring diverse large-amplitude camera motions and scenes with varied subject dynamics. Extensive experiments show that our online RL post-training clearly outperforms SFT baselines across multiple aspects, including camera-control accuracy, geometric consistency, and visual quality, demonstrating its superiority in advancing camera-controlled video generation.

