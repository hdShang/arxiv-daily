---
layout: default
title: "BOW: Reinforcement Learning for Bottlenecked Next Word Prediction"
---

# BOW: Reinforcement Learning for Bottlenecked Next Word Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13502" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13502v2</a>
  <a href="https://arxiv.org/pdf/2506.13502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13502v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13502v2', 'BOW: Reinforcement Learning for Bottlenecked Next Word Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ming Shen, Zhikun Xu, Jacob Dineen, Xiao Ye, Ben Zhou

**分类**: cs.CL

**发布日期**: 2025-06-16 (更新: 2025-09-26)

---

## 💡 一句话要点

**提出BOW方法以解决语言模型推理能力不足的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `下一个词预测` `强化学习` `推理能力` `自然语言处理` `语言模型`

## 📋 核心要点

1. 现有的下一个词预测方法在推理能力上存在不足，缺乏明确的推理过程，导致模型生成的内容流畅但缺乏深度。
2. 本文提出了BOW方法，通过引入中间推理瓶颈，迫使模型在预测下一个词之前生成推理轨迹，从而增强推理能力。
3. 在多个基准测试中，BOW方法在零-shot推理上表现优异，较强的持续预训练基线提升近5%，并在10个评估中获得7个最佳结果。

## 📝 摘要（中文）

大型语言模型（LLMs）通常通过下一个词预测（NWP）进行预训练，虽然在表面流畅性上表现良好，但对模型进行明确推理的压力有限。本文研究了通过改变监督信号是否能更好地引导明确推理，并增强模型的整体推理能力。我们提出了瓶颈下一个词预测（BOW），这是一种将中间推理瓶颈插入的强化学习（RL）形式的NWP。模型首先生成下一个词的推理轨迹，然后通过一个冻结的评分器为该轨迹分配软的分布式奖励，以指导RL优化。实验表明，BOW在多个基准测试中显著提升了零-shot推理能力，并在10个内在NWP评估中取得了7个最佳结果。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在下一个词预测中缺乏明确推理过程的问题。现有方法往往只关注生成流畅的文本，而忽视了推理能力的培养。

**核心思路**：BOW方法通过引入一个推理瓶颈，要求模型在生成下一个词之前，首先生成一个推理轨迹。这种设计旨在增强模型的推理能力，促使其在生成过程中进行更深层次的思考。

**技术框架**：BOW的整体架构包括两个主要模块：政策模型和评分器。政策模型负责生成推理轨迹，而冻结的评分器则根据该轨迹为模型提供奖励信号，指导强化学习的优化过程。

**关键创新**：BOW的核心创新在于将推理过程引入下一个词预测中，显著区别于传统的直接预测方法。通过这种方式，模型能够在生成过程中进行更为复杂的推理，从而提升整体推理能力。

**关键设计**：在奖励设计上，BOW采用了软分布式奖励机制，基于推理轨迹的概率来指导优化。此外，论文还提出了一种可选的L1风格正则化，以防止模型采用简单的“命名答案”策略。

## 📊 实验亮点

实验结果显示，BOW方法在10个基准测试中，较强的持续预训练基线平均提升近5%。在10个内在NWP评估中，BOW取得了7个最佳结果，表明其在零-shot推理能力上的显著优势。

## 🎯 应用场景

BOW方法在自然语言处理领域具有广泛的应用潜力，尤其是在需要深度推理的任务中，如问答系统、对话生成和文本摘要等。通过增强模型的推理能力，BOW有望提升这些应用的智能水平和用户体验。

## 📄 摘要（原文）

> Large language models (LLMs) are typically pretrained with next-word prediction (NWP), which yields strong surface fluency but places limited pressure on models to form explicit reasoning before emitting tokens. We study whether shifting the supervision signal can better elicit explicit reasoning and, more broadly, strengthen models' general reasoning capability. We present BOttlenecked next-Word prediction (BOW), a RL formulation of NWP that inserts an intermediate reasoning bottleneck. Instead of predicting the next word directly from context, the policy model must first generate a next-word reasoning trajectory. A frozen scorer then assigns this trajectory a soft, distributional reward equal to the probability of the gold next token conditioned solely on the trajectory to guide the RL optimization. We also propose an optional L1-style regularizer on the reward to discourage "name-the-answer" shortcuts. Across ten benchmarks, a brief BOW adaptation phase on Qwen2.5-7B-Instruct and Llama3.1-8B-Instruct improves zero-shot reasoning and outperforms strong continual-pretraining baselines, including an RL variant with a hard, binary reward and a supervised finetuning approach with augmented data, by nearly 5% on average, while achieving the top result in 7 of 10 intrinsic NWP evaluations. These results indicate that BOW is a viable alternative to vanilla NWP, inducing explicit next-word reasoning and strengthening general reasoning ability.

