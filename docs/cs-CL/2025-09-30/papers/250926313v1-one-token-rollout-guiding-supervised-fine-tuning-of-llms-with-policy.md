---
layout: default
title: "One-Token Rollout: Guiding Supervised Fine-Tuning of LLMs with Policy Gradient"
---

# One-Token Rollout: Guiding Supervised Fine-Tuning of LLMs with Policy Gradient

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26313" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26313v1</a>
  <a href="https://arxiv.org/pdf/2509.26313.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26313v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26313v1', 'One-Token Rollout: Guiding Supervised Fine-Tuning of LLMs with Policy Gradient')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Ming, Haoyuan Wu, Shoubo Hu, Zhuolun He, Bei Yu

**分类**: cs.CL

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出One-Token Rollout算法，利用策略梯度指导LLM的监督微调，提升泛化能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `监督微调` `策略梯度` `强化学习` `泛化能力` `On-Policy学习` `One-Token Rollout`

## 📋 核心要点

1. 监督微调SFT在LLM泛化能力上存在不足，其主要原因是SFT学习的是固定的off-policy数据。
2. One-Token Rollout (OTR)算法将每个token生成视为单步强化学习，利用策略梯度将off-policy数据转化为on-policy信号。
3. 实验表明，OTR在数学推理、代码生成和通用领域推理等任务上始终优于标准SFT，验证了on-policy数据对泛化的重要性。

## 📝 摘要（中文）

监督微调(SFT)是调整大型语言模型(LLM)的主要方法，但与强化学习(RL)相比，它在泛化方面常常表现不佳。本文认为，这种性能差异不仅源于损失函数，更源于一个更根本的区别：SFT从固定的、预先收集的数据集中学习，而RL利用从当前策略中采样的on-policy数据。基于此，我们引入了one-token rollout (OTR)，这是一种新的微调算法，它使用策略梯度方法指导SFT。OTR通过将每个token生成视为单步强化学习轨迹来重构自回归学习过程。在每一步，它通过从当前策略的分布中采样多个候选token来执行蒙特卡罗“rollout”。然后，使用来自监督数据的ground-truth token为这些样本提供奖励信号。在策略梯度的指导下，我们的算法将静态的、off-policy的监督数据转化为token级别的动态的、on-policy信号，从而获得on-policy学习的泛化优势，同时避免了完整句子生成的高昂开销。通过在涵盖数学推理、代码生成和通用领域推理等各种具有挑战性的基准上进行的大量实验，我们证明了OTR始终优于标准SFT。我们的研究结果表明，OTR是一种强大而实用的LLM微调替代方案，并提供了令人信服的证据，表明数据的on-policy性质是泛化的关键驱动因素，为微调LLM提供了一个有希望的新方向。

## 🔬 方法详解

**问题定义**：监督微调（SFT）是微调大型语言模型（LLM）的常用方法，但其泛化能力不如强化学习（RL）。SFT使用预先收集的静态数据集进行训练，这限制了模型探索和适应新数据的能力。因此，如何提高SFT的泛化能力是一个关键问题。

**核心思路**：论文的核心思路是将SFT过程转化为一个强化学习过程，具体来说，将每个token的生成视为一个单步强化学习任务。通过引入策略梯度，模型可以根据当前策略生成token，并根据ground truth token获得奖励，从而实现on-policy学习。这种方法旨在利用on-policy数据的优势，提高模型的泛化能力。

**技术框架**：OTR算法的核心流程如下：1. 对于每个token生成步骤，从当前LLM策略中采样多个候选token。2. 使用监督数据中的ground-truth token作为奖励信号，评估每个候选token的质量。3. 使用策略梯度算法更新LLM的参数，使得模型更倾向于生成高质量的token。这个过程在整个训练数据集上迭代进行，直到模型收敛。

**关键创新**：OTR的关键创新在于将静态的、off-policy的监督数据转化为动态的、on-policy信号。通过在token级别进行rollout和奖励，OTR能够模拟强化学习中的探索过程，从而提高模型的泛化能力。与传统的SFT方法相比，OTR不需要额外的强化学习数据或复杂的奖励函数设计。

**关键设计**：OTR的关键设计包括：1. Rollout策略：从当前LLM策略中采样多个候选token。可以使用不同的采样方法，如top-k采样或nucleus采样。2. 奖励函数：使用监督数据中的ground-truth token作为奖励信号。如果生成的token与ground-truth token相同，则奖励为1，否则为0。3. 策略梯度算法：可以使用不同的策略梯度算法，如REINFORCE或PPO。论文中具体使用的策略梯度算法未知。

## 📊 实验亮点

实验结果表明，OTR在数学推理、代码生成和通用领域推理等多个基准测试中均优于标准的SFT方法。具体性能提升数据未知，但论文强调OTR在各种任务上都表现出一致的优越性，证明了其有效性和泛化能力。

## 🎯 应用场景

该研究成果可应用于各种需要微调LLM的场景，例如对话系统、文本生成、代码生成等。通过提高LLM的泛化能力，可以使其更好地适应新的任务和数据，从而提高其在实际应用中的性能和效果。该方法在教育、客服、内容创作等领域具有广泛的应用前景。

## 📄 摘要（原文）

> Supervised fine-tuning (SFT) is the predominant method for adapting large language models (LLMs), yet it often struggles with generalization compared to reinforcement learning (RL). In this work, we posit that this performance disparity stems not just from the loss function, but from a more fundamental difference: SFT learns from a fixed, pre-collected dataset, whereas RL utilizes on-policy data sampled from the current policy. Building on this hypothesis, we introduce one-token rollout (OTR), a novel fine-tuning algorithm that guides SFT with the policy gradient method. OTR reframes the autoregressive learning process by treating each token generation as a single-step reinforcement learning trajectory. At each step, it performs a Monte Carlo ``rollout'' by sampling multiple candidate tokens from the current policy's distribution. The ground-truth token from the supervised data is then used to provide a reward signal to these samples. Guided by policy gradient, our algorithm repurposes static, off-policy supervised data into a dynamic, on-policy signal at the token level, capturing the generalization benefits of on-policy learning while bypassing the costly overhead of full sentence generation. Through extensive experiments on a diverse suite of challenging benchmarks spanning mathematical reasoning, code generation, and general domain reasoning, we demonstrate that OTR consistently outperforms standard SFT. Our findings establish OTR as a powerful and practical alternative for fine-tuning LLMs and provide compelling evidence that the on-policy nature of data is a critical driver of generalization, offering a promising new direction for fine-tuning LLMs.

