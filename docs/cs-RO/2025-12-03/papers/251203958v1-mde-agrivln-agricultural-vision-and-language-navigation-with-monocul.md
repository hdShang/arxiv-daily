---
layout: default
title: MDE-AgriVLN: Agricultural Vision-and-Language Navigation with Monocular Depth Estimation
---

# MDE-AgriVLN: Agricultural Vision-and-Language Navigation with Monocular Depth Estimation

**arXiv**: [2512.03958v1](https://arxiv.org/abs/2512.03958) | [PDF](https://arxiv.org/pdf/2512.03958.pdf)

**作者**: Xiaobei Zhao, Xingqi Lyu, Xiang Li

---

## 💡 一句话要点

**提出MDE-AgriVLN方法，通过单目深度估计增强农业视觉语言导航的空间感知能力。**

**关键词**: `农业视觉语言导航` `单目深度估计` `机器人导航` `空间感知增强` `A2A基准`

## 📋 核心要点

1. 核心问题：农业机器人仅配备单目相机，空间感知受限，影响导航精度。
2. 方法要点：引入MDE模块，从RGB图像生成深度特征，辅助决策推理。
3. 实验或效果：在A2A基准上，成功率从0.23提升至0.32，导航误差从4.43m降至4.08m。

## 📄 摘要（原文）

> Agricultural robots are serving as powerful assistants across a wide range of agricultural tasks, nevertheless, still heavily relying on manual operations or railway systems for movement. The AgriVLN method and the A2A benchmark pioneeringly extend Vision-and-Language Navigation (VLN) to the agricultural domain, enabling a robot to navigate to a target position following a natural language instruction. Unlike human binocular vision, most agricultural robots are only given a single camera for monocular vision, which results in limited spatial perception. To bridge this gap, we present the method of Agricultural Vision-and-Language Navigation with Monocular Depth Estimation (MDE-AgriVLN), in which we propose the MDE module generating depth features from RGB images, to assist the decision-maker on reasoning. When evaluated on the A2A benchmark, our MDE-AgriVLN method successfully increases Success Rate from 0.23 to 0.32 and decreases Navigation Error from 4.43m to 4.08m, demonstrating the state-of-the-art performance in the agricultural VLN domain. Code: https://github.com/AlexTraveling/MDE-AgriVLN.

