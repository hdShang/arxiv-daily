---
layout: default
title: Unlocking Generalization in Polyp Segmentation with DINO Self-Attention "keys"
---

# Unlocking Generalization in Polyp Segmentation with DINO Self-Attention "keys"

**arXiv**: [2512.13376v1](https://arxiv.org/abs/2512.13376) | [PDF](https://arxiv.org/pdf/2512.13376.pdf)

**作者**: Carla Monteiro, Valentina Corbetta, Regina Beets-Tan, Luís F. Teixeira, Wilson Silva

---

## 💡 一句话要点

**提出利用DINO自注意力键特征框架以增强息肉分割的泛化能力**

**关键词**: `息肉分割` `自注意力机制` `域泛化` `DINO框架` `卷积解码器`

## 📋 核心要点

1. 核心问题：现有息肉分割方法泛化性差，尤其在数据受限或挑战性场景中。
2. 方法要点：利用DINO自注意力键特征，结合简单卷积解码器，避免复杂任务特定架构。
3. 实验或效果：在多中心数据集上验证，在域泛化和极端单域泛化协议下达到SOTA性能。

## 📄 摘要（原文）

> Automatic polyp segmentation is crucial for improving the clinical identification of colorectal cancer (CRC). While Deep Learning (DL) techniques have been extensively researched for this problem, current methods frequently struggle with generalization, particularly in data-constrained or challenging settings. Moreover, many existing polyp segmentation methods rely on complex, task-specific architectures. To address these limitations, we present a framework that leverages the intrinsic robustness of DINO self-attention "key" features for robust segmentation. Unlike traditional methods that extract tokens from the deepest layers of the Vision Transformer (ViT), our approach leverages the key features of the self-attention module with a simple convolutional decoder to predict polyp masks, resulting in enhanced performance and better generalizability. We validate our approach using a multi-center dataset under two rigorous protocols: Domain Generalization (DG) and Extreme Single Domain Generalization (ESDG). Our results, supported by a comprehensive statistical analysis, demonstrate that this pipeline achieves state-of-the-art (SOTA) performance, significantly enhancing generalization, particularly in data-scarce and challenging scenarios. While avoiding a polyp-specific architecture, we surpass well-established models like nnU-Net and UM-Net. Additionally, we provide a systematic benchmark of the DINO framework's evolution, quantifying the specific impact of architectural advancements on downstream polyp segmentation performance.

