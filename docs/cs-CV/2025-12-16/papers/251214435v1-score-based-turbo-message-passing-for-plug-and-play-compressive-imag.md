---
layout: default
title: Score-Based Turbo Message Passing for Plug-and-Play Compressive Imaging
---

# Score-Based Turbo Message Passing for Plug-and-Play Compressive Imaging

**arXiv**: [2512.14435v1](https://arxiv.org/abs/2512.14435) | [PDF](https://arxiv.org/pdf/2512.14435.pdf)

**作者**: Chang Cai, Hao Jiang, Xiaojun Yuan, Ying-Jun Angela Zhang

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于Score的Turbo消息传递算法STMP，用于即插即用压缩感知成像。**

🎯 **匹配领域**: **动作生成与物理动画 (Animation & Physics)**

**关键词**: `压缩感知成像` `即插即用` `Score-based生成模型` `消息传递算法` `最小均方误差` `量化测量` `状态演化`

## 📋 核心要点

1. 传统PnP方法在压缩感知成像中依赖手工先验，难以捕捉自然图像的复杂统计结构，导致重建效果不佳。
2. 利用Score-based生成模型与经验贝叶斯去噪的联系，设计了一种基于Score的MMSE去噪器，并融入消息传递框架。
3. 实验表明，STMP在性能和复杂度之间取得了平衡，Q-STMP在低比特量化下依然鲁棒，且收敛速度快。

## 📝 摘要（中文）

本文针对压缩感知成像问题，提出了一种基于Score的Turbo消息传递（STMP）算法。现有即插即用（PnP）方法依赖于通用或手工设计的先验，难以准确捕捉自然图像的复杂统计结构，导致重建效果欠佳，尤其是在高度欠定情况下。本文利用基于Score的生成模型与经验贝叶斯去噪之间的紧密联系，设计了一种消息传递框架，集成了基于Score的最小均方误差（MMSE）去噪器用于压缩图像恢复。对于量化测量系统，进一步提出了量化STMP（Q-STMP），通过组件式MMSE反量化模块增强STMP。状态演化（SE）方程可以准确预测STMP和Q-STMP的渐近性能。在FFHQ数据集上的实验表明，STMP在性能和复杂度之间取得了显著的平衡，Q-STMP在1比特量化下仍然保持鲁棒性。STMP和Q-STMP通常在10次迭代内收敛。

## 🔬 方法详解

**问题定义**：论文旨在解决压缩感知成像中，传统即插即用（PnP）方法由于依赖手工或通用先验，无法准确捕捉自然图像的复杂统计结构，导致重建效果在高度欠定情况下不佳的问题。现有方法难以在性能和计算复杂度之间取得平衡，并且在量化测量场景下表现不佳。

**核心思路**：论文的核心思路是将近年来表现出色的基于Score的生成模型（Score-based generative models）融入到消息传递框架中，利用其强大的图像先验表达能力，提升压缩感知成像的重建质量。同时，通过与经验贝叶斯去噪的联系，设计高效的基于Score的MMSE去噪器，降低计算复杂度。

**技术框架**：STMP算法的整体框架是一个消息传递算法，其中核心模块是基于Score的MMSE去噪器。算法迭代地更新图像的估计值和辅助变量，并在每次迭代中使用Score-based MMSE去噪器对图像估计进行去噪。对于量化测量，Q-STMP在STMP的基础上增加了一个组件式的MMSE反量化模块，用于处理量化后的测量值。此外，论文还推导了状态演化（SE）方程，用于预测STMP和Q-STMP的渐近性能。

**关键创新**：论文的关键创新在于将Score-based生成模型与消息传递算法相结合，提出了一种新的压缩感知成像算法STMP。与传统PnP方法相比，STMP利用Score-based生成模型学习到的图像先验，能够更准确地捕捉自然图像的复杂统计结构，从而提升重建质量。此外，Q-STMP通过引入组件式MMSE反量化模块，实现了在量化测量下的鲁棒重建。

**关键设计**：STMP算法的关键设计包括：1) 基于Score的MMSE去噪器的具体实现，可能涉及到求解一个微分方程或使用预训练的Score网络；2) 消息传递算法的具体更新规则，需要仔细设计以保证算法的收敛性和性能；3) Q-STMP中组件式MMSE反量化模块的设计，需要考虑量化噪声的统计特性；4) 状态演化方程的推导，需要对算法的渐近行为进行精确分析。

## 📊 实验亮点

实验结果表明，STMP算法在FFHQ数据集上取得了显著的性能提升，在性能和复杂度之间取得了更好的平衡。Q-STMP算法在1比特量化下仍然保持了良好的重建性能，展示了其在极端量化条件下的鲁棒性。值得注意的是，STMP和Q-STMP算法通常在10次迭代内即可收敛，表明其具有较高的计算效率。

## 🎯 应用场景

该研究成果可应用于医学成像、遥感成像、安防监控等领域，尤其是在带宽受限或需要低功耗采集的场景下，具有重要的应用价值。通过压缩感知技术，可以在减少数据采集量的同时，保证图像的重建质量，从而降低硬件成本和传输压力。未来，该方法有望推广到其他逆问题求解领域。

## 📄 摘要（原文）

> Message-passing algorithms have been adapted for compressive imaging by incorporating various off-the-shelf image denoisers. However, these denoisers rely largely on generic or hand-crafted priors and often fall short in accurately capturing the complex statistical structure of natural images. As a result, traditional plug-and-play (PnP) methods often lead to suboptimal reconstruction, especially in highly underdetermined regimes. Recently, score-based generative models have emerged as a powerful framework for accurately characterizing sophisticated image distribution. Yet, their direct use for posterior sampling typically incurs prohibitive computational complexity. In this paper, by exploiting the close connection between score-based generative modeling and empirical Bayes denoising, we devise a message-passing framework that integrates a score-based minimum mean-squared error (MMSE) denoiser for compressive image recovery. The resulting algorithm, named score-based turbo message passing (STMP), combines the fast convergence of message passing with the expressive power of score-based generative priors. For practical systems with quantized measurements, we further propose quantized STMP (Q-STMP), which augments STMP with a component-wise MMSE dequantization module. We demonstrate that the asymptotic performance of STMP and Q-STMP can be accurately predicted by a set of state-evolution (SE) equations. Experiments on the FFHQ dataset demonstrate that STMP strikes a significantly better performance-complexity tradeoff compared with competing baselines, and that Q-STMP remains robust even under 1-bit quantization. Remarkably, both STMP and Q-STMP typically converge within 10 iterations.

