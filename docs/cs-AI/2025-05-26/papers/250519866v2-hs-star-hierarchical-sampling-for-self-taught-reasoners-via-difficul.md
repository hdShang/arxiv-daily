---
layout: default
title: "HS-STaR: Hierarchical Sampling for Self-Taught Reasoners via Difficulty Estimation and Budget Reallocation"
---

# HS-STaR: Hierarchical Sampling for Self-Taught Reasoners via Difficulty Estimation and Budget Reallocation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19866" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19866v2</a>
  <a href="https://arxiv.org/pdf/2505.19866.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19866v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19866v2', 'HS-STaR: Hierarchical Sampling for Self-Taught Reasoners via Difficulty Estimation and Budget Reallocation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feng Xiong, Hongling Xu, Yifei Wang, Runxi Cheng, Yong Wang, Xiangxiang Chu

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-05-26 (更新: 2025-09-28)

---

## 💡 一句话要点

**提出HS-STaR以优化自学推理者的样本选择**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自学推理者` `层次化采样` `难度估计` `预算重新分配` `大型语言模型` `数学推理` `训练数据优化`

## 📋 核心要点

1. 现有方法在样本选择上均匀分配预算，未能充分利用不同难度问题的学习效用，导致训练效率低下。
2. HS-STaR通过奖励引导的难度估计策略，优先识别和利用接近模型推理能力边界的问题，从而提高训练数据的质量。
3. 在多个推理基准上，HS-STaR显著提升了模型的推理能力，相较于其他基线方法，性能提升明显且无需额外预算。

## 📝 摘要（中文）

自学推理者（STaRs）通过利用自生成的响应来增强大型语言模型（LLMs）的数学推理能力。现有研究通常在所有问题上均匀分配采样预算，忽视了不同难度级别问题的效用差异。本文提出HS-STaR，一个层次化采样框架，首先通过奖励引导的难度估计策略进行轻量级预采样，以识别边界级问题，然后在重新采样阶段动态重新分配预算，最大化高效训练数据的生成。实验表明，HS-STaR在多个推理基准和基础LLMs上显著优于其他基线，且无需额外的采样预算。

## 🔬 方法详解

**问题定义**：本文旨在解决自学推理者在样本选择时的预算分配问题，现有方法未能考虑不同难度问题的效用差异，导致训练效果不佳。

**核心思路**：HS-STaR的核心思想是通过层次化采样策略，优先选择那些接近模型推理能力边界的问题，以最大化学习效用。这样的设计能够更有效地利用有限的采样预算。

**技术框架**：HS-STaR的整体架构包括两个主要阶段：首先是轻量级预采样阶段，通过奖励引导的难度估计策略识别边界级问题；其次是重新采样阶段，动态调整预算，集中在高效问题上。

**关键创新**：HS-STaR的创新在于引入了难度估计和预算重新分配机制，使得模型能够在不同难度问题上进行更有针对性的学习，这与传统的均匀采样方法有本质区别。

**关键设计**：在技术细节上，HS-STaR使用了奖励模型来评估问题的难度，并根据预设的预算动态调整采样策略，确保高效利用每一份训练资源。具体的参数设置和损失函数设计在实验中经过优化。

## 📊 实验亮点

实验结果显示，HS-STaR在多个推理基准上显著优于其他基线方法，具体表现为在某些任务上性能提升超过20%。此外，HS-STaR在不增加额外采样预算的情况下，成功提高了训练数据的质量和模型的推理能力。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和自动化问题生成等。通过优化样本选择，HS-STaR能够在这些领域中提升模型的推理能力和学习效率，进而推动个性化学习和智能教育的发展。

## 📄 摘要（原文）

> Self-taught reasoners (STaRs) enhance the mathematical reasoning abilities of large language models (LLMs) by leveraging self-generated responses for self-training. Recent studies have incorporated reward models to guide response selection or decoding, aiming to obtain higher-quality data. However, they typically allocate a uniform sampling budget across all problems, overlooking the varying utility of problems at different difficulty levels. In this work, we conduct an empirical study and find that problems near the boundary of the LLM's reasoning capability offer significantly greater learning utility than both easy and overly difficult ones. To identify and exploit such problems, we propose HS-STaR, a Hierarchical Sampling framework for Self-Taught Reasoners. Given a fixed sampling budget, HS-STaR first performs lightweight pre-sampling with a reward-guided difficulty estimation strategy to efficiently identify boundary-level problems. Subsequently, it dynamically reallocates the remaining budget toward these high-utility problems during a re-sampling phase, maximizing the generation of valuable training data. Extensive experiments across multiple reasoning benchmarks and backbone LLMs demonstrate that HS-STaR significantly outperforms other baselines without requiring additional sampling budget.

