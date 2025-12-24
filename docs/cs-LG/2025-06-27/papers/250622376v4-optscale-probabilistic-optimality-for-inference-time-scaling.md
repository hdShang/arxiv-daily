---
layout: default
title: "OptScale: Probabilistic Optimality for Inference-time Scaling"
---

# OptScale: Probabilistic Optimality for Inference-time Scaling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22376" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22376v4</a>
  <a href="https://arxiv.org/pdf/2506.22376.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22376v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22376v4', 'OptScale: Probabilistic Optimality for Inference-time Scaling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youkang Wang, Jian Wang, Rubing Chen, Xiao-Yong Wei

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-27 (更新: 2025-12-19)

**备注**: Accepted by AAAI-2026

---

## 💡 一句话要点

**提出OptScale以解决推理时间缩放的效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理时间缩放` `概率框架` `大型语言模型` `样本选择` `计算效率` `复杂推理` `性能评估`

## 📋 核心要点

1. 现有推理时间缩放方法多依赖启发式策略，缺乏系统性的理论支持，导致效率低下。
2. 本文提出了一种概率框架，形式化推理时间缩放的最优性，并推导出样本数量的理论下界。
3. 实验结果表明，OptScale在多个推理基准上显著降低了采样开销，同时保持或提升了推理性能。

## 📝 摘要（中文）

推理时间缩放已成为提升大型语言模型（LLMs）推理性能的重要技术。然而，现有方法往往依赖于启发式策略进行并行采样，缺乏系统性的理论基础。为此，本文提出了一种概率框架，形式化推理时间缩放的最优性，假设并行样本是独立同分布的，并且Best-of-$N$选择策略遵循可估计的概率分布。在此框架下，我们推导出实现目标性能水平所需样本数量的理论下界，为计算高效的缩放提供了首个系统性指导。基于这一洞察，我们开发了OptScale算法，动态确定最优采样响应数量。OptScale利用语言模型预测器估计概率先验参数，从而决定满足预定义性能阈值和置信水平所需的最小样本数量。大量实验表明，OptScale显著减少了采样开销，同时在推理性能上与最先进的方法相当或更优。我们的工作为推理时间缩放提供了理论基础和实际解决方案，填补了LLMs在复杂推理应用中的关键空白。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推理时间缩放方法缺乏理论基础和效率低下的问题。现有方法往往依赖启发式策略，导致在复杂推理任务中表现不佳。

**核心思路**：我们提出了一种概率框架，假设并行样本是独立同分布的，并推导出实现目标性能所需的样本数量的理论下界。这一框架为计算高效的推理时间缩放提供了系统性指导。

**技术框架**：整体架构包括一个语言模型预测器，用于估计概率先验参数，并根据这些参数动态确定最优的样本数量。该框架的主要模块包括样本生成、性能评估和最优选择。

**关键创新**：最重要的创新在于首次提出了基于概率的推理时间缩放理论，提供了样本数量的理论下界，与现有方法的启发式策略形成鲜明对比。

**关键设计**：在参数设置上，OptScale通过语言模型预测器估计先验参数，并设定性能阈值和置信水平，以确保所需样本数量的最小化。

## 📊 实验亮点

在多个推理基准（如MATH-500、GSM8K、AIME和AMC）上的实验结果显示，OptScale在减少采样开销的同时，推理性能与最先进的方法相当或更优，展现出显著的效率提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的复杂推理任务，如数学问题求解、逻辑推理和对话系统等。通过提供高效的推理时间缩放方案，OptScale能够在实际应用中显著提升大型语言模型的推理能力，降低计算成本，推动智能系统的广泛应用。

## 📄 摘要（原文）

> Inference-time scaling has emerged as a powerful technique for enhancing the reasoning performance of Large Language Models (LLMs). However, existing approaches often rely on heuristic strategies for parallel sampling, lacking a principled foundation. To address this gap, we propose a probabilistic framework that formalizes the optimality of inference-time scaling under the assumption that parallel samples are independently and identically distributed (i.i.d.), and where the Best-of-$N$ selection strategy follows a probability distribution that can be estimated. Within this framework, we derive a theoretical lower bound on the required number of samples to achieve a target performance level, providing the first principled guidance for compute-efficient scaling. Leveraging this insight, we develop \textsc{OptScale}, a practical algorithm that dynamically determines the optimal number of sampled responses. \textsc{OptScale} employs a language model-based predictor to estimate probabilistic prior parameters, enabling the decision of the minimal number of samples needed that satisfy predefined performance thresholds and confidence levels. Extensive experiments on representative reasoning benchmarks (including MATH-500, GSM8K, AIME, and AMC) demonstrate that \textsc{OptScale} significantly reduces sampling overhead while remaining better or on par with state-of-the-art reasoning performance. Our work offers both a theoretical foundation and a practical solution for principled inference-time scaling, addressing a critical gap in the efficient deployment of LLMs for complex reasoning.

