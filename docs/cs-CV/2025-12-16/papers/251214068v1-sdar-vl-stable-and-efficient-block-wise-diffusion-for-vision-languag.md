---
layout: default
title: SDAR-VL: Stable and Efficient Block-wise Diffusion for Vision-Language Understanding
---

# SDAR-VL: Stable and Efficient Block-wise Diffusion for Vision-Language Understanding

**arXiv**: [2512.14068v1](https://arxiv.org/abs/2512.14068) | [PDF](https://arxiv.org/pdf/2512.14068.pdf)

**作者**: Shuang Cheng, Yuhua Jiang, Zineng Zhou, Dawei Liu, Wang Tao, Linfeng Zhang, Biqing Qi, Bowen Zhou

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出SDAR-VL框架，通过异步块噪声调度等技术解决块状离散扩散在视觉语言理解中的训练不稳定和效率低问题。**

**关键词**: `块状离散扩散` `视觉语言理解` `异步噪声调度` `掩码比率缩放` `噪声课程学习` `多模态建模` `训练稳定性` `高效训练`

## 📋 核心要点

1. 块状离散扩散在视觉语言理解中面临训练成本高、收敛慢和不稳定性，限制了其实际应用。
2. SDAR-VL通过异步块噪声调度、有效掩码比率缩放和渐进式Beta噪声课程，实现高效稳定训练。
3. 在21个基准测试中，SDAR-VL提升了训练效率、收敛稳定性和性能，达到或超越强基线。

## 📝 摘要（中文）

块状离散扩散在并行生成与因果依赖建模之间提供了有吸引力的平衡，使其成为视觉语言建模的有前景的骨干。然而，其实际应用受到高训练成本、收敛慢和不稳定性的限制，迄今仍落后于强大的自回归基线。我们提出了SDAR-VL，这是块状离散扩散在大规模视觉语言理解中的首次系统性应用，同时提供了一个高效稳定训练的综合框架。该框架统一了三个组件：(1) 异步块状噪声调度，以在每个批次内多样化监督；(2) 有效掩码比率缩放，用于在随机掩码下进行无偏损失归一化；(3) 渐进式Beta噪声课程，增加有效掩码覆盖率同时保持破坏多样性。在21个单图像、多图像和视频基准测试上的实验表明，SDAR-VL在训练效率、收敛稳定性和任务性能方面持续优于传统块扩散。在此评估套件中，SDAR-VL在基于扩散的视觉语言模型中设立了新的最先进水平，并在匹配设置下，达到或超越了如LLaVA-OneVision等强自回归基线以及全局扩散基线LLaDA-V，确立了块状扩散作为视觉语言理解的实用骨干。

## 🔬 方法详解

SDAR-VL是一个集成框架，将块状离散扩散应用于大规模视觉语言理解。整体框架包括三个关键技术创新：异步块状噪声调度，通过在不同块中应用不同噪声水平来多样化监督；有效掩码比率缩放，确保在随机掩码策略下损失计算的公平性；渐进式Beta噪声课程，逐步增加掩码覆盖率同时维持噪声多样性。与现有方法的主要区别在于，它系统性地解决了块扩散的训练不稳定和效率问题，而传统方法通常忽视这些优化，导致性能受限。

## 📊 实验亮点

在21个基准测试中，SDAR-VL在训练效率、收敛稳定性和任务性能上优于传统块扩散，达到基于扩散模型的新SOTA，并在匹配设置下匹配或超越LLaVA-OneVision等强基线。

## 🎯 应用场景

该研究可应用于视觉语言理解任务，如单图像描述、多图像推理和视频理解，提升模型在医疗影像分析、自动驾驶、智能助手等领域的实际性能，推动多模态AI的发展。

## 📄 摘要（原文）

> Block-wise discrete diffusion offers an attractive balance between parallel generation and causal dependency modeling, making it a promising backbone for vision-language modeling. However, its practical adoption has been limited by high training cost, slow convergence, and instability, which have so far kept it behind strong autoregressive (AR) baselines. We present \textbf{SDAR-VL}, the first systematic application of block-wise discrete diffusion to large-scale vision-language understanding (VLU), together with an \emph{integrated framework for efficient and stable training}. This framework unifies three components: (1) \textbf{Asynchronous Block-wise Noise Scheduling} to diversify supervision within each batch; (2) \textbf{Effective Mask Ratio Scaling} for unbiased loss normalization under stochastic masking; and (3) a \textbf{Progressive Beta Noise Curriculum} that increases effective mask coverage while preserving corruption diversity. Experiments on 21 single-image, multi-image, and video benchmarks show that SDAR-VL consistently improves \emph{training efficiency}, \emph{convergence stability}, and \emph{task performance} over conventional block diffusion. On this evaluation suite, SDAR-VL sets a new state of the art among diffusion-based vision-language models and, under matched settings, matches or surpasses strong AR baselines such as LLaVA-OneVision as well as the global diffusion baseline LLaDA-V, establishing block-wise diffusion as a practical backbone for VLU.

