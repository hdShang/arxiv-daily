---
layout: default
title: LeCoT: revisiting network architecture for two-view correspondence pruning
---

# LeCoT: revisiting network architecture for two-view correspondence pruning

**arXiv**: [2511.07078v1](https://arxiv.org/abs/2511.07078) | [PDF](https://arxiv.org/pdf/2511.07078.pdf)

**作者**: Luanyuan Dai, Xiaoyu Du, Jinhui Tang

---

## 💡 一句话要点

**提出LeCoT网络以改进双视图对应点修剪，利用全局上下文信息。**

**关键词**: `双视图对应点修剪` `全局上下文信息` `Transformer块` `计算机视觉任务` `概率集优化`

## 📋 核心要点

1. 核心问题：MLP在双视图对应点修剪中处理上下文信息能力有限，需额外模块增强。
2. 方法要点：设计Spatial-Channel Fusion Transformer块，融合空间和通道全局上下文信息。
3. 实验效果：在多个任务中优于现有方法，包括对应点修剪和3D重建。

## 📄 摘要（原文）

> Two-view correspondence pruning aims to accurately remove incorrect
> correspondences (outliers) from initial ones and is widely applied to various
> computer vision tasks. Current popular strategies adopt multilayer perceptron
> (MLP) as the backbone, supplemented by additional modules to enhance the
> network ability to handle context information, which is a known limitation of
> MLPs. In contrast, we introduce a novel perspective for capturing
> correspondence context information without extra design modules. To this end,
> we design a two-view correspondence pruning network called LeCoT, which can
> naturally leverage global context information at different stages.
> Specifically, the core design of LeCoT is the Spatial-Channel Fusion
> Transformer block, a newly proposed component that efficiently utilizes both
> spatial and channel global context information among sparse correspondences. In
> addition, we integrate the proposed prediction block that utilizes
> correspondence features from intermediate stages to generate a probability set,
> which acts as guiding information for subsequent learning phases, allowing the
> network to more effectively capture robust global context information. Notably,
> this prediction block progressively refines the probability set, thereby
> mitigating the issue of information loss that is common in the traditional one.
> Extensive experiments prove that the proposed LeCoT outperforms
> state-of-the-art methods in correspondence pruning, relative pose estimation,
> homography estimation, visual localization, and $3$D~reconstruction tasks. The
> code is provided in
> https://github.com/Dailuanyuan2024/LeCoT-Revisiting-Network-Architecture-for-Two-View-Correspondence-Pruning.

