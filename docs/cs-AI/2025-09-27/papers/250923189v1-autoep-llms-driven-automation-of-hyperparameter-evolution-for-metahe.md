---
layout: default
title: "AutoEP: LLMs-Driven Automation of Hyperparameter Evolution for Metaheuristic Algorithms"
---

# AutoEP: LLMs-Driven Automation of Hyperparameter Evolution for Metaheuristic Algorithms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23189" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23189v1</a>
  <a href="https://arxiv.org/pdf/2509.23189.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23189v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23189v1', 'AutoEP: LLMs-Driven Automation of Hyperparameter Evolution for Metaheuristic Algorithms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenxing Xu, Yizhe Zhang, Weidong Bao, Hao Wang, Ming Chen, Haoran Ye, Wenzheng Jiang, Hui Yan, Ji Wang

**分类**: cs.AI

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**AutoEP：利用LLM驱动的超参数进化自动优化元启发式算法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `超参数优化` `元启发式算法` `大型语言模型` `零样本学习` `探索性景观分析`

## 📋 核心要点

1. 现有学习方法在超参数优化中面临样本复杂性和泛化性难题。
2. AutoEP利用LLM作为零样本推理引擎，结合在线ELA反馈，实现超参数自适应调整。
3. 实验表明AutoEP优于现有调优器，开源模型Qwen3-30B可媲美GPT-4。

## 📝 摘要（中文）

动态配置算法超参数是计算智能领域的一个根本挑战。虽然基于学习的方法提供了自动化，但它们面临着过高的样本复杂性和较差的泛化能力。我们引入了AutoEP，这是一个新颖的框架，它通过利用大型语言模型（LLM）作为算法控制的零样本推理引擎，完全绕过了训练过程。AutoEP的核心创新在于两个组件之间的紧密协同：(1) 一个在线探索性景观分析（ELA）模块，提供关于搜索动态的实时、定量反馈，以及 (2) 一个多LLM推理链，解释这些反馈以生成自适应的超参数策略。这种方法将高层次的推理建立在经验数据的基础上，从而减轻了幻觉。在不同的组合优化基准上对三种不同的元启发式算法进行评估，AutoEP始终优于最先进的调优器，包括神经进化和其他基于LLM的方法。值得注意的是，我们的框架使像Qwen3-30B这样的开源模型能够与GPT-4的性能相匹配，展示了一种强大且易于访问的自动化超参数设计的新范例。

## 🔬 方法详解

**问题定义**：论文旨在解决元启发式算法中超参数动态配置的难题。现有基于学习的方法需要大量的训练样本，泛化能力差，难以适应不同的问题和算法。手动调参耗时耗力，且依赖专家经验。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的零样本推理能力，结合在线探索性景观分析（ELA）提供的实时反馈，动态调整元启发式算法的超参数。通过将高层次的推理建立在经验数据的基础上，减轻LLM的幻觉问题，实现更有效的超参数优化。

**技术框架**：AutoEP框架包含两个主要模块：在线探索性景观分析（ELA）模块和多LLM推理链。ELA模块负责实时分析搜索过程中的景观特征，提供定量反馈。多LLM推理链则根据ELA的反馈，生成自适应的超参数策略。整个流程无需训练，实现了零样本的超参数优化。

**关键创新**：AutoEP的关键创新在于将LLM的推理能力与在线ELA反馈相结合，构建了一个无需训练的超参数优化框架。与传统的基于学习的方法相比，AutoEP避免了样本复杂性和泛化性问题。与直接使用LLM生成超参数的方法相比，AutoEP通过ELA反馈减轻了LLM的幻觉问题。

**关键设计**：ELA模块选择合适的景观特征进行分析，例如fitness distance correlation等。多LLM推理链的设计包括prompt的设计，如何将ELA的反馈信息有效地输入LLM，以及如何将LLM的输出转化为超参数的调整策略。论文还探索了不同LLM（包括开源模型和闭源模型）在AutoEP框架中的性能表现。

## 📊 实验亮点

实验结果表明，AutoEP在三种不同的元启发式算法和多个组合优化基准上，均优于最先进的调优器，包括神经进化和其他基于LLM的方法。值得注意的是，开源模型Qwen3-30B在AutoEP框架下，能够达到与GPT-4相媲美的性能，这表明AutoEP具有很高的可访问性和实用性。实验结果充分验证了AutoEP的有效性和优越性。

## 🎯 应用场景

AutoEP具有广泛的应用前景，可用于优化各种组合优化问题，例如旅行商问题、车辆路径问题、调度问题等。该方法可以显著降低算法调参的成本，提高算法的性能和鲁棒性。AutoEP的零样本特性使其能够快速应用于新的问题和算法，具有很高的实用价值。未来，AutoEP可以扩展到其他类型的算法和优化问题，例如深度学习模型的超参数优化。

## 📄 摘要（原文）

> Dynamically configuring algorithm hyperparameters is a fundamental challenge in computational intelligence. While learning-based methods offer automation, they suffer from prohibitive sample complexity and poor generalization. We introduce AutoEP, a novel framework that bypasses training entirely by leveraging Large Language Models (LLMs) as zero-shot reasoning engines for algorithm control. AutoEP's core innovation lies in a tight synergy between two components: (1) an online Exploratory Landscape Analysis (ELA) module that provides real-time, quantitative feedback on the search dynamics, and (2) a multi-LLM reasoning chain that interprets this feedback to generate adaptive hyperparameter strategies. This approach grounds high-level reasoning in empirical data, mitigating hallucination. Evaluated on three distinct metaheuristics across diverse combinatorial optimization benchmarks, AutoEP consistently outperforms state-of-the-art tuners, including neural evolution and other LLM-based methods. Notably, our framework enables open-source models like Qwen3-30B to match the performance of GPT-4, demonstrating a powerful and accessible new paradigm for automated hyperparameter design. Our code is available at https://anonymous.4open.science/r/AutoEP-3E11

