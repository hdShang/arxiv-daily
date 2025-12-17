---
layout: default
title: GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures
---

# GAINS: Gaussian-based Inverse Rendering from Sparse Multi-View Captures

**arXiv**: [2512.09925v1](https://arxiv.org/abs/2512.09925) | [PDF](https://arxiv.org/pdf/2512.09925.pdf)

**作者**: Patrick Noras, Jun Myeong Choi, Didier Stricker, Pieter Peers, Roni Sengupta

---

## 💡 一句话要点

**提出GAINS框架以解决稀疏多视角下高斯溅射逆渲染的几何与材质模糊问题**

**关键词**: `高斯溅射` `逆渲染` `稀疏多视角` `材质恢复` `学习先验` `几何优化`

## 📋 核心要点

1. 核心问题：稀疏多视角捕获导致几何、反射率和光照严重模糊，现有方法性能下降
2. 方法要点：两阶段框架，先基于学习先验优化几何，再用分割、IID和扩散先验正则化材质恢复
3. 实验或效果：在合成和真实数据集上显著提升材质参数精度、重光照质量和新视角合成

## 📄 摘要（原文）

> Recent advances in Gaussian Splatting-based inverse rendering extend Gaussian primitives with shading parameters and physically grounded light transport, enabling high-quality material recovery from dense multi-view captures. However, these methods degrade sharply under sparse-view settings, where limited observations lead to severe ambiguity between geometry, reflectance, and lighting. We introduce GAINS (Gaussian-based Inverse rendering from Sparse multi-view captures), a two-stage inverse rendering framework that leverages learning-based priors to stabilize geometry and material estimation. GAINS first refines geometry using monocular depth/normal and diffusion priors, then employs segmentation, intrinsic image decomposition (IID), and diffusion priors to regularize material recovery. Extensive experiments on synthetic and real-world datasets show that GAINS significantly improves material parameter accuracy, relighting quality, and novel-view synthesis compared to state-of-the-art Gaussian-based inverse rendering methods, especially under sparse-view settings. Project page: https://patrickbail.github.io/gains/

