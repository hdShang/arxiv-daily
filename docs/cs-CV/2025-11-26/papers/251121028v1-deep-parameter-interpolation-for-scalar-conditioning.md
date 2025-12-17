---
layout: default
title: Deep Parameter Interpolation for Scalar Conditioning
---

# Deep Parameter Interpolation for Scalar Conditioning

**arXiv**: [2511.21028v1](https://arxiv.org/abs/2511.21028) | [PDF](https://arxiv.org/pdf/2511.21028.pdf)

**作者**: Chicago Y. Park, Michael T. McCann, Cristina Garcia-Cardona, Brendt Wohlberg, Ulugbek S. Kamilov

---

## 💡 一句话要点

**提出深度参数插值方法，为深度神经网络添加标量输入依赖。**

**关键词**: `深度参数插值` `标量条件化` `生成模型` `扩散模型` `流匹配` `神经网络架构`

## 📋 核心要点

1. 核心问题：深度生成模型中，网络需同时处理高维向量和标量输入，架构设计受限。
2. 方法要点：在单网络中维护两套可学习参数，基于标量值动态插值参数。
3. 实验或效果：在扩散和流匹配模型中，提升去噪性能和样本质量，计算效率高。

## 📄 摘要（原文）

> We propose deep parameter interpolation (DPI), a general-purpose method for transforming an existing deep neural network architecture into one that accepts an additional scalar input. Recent deep generative models, including diffusion models and flow matching, employ a single neural network to learn a time- or noise level-dependent vector field. Designing a network architecture to accurately represent this vector field is challenging because the network must integrate information from two different sources: a high-dimensional vector (usually an image) and a scalar. Common approaches either encode the scalar as an additional image input or combine scalar and vector information in specific network components, which restricts architecture choices. Instead, we propose to maintain two learnable parameter sets within a single network and to introduce the scalar dependency by dynamically interpolating between the parameter sets based on the scalar value during training and sampling. DPI is a simple, architecture-agnostic method for adding scalar dependence to a neural network. We demonstrate that our method improves denoising performance and enhances sample quality for both diffusion and flow matching models, while achieving computational efficiency comparable to standard scalar conditioning techniques. Code is available at https://github.com/wustl-cig/parameter_interpolation.

