---
layout: default
title: Generative Editing in the Joint Vision-Language Space for Zero-Shot Composed Image Retrieval
---

# Generative Editing in the Joint Vision-Language Space for Zero-Shot Composed Image Retrieval

**arXiv**: [2512.01636v1](https://arxiv.org/abs/2512.01636) | [PDF](https://arxiv.org/pdf/2512.01636.pdf)

**作者**: Xin Wang, Haipeng Zhang, Mang Li, Zhaohui Xia, Yueguo Chen, Yu Zhang, Chunyu Wei

---

## 💡 一句话要点

**提出Fusion-Diff框架，通过联合视觉-语言空间编辑解决零样本组合图像检索的模态鸿沟问题。**

**关键词**: `零样本组合图像检索` `多模态对齐` `生成编辑` `视觉-语言空间` `数据效率` `特征融合`

## 📋 核心要点

1. 核心问题：零样本组合图像检索中，现有方法难以有效弥合视觉与语言模态之间的鸿沟。
2. 方法要点：在联合视觉-语言空间引入多模态融合特征编辑策略，并采用轻量级Control-Adapter提升数据效率。
3. 实验或效果：在CIRR、FashionIQ和CIRCO基准上显著超越先前零样本方法，仅需20万合成样本微调。

## 📄 摘要（原文）

> Composed Image Retrieval (CIR) enables fine-grained visual search by combining a reference image with a textual modification. While supervised CIR methods achieve high accuracy, their reliance on costly triplet annotations motivates zero-shot solutions. The core challenge in zero-shot CIR (ZS-CIR) stems from a fundamental dilemma: existing text-centric or diffusion-based approaches struggle to effectively bridge the vision-language modality gap. To address this, we propose Fusion-Diff, a novel generative editing framework with high effectiveness and data efficiency designed for multimodal alignment. First, it introduces a multimodal fusion feature editing strategy within a joint vision-language (VL) space, substantially narrowing the modality gap. Second, to maximize data efficiency, the framework incorporates a lightweight Control-Adapter, enabling state-of-the-art performance through fine-tuning on only a limited-scale synthetic dataset of 200K samples. Extensive experiments on standard CIR benchmarks (CIRR, FashionIQ, and CIRCO) demonstrate that Fusion-Diff significantly outperforms prior zero-shot approaches. We further enhance the interpretability of our model by visualizing the fused multimodal representations.

