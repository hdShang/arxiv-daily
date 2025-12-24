---
layout: default
title: "Towards Self-Evolving Benchmarks: Synthesizing Agent Trajectories via Test-Time Exploration under Validate-by-Reproduce Paradigm"
---

# Towards Self-Evolving Benchmarks: Synthesizing Agent Trajectories via Test-Time Exploration under Validate-by-Reproduce Paradigm

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00415" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00415v2</a>
  <a href="https://arxiv.org/pdf/2510.00415.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00415v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00415v2', 'Towards Self-Evolving Benchmarks: Synthesizing Agent Trajectories via Test-Time Exploration under Validate-by-Reproduce Paradigm')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dadi Guo, Tianyi Zhou, Dongrui Liu, Chen Qian, Qihan Ren, Shuai Shao, Zhiyuan Fan, Yi R. Fung, Kun Wang, Linfeng Zhang, Jing Shao

**分类**: cs.AI

**发布日期**: 2025-10-01 (更新: 2025-10-23)

**备注**: This is a work in progress due to methodology refinement and further evaluation

---

## 💡 一句话要点

**提出TRACE框架，通过测试时探索与验证，实现Agent基准的自进化。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agent基准测试` `自进化学习` `任务复杂度` `轨迹验证` `大型语言模型`

## 📋 核心要点

1. 现有Agent基准测试难以跟上Agent能力快速提升的步伐，面临被迅速突破上限的挑战。
2. TRACE框架鼓励Agent探索和演化现有任务，生成难度更高的新任务，并记录可验证的轨迹。
3. 实验表明，TRACE框架能有效提升任务复杂度，并保证结果的可验证性和可复现性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）和Agent系统设计的快速发展，Agent的能力得到了前所未有的提升。然而，现有的Agent基准测试正面临着被新开发的Agent迅速突破上限的趋势，难以满足评估Agent能力的需求。为了解决这个问题，我们提出了基于轨迹的、通过复现进行验证的Agent基准复杂度进化（TRACE）框架。该框架从现有基准中选取原始任务，鼓励Agent自由探索并将其演化为难度更高的新任务，同时记录可验证的Agent轨迹。框架包括三个阶段：（1）进化提案挖掘，通过初步探索和发散思维提供任务进化提案；（2）问题形成和自由探索，将提案概念化为可行的候选问题，然后Agent自由探索这些问题并记录其执行轨迹；（3）多级验证，确保演化的任务伴随有可验证和可复现的轨迹。在GAIA基准上的实验表明，TRACE框架持续增强了任务的复杂度，同时通过可验证的执行轨迹提高了正确性的可靠性。此外，我们的框架可以成功地适应和改进以AIME-2024为代表的推理数据集。这项工作标志着从静态、手动策划的基准测试到动态、自进化的评估系统的范式转变，为Agent开发提供了一个可持续且具有挑战性的跑道。

## 🔬 方法详解

**问题定义**：现有Agent基准测试的静态性和人工设计使其难以充分评估快速发展的Agent能力。Agent在这些基准上迅速达到性能上限，导致评估结果缺乏区分度，无法有效指导Agent的进一步发展。因此，需要一种能够动态生成更具挑战性任务的基准测试方法。

**核心思路**：TRACE框架的核心思路是通过Agent在测试时的主动探索和演化，自动生成更复杂的任务。通过记录Agent的执行轨迹，并进行多级验证，确保生成任务的有效性和可复现性。这种自进化机制能够持续提供具有挑战性的评估环境，从而推动Agent能力的提升。

**技术框架**：TRACE框架包含三个主要阶段：（1）**进化提案挖掘**：Agent对原始任务进行初步探索，提出多种可能的任务演化方案。（2）**问题形成和自由探索**：将提案转化为具体的候选问题，Agent在这些问题上进行自由探索，并记录执行轨迹。（3）**多级验证**：对Agent的执行轨迹进行验证，确保任务的可解决性和结果的可复现性。通过这三个阶段的循环迭代，不断生成更具挑战性的任务。

**关键创新**：TRACE框架的关键创新在于其自进化的基准测试机制。与传统的静态基准测试相比，TRACE能够根据Agent的能力动态调整任务难度，从而提供更具区分度的评估结果。此外，通过记录和验证Agent的执行轨迹，保证了评估结果的可靠性和可解释性。

**关键设计**：在进化提案挖掘阶段，可以使用不同的探索策略来鼓励Agent提出多样化的演化方案。在问题形成阶段，需要设计合适的规则来将提案转化为可执行的任务。在多级验证阶段，可以采用多种验证方法，例如复现Agent的执行轨迹，或者使用独立的验证Agent来评估任务的难度。

## 📊 实验亮点

在GAIA基准测试中，TRACE框架成功地提升了任务的复杂度，并提高了结果的可验证性。此外，该框架还成功地应用于AIME-2024数据集，表明其具有良好的泛化能力。实验结果表明，TRACE框架能够有效地解决现有Agent基准测试的局限性，为Agent的评估和发展提供了一个新的方向。

## 🎯 应用场景

TRACE框架可应用于各种Agent系统的评估和开发，尤其适用于需要持续提升Agent能力的场景，例如智能助手、自动化决策系统和机器人控制等。该框架能够帮助研究人员和开发者更好地了解Agent的优势和不足，从而有针对性地进行改进和优化，加速Agent技术的进步。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) and agent system designs have empowered agents with unprecedented levels of capability. However, existing agent benchmarks are showing a trend of rapid ceiling-hitting by newly developed agents, making it difficult to meet the demands for evaluating agent abilities. To address this problem, we propose the Trajectory-based Validated-by-Reproducing Agent-benchmark Complexity Evolution (TRACE) framework. This framework takes an original task from an existing benchmark and encourages agents to freely explore and evolve it into a new task with higher difficulty while recording validatable agent trajectories. The framework proceeds in three stages: (1) evolutionary proposal mining, which provides task evolution proposals through preliminary exploration and divergent thinking; (2) problem formation and free exploration, where proposals are conceptualized into feasible problem candidates and the agents then explore them freely while recording their execution trajectories; and (3) multi-level validation, which ensures that the evolved tasks are accompanied by validatable and reproducible trajectories. Experiments on the GAIA benchmark demonstrate that the TRACE framework consistently enhances task complexity while improving the reliability of correctness through validatable execution trajectories. In addition, our framework can successfully adapt to and improve reasoning datasets represented by AIME-2024. This work marks a paradigm shift from static, manually curated benchmarks to dynamic, self-evolving evaluation systems, providing a sustainable and challenging runway for agent development

