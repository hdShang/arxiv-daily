---
layout: default
title: Denoise to Track: Harnessing Video Diffusion Priors for Robust Correspondence
---

# Denoise to Track: Harnessing Video Diffusion Priors for Robust Correspondence

**arXiv**: [2512.04619v1](https://arxiv.org/abs/2512.04619) | [PDF](https://arxiv.org/pdf/2512.04619.pdf)

**作者**: Tianyu Yuan, Yuanbo Yang, Lin-Zhuo Chen, Yao Yao, Zhuzhong Qian

**分类**: cs.CV

**发布日期**: 2025-12-04

---

## 💡 一句话要点

**提出HeFT，利用视频扩散先验实现鲁棒的零样本点跟踪**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `零样本学习` `点跟踪` `视频扩散模型` `视觉先验` `注意力机制`

## 📋 核心要点

1. 现有方法在零样本点跟踪中面临挑战，缺乏对视频时空信息的有效利用。
2. HeFT利用预训练视频扩散模型的视觉先验，通过分析VDiT的内部表示，实现更鲁棒的跟踪。
3. 实验表明，HeFT在TAP-Vid基准上取得了最先进的零样本跟踪性能，接近监督方法。

## 📝 摘要（中文）

本文提出了一种名为HeFT（Head-Frequency Tracker）的零样本点跟踪框架，该框架利用了预训练视频扩散模型的视觉先验。为了更好地理解视频扩散Transformer（VDiT）如何编码时空信息，我们分析了其内部表示。分析表明，注意力头作为最小功能单元，在匹配、语义理解和位置编码方面具有不同的专业化分工。此外，我们发现VDiT特征中的低频分量对于建立对应关系至关重要，而高频分量往往会引入噪声。基于这些发现，我们提出了一种头和频率感知的特征选择策略，该策略联合选择信息量最大的注意力头和低频分量，以提高跟踪性能。具体而言，我们的方法通过单步去噪提取判别性特征，应用特征选择，并采用具有前后一致性检查的软argmax定位进行对应关系估计。在TAP-Vid基准上的大量实验表明，HeFT实现了最先进的零样本跟踪性能，接近于监督方法的准确性，同时消除了对带注释训练数据的需求。我们的工作进一步强调了视频扩散模型作为强大基础模型在各种下游任务中的潜力，为统一的视觉基础模型铺平了道路。

## 🔬 方法详解

**问题定义**：论文旨在解决零样本点跟踪问题，即在没有标注数据的情况下，如何准确地跟踪视频中的特定点。现有方法通常依赖于手工设计的特征或在特定数据集上训练的模型，泛化能力有限，且难以有效利用视频的时空信息。

**核心思路**：论文的核心思路是利用预训练视频扩散模型（如VDiT）中蕴含的丰富视觉先验知识。通过分析VDiT的内部表示，发现不同注意力头和频率分量在时空信息编码中的作用，并选择最适合跟踪的特征。这种方法避免了对标注数据的依赖，提高了模型的泛化能力。

**技术框架**：HeFT框架主要包含三个阶段：1) 特征提取：通过单步去噪过程从VDiT中提取特征。2) 特征选择：采用头和频率感知的策略，选择信息量最大的注意力头和低频分量。3) 对应关系估计：使用软argmax定位和前后一致性检查来估计对应关系。

**关键创新**：论文的关键创新在于提出了头和频率感知的特征选择策略。通过分析VDiT的内部表示，发现不同注意力头和频率分量在时空信息编码中的作用，并选择最适合跟踪的特征。这种策略能够有效地去除噪声，提高跟踪的准确性。

**关键设计**：论文的关键设计包括：1) 使用单步去噪提取特征，减少计算量。2) 设计头和频率感知的特征选择策略，选择信息量最大的特征。3) 采用软argmax定位和前后一致性检查，提高对应关系估计的准确性。

## 📊 实验亮点

HeFT在TAP-Vid基准测试中取得了显著成果，实现了最先进的零样本跟踪性能，并且性能接近有监督方法。这表明了预训练视频扩散模型在下游任务中的巨大潜力，并为未来的研究方向提供了新的思路。

## 🎯 应用场景

该研究成果可应用于视频监控、自动驾驶、机器人导航等领域，实现对视频中特定目标的精确跟踪。通过利用预训练模型的视觉先验，可以降低对标注数据的依赖，提高跟踪系统的鲁棒性和泛化能力，为更广泛的视觉任务提供基础支持。

## 📄 摘要（原文）

> In this work, we introduce HeFT (Head-Frequency Tracker), a zero-shot point tracking framework that leverages the visual priors of pretrained video diffusion models. To better understand how they encode spatiotemporal information, we analyze the internal representations of Video Diffusion Transformer (VDiT). Our analysis reveals that attention heads act as minimal functional units with distinct specializations for matching, semantic understanding, and positional encoding. Additionally, we find that the low-frequency components in VDiT features are crucial for establishing correspondences, whereas the high-frequency components tend to introduce noise. Building on these insights, we propose a head- and frequency-aware feature selection strategy that jointly selects the most informative attention head and low-frequency components to enhance tracking performance. Specifically, our method extracts discriminative features through single-step denoising, applies feature selection, and employs soft-argmax localization with forward-backward consistency checks for correspondence estimation. Extensive experiments on TAP-Vid benchmarks demonstrate that HeFT achieves state-of-the-art zero-shot tracking performance, approaching the accuracy of supervised methods while eliminating the need for annotated training data. Our work further underscores the promise of video diffusion models as powerful foundation models for a wide range of downstream tasks, paving the way toward unified visual foundation models.

