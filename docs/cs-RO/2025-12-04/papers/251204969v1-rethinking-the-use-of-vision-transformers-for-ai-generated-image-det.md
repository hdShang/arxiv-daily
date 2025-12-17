---
layout: default
title: Rethinking the Use of Vision Transformers for AI-Generated Image Detection
---

# Rethinking the Use of Vision Transformers for AI-Generated Image Detection

**arXiv**: [2512.04969v1](https://arxiv.org/abs/2512.04969) | [PDF](https://arxiv.org/pdf/2512.04969.pdf)

**作者**: NaHyeon Park, Kunhee Kim, Junsuk Choe, Hyunjung Shim

---

## 💡 一句话要点

**提出MoLD方法，通过动态集成ViT多层特征以提升AI生成图像检测性能。**

**关键词**: `AI生成图像检测` `视觉Transformer` `多层特征集成` `门控机制` `泛化能力`

## 📋 核心要点

1. 核心问题：现有方法主要依赖CLIP-ViT最终层特征，忽略了多层特征的贡献。
2. 方法要点：引入基于门控机制的自适应方法MoLD，动态整合ViT多层特征。
3. 实验或效果：在GAN和扩散生成图像上验证，MoLD显著提升检测性能、泛化能力和鲁棒性。

## 📄 摘要（原文）

> Rich feature representations derived from CLIP-ViT have been widely utilized in AI-generated image detection. While most existing methods primarily leverage features from the final layer, we systematically analyze the contributions of layer-wise features to this task. Our study reveals that earlier layers provide more localized and generalizable features, often surpassing the performance of final-layer features in detection tasks. Moreover, we find that different layers capture distinct aspects of the data, each contributing uniquely to AI-generated image detection. Motivated by these findings, we introduce a novel adaptive method, termed MoLD, which dynamically integrates features from multiple ViT layers using a gating-based mechanism. Extensive experiments on both GAN- and diffusion-generated images demonstrate that MoLD significantly improves detection performance, enhances generalization across diverse generative models, and exhibits robustness in real-world scenarios. Finally, we illustrate the scalability and versatility of our approach by successfully applying it to other pre-trained ViTs, such as DINOv2.

