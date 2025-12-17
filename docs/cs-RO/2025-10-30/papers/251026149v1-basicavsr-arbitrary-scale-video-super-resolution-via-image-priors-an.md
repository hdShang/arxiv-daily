---
layout: default
title: BasicAVSR: Arbitrary-Scale Video Super-Resolution via Image Priors and Enhanced Motion Compensation
---

# BasicAVSR: Arbitrary-Scale Video Super-Resolution via Image Priors and Enhanced Motion Compensation

**arXiv**: [2510.26149v1](https://arxiv.org/abs/2510.26149) | [PDF](https://arxiv.org/pdf/2510.26149.pdf)

**作者**: Wei Shang, Wanying Zhang, Shuhang Gu, Pengfei Zhu, Qinghua Hu, Dongwei Ren

---

## 💡 一句话要点

**提出BasicAVSR以解决任意尺度视频超分辨率的时空一致性和计算效率问题**

**关键词**: `视频超分辨率` `任意尺度上采样` `运动补偿` `拉普拉斯金字塔` `RNN传播` `超上采样单元`

## 📋 核心要点

1. 核心问题：任意尺度视频超分辨率在空间细节、时间一致性和计算复杂度方面存在挑战
2. 方法要点：集成图像拉普拉斯金字塔先验、流引导传播单元、二阶运动补偿和超上采样单元
3. 实验或效果：在超分辨率质量、泛化能力和推理速度上显著优于现有方法

## 📄 摘要（原文）

> Arbitrary-scale video super-resolution (AVSR) aims to enhance the resolution
> of video frames, potentially at various scaling factors, which presents several
> challenges regarding spatial detail reproduction, temporal consistency, and
> computational complexity. In this paper, we propose a strong baseline BasicAVSR
> for AVSR by integrating four key components: 1) adaptive multi-scale frequency
> priors generated from image Laplacian pyramids, 2) a flow-guided propagation
> unit to aggregate spatiotemporal information from adjacent frames, 3) a
> second-order motion compensation unit for more accurate spatial alignment of
> adjacent frames, and 4) a hyper-upsampling unit to generate scale-aware and
> content-independent upsampling kernels. To meet diverse application demands, we
> instantiate three propagation variants: (i) a unidirectional RNN unit for
> strictly online inference, (ii) a unidirectional RNN unit empowered with a
> limited lookahead that tolerates a small output delay, and (iii) a
> bidirectional RNN unit designed for offline tasks where computational resources
> are less constrained. Experimental results demonstrate the effectiveness and
> adaptability of our model across these different scenarios. Through extensive
> experiments, we show that BasicAVSR significantly outperforms existing methods
> in terms of super-resolution quality, generalization ability, and inference
> speed. Our work not only advances the state-of-the-art in AVSR but also extends
> its core components to multiple frameworks for diverse scenarios. The code is
> available at https://github.com/shangwei5/BasicAVSR.

