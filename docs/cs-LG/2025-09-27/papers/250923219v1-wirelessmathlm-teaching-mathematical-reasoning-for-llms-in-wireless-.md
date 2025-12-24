---
layout: default
title: "WirelessMathLM: Teaching Mathematical Reasoning for LLMs in Wireless Communications with Reinforcement Learning"
---

# WirelessMathLM: Teaching Mathematical Reasoning for LLMs in Wireless Communications with Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23219" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23219v1</a>
  <a href="https://arxiv.org/pdf/2509.23219.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23219v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23219v1', 'WirelessMathLM: Teaching Mathematical Reasoning for LLMs in Wireless Communications with Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Li, Mengbing Liu, Yiyang Zhu, Wenhe Zhang, Li Wei, Jiancheng An, Chau Yuen

**分类**: cs.LG

**发布日期**: 2025-09-27

**备注**: Project Homepage: https://lixin.ai/WirelessMathLM

---

## 💡 一句话要点

**WirelessMathLM：利用强化学习提升LLM在无线通信数学推理中的能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无线通信` `大型语言模型` `强化学习` `数学推理` `领域自适应` `可验证性` `策略优化`

## 📋 核心要点

1. 现有LLM在通用数学推理表现良好，但在无线通信等专业领域的技术数学问题上存在不足。
2. WirelessMathLM利用无线数学问题可验证正确性的特点，通过强化学习训练模型，无需人工反馈。
3. 实验表明，该方法显著提升了模型在无线通信数学推理上的准确率，并对通用数学问题有正向迁移。

## 📝 摘要（中文）

大型语言模型(LLM)擅长通用数学推理，但在专业技术数学方面表现不佳。在无线通信领域，问题需要精确处理信息论边界、优化约束和信号处理公式，即使是最先进的模型也难以达到令人满意的性能。我们提出了WirelessMathLM，证明了紧凑模型(0.5B-7B参数)可以通过领域特定的强化学习和可验证的奖励来匹配甚至超过更大的模型。我们的关键见解是，无线数学问题具有独特的属性——可验证的正确性——这使得无需人工反馈即可进行有效的强化学习。我们构建了WirelessMathBench-XL，这是一个包含来自970篇论文的4027个问题的综合基准。使用带有二元验证奖励的Group Relative Policy Optimization (GRPO)，我们直接从基础检查点训练模型，而无需监督预热。我们的7B模型在WirelessMathBench-XL上实现了39.5%的准确率，接近GPT-4o (40.4%)，同时使用的参数比DeepSeek-R1 (671B, 57.4%)少约100倍。值得注意的是，GRPO训练几乎使所有模型规模的性能翻倍(0.5B +11%, 3B +103%, 7B +81%)，并对通用数学基准产生积极的迁移——我们的模型在MATH、Minerva-Math、OlympiadBench、AMC和AIME上平均获得+8.4分，而没有在这些任务上进行任何训练。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在无线通信领域专业数学问题上表现不佳的问题。现有方法，即使是最先进的LLM，也难以处理无线通信中涉及的信息论边界、优化约束和信号处理公式等复杂问题，导致性能不足。

**核心思路**：论文的核心思路是利用无线通信数学问题具有“可验证正确性”的特性，即可以通过算法或公式验证答案的正确与否。基于此，可以使用强化学习方法，通过二元验证奖励（正确或错误）来训练模型，而无需人工标注或反馈。

**技术框架**：整体框架包括：1) 构建WirelessMathBench-XL基准数据集，包含4027个来自无线通信论文的数学问题；2) 使用Group Relative Policy Optimization (GRPO)算法进行强化学习训练；3) 使用二元验证奖励函数，根据模型输出答案的正确性给予奖励或惩罚；4) 从预训练的LLM基础模型（如0.5B、3B、7B参数的模型）开始训练，无需监督预训练。

**关键创新**：最重要的创新点在于利用了无线通信数学问题固有的可验证性，从而可以使用强化学习方法，在没有人工干预的情况下，有效地训练LLM。这与传统的需要大量人工标注数据的监督学习方法不同，也避免了人工反馈带来的主观性和偏差。

**关键设计**：关键设计包括：1) WirelessMathBench-XL数据集的构建，保证了训练数据的质量和多样性；2) GRPO算法的使用，能够更有效地探索策略空间，提高训练效率；3) 二元验证奖励函数的设计，简单有效，避免了复杂的奖励塑造；4) 从预训练模型开始训练，利用了预训练模型的通用知识，加速了训练过程。

## 📊 实验亮点

实验结果表明，使用GRPO训练的7B模型在WirelessMathBench-XL上达到了39.5%的准确率，接近GPT-4o (40.4%)，同时参数量远小于DeepSeek-R1 (671B, 57.4%)。GRPO训练使模型性能显著提升，0.5B模型提升11%，3B模型提升103%，7B模型提升81%。此外，模型在通用数学基准测试中也获得了平均8.4分的提升。

## 🎯 应用场景

该研究成果可应用于无线通信系统设计、优化和性能分析等领域。例如，可以利用训练好的模型自动推导信息论界限，优化资源分配策略，或辅助信号处理算法的设计。此外，该方法还可以推广到其他具有可验证正确性的专业领域，例如控制理论、运筹学等。

## 📄 摘要（原文）

> Large language models (LLMs) excel at general mathematical reasoning but fail catastrophically on specialized technical mathematics. In wireless communications, where problems require precise manipulation of information-theoretic bounds, optimization constraints, and signal processing formulations, even state-of-the-art models struggle to achieve competent performance. We present WirelessMathLM, demonstrating that compact models (0.5B-7B parameters) can match or exceed much larger models through domain-specific reinforcement learning with verifiable rewards. Our key insight is that wireless mathematics problems possess a unique property--verifiable correctness--that enables effective reinforcement learning without human feedback. We construct WirelessMathBench-XL, a comprehensive benchmark of 4,027 problems from 970 papers. Using Group Relative Policy Optimization (GRPO) with binary verification rewards, we train models directly from base checkpoints without supervised warm-start. Our 7B model achieves 39.5% accuracy on WirelessMathBench-XL, approaching GPT-4o (40.4%) while using about 100 times fewer parameters than DeepSeek-R1 (671B, 57.4%). Remarkably, GRPO training nearly doubles performance across all model scales (0.5B +11%, 3B +103%, 7B +81%), with positive transfer to general mathematics benchmarks--our models gain +8.4 points on average across MATH, Minerva-Math, OlympiadBench, AMC, and AIME without any training on these tasks.

