---
layout: default
title: RL in Name Only? Analyzing the Structural Assumptions in RL post-training for LLMs
---

# RL in Name Only? Analyzing the Structural Assumptions in RL post-training for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13697" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13697v3</a>
  <a href="https://arxiv.org/pdf/2505.13697.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13697v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13697v3', 'RL in Name Only? Analyzing the Structural Assumptions in RL post-training for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Soumya Rani Samineni, Durgesh Kalwar, Karthik Valmeekam, Kaya Stechly, Subbarao Kambhampati

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-19 (更新: 2025-11-10)

---

## 💡 一句话要点

**分析强化学习后训练在大语言模型中的结构假设**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `强化学习` `监督学习` `模型假设` `性能评估` `自然语言处理` `推理能力`

## 📋 核心要点

1. 现有的基于强化学习的后训练方法在结构假设上存在简化，导致模型性能的质疑。
2. 论文通过分析强化学习后训练的结构假设，提出了将LLM训练视为监督学习的观点。
3. 实验结果表明，迭代的监督微调方法在多个基准上表现出与GRPO训练相当的性能。

## 📝 摘要（中文）

基于强化学习的后训练方法在大语言模型（LLMs）中受到广泛关注，尤其是在DeepSeek R1发布后。本文批判性地分析了这些方法的模型假设，指出将LLM训练建模为马尔可夫决策过程（MDP）所做的简化假设导致了一个退化的MDP，实际上并不需要强化学习（RL）或GRPO的框架。通过对GSM8K和Countdown基准的实验，发现迭代的监督微调方法在性能上与GRPO训练相当，表明现有的RL框架和解释存在质疑的空间。

## 🔬 方法详解

**问题定义**：本文旨在解决现有基于强化学习的后训练方法在结构假设上的不足，指出这些假设导致了模型的退化，影响了其有效性。

**核心思路**：论文提出将LLM训练视为监督学习，而非依赖于复杂的强化学习框架，强调了简化假设的局限性。

**技术框架**：研究首先分析了将LLM训练建模为MDP的常见假设，然后通过实验验证了迭代监督微调的有效性，整体流程包括数据准备、模型训练和性能评估。

**关键创新**：最重要的创新在于揭示了现有RL框架的简化假设使得其与监督学习等效，质疑了RL在LLM训练中的必要性。

**关键设计**：在实验中，采用了正负样本的迭代微调策略，使用了GSM8K和Countdown等基准数据集，确保了模型的全面评估。实验中对奖励的分配和状态的定义进行了深入探讨。

## 📊 实验亮点

实验结果显示，采用迭代监督微调的模型在GSM8K和Countdown基准上达到了与GRPO训练相当的性能，验证了该方法的有效性和可行性，表明在某些情况下，强化学习的复杂性并非必要。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等。通过优化大语言模型的训练方法，可以提高其推理能力和生成质量，进而推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Reinforcement learning-based post-training of large language models (LLMs) has recently gained attention, particularly following the release of DeepSeek R1, which applied GRPO for fine-tuning. Amid the growing hype around improved reasoning abilities attributed to RL post-training, we critically examine the formulation and assumptions underlying these methods. We start by highlighting the popular structural assumptions made in modeling LLM training as a Markov Decision Process (MDP), and show how they lead to a degenerate MDP that doesn't quite need the RL/GRPO apparatus. The two critical structural assumptions include (1) making the MDP states be just a concatenation of the actions-with states becoming the context window and the actions becoming the tokens in LLMs and (2) splitting the reward of a state-action trajectory uniformly across the trajectory. Through a comprehensive analysis, we demonstrate that these simplifying assumptions make the approach effectively equivalent to an outcome-driven supervised learning. Our experiments on benchmarks including GSM8K and Countdown using Qwen-2.5 base models show that iterative supervised fine-tuning, incorporating both positive and negative samples, achieves performance comparable to GRPO-based training. We will also argue that the structural assumptions indirectly incentivize the RL to generate longer sequences of intermediate tokens-which in turn feeds into the narrative of "RL generating longer thinking traces." While RL may well be a very useful technique for improving the reasoning abilities of LLMs, our analysis shows that the simplistic structural assumptions made in modeling the underlying MDP render the popular LLM RL frameworks and their interpretations questionable.

