---
layout: default
title: Learning to Restore Multi-Degraded Images via Ingredient Decoupling and Task-Aware Path Adaptation
---

# Learning to Restore Multi-Degraded Images via Ingredient Decoupling and Task-Aware Path Adaptation

**arXiv**: [2511.04920v1](https://arxiv.org/abs/2511.04920) | [PDF](https://arxiv.org/pdf/2511.04920.pdf)

**作者**: Hu Gao, Xiaoning Lei, Ying Zhang, Xichen Xu, Guannan Jiang, Lizhuang Ma

---

## 💡 一句话要点

**提出IMDNet网络，通过解耦降解成分和任务感知路径适应，解决多降解图像恢复问题。**

**关键词**: `图像恢复` `多降解处理` `成分解耦` `路径适应` `深度学习`

## 📋 核心要点

1. 核心问题：现实图像常存在多种降解共存，现有方法多针对单一降解，效果受限。
2. 方法要点：设计DIDBlock解耦降解成分，TABlock动态选择恢复路径，提升适应性。
3. 实验或效果：在单降解和多降解任务上均表现优越，验证了网络的有效性。

## 📄 摘要（原文）

> Image restoration (IR) aims to recover clean images from degraded
> observations. Despite remarkable progress, most existing methods focus on a
> single degradation type, whereas real-world images often suffer from multiple
> coexisting degradations, such as rain, noise, and haze coexisting in a single
> image, which limits their practical effectiveness. In this paper, we propose an
> adaptive multi-degradation image restoration network that reconstructs images
> by leveraging decoupled representations of degradation ingredients to guide
> path selection. Specifically, we design a degradation ingredient decoupling
> block (DIDBlock) in the encoder to separate degradation ingredients
> statistically by integrating spatial and frequency domain information,
> enhancing the recognition of multiple degradation types and making their
> feature representations independent. In addition, we present fusion block
> (FBlock) to integrate degradation information across all levels using learnable
> matrices. In the decoder, we further introduce a task adaptation block
> (TABlock) that dynamically activates or fuses functional branches based on the
> multi-degradation representation, flexibly selecting optimal restoration paths
> under diverse degradation conditions. The resulting tightly integrated
> architecture, termed IMDNet, is extensively validated through experiments,
> showing superior performance on multi-degradation restoration while maintaining
> strong competitiveness on single-degradation tasks.

