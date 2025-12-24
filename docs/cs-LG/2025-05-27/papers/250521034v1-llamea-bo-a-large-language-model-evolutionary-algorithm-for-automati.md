---
layout: default
title: LLaMEA-BO: A Large Language Model Evolutionary Algorithm for Automatically Generating Bayesian Optimization Algorithms
---

# LLaMEA-BO: A Large Language Model Evolutionary Algorithm for Automatically Generating Bayesian Optimization Algorithms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21034" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21034v1</a>
  <a href="https://arxiv.org/pdf/2505.21034.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21034v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21034v1', 'LLaMEA-BO: A Large Language Model Evolutionary Algorithm for Automatically Generating Bayesian Optimization Algorithms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhu Li, Niki van Stein, Thomas Bäck, Elena Raponi

**分类**: cs.LG, cs.NE

**发布日期**: 2025-05-27

**🔗 代码/项目**: [GITHUB](https://github.com/Ewendawi/LLaMEA-BO)

---

## 💡 一句话要点

**提出LLaMEA-BO以自动生成贝叶斯优化算法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `贝叶斯优化` `自动化设计` `大型语言模型` `进化策略` `算法生成`

## 📋 核心要点

1. 现有的贝叶斯优化算法设计依赖于专家知识，过程繁琐且效率低下。
2. 论文提出利用大型语言模型自动生成贝叶斯优化算法代码，结合进化策略进行迭代优化。
3. 实验结果显示，生成的算法在19个BBOB基准函数中超越了现有最优算法，具有良好的泛化能力。

## 📝 摘要（中文）

贝叶斯优化（BO）是一类强大的算法，用于优化昂贵的黑箱函数，但设计有效的BO算法仍然是一个依赖专业知识的手动任务。最近，大型语言模型（LLMs）的进展为自动化科学发现开辟了新途径，包括优化算法的自动设计。本文提出了一种新方法，利用LLMs自动生成完整的BO算法代码。该框架使用进化策略引导LLM生成保留BO算法关键组件的Python代码。实验结果表明，生成的算法在19个BBOB基准函数中超越了现有的BO基线，并在更高维度和不同任务中表现良好，展示了LLMs作为算法共同设计者的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决贝叶斯优化算法设计的手动和专家依赖性问题，现有方法在效率和自动化程度上存在不足。

**核心思路**：通过结合大型语言模型和进化策略，自动生成符合贝叶斯优化关键组件的算法代码，从而实现算法的自动化设计。

**技术框架**：整体架构包括三个主要模块：初始设计生成、代理模型构建和获取函数定义。LLM生成多个候选算法，并通过BBOB基准测试评估其性能。

**关键创新**：最重要的创新在于将LLM与进化策略结合，形成一种新的算法生成机制，显著提高了算法设计的自动化水平。

**关键设计**：在生成过程中，设置了多种提示变体以引导LLM生成不同候选算法，采用控制变异的方法进行迭代优化，确保生成算法的多样性和有效性。

## 📊 实验亮点

实验结果显示，LLaMEA-BO生成的算法在19个BBOB基准函数中超越了现有的最优贝叶斯优化基线，尤其在5维情况下表现突出，且在更高维度和不同任务中也展现出良好的泛化能力，证明了该方法的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括自动化算法设计、机器学习优化和科学计算等。通过自动生成高效的贝叶斯优化算法，可以加速科学发现和工程应用，降低对专家知识的依赖，提升研究效率。未来，该方法有望扩展到其他类型的优化问题和算法设计领域。

## 📄 摘要（原文）

> Bayesian optimization (BO) is a powerful class of algorithms for optimizing expensive black-box functions, but designing effective BO algorithms remains a manual, expertise-driven task. Recent advancements in Large Language Models (LLMs) have opened new avenues for automating scientific discovery, including the automatic design of optimization algorithms. While prior work has used LLMs within optimization loops or to generate non-BO algorithms, we tackle a new challenge: Using LLMs to automatically generate full BO algorithm code. Our framework uses an evolution strategy to guide an LLM in generating Python code that preserves the key components of BO algorithms: An initial design, a surrogate model, and an acquisition function. The LLM is prompted to produce multiple candidate algorithms, which are evaluated on the established Black-Box Optimization Benchmarking (BBOB) test suite from the COmparing Continuous Optimizers (COCO) platform. Based on their performance, top candidates are selected, combined, and mutated via controlled prompt variations, enabling iterative refinement. Despite no additional fine-tuning, the LLM-generated algorithms outperform state-of-the-art BO baselines in 19 (out of 24) BBOB functions in dimension 5 and generalize well to higher dimensions, and different tasks (from the Bayesmark framework). This work demonstrates that LLMs can serve as algorithmic co-designers, offering a new paradigm for automating BO development and accelerating the discovery of novel algorithmic combinations. The source code is provided at https://github.com/Ewendawi/LLaMEA-BO.

