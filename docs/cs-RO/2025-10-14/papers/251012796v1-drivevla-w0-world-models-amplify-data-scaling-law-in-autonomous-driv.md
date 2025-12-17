---
layout: default
title: DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving
---

# DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving

**arXiv**: [2510.12796v1](https://arxiv.org/abs/2510.12796) | [PDF](https://arxiv.org/pdf/2510.12796.pdf)

**作者**: Yingyan Li, Shuyao Shang, Weisong Liu, Bing Zhan, Haochen Wang, Yuqi Wang, Yuntao Chen, Xiaoman Wang, Yasong An, Chufeng Tang, Lu Hou, Lue Fan, Zhaoxiang Zhang

---

## 💡 一句话要点

**提出DriveVLA-W0训练范式，利用世界模型预测未来图像以增强自动驾驶VLA模型泛化能力。**

**关键词**: `自动驾驶` `视觉语言动作模型` `世界建模` `自监督学习` `数据缩放定律`

## 📋 核心要点

1. 核心问题：VLA模型存在监督不足，模型容量大但仅由稀疏动作监督，表示能力未充分利用。
2. 方法要点：采用世界建模预测未来图像，提供密集自监督信号，学习驾驶环境动态。
3. 实验效果：在NAVSIM基准和内部数据集上显著超越基线，并放大数据缩放定律。

## 📄 摘要（原文）

> Scaling Vision-Language-Action (VLA) models on large-scale data offers a
> promising path to achieving a more generalized driving intelligence. However,
> VLA models are limited by a ``supervision deficit'': the vast model capacity is
> supervised by sparse, low-dimensional actions, leaving much of their
> representational power underutilized. To remedy this, we propose
> \textbf{DriveVLA-W0}, a training paradigm that employs world modeling to
> predict future images. This task generates a dense, self-supervised signal that
> compels the model to learn the underlying dynamics of the driving environment.
> We showcase the paradigm's versatility by instantiating it for two dominant VLA
> archetypes: an autoregressive world model for VLAs that use discrete visual
> tokens, and a diffusion world model for those operating on continuous visual
> features. Building on the rich representations learned from world modeling, we
> introduce a lightweight action expert to address the inference latency for
> real-time deployment. Extensive experiments on the NAVSIM v1/v2 benchmark and a
> 680x larger in-house dataset demonstrate that DriveVLA-W0 significantly
> outperforms BEV and VLA baselines. Crucially, it amplifies the data scaling
> law, showing that performance gains accelerate as the training dataset size
> increases.

