---
layout: default
title: "J4R: Learning to Judge with Equivalent Initial State Group Relative Policy Optimization"
---

# J4R: Learning to Judge with Equivalent Initial State Group Relative Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13346" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13346v3</a>
  <a href="https://arxiv.org/pdf/2505.13346.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13346v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13346v3', 'J4R: Learning to Judge with Equivalent Initial State Group Relative Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Austin Xu, Yilun Zhou, Xuan-Phi Nguyen, Caiming Xiong, Shafiq Joty

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-19 (更新: 2025-06-18)

**备注**: 25 pages, 4 figures, 6 tables. Updated with code and benchmark

---

## 💡 一句话要点

**提出EIS-GRPO算法以提升模型输出评估的准确性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模型评估` `强化学习` `推理能力` `自动化评估` `语言模型`

## 📋 核心要点

1. 现有的LLM作为评判者在复杂推理领域的评估能力不足，导致评估结果的准确性受到影响。
2. 本文提出了EIS-GRPO算法，通过强化学习训练评判者，以克服复杂评估环境中的位置偏差问题。
3. 训练出的J4R模型在JudgeBench和ReasoningJudgeBench上分别超越了GPT-4o和其他小型评判者，提升幅度达到6.7%和9%。

## 📝 摘要（中文）

随着大型语言模型（LLM）发展的加速，模型输出评估已从耗时的人力评估转向自动评估，LLM被赋予评估其他模型输出的任务。然而，现有的LLM作为评判者的模型在复杂推理领域表现不佳。为了解决这一问题，本文提出了等效初始状态组相对策略优化（EIS-GRPO）算法，旨在提高评判者在复杂评估环境中的鲁棒性。此外，本文还引入了ReasoningJudgeBench基准，评估评判者在多样化推理场景下的表现。最终，训练出的Judge for Reasoning（J4R）模型在多个基准上超越了GPT-4o和其他小型评判者，展现出显著的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM作为评判者在复杂推理领域评估能力不足的问题，现有方法在处理更具挑战性的内容时表现不佳。

**核心思路**：提出EIS-GRPO算法，通过强化学习训练评判者，使其在复杂评估环境中对位置偏差具有更强的鲁棒性，从而提高评估的准确性。

**技术框架**：整体架构包括数据收集、模型训练和评估三个主要阶段。首先，收集多样化的评估数据，然后利用EIS-GRPO算法进行模型训练，最后在ReasoningJudgeBench上进行评估。

**关键创新**：EIS-GRPO算法是本文的核心创新，它通过引入等效初始状态的概念，显著提升了评判者在复杂推理任务中的表现，与传统方法相比，能够更有效地处理位置偏差。

**关键设计**：在模型训练中，采用了特定的损失函数以优化评判者的输出，同时设计了适应性网络结构以增强模型的学习能力，确保其在多样化推理场景下的表现。

## 📊 实验亮点

实验结果显示，J4R模型在JudgeBench和ReasoningJudgeBench上分别超越了GPT-4o和其他小型评判者，提升幅度达到6.7%和9%。这一结果表明，EIS-GRPO算法在复杂推理任务中的有效性，验证了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自动化内容评估、智能客服系统和教育评估等。通过提升模型在复杂推理任务中的评估能力，能够为相关行业提供更准确的反馈和评估结果，进而推动智能系统的进一步发展与应用。

## 📄 摘要（原文）

> To keep pace with the increasing pace of large language models (LLM) development, model output evaluation has transitioned away from time-consuming human evaluation to automatic evaluation, where LLMs themselves are tasked with assessing and critiquing other model outputs. LLM-as-judge models are a class of generative evaluators that excel in evaluating relatively simple domains, like chat quality, but struggle in reasoning intensive domains where model responses contain more substantive and challenging content. To remedy existing judge shortcomings, we explore training judges with reinforcement learning (RL). We make three key contributions: (1) We propose the Equivalent Initial State Group Relative Policy Optimization (EIS-GRPO) algorithm, which allows us to train our judge to be robust to positional biases that arise in more complex evaluation settings. (2) We introduce ReasoningJudgeBench, a benchmark that evaluates judges in diverse reasoning settings not covered by prior work. (3) We train Judge for Reasoning (J4R), a 7B judge trained with EIS-GRPO that outperforms GPT-4o and the next best small judge by 6.7% and 9%, matching or exceeding the performance of larger GRPO-trained judges on both JudgeBench and ReasoningJudgeBench.

