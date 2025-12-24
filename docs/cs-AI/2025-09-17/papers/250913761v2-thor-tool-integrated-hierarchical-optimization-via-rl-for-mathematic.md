---
layout: default
title: "THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning"
---

# THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13761" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13761v2</a>
  <a href="https://arxiv.org/pdf/2509.13761.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13761v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13761v2', 'THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qikai Chang, Zhenrong Zhang, Pengfei Hu, Jun Du, Jiefeng Ma, Yicheng Pan, Jianshu Zhang, Quan Liu, Jianqing Gao

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-17 (更新: 2025-10-03)

**备注**: 22 pages, 13 figures

**🔗 代码/项目**: [GITHUB](https://github.com/JingMog/THOR)

---

## 💡 一句话要点

**THOR：基于强化学习的工具集成层次优化，用于数学推理**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学推理` `工具集成` `强化学习` `层次优化` `自我纠正` `大型语言模型` `代码生成`

## 📋 核心要点

1. 现有方法在构建高质量的工具集成推理数据、进行细粒度优化以及增强推理能力方面存在不足。
2. THOR通过强化学习进行工具集成层次优化，联合优化问题解决和代码生成，并引入自我纠正机制。
3. THOR在数学和代码基准测试中取得了最先进的性能，并在不同模型中展现出强大的泛化能力。

## 📝 摘要（中文）

大型语言模型（LLMs）在数学推理方面取得了显著进展，但在数值计算和形式符号操作等高精度任务中仍然面临挑战。集成外部工具已成为弥合这一差距的一种有前景的方法。然而，现有方法在构建工具集成推理数据、执行细粒度优化和增强推理方面存在困难。为了克服这些限制，我们提出了THOR（Tool-Integrated Hierarchical Optimization via RL）。首先，我们引入了TIRGen，这是一个基于多智能体Actor-Critic的pipeline，用于构建高质量的工具集成推理路径数据集，与策略对齐并在不同模型中泛化。其次，为了执行细粒度的层次优化，我们引入了一种RL策略，该策略联合优化episode级别的问题解决和step级别的代码生成。这是基于我们的关键洞察，即中间工具调用的成功是最终答案正确性的有力预测指标。最后，THOR结合了一种自我纠正机制，该机制利用即时工具反馈来动态修改推理过程中的错误推理路径。我们的方法在不同的模型中表现出强大的泛化能力，在推理和非推理模型中均表现有效。它还在多个数学基准测试中为类似规模的模型实现了最先进的性能，同时在代码基准测试中也提供了持续的改进。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在数学推理任务中，尤其是在需要高精度计算和符号操作的任务中表现不足。现有的工具集成方法在数据构建、优化粒度和推理能力上存在瓶颈，难以充分利用外部工具的优势。

**核心思路**：THOR的核心思路是通过强化学习来优化工具集成推理过程，将问题分解为层次化的步骤，并利用中间步骤的成功与否来指导整体优化。通过联合优化episode级别的问题解决和step级别的代码生成，实现更细粒度的控制和更高的准确性。

**技术框架**：THOR包含三个主要组成部分：TIRGen（工具集成推理数据生成器）、层次优化RL策略和自我纠正机制。TIRGen使用多智能体Actor-Critic框架生成高质量的工具集成推理路径数据集。层次优化RL策略同时优化episode级别的问题解决和step级别的代码生成。自我纠正机制利用工具的即时反馈动态修正推理路径。

**关键创新**：THOR的关键创新在于其层次化的优化策略和自我纠正机制。层次优化允许模型更细粒度地控制推理过程，而自我纠正机制则能够利用工具的反馈信息动态地修正错误，从而提高整体的准确性和鲁棒性。

**关键设计**：TIRGen使用多智能体Actor-Critic框架，其中每个智能体负责生成推理路径中的一个步骤。RL策略使用奖励函数来鼓励正确的工具调用和最终答案的正确性。自我纠正机制使用工具的反馈信息来判断当前步骤是否正确，并根据需要重新生成该步骤。

## 📊 实验亮点

THOR在多个数学基准测试中取得了最先进的性能，超越了同等规模的模型。此外，THOR在代码基准测试中也取得了持续的改进，证明了其在不同领域的泛化能力。实验结果表明，THOR的层次优化策略和自我纠正机制能够显著提高模型的准确性和鲁棒性。

## 🎯 应用场景

THOR具有广泛的应用前景，可以应用于各种需要复杂推理和计算的任务，例如科学研究、金融分析、软件开发等。通过集成外部工具，THOR可以显著提高这些任务的自动化程度和准确性，从而提高工作效率和降低成本。未来，THOR可以进一步扩展到其他领域，例如自然语言处理、图像识别等，从而实现更智能化的应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have made remarkable progress in mathematical reasoning, but still continue to struggle with high-precision tasks like numerical computation and formal symbolic manipulation. Integrating external tools has emerged as a promising approach to bridge this gap. Despite recent advances, existing methods struggle with three key challenges: constructing tool-integrated reasoning data, performing fine-grained optimization, and enhancing inference. To overcome these limitations, we propose THOR (Tool-Integrated Hierarchical Optimization via RL). First, we introduce TIRGen, a multi-agent actor-critic-based pipeline for constructing high-quality datasets of tool-integrated reasoning paths, aligning with the policy and generalizing well across diverse models. Second, to perform fine-grained hierarchical optimization, we introduce an RL strategy that jointly optimizes for both episode-level problem solving and step-level code generation. This is motivated by our key insight that the success of an intermediate tool call is a strong predictor of the final answer's correctness. Finally, THOR incorporates a self-correction mechanism that leverages immediate tool feedback to dynamically revise erroneous reasoning paths during inference. Our approach demonstrates strong generalization across diverse models, performing effectively in both reasoning and non-reasoning models. It further achieves state-of-the-art performance for models of a similar scale on multiple mathematical benchmarks, while also delivering consistent improvements on code benchmarks. Our code will be publicly available at https://github.com/JingMog/THOR.

