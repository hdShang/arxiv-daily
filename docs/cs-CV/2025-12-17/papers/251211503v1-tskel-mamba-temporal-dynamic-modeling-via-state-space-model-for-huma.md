---
layout: default
title: TSkel-Mamba: Temporal Dynamic Modeling via State Space Model for Human Skeleton-based Action Recognition
---

# TSkel-Mamba: Temporal Dynamic Modeling via State Space Model for Human Skeleton-based Action Recognition

**arXiv**: [2512.11503v1](https://arxiv.org/abs/2512.11503) | [PDF](https://arxiv.org/pdf/2512.11503.pdf)

**作者**: Yanan Liu, Jun Liu, Hao Zhang, Dan Xu, Hossein Rahmani, Mohammed Bennamoun, Qiuhong Ke

**分类**: cs.CV

**发布日期**: 2025-12-12

---

## 💡 一句话要点

**TSkel-Mamba：利用状态空间模型进行人体骨骼动作识别的时序动态建模**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `骨骼动作识别` `状态空间模型` `Mamba` `时间动态建模` `多尺度时间交互` `空间Transformer` `人体行为分析`

## 📋 核心要点

1. 现有基于骨骼的动作识别方法难以充分建模时序动态和通道间依赖关系。
2. TSkel-Mamba通过结合空间Transformer和Mamba，并引入TDM模块来增强时间建模能力。
3. 实验结果表明，TSkel-Mamba在多个数据集上取得了SOTA性能，并保持了较低的推理时间。

## 📝 摘要（中文）

本文提出了一种名为TSkel-Mamba的混合Transformer-Mamba框架，用于有效捕捉空间和时间动态，从而解决基于骨骼的动作识别问题。该方法利用空间Transformer进行空间特征学习，同时利用Mamba进行时间建模。针对Mamba在通道间依赖建模方面的局限性，本文引入了时间动态建模（TDM）模块，该模块是一个通用的即插即用组件，集成了新颖的多尺度时间交互（MTI）模块。MTI模块采用多尺度循环算子来捕获跨通道的时间交互，这对于动作识别至关重要。在NTU-RGB+D 60、NTU-RGB+D 120、NW-UCLA和UAV-Human数据集上的大量实验表明，TSkel-Mamba在保持低推理时间的同时，实现了最先进的性能，使其既高效又有效。

## 🔬 方法详解

**问题定义**：基于骨骼的动作识别旨在根据人体骨骼序列预测动作类别。现有方法，如基于RNN或Transformer的方法，在建模长时序依赖和通道间交互方面存在局限性。Mamba虽然在1D序列建模上表现出色，但其独立通道处理方式限制了其对骨骼数据通道间关系的建模能力。

**核心思路**：本文的核心思路是结合Transformer的空间特征提取能力和Mamba的时序建模能力，并针对Mamba的不足，引入TDM模块来增强其对通道间时序依赖的建模。通过多尺度时间交互（MTI）模块，模型能够捕获不同时间尺度下的通道间关系，从而更有效地进行动作识别。

**技术框架**：TSkel-Mamba框架主要包含三个部分：空间Transformer、Mamba模块和时间动态建模（TDM）模块。首先，空间Transformer用于提取每一帧骨骼的空间特征。然后，将提取的空间特征输入到Mamba模块中进行时序建模。最后，TDM模块被插入到Mamba模块中，用于增强通道间的时间交互建模能力。TDM模块包含一个MTI模块，该模块使用多尺度循环算子来捕获跨通道的时间交互。

**关键创新**：本文的关键创新在于提出了时间动态建模（TDM）模块，特别是其中的多尺度时间交互（MTI）模块。与传统的Mamba独立通道处理方式不同，MTI模块通过多尺度循环算子显式地建模了通道间的时间依赖关系，从而更好地适应了骨骼数据的特点。

**关键设计**：MTI模块的关键设计在于多尺度循环算子的使用。具体来说，MTI模块使用不同大小的循环核来捕获不同时间尺度下的通道间交互。此外，TDM模块作为一个即插即用组件，可以灵活地插入到Mamba模块的不同位置，从而方便地调整模型的结构。

## 📊 实验亮点

TSkel-Mamba在NTU-RGB+D 60、NTU-RGB+D 120、NW-UCLA和UAV-Human数据集上取得了state-of-the-art的性能。例如，在NTU-RGB+D 60数据集上，TSkel-Mamba的准确率达到了X%，相比于之前的最佳方法提升了Y%。同时，TSkel-Mamba保持了较低的推理时间，使其在实际应用中更具优势。

## 🎯 应用场景

TSkel-Mamba在人体动作识别领域具有广泛的应用前景，例如视频监控、人机交互、康复训练、运动分析等。该方法能够准确高效地识别各种人体动作，为相关应用提供可靠的技术支持，并有望推动相关领域的发展。

## 📄 摘要（原文）

> Skeleton-based action recognition has garnered significant attention in the computer vision community. Inspired by the recent success of the selective state-space model (SSM) Mamba in modeling 1D temporal sequences, we propose TSkel-Mamba, a hybrid Transformer-Mamba framework that effectively captures both spatial and temporal dynamics. In particular, our approach leverages Spatial Transformer for spatial feature learning while utilizing Mamba for temporal modeling. Mamba, however, employs separate SSM blocks for individual channels, which inherently limits its ability to model inter-channel dependencies. To better adapt Mamba for skeleton data and enhance Mamba`s ability to model temporal dependencies, we introduce a Temporal Dynamic Modeling (TDM) block, which is a versatile plug-and-play component that integrates a novel Multi-scale Temporal Interaction (MTI) module. The MTI module employs multi-scale Cycle operators to capture cross-channel temporal interactions, a critical factor in action recognition. Extensive experiments on NTU-RGB+D 60, NTU-RGB+D 120, NW-UCLA and UAV-Human datasets demonstrate that TSkel-Mamba achieves state-of-the-art performance while maintaining low inference time, making it both efficient and highly effective.

