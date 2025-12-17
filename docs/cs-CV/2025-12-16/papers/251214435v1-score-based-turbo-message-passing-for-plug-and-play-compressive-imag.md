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

**提出基于分数的Turbo消息传递算法，以解决压缩成像中传统插拔式方法重建性能不足的问题。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `压缩成像` `消息传递算法` `基于分数的生成模型` `插拔式方法` `图像去噪` `量化测量` `状态演化方程` `FFHQ数据集`

## 📋 核心要点

1. 核心问题：传统插拔式压缩成像方法依赖通用或手工先验，难以准确建模自然图像复杂统计结构，导致重建性能不足，尤其在高度欠定场景下。
2. 方法要点：提出基于分数的Turbo消息传递框架，整合基于分数的最小均方误差去噪器，结合消息传递快速收敛性和分数生成先验表达能力。
3. 实验或效果：在FFHQ数据集上，STMP显著优于基线方法，Q-STMP在1位量化下保持鲁棒，两者通常10次迭代内收敛，性能可预测。

## 📝 摘要（中文）

消息传递算法已通过整合各种现成图像去噪器应用于压缩成像。然而，这些去噪器主要依赖通用或手工先验，往往难以准确捕捉自然图像的复杂统计结构，导致传统插拔式方法在高度欠定情况下重建效果不佳。最近，基于分数的生成模型已成为准确表征复杂图像分布的强大框架，但其直接用于后验采样通常计算复杂度极高。本文通过利用基于分数的生成建模与经验贝叶斯去噪之间的紧密联系，设计了一个消息传递框架，整合基于分数的最小均方误差去噪器用于压缩图像恢复。所得算法称为基于分数的Turbo消息传递，结合了消息传递的快速收敛性和基于分数生成先验的表达能力。对于具有量化测量的实际系统，我们进一步提出量化STMP，通过分量级MMSE去量化模块增强STMP。我们证明STMP和Q-STMP的渐近性能可以通过一组状态演化方程准确预测。在FFHQ数据集上的实验表明，STMP在性能与复杂度权衡方面显著优于竞争基线，且Q-STMP即使在1位量化下仍保持鲁棒性。值得注意的是，STMP和Q-STMP通常能在10次迭代内收敛。

## 🔬 方法详解

整体框架是基于消息传递的压缩成像算法，核心创新点在于整合基于分数的生成模型作为先验，通过经验贝叶斯去噪连接，实现最小均方误差去噪。关键技术创新包括设计STMP算法，结合Turbo消息传递的快速迭代和分数模型的表达能力，以及针对量化测量扩展为Q-STMP，加入分量级MMSE去量化模块。与现有方法的主要区别在于：传统插拔式方法依赖通用去噪器，而STMP利用分数模型更准确捕捉图像分布；相比直接后验采样，STMP通过消息传递降低计算复杂度，实现高效重建。

## 📊 实验亮点

实验在FFHQ数据集上进行，STMP在性能-复杂度权衡上显著优于基线方法，Q-STMP在1位量化下保持鲁棒性，两者均能在10次迭代内快速收敛，且性能可通过状态演化方程准确预测，验证了方法的有效性和高效性。

## 🎯 应用场景

该研究主要应用于压缩成像领域，如医学成像、遥感图像处理和低功耗传感器系统，通过高效算法提升图像重建质量，尤其在资源受限或高压缩比场景下具有实际价值，可促进智能视觉系统的发展。

## 📄 摘要（原文）

> Message-passing algorithms have been adapted for compressive imaging by incorporating various off-the-shelf image denoisers. However, these denoisers rely largely on generic or hand-crafted priors and often fall short in accurately capturing the complex statistical structure of natural images. As a result, traditional plug-and-play (PnP) methods often lead to suboptimal reconstruction, especially in highly underdetermined regimes. Recently, score-based generative models have emerged as a powerful framework for accurately characterizing sophisticated image distribution. Yet, their direct use for posterior sampling typically incurs prohibitive computational complexity. In this paper, by exploiting the close connection between score-based generative modeling and empirical Bayes denoising, we devise a message-passing framework that integrates a score-based minimum mean-squared error (MMSE) denoiser for compressive image recovery. The resulting algorithm, named score-based turbo message passing (STMP), combines the fast convergence of message passing with the expressive power of score-based generative priors. For practical systems with quantized measurements, we further propose quantized STMP (Q-STMP), which augments STMP with a component-wise MMSE dequantization module. We demonstrate that the asymptotic performance of STMP and Q-STMP can be accurately predicted by a set of state-evolution (SE) equations. Experiments on the FFHQ dataset demonstrate that STMP strikes a significantly better performance-complexity tradeoff compared with competing baselines, and that Q-STMP remains robust even under 1-bit quantization. Remarkably, both STMP and Q-STMP typically converge within 10 iterations.

