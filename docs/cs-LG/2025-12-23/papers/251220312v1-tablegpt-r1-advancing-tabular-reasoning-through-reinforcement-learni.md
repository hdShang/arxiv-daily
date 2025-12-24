---
layout: default
title: TableGPT-R1: Advancing Tabular Reasoning Through Reinforcement Learning
---

# TableGPT-R1: Advancing Tabular Reasoning Through Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20312" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20312v1</a>
  <a href="https://arxiv.org/pdf/2512.20312.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20312v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20312v1', 'TableGPT-R1: Advancing Tabular Reasoning Through Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saisai Yang, Qingyi Huang, Jing Yuan, Liangyu Zha, Kai Tang, Yuhang Yang, Ning Wang, Yucheng Wei, Liyao Li, Wentao Ye, Hao Chen, Tao Zhang, Junlin Zhou, Haobo Wang, Gang Chen, Junbo Zhao

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-23

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/tablegpt/TableGPT-R1)

---

## 💡 一句话要点

**TableGPT-R1：通过强化学习提升表格推理能力，实现SOTA性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格推理` `强化学习` `大语言模型` `数据分析` `代码执行` `多步骤推理` `奖励塑造`

## 📋 核心要点

1. 现有大语言模型在表格数据处理中，难以胜任复杂推理和代码执行任务，尤其是在多步骤推理和闭环反馈场景下。
2. TableGPT-R1通过系统性的强化学习框架，结合数据工程管道、任务自适应奖励系统和多阶段训练框架，提升表格推理能力。
3. 实验结果表明，TableGPT-R1在权威基准测试中取得了SOTA性能，显著超越了现有模型，并保持了良好的通用能力。

## 📝 摘要（中文）

表格数据是现代数据分析和科学研究的基石。虽然通过监督微调(SFT)的大型语言模型(LLM)显著改善了与此类结构化数据的自然语言交互，但它们在处理真实世界表格任务所需的复杂、多步骤推理和强大的代码执行方面往往表现不足。强化学习(RL)为增强这些能力提供了一个有希望的途径，但其在表格领域的应用面临三个关键障碍：缺乏高质量的agent轨迹，这些轨迹具有在不同表格结构上的闭环代码执行和环境反馈；反馈信号的极端异质性，范围从刚性的SQL执行到开放式的数据解释；以及在垂直专业化过程中灾难性地遗忘一般知识的风险。为了克服这些挑战并解锁对复杂表格的高级推理，我们引入了TableGPT-R1，这是一个建立在系统RL框架上的专用表格模型。我们的方法整合了一个全面的数据工程管道，该管道合成了难度分层的agent轨迹，用于监督对齐和RL rollout；一个任务自适应奖励系统，该系统将基于规则的验证与标准注入的奖励模型相结合，并结合了过程级别的步骤奖励塑造和行为正则化；以及一个多阶段训练框架，该框架在专门从事表格特定任务之前逐步稳定推理。广泛的评估表明，TableGPT-R1在权威基准测试中实现了最先进的性能，显著优于基线模型，同时保留了强大的通用能力。我们的模型可在https://huggingface.co/tablegpt/TableGPT-R1上找到。

## 🔬 方法详解

**问题定义**：现有的大语言模型在处理表格数据时，尤其是在需要复杂推理和代码执行的任务中，表现出明显的不足。它们难以处理多步骤推理、闭环反馈以及异构的反馈信号，并且容易在特定任务上过拟合，导致通用知识的遗忘。

**核心思路**：TableGPT-R1的核心思路是利用强化学习(RL)来提升模型在表格数据上的推理能力。通过精心设计的奖励机制和训练流程，引导模型学习如何有效地执行代码、理解表格数据，并进行多步骤推理。同时，采用多阶段训练策略，避免模型在特定任务上过拟合，保持其通用性。

**技术框架**：TableGPT-R1的整体框架包含以下几个主要模块：1) 数据工程管道：用于生成难度分层的agent轨迹，包括监督对齐和RL rollout所需的数据。2) 任务自适应奖励系统：结合基于规则的验证和标准注入的奖励模型，并进行过程级别的步骤奖励塑造和行为正则化。3) 多阶段训练框架：逐步稳定推理能力，然后再专注于表格特定任务的训练。

**关键创新**：TableGPT-R1的关键创新在于其系统性的强化学习框架，该框架能够有效地解决表格数据处理中的三个主要挑战：缺乏高质量的agent轨迹、反馈信号的异质性以及通用知识的遗忘。通过数据工程管道生成高质量的训练数据，通过任务自适应奖励系统引导模型学习正确的行为，并通过多阶段训练框架保持模型的通用性。

**关键设计**：在数据工程管道中，采用了难度分层的策略，逐步增加训练数据的难度，以提高模型的泛化能力。在任务自适应奖励系统中，结合了基于规则的验证和标准注入的奖励模型，以提供更准确的反馈信号。在多阶段训练框架中，首先进行预训练，以提高模型的通用能力，然后再进行微调，以适应特定的表格任务。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20312v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20312v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20312v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TableGPT-R1在多个权威表格推理基准测试中取得了SOTA性能，显著优于现有的基线模型。具体性能数据和提升幅度在论文中进行了详细展示。该模型在提升表格推理能力的同时，还保持了良好的通用能力，避免了在特定任务上过拟合的问题。

## 🎯 应用场景

TableGPT-R1在数据分析、商业智能、科学研究等领域具有广泛的应用前景。它可以帮助用户更高效地从表格数据中提取信息、进行决策分析，并支持自动化报告生成等任务。该研究的成果有望推动表格数据处理技术的发展，并为各行业带来实际价值。

## 📄 摘要（原文）

> Tabular data serves as the backbone of modern data analysis and scientific research. While Large Language Models (LLMs) fine-tuned via Supervised Fine-Tuning (SFT) have significantly improved natural language interaction with such structured data, they often fall short in handling the complex, multi-step reasoning and robust code execution required for real-world table tasks. Reinforcement Learning (RL) offers a promising avenue to enhance these capabilities, yet its application in the tabular domain faces three critical hurdles: the scarcity of high-quality agentic trajectories with closed-loop code execution and environment feedback on diverse table structures, the extreme heterogeneity of feedback signals ranging from rigid SQL execution to open-ended data interpretation, and the risk of catastrophic forgetting of general knowledge during vertical specialization. To overcome these challenges and unlock advanced reasoning on complex tables, we introduce \textbf{TableGPT-R1}, a specialized tabular model built on a systematic RL framework. Our approach integrates a comprehensive data engineering pipeline that synthesizes difficulty-stratified agentic trajectories for both supervised alignment and RL rollouts, a task-adaptive reward system that combines rule-based verification with a criteria-injected reward model and incorporates process-level step reward shaping with behavioral regularization, and a multi-stage training framework that progressively stabilizes reasoning before specializing in table-specific tasks. Extensive evaluations demonstrate that TableGPT-R1 achieves state-of-the-art performance on authoritative benchmarks, significantly outperforming baseline models while retaining robust general capabilities. Our model is available at https://huggingface.co/tablegpt/TableGPT-R1.

