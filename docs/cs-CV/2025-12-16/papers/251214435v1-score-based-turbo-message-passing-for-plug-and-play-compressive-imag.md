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

**提出基于分数的Turbo消息传递算法，以解决压缩成像中传统去噪器表达能力不足的问题**

**关键词**: `压缩成像` `消息传递算法` `基于分数的生成模型` `即插即用方法` `图像去噪` `量化测量` `状态演化方程` `图像重建`

## 📋 核心要点

1. 核心问题：传统即插即用方法依赖表达能力有限的去噪器，在高度欠定压缩成像中重建效果不佳。
2. 方法要点：结合基于分数的生成先验与消息传递框架，设计STMP算法实现高效后验采样。
3. 实验或效果：STMP在FFHQ数据集上优于基线，Q-STMP在1比特量化下鲁棒，两者均快速收敛。

## 📝 摘要（中文）

消息传递算法通过集成现成的图像去噪器已应用于压缩成像，但这些去噪器主要依赖通用或手工设计的先验，往往难以准确捕捉自然图像的复杂统计结构，导致传统即插即用方法在高度欠定情况下重建效果不佳。最近，基于分数的生成模型成为准确表征复杂图像分布的强大框架，但其直接用于后验采样通常计算复杂度极高。本文通过利用基于分数的生成建模与经验贝叶斯去噪之间的紧密联系，设计了一个消息传递框架，该框架集成了基于分数的最小均方误差去噪器用于压缩图像恢复。所得算法称为基于分数的Turbo消息传递，结合了消息传递的快速收敛性和基于分数的生成先验的表达能力。对于具有量化测量的实际系统，我们进一步提出了量化STMP，它在STMP基础上增加了分量级MMSE去量化模块。我们证明STMP和Q-STMP的渐近性能可以通过一组状态演化方程准确预测。在FFHQ数据集上的实验表明，与竞争基线相比，STMP在性能与复杂度之间取得了显著更好的权衡，且Q-STMP即使在1比特量化下仍保持鲁棒性。值得注意的是，STMP和Q-STMP通常能在10次迭代内收敛。

## 🔬 方法详解

论文提出基于分数的Turbo消息传递框架，整体上是一个迭代式消息传递算法，用于压缩图像恢复。关键技术创新点在于：1) 利用基于分数的生成模型与经验贝叶斯去噪的关联，设计基于分数的最小均方误差去噪器，以更准确地建模图像先验；2) 引入Turbo消息传递机制，加速收敛并提高效率；3) 针对量化测量系统，扩展为Q-STMP，加入分量级MMSE去量化模块。与现有方法的主要区别在于：传统即插即用方法使用通用或手工去噪器，而STMP集成了基于分数的生成先验，能更好地捕捉图像复杂统计结构，同时避免了直接后验采样的高计算成本。

## 📊 实验亮点

在FFHQ数据集上，STMP相比基线方法在性能与复杂度权衡上显著更优；Q-STMP在1比特量化下仍保持鲁棒重建能力；两种算法均能在10次迭代内快速收敛，验证了高效性和实用性。

## 🎯 应用场景

该研究主要应用于压缩成像领域，如医学成像、遥感图像处理和低功耗视觉系统，通过高效恢复高质量图像，提升图像重建的准确性和鲁棒性，尤其在资源受限或量化测量场景中具有实际价值。

## 📄 摘要（原文）

> Message-passing algorithms have been adapted for compressive imaging by incorporating various off-the-shelf image denoisers. However, these denoisers rely largely on generic or hand-crafted priors and often fall short in accurately capturing the complex statistical structure of natural images. As a result, traditional plug-and-play (PnP) methods often lead to suboptimal reconstruction, especially in highly underdetermined regimes. Recently, score-based generative models have emerged as a powerful framework for accurately characterizing sophisticated image distribution. Yet, their direct use for posterior sampling typically incurs prohibitive computational complexity. In this paper, by exploiting the close connection between score-based generative modeling and empirical Bayes denoising, we devise a message-passing framework that integrates a score-based minimum mean-squared error (MMSE) denoiser for compressive image recovery. The resulting algorithm, named score-based turbo message passing (STMP), combines the fast convergence of message passing with the expressive power of score-based generative priors. For practical systems with quantized measurements, we further propose quantized STMP (Q-STMP), which augments STMP with a component-wise MMSE dequantization module. We demonstrate that the asymptotic performance of STMP and Q-STMP can be accurately predicted by a set of state-evolution (SE) equations. Experiments on the FFHQ dataset demonstrate that STMP strikes a significantly better performance-complexity tradeoff compared with competing baselines, and that Q-STMP remains robust even under 1-bit quantization. Remarkably, both STMP and Q-STMP typically converge within 10 iterations.

