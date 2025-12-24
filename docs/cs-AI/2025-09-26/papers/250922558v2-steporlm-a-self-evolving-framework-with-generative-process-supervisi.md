---
layout: default
title: "StepORLM: A Self-Evolving Framework With Generative Process Supervision For Operations Research Language Models"
---

# StepORLM: A Self-Evolving Framework With Generative Process Supervision For Operations Research Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22558" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22558v2</a>
  <a href="https://arxiv.org/pdf/2509.22558.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22558v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22558v2', 'StepORLM: A Self-Evolving Framework With Generative Process Supervision For Operations Research Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenyu Zhou, Tianyi Xu, Jianghao Lin, Dongdong Ge

**分类**: cs.AI

**发布日期**: 2025-09-26 (更新: 2025-10-01)

---

## 💡 一句话要点

**StepORLM：一个自进化框架，通过生成过程监督提升运筹学语言模型性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `运筹学` `语言模型` `强化学习` `过程监督` `协同进化` `奖励模型` `直接偏好优化`

## 📋 核心要点

1. 现有运筹学语言模型训练面临信用分配问题和过程监督的短视性，导致模型推理过程存在缺陷。
2. StepORLM通过协同进化策略模型和生成过程奖励模型，利用双重反馈机制进行优化，解决上述问题。
3. 实验表明，StepORLM在多个基准测试中显著优于现有模型，并能有效提升其他LLM的推理性能。

## 📝 摘要（中文）

大型语言模型(LLMs)在解决运筹学(OR)问题方面展现出巨大潜力。然而，现有基于强化学习的LLM训练方法通常面临两个关键限制：一是结果奖励存在信用分配问题，正确的最终答案可能会强化错误的推理过程；二是传统的判别式过程监督是短视的，无法全面评估OR建模中相互依赖的步骤。为此，我们提出了StepORLM，一种具有生成过程监督的新型自进化框架。StepORLM的核心是一个协同进化循环，其中策略模型和生成过程奖励模型(GenPRM)迭代地相互改进。该循环由双重反馈机制驱动：来自外部求解器的明确的、基于结果的验证，以及来自GenPRM的细致的、全面的过程评估。结合后的信号用于通过加权直接偏好优化(W-DPO)来对齐策略，并同时改进GenPRM。我们得到的80亿参数StepORLM在六个基准测试中建立了新的最先进水平，显著优于更大的通用模型、智能体方法和专门的基线。此外，协同进化的GenPRM能够充当强大且普遍适用的过程验证器，从而显著提高我们自己的模型和其他现有LLM的推理扩展性能。

## 🔬 方法详解

**问题定义**：现有运筹学语言模型在解决问题时，仅仅依赖最终结果进行奖励，无法区分正确的推理过程和错误的推理过程碰巧得到正确答案的情况，导致模型学习到错误的推理逻辑。此外，现有的过程监督方法通常是判别式的，只关注当前步骤的正确性，忽略了步骤之间的依赖关系，无法进行全局优化。

**核心思路**：StepORLM的核心思路是引入一个生成过程奖励模型(GenPRM)，该模型能够评估整个推理过程的质量，而不仅仅是最终结果。通过让策略模型和GenPRM协同进化，策略模型可以学习到更合理的推理过程，而GenPRM也可以不断提升评估过程的能力。

**技术框架**：StepORLM包含一个策略模型和一个生成过程奖励模型(GenPRM)。策略模型负责生成解决运筹学问题的步骤，GenPRM负责评估策略模型生成的步骤的质量。整个框架通过一个协同进化循环进行训练。在每个循环中，策略模型首先生成一系列步骤，然后GenPRM对这些步骤进行评估，并给出奖励。策略模型根据奖励调整自身的参数，以生成更好的步骤。同时，GenPRM也根据策略模型的表现调整自身的参数，以更准确地评估步骤的质量。最终，通过不断迭代，策略模型和GenPRM都能够得到提升。

**关键创新**：StepORLM的关键创新在于引入了生成过程奖励模型(GenPRM)和协同进化机制。GenPRM能够对整个推理过程进行评估，从而避免了信用分配问题。协同进化机制使得策略模型和GenPRM能够相互促进，共同提升性能。与现有方法相比，StepORLM能够学习到更合理的推理过程，并取得更好的性能。

**关键设计**：StepORLM使用加权直接偏好优化(W-DPO)来对齐策略模型。W-DPO是一种基于偏好学习的强化学习算法，它能够根据GenPRM给出的奖励来调整策略模型的参数。GenPRM的训练目标是最大化策略模型生成的正确步骤的奖励，同时最小化策略模型生成的错误步骤的奖励。GenPRM可以使用各种神经网络结构，例如Transformer。

## 📊 实验亮点

StepORLM在六个运筹学基准测试中取得了最先进的性能，显著优于现有的通用模型、智能体方法和专门的基线模型。例如，在某些基准测试中，StepORLM的性能提升超过了10%。此外，协同进化的GenPRM能够有效提升其他LLM的推理扩展性能，表明其具有很强的通用性和实用价值。

## 🎯 应用场景

StepORLM可应用于各种运筹学问题的求解，例如优化调度、资源分配、路径规划等。该研究成果有助于提升人工智能在解决复杂优化问题方面的能力，具有广泛的应用前景，例如智能物流、智能制造、智能交通等领域。未来，该方法可以扩展到其他需要复杂推理过程的任务中。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown promising capabilities for solving Operations Research (OR) problems. While reinforcement learning serves as a powerful paradigm for LLM training on OR problems, existing works generally face two key limitations. First, outcome reward suffers from the credit assignment problem, where correct final answers can reinforce flawed reasoning. Second, conventional discriminative process supervision is myopic, failing to evaluate the interdependent steps of OR modeling holistically. To this end, we introduce StepORLM, a novel self-evolving framework with generative process supervision. At its core, StepORLM features a co-evolutionary loop where a policy model and a generative process reward model (GenPRM) iteratively improve on each other. This loop is driven by a dual-feedback mechanism: definitive, outcome-based verification from an external solver, and nuanced, holistic process evaluation from the GenPRM. The combined signal is used to align the policy via Weighted Direct Preference Optimization (W-DPO) and simultaneously refine the GenPRM. Our resulting 8B-parameter StepORLM establishes a new state-of-the-art across six benchmarks, significantly outperforming vastly larger generalist models, agentic methods, and specialized baselines. Moreover, the co-evolved GenPRM is able to act as a powerful and universally applicable process verifier, substantially boosting the inference scaling performance of both our own model and other existing LLMs.

