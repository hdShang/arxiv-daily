---
layout: default
title: "AWPO: Enhancing Tool-Use of Large Language Models through Explicit Integration of Reasoning Rewards"
---

# AWPO: Enhancing Tool-Use of Large Language Models through Explicit Integration of Reasoning Rewards

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19126" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19126v1</a>
  <a href="https://arxiv.org/pdf/2512.19126.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19126v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19126v1', 'AWPO: Enhancing Tool-Use of Large Language Models through Explicit Integration of Reasoning Rewards')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Lin, Xiaohan Wang, Hexiong Yang, Jiajun Chai, Jie Cao, Guojun Yin, Wei Lin, Ran He

**分类**: cs.CL

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出AWPO，通过显式整合推理奖励增强大语言模型工具使用能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `工具使用` `强化学习` `推理奖励` `策略优化`

## 📋 核心要点

1. 现有方法在训练工具使用LLM时，忽略了显式推理奖励对提升推理和工具利用的潜力。
2. AWPO通过方差感知门控和难度感知加权，自适应地调节推理信号的优势，并采用裁剪机制。
3. 实验表明，AWPO在工具使用基准测试中达到SOTA，4B模型超越Grok-4，并保持泛化能力。

## 📝 摘要（中文）

现有强化学习方法在训练工具使用的大语言模型时，主要依赖可验证的结果奖励，忽略了显式推理奖励在提升推理和工具利用方面的潜力。直接结合推理和结果奖励可能导致次优性能或与主要优化目标冲突。为了解决这个问题，我们提出了优势加权策略优化（AWPO），一个有效的强化学习框架，它有效地整合了显式推理奖励以增强工具使用能力。AWPO结合了方差感知门控和难度感知加权，基于群体相对统计自适应地调节来自推理信号的优势，并采用定制的裁剪机制以实现稳定的优化。大量实验表明，AWPO在标准工具使用基准测试中取得了最先进的性能，显著优于强大的基线模型，并在具有挑战性的多轮场景中领先于闭源模型。值得注意的是，凭借卓越的参数效率，我们的4B模型在多轮准确率方面超越Grok-4 16.0%，同时保持了对分布外MMLU-Pro基准的泛化能力。

## 🔬 方法详解

**问题定义**：现有强化学习方法在训练工具使用的大语言模型时，主要依赖于可验证的结果奖励，而忽略了显式推理奖励在提升推理能力和工具利用方面的潜力。直接将推理奖励和结果奖励结合，可能会导致性能下降，甚至与主要的优化目标相冲突。因此，如何有效地整合推理奖励，同时避免其负面影响，是本文要解决的关键问题。

**核心思路**：本文的核心思路是提出一种名为优势加权策略优化（AWPO）的强化学习框架，该框架能够有效地整合显式推理奖励，从而增强大语言模型的工具使用能力。AWPO通过自适应地调节来自推理信号的优势，并采用定制的裁剪机制，来保证优化的稳定性和有效性。

**技术框架**：AWPO的整体框架包括以下几个主要模块：1) 大语言模型（LLM）：作为策略网络，负责生成工具使用序列。2) 环境：模拟真实世界或特定任务环境，提供状态和奖励信号。3) 推理奖励模块：根据LLM的推理过程生成推理奖励。4) 结果奖励模块：根据LLM的最终结果生成结果奖励。5) 优势加权模块：根据方差感知门控和难度感知加权，自适应地调节推理奖励的优势。6) 策略优化模块：使用裁剪机制，稳定地更新LLM的策略。

**关键创新**：AWPO的关键创新在于其优势加权机制，该机制能够根据群体相对统计信息，自适应地调节来自推理信号的优势。具体来说，AWPO采用了方差感知门控和难度感知加权，前者用于抑制不稳定的推理信号，后者用于提升对困难样本的关注度。此外，AWPO还采用了定制的裁剪机制，以保证优化的稳定性。与现有方法相比，AWPO能够更有效地利用推理奖励，从而提升大语言模型的工具使用能力。

**关键设计**：AWPO的关键设计包括：1) 方差感知门控：使用推理奖励的方差来衡量其稳定性，并根据方差动态地调整推理奖励的权重。2) 难度感知加权：使用样本的难度来衡量其重要性，并根据难度动态地调整样本的权重。3) 定制的裁剪机制：使用一种特殊的裁剪函数，限制策略更新的幅度，从而保证优化的稳定性。损失函数是标准策略梯度损失函数，但加入了优势加权后的推理奖励和结果奖励。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19126v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19126v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，AWPO在标准工具使用基准测试中取得了最先进的性能，显著优于强大的基线模型，并在具有挑战性的多轮场景中领先于闭源模型。例如，在多轮准确率方面，AWPO的4B模型超越Grok-4 16.0%，同时保持了对分布外MMLU-Pro基准的泛化能力。这表明AWPO能够有效地提升大语言模型的工具使用能力，并具有良好的泛化性能。

## 🎯 应用场景

AWPO具有广泛的应用前景，可以应用于各种需要工具使用的大语言模型任务，例如智能助手、自动化编程、科学研究等。通过提升大语言模型的工具使用能力，AWPO可以帮助人们更高效地完成各种任务，提高生产力，并促进人工智能技术的发展。

## 📄 摘要（原文）

> While reinforcement learning (RL) shows promise in training tool-use large language models (LLMs) using verifiable outcome rewards, existing methods largely overlook the potential of explicit reasoning rewards to bolster reasoning and tool utilization. Furthermore, natively combining reasoning and outcome rewards may yield suboptimal performance or conflict with the primary optimization objective. To address this, we propose advantage-weighted policy optimization (AWPO) -- a principled RL framework that effectively integrates explicit reasoning rewards to enhance tool-use capability. AWPO incorporates variance-aware gating and difficulty-aware weighting to adaptively modulate advantages from reasoning signals based on group-relative statistics, alongside a tailored clipping mechanism for stable optimization. Extensive experiments demonstrate that AWPO achieves state-of-the-art performance across standard tool-use benchmarks, significantly outperforming strong baselines and leading closed-source models in challenging multi-turn scenarios. Notably, with exceptional parameter efficiency, our 4B model surpasses Grok-4 by 16.0 percent in multi-turn accuracy while preserving generalization capability on the out-of-distribution MMLU-Pro benchmark.

