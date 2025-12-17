---
layout: default
title: MACE: Mixture-of-Experts Accelerated Coordinate Encoding for Large-Scale Scene Localization and Rendering
---

# MACE: Mixture-of-Experts Accelerated Coordinate Encoding for Large-Scale Scene Localization and Rendering

**arXiv**: [2510.14251v1](https://arxiv.org/abs/2510.14251) | [PDF](https://arxiv.org/pdf/2510.14251.pdf)

**作者**: Mingkai Liu, Dikai Fan, Haohua Que, Haojia Gao, Xiao Liu, Shuxue Peng, Meixia Lin, Shengyu Gu, Ruicong Ye, Wanli Qiu, Handong Yao, Ruopeng Zhang, Xianliang Huang

---

## 💡 一句话要点

**提出MACE方法以解决大规模场景定位与渲染中的计算效率问题**

**关键词**: `场景坐标回归` `混合专家模型` `门控网络` `负载均衡` `大规模场景定位` `高效渲染`

## 📋 核心要点

1. 核心问题：大规模场景定位与渲染计算成本高，单网络容量不足。
2. 方法要点：引入门控网络选择子网络，仅激活单个子网络进行推理。
3. 实验效果：在剑桥测试集上，仅10分钟训练即可实现高质量渲染。

## 📄 摘要（原文）

> Efficient localization and high-quality rendering in large-scale scenes
> remain a significant challenge due to the computational cost involved. While
> Scene Coordinate Regression (SCR) methods perform well in small-scale
> localization, they are limited by the capacity of a single network when
> extended to large-scale scenes. To address these challenges, we propose the
> Mixed Expert-based Accelerated Coordinate Encoding method (MACE), which enables
> efficient localization and high-quality rendering in large-scale scenes.
> Inspired by the remarkable capabilities of MOE in large model domains, we
> introduce a gating network to implicitly classify and select sub-networks,
> ensuring that only a single sub-network is activated during each inference.
> Furtheremore, we present Auxiliary-Loss-Free Load Balancing(ALF-LB) strategy to
> enhance the localization accuracy on large-scale scene. Our framework provides
> a significant reduction in costs while maintaining higher precision, offering
> an efficient solution for large-scale scene applications. Additional
> experiments on the Cambridge test set demonstrate that our method achieves
> high-quality rendering results with merely 10 minutes of training.

