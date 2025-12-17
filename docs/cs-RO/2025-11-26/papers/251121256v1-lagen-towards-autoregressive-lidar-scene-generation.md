---
layout: default
title: LaGen: Towards Autoregressive LiDAR Scene Generation
---

# LaGen: Towards Autoregressive LiDAR Scene Generation

**arXiv**: [2511.21256v1](https://arxiv.org/abs/2511.21256) | [PDF](https://arxiv.org/pdf/2511.21256.pdf)

**作者**: Sizhuo Zhou, Xiaosong Jia, Fanrui Zhang, Junjie Li, Juyong Zhang, Yukang Feng, Jianwen Sun, Songbur Wong, Junqi You, Junchi Yan

---

## 💡 一句话要点

**提出LaGen框架，实现单帧输入的长时程自回归LiDAR场景生成。**

**关键词**: `LiDAR场景生成` `自回归模型` `长时程预测` `点云生成` `自动驾驶世界模型`

## 📋 核心要点

1. 核心问题：现有LiDAR生成方法仅支持单帧，预测方法缺乏交互性，无法长时程生成。
2. 方法要点：引入场景解耦估计和噪声调制模块，增强对象级交互生成和减少误差累积。
3. 实验或效果：在nuScenes基准上，LaGen优于现有方法，尤其在后期帧表现突出。

## 📄 摘要（原文）

> Generative world models for autonomous driving (AD) have become a trending topic. Unlike the widely studied image modality, in this work we explore generative world models for LiDAR data. Existing generation methods for LiDAR data only support single frame generation, while existing prediction approaches require multiple frames of historical input and can only deterministically predict multiple frames at once, lacking interactivity. Both paradigms fail to support long-horizon interactive generation. To this end, we introduce LaGen, which to the best of our knowledge is the first framework capable of frame-by-frame autoregressive generation of long-horizon LiDAR scenes. LaGen is able to take a single-frame LiDAR input as a starting point and effectively utilize bounding box information as conditions to generate high-fidelity 4D scene point clouds. In addition, we introduce a scene decoupling estimation module to enhance the model's interactive generation capability for object-level content, as well as a noise modulation module to mitigate error accumulation during long-horizon generation. We construct a protocol based on nuScenes for evaluating long-horizon LiDAR scene generation. Experimental results comprehensively demonstrate LaGen outperforms state-of-the-art LiDAR generation and prediction models, especially on the later frames.

