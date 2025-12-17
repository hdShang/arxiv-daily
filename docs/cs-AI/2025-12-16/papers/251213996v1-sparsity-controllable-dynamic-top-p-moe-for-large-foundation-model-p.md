---
layout: default
title: Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training
---

# Sparsity-Controllable Dynamic Top-p MoE for Large Foundation Model Pre-training

**arXiv**: [2512.13996v1](https://arxiv.org/abs/2512.13996) | [PDF](https://arxiv.org/pdf/2512.13996.pdf)

**作者**: Can Jin, Hongwu Peng, Mingcan Xiang, Qixin Zhang, Xiangchi Yuan, Amit Hasan, Ohiremen Dibua, Yifan Gong, Yan Kang, Dimitris N. Metaxas

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出DTop-p MoE以解决稀疏专家混合模型中动态控制激活专家数量的问题**

**关键词**: `稀疏专家混合` `动态路由机制` `比例积分控制器` `大规模预训练` `模型扩展性` `计算成本控制` `自适应资源分配` `基础模型优化`

## 📋 核心要点

1. 现有Top-k路由采用统一稀疏模式，忽略令牌难度差异，而Top-p路由依赖固定阈值，导致计算成本不可控和超参数敏感。
2. 提出DTop-p MoE，使用PI控制器动态调整概率阈值以控制稀疏度，并引入动态路由归一化机制自适应调整层间路由逻辑。
3. 实验表明DTop-p在大型语言模型和扩散变换器中优于基线，能精确控制激活专家数量并自适应分配资源，具有强扩展性。

## 📝 摘要（中文）

稀疏专家混合（MoE）架构通过为每个输入令牌仅激活专家子集来有效扩展模型容量。然而，标准的Top-k路由策略采用统一的稀疏模式，忽略了令牌难度的变化。虽然Top-p路由提供了灵活的替代方案，但现有实现通常依赖于固定的全局概率阈值，这导致计算成本不可控且对超参数选择敏感。本文提出DTop-p MoE，一种稀疏可控的动态Top-p路由机制。为解决优化不可微分阈值的挑战，我们利用比例积分（PI）控制器动态调整概率阈值，使运行中的激活专家稀疏度与指定目标对齐。此外，我们引入动态路由归一化机制，自适应调整层间路由逻辑，允许不同层学习不同的专家选择模式，同时使用全局概率阈值。在大型语言模型和扩散变换器上的大量实验表明，DTop-p始终优于Top-k和固定阈值Top-p基线。我们的分析证实，DTop-p在精确控制激活专家数量的同时，自适应地在不同令牌和层间分配资源。此外，DTop-p在专家粒度、专家容量、模型大小和数据集大小方面表现出强大的扩展性，为大规模MoE预训练提供了稳健框架。

## 🔬 方法详解

DTop-p MoE的整体框架基于稀疏专家混合架构，核心创新点包括：1）使用比例积分（PI）控制器动态调整Top-p路由的概率阈值，通过反馈机制使激活专家稀疏度与目标值对齐，解决阈值不可微分优化问题；2）引入动态路由归一化机制，自适应调整不同层的路由逻辑，允许各层学习独特的专家选择模式，同时维持全局概率阈值。与现有方法的主要区别在于：Top-k路由强制统一激活专家数量，而DTop-p通过动态阈值实现稀疏可控；相比固定阈值Top-p，DTop-p能精确控制计算成本并减少超参数敏感性。

## 📊 实验亮点

在大型语言模型和扩散变换器实验中，DTop-p MoE一致优于Top-k和固定阈值Top-p基线，能精确控制激活专家数量，自适应分配资源，并在专家粒度、容量、模型大小和数据集大小方面展现出强扩展性。

## 🎯 应用场景

该研究适用于大规模基础模型预训练场景，如大型语言模型和扩散变换器的开发，能有效扩展模型容量并优化资源分配。潜在应用包括自然语言处理、图像生成和多模态AI系统，为构建高效、可扩展的AI模型提供技术支撑。

## 📄 摘要（原文）

> Sparse Mixture-of-Experts (MoE) architectures effectively scale model capacity by activating only a subset of experts for each input token. However, the standard Top-k routing strategy imposes a uniform sparsity pattern that ignores the varying difficulty of tokens. While Top-p routing offers a flexible alternative, existing implementations typically rely on a fixed global probability threshold, which results in uncontrolled computational costs and sensitivity to hyperparameter selection. In this paper, we propose DTop-p MoE, a sparsity-controllable dynamic Top-p routing mechanism. To resolve the challenge of optimizing a non-differentiable threshold, we utilize a Proportional-Integral (PI) Controller that dynamically adjusts the probability threshold to align the running activated-expert sparsity with a specified target. Furthermore, we introduce a dynamic routing normalization mechanism that adapts layer-wise routing logits, allowing different layers to learn distinct expert-selection patterns while utilizing a global probability threshold. Extensive experiments on Large Language Models and Diffusion Transformers demonstrate that DTop-p consistently outperforms both Top-k and fixed-threshold Top-p baselines. Our analysis confirms that DTop-p maintains precise control over the number of activated experts while adaptively allocating resources across different tokens and layers. Furthermore, DTop-p exhibits strong scaling properties with respect to expert granularity, expert capacity, model size, and dataset size, offering a robust framework for large-scale MoE pre-training.

