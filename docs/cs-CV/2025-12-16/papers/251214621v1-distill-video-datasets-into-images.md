---
layout: default
title: Distill Video Datasets into Images
---

# Distill Video Datasets into Images

**arXiv**: [2512.14621v1](https://arxiv.org/abs/2512.14621) | [PDF](https://arxiv.org/pdf/2512.14621.pdf)

**作者**: Zhenghao Zhao, Haoxuan Wang, Kai Wang, Yuzhang Shang, Yuan Hong, Yan Yan

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出单帧视频集蒸馏框架以解决视频数据集蒸馏中参数激增和优化困难的问题。**

**关键词**: `视频数据集蒸馏` `单帧蒸馏` `可微分插值` `通道重塑` `优化效率` `动作识别` `视频分类` `计算成本降低`

## 📋 核心要点

1. 视频数据集蒸馏面临时间维度导致参数激增，优化复杂且收敛困难。
2. 提出SFVD框架，将视频蒸馏为单帧，通过可微分插值和通道重塑整合时间信息。
3. 在MiniUCF等基准上显著超越现有方法，性能提升最高达5.3%。

## 📝 摘要（中文）

数据集蒸馏旨在合成紧凑而信息丰富的数据集，使在其上训练的模型能达到与在全数据集上训练相当的性能。虽然该方法在图像数据上已显示出有希望的结果，但将数据集蒸馏方法扩展到视频数据已被证明具有挑战性，并且通常导致次优性能。在这项工作中，我们首先将视频集蒸馏的核心挑战确定为视频时间维度引入的可学习参数大幅增加，这使优化复杂化并阻碍收敛。为解决此问题，我们观察到单个帧通常足以捕捉视频的判别性语义。利用这一见解，我们提出了单帧视频集蒸馏（SFVD），这是一个将视频蒸馏为每个类别高度信息丰富的帧的框架。使用可微分插值，这些帧被转换为视频序列并与原始数据集匹配，同时更新仅限于帧本身以提高优化效率。为了进一步整合时间信息，在匹配过程中通过通道重塑层将蒸馏帧与从真实视频中采样的真实视频结合。在多个基准上的广泛实验表明，SFVD显著优于先前方法，在MiniUCF上实现了高达5.3%的改进，从而提供了更有效的解决方案。

## 🔬 方法详解

SFVD框架的核心是将视频数据集蒸馏为每个类别的代表性单帧。整体框架包括：首先，为每个类别合成高度信息丰富的单帧作为蒸馏核心；其次，通过可微分插值技术将这些单帧扩展为视频序列，以模拟原始视频的时间动态；第三，在匹配过程中，通过通道重塑层将蒸馏帧与采样的真实视频结合，以整合额外的时间信息。关键技术创新在于将优化限制在单帧上，大幅减少可学习参数，从而简化优化过程并提高效率。与现有方法的主要区别在于避免了直接处理高维视频序列的复杂性，而是通过单帧蒸馏和插值策略有效捕捉视频的判别性语义，同时通过通道重塑引入时间上下文，实现更优的性能。

## 📊 实验亮点

在MiniUCF基准上，SFVD实现了高达5.3%的性能提升，显著优于先前视频数据集蒸馏方法，验证了单帧蒸馏框架的有效性和优化效率。

## 🎯 应用场景

该研究在视频理解、动作识别和视频分类等领域具有潜在应用价值，能显著降低视频数据存储和计算成本，加速模型训练，适用于资源受限环境如边缘设备或大规模视频分析系统。

## 📄 摘要（原文）

> Dataset distillation aims to synthesize compact yet informative datasets that allow models trained on them to achieve performance comparable to training on the full dataset. While this approach has shown promising results for image data, extending dataset distillation methods to video data has proven challenging and often leads to suboptimal performance. In this work, we first identify the core challenge in video set distillation as the substantial increase in learnable parameters introduced by the temporal dimension of video, which complicates optimization and hinders convergence. To address this issue, we observe that a single frame is often sufficient to capture the discriminative semantics of a video. Leveraging this insight, we propose Single-Frame Video set Distillation (SFVD), a framework that distills videos into highly informative frames for each class. Using differentiable interpolation, these frames are transformed into video sequences and matched with the original dataset, while updates are restricted to the frames themselves for improved optimization efficiency. To further incorporate temporal information, the distilled frames are combined with sampled real videos from real videos during the matching process through a channel reshaping layer. Extensive experiments on multiple benchmarks demonstrate that SFVD substantially outperforms prior methods, achieving improvements of up to 5.3% on MiniUCF, thereby offering a more effective solution.

