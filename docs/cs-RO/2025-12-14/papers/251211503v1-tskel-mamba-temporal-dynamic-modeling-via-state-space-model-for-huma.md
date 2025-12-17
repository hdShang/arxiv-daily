---
layout: default
title: TSkel-Mamba: Temporal Dynamic Modeling via State Space Model for Human Skeleton-based Action Recognition
---

# TSkel-Mamba: Temporal Dynamic Modeling via State Space Model for Human Skeleton-based Action Recognition

**arXiv**: [2512.11503v1](https://arxiv.org/abs/2512.11503) | [PDF](https://arxiv.org/pdf/2512.11503.pdf)

**作者**: Yanan Liu, Jun Liu, Hao Zhang, Dan Xu, Hossein Rahmani, Mohammed Bennamoun, Qiuhong Ke

---

## 💡 一句话要点

**提出TSkel-Mamba框架，通过状态空间模型增强骨架动作识别中的时空动态建模。**

**关键词**: `骨架动作识别` `状态空间模型` `时空建模` `Transformer-Mamba混合框架` `多尺度时间交互`

## 📋 核心要点

1. 核心问题：Mamba在骨架动作识别中建模通道间依赖能力有限，影响时间动态捕捉。
2. 方法要点：结合Transformer处理空间特征，引入TDM块和MTI模块以多尺度循环算子增强跨通道时间交互。
3. 实验或效果：在多个数据集上实现最优性能，同时保持低推理时间，高效有效。

## 📄 摘要（原文）

> Skeleton-based action recognition has garnered significant attention in the computer vision community. Inspired by the recent success of the selective state-space model (SSM) Mamba in modeling 1D temporal sequences, we propose TSkel-Mamba, a hybrid Transformer-Mamba framework that effectively captures both spatial and temporal dynamics. In particular, our approach leverages Spatial Transformer for spatial feature learning while utilizing Mamba for temporal modeling. Mamba, however, employs separate SSM blocks for individual channels, which inherently limits its ability to model inter-channel dependencies. To better adapt Mamba for skeleton data and enhance Mamba`s ability to model temporal dependencies, we introduce a Temporal Dynamic Modeling (TDM) block, which is a versatile plug-and-play component that integrates a novel Multi-scale Temporal Interaction (MTI) module. The MTI module employs multi-scale Cycle operators to capture cross-channel temporal interactions, a critical factor in action recognition. Extensive experiments on NTU-RGB+D 60, NTU-RGB+D 120, NW-UCLA and UAV-Human datasets demonstrate that TSkel-Mamba achieves state-of-the-art performance while maintaining low inference time, making it both efficient and highly effective.

