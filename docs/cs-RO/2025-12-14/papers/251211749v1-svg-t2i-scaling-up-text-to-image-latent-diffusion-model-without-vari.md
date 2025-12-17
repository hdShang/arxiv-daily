---
layout: default
title: SVG-T2I: Scaling Up Text-to-Image Latent Diffusion Model Without Variational Autoencoder
---

# SVG-T2I: Scaling Up Text-to-Image Latent Diffusion Model Without Variational Autoencoder

**arXiv**: [2512.11749v1](https://arxiv.org/abs/2512.11749) | [PDF](https://arxiv.org/pdf/2512.11749.pdf)

**作者**: Minglei Shi, Haolin Wang, Borui Zhang, Wenzhao Zheng, Bohan Zeng, Ziyang Yuan, Xiaoshi Wu, Yuanxing Zhang, Huan Yang, Xintao Wang, Pengfei Wan, Kun Gai, Jie Zhou, Jiwen Lu

---

## 💡 一句话要点

**提出SVG-T2I以在视觉基础模型表示空间中实现高质量文本到图像合成**

**关键词**: `文本到图像生成` `视觉基础模型` `扩散模型` `表示学习` `开源框架`

## 📋 核心要点

1. 核心问题：在视觉基础模型表示空间中训练大规模文本到图像扩散模型尚未充分探索
2. 方法要点：扩展SVG框架，直接在VFM特征域使用标准文本到图像扩散流程
3. 实验或效果：在GenEval和DPG-Bench上达到竞争性性能，验证VFM表示能力

## 📄 摘要（原文）

> Visual generation grounded in Visual Foundation Model (VFM) representations offers a highly promising unified pathway for integrating visual understanding, perception, and generation. Despite this potential, training large-scale text-to-image diffusion models entirely within the VFM representation space remains largely unexplored. To bridge this gap, we scale the SVG (Self-supervised representations for Visual Generation) framework, proposing SVG-T2I to support high-quality text-to-image synthesis directly in the VFM feature domain. By leveraging a standard text-to-image diffusion pipeline, SVG-T2I achieves competitive performance, reaching 0.75 on GenEval and 85.78 on DPG-Bench. This performance validates the intrinsic representational power of VFMs for generative tasks. We fully open-source the project, including the autoencoder and generation model, together with their training, inference, evaluation pipelines, and pre-trained weights, to facilitate further research in representation-driven visual generation.

