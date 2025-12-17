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

**提出基于分数的Turbo消息传递算法，用于解决压缩成像中传统插拔式方法重建性能不足的问题。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `压缩成像` `消息传递算法` `基于分数的生成模型` `插拔式方法` `量化测量` `图像重建` `状态演化方程` `最小均方误差去噪`

## 📋 核心要点

1. 核心问题：传统插拔式压缩成像方法依赖通用先验，难以捕捉图像复杂统计结构，导致重建性能不佳，尤其在欠定场景下。
2. 方法要点：提出STMP算法，将基于分数的生成模型作为MMSE去噪器集成到消息传递框架中，结合快速收敛与强表达能力。
3. 实验或效果：在FFHQ数据集上，STMP显著优于基线，Q-STMP在1位量化下鲁棒，两者均在10次迭代内快速收敛。

## 📝 摘要（中文）

消息传递算法通过集成各种现成的图像去噪器，已被应用于压缩成像。然而，这些去噪器主要依赖于通用或手工设计的先验，往往难以准确捕捉自然图像的复杂统计结构。因此，传统的插拔式方法通常导致次优重建，特别是在高度欠定的情况下。最近，基于分数的生成模型已成为准确描述复杂图像分布的强大框架。然而，它们直接用于后验采样通常会产生过高的计算复杂度。本文通过利用基于分数的生成建模与经验贝叶斯去噪之间的紧密联系，设计了一个消息传递框架，该框架集成了基于分数的最小均方误差去噪器用于压缩图像恢复。所得算法称为基于分数的Turbo消息传递，结合了消息传递的快速收敛性和基于分数的生成先验的表达能力。对于具有量化测量的实际系统，我们进一步提出了量化STMP，它通过分量级MMSE去量化模块增强了STMP。我们证明STMP和Q-STMP的渐近性能可以通过一组状态演化方程准确预测。在FFHQ数据集上的实验表明，与竞争基线相比，STMP在性能与复杂度之间取得了显著更好的权衡，并且Q-STMP即使在1位量化下仍保持鲁棒性。值得注意的是，STMP和Q-STMP通常都在10次迭代内收敛。

## 🔬 方法详解

**问题定义**：论文解决压缩成像中的图像重建问题，特别是在高度欠定测量下。现有插拔式方法依赖通用或手工先验的去噪器，难以准确建模自然图像的复杂分布，导致重建质量下降，且计算复杂度高。

**核心思路**：通过利用基于分数的生成模型与经验贝叶斯去噪的紧密联系，将基于分数的MMSE去噪器嵌入消息传递框架，实现高效后验采样，从而提升重建性能并降低复杂度。

**技术框架**：整体框架包括STMP和Q-STMP两个版本。STMP基于Turbo消息传递，迭代执行线性估计和基于分数的去噪步骤；Q-STMP在STMP基础上增加分量级MMSE去量化模块，处理量化测量。状态演化方程用于理论性能预测。

**关键创新**：首次将基于分数的生成模型作为MMSE去噪器集成到消息传递中，实现快速收敛与强表达能力的结合；提出Q-STMP扩展以处理量化系统，增强实用性。

**关键设计**：使用基于分数的生成模型学习图像分布分数函数，作为MMSE去噪器；在消息传递中采用Turbo结构加速收敛；对于量化场景，设计分量级MMSE去量化模块；通过状态演化方程分析渐近性能，无需复杂采样。

## 📊 实验亮点

在FFHQ数据集实验中，STMP相比竞争基线（如传统PnP方法）在性能-复杂度权衡上显著更优，具体提升幅度未量化但强调“显著更好”。Q-STMP在1位量化下仍保持鲁棒重建能力，验证了其对实际系统的适应性。两者均展示快速收敛特性，通常在10次迭代内达到稳定，提高了计算效率。

## 🎯 应用场景

该研究在压缩成像领域具有广泛应用潜力，如医学成像、遥感、安全监控和低功耗物联网设备。通过提升欠定测量下的重建质量并支持量化系统，STMP和Q-STMP可降低数据采集成本、提高传输效率，推动高效图像处理技术的发展，未来可能扩展到视频重建和多模态成像等场景。

## 📄 摘要（原文）

> Message-passing algorithms have been adapted for compressive imaging by incorporating various off-the-shelf image denoisers. However, these denoisers rely largely on generic or hand-crafted priors and often fall short in accurately capturing the complex statistical structure of natural images. As a result, traditional plug-and-play (PnP) methods often lead to suboptimal reconstruction, especially in highly underdetermined regimes. Recently, score-based generative models have emerged as a powerful framework for accurately characterizing sophisticated image distribution. Yet, their direct use for posterior sampling typically incurs prohibitive computational complexity. In this paper, by exploiting the close connection between score-based generative modeling and empirical Bayes denoising, we devise a message-passing framework that integrates a score-based minimum mean-squared error (MMSE) denoiser for compressive image recovery. The resulting algorithm, named score-based turbo message passing (STMP), combines the fast convergence of message passing with the expressive power of score-based generative priors. For practical systems with quantized measurements, we further propose quantized STMP (Q-STMP), which augments STMP with a component-wise MMSE dequantization module. We demonstrate that the asymptotic performance of STMP and Q-STMP can be accurately predicted by a set of state-evolution (SE) equations. Experiments on the FFHQ dataset demonstrate that STMP strikes a significantly better performance-complexity tradeoff compared with competing baselines, and that Q-STMP remains robust even under 1-bit quantization. Remarkably, both STMP and Q-STMP typically converge within 10 iterations.

