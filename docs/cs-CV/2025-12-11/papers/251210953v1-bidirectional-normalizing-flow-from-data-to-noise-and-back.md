---
layout: default
title: Bidirectional Normalizing Flow: From Data to Noise and Back
---

# Bidirectional Normalizing Flow: From Data to Noise and Back

**arXiv**: [2512.10953v1](https://arxiv.org/abs/2512.10953) | [PDF](https://arxiv.org/pdf/2512.10953.pdf)

**作者**: Yiyang Lu, Qiao Sun, Xianbang Wang, Zhicheng Jiang, Hanhong Zhao, Kaiming He

---

## 💡 一句话要点

**提出双向归一化流以解决因果解码瓶颈，提升生成质量与采样速度**

**关键词**: `归一化流` `生成模型` `双向学习` `采样加速` `ImageNet生成`

## 📋 核心要点

1. 核心问题：标准归一化流需精确解析逆变换，因果解码成为性能瓶颈
2. 方法要点：学习近似逆映射的逆向模型，无需精确逆变换，支持更灵活的损失函数与架构
3. 实验或效果：在ImageNet上，相比因果解码方法，生成质量提升，采样加速达两个数量级

## 📄 摘要（原文）

> Normalizing Flows (NFs) have been established as a principled framework for generative modeling. Standard NFs consist of a forward process and a reverse process: the forward process maps data to noise, while the reverse process generates samples by inverting it. Typical NF forward transformations are constrained by explicit invertibility, ensuring that the reverse process can serve as their exact analytic inverse. Recent developments in TARFlow and its variants have revitalized NF methods by combining Transformers and autoregressive flows, but have also exposed causal decoding as a major bottleneck. In this work, we introduce Bidirectional Normalizing Flow ($\textbf{BiFlow}$), a framework that removes the need for an exact analytic inverse. BiFlow learns a reverse model that approximates the underlying noise-to-data inverse mapping, enabling more flexible loss functions and architectures. Experiments on ImageNet demonstrate that BiFlow, compared to its causal decoding counterpart, improves generation quality while accelerating sampling by up to two orders of magnitude. BiFlow yields state-of-the-art results among NF-based methods and competitive performance among single-evaluation ("1-NFE") methods. Following recent encouraging progress on NFs, we hope our work will draw further attention to this classical paradigm.

