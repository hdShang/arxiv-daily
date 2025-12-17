---
layout: default
title: Recurrent Video Masked Autoencoders
---

# Recurrent Video Masked Autoencoders

**arXiv**: [2512.13684v1](https://arxiv.org/abs/2512.13684) | [PDF](https://arxiv.org/pdf/2512.13684.pdf)

**作者**: Daniel Zoran, Nikhil Parthasarathy, Yi Yang, Drew A Hudson, Joao Carreira, Andrew Zisserman

---

## 💡 一句话要点

**提出循环视频掩码自编码器，通过循环聚合图像特征高效学习视频时空表示。**

**关键词**: `视频表示学习` `循环神经网络` `掩码自编码器` `时空建模` `参数效率` `长视频理解`

## 📋 核心要点

1. 核心问题：视频表示学习需高效捕获时空结构，传统方法计算成本高或依赖复杂目标。
2. 方法要点：使用基于Transformer的循环神经网络，通过非对称掩码预测任务学习，仅需像素重建目标。
3. 实验或效果：在动作识别等任务上媲美先进视频模型，参数效率提升高达30倍，支持长时稳定特征传播。

## 📄 摘要（原文）

> We present Recurrent Video Masked-Autoencoders (RVM): a novel video representation learning approach that uses a transformer-based recurrent neural network to aggregate dense image features over time, effectively capturing the spatio-temporal structure of natural video data. RVM learns via an asymmetric masked prediction task requiring only a standard pixel reconstruction objective. This design yields a highly efficient ``generalist'' encoder: RVM achieves competitive performance with state-of-the-art video models (e.g. VideoMAE, V-JEPA) on video-level tasks like action recognition and point/object tracking, while also performing favorably against image models (e.g. DINOv2) on tasks that test geometric and dense spatial understanding. Notably, RVM achieves strong performance in the small-model regime without requiring knowledge distillation, exhibiting up to 30x greater parameter efficiency than competing video masked autoencoders. Moreover, we demonstrate that RVM's recurrent nature allows for stable feature propagation over long temporal horizons with linear computational cost, overcoming some of the limitations of standard spatio-temporal attention-based architectures. Finally, we use qualitative visualizations to highlight that RVM learns rich representations of scene semantics, structure, and motion.

