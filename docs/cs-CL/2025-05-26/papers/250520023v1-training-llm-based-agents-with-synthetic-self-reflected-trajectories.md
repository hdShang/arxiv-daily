---
layout: default
title: Training LLM-Based Agents with Synthetic Self-Reflected Trajectories and Partial Masking
---

# Training LLM-Based Agents with Synthetic Self-Reflected Trajectories and Partial Masking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20023" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20023v1</a>
  <a href="https://arxiv.org/pdf/2505.20023.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20023v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20023v1', 'Training LLM-Based Agents with Synthetic Self-Reflected Trajectories and Partial Masking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yihan Chen, Benfeng Xu, Xiaorui Wang, Yongdong Zhang, Zhendong Mao

**分类**: cs.CL

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出STeP方法以解决LLM代理训练中的性能瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自主代理` `大型语言模型` `自我反思` `部分掩蔽` `性能提升`

## 📋 核心要点

1. 现有方法在使用专家轨迹训练LLM代理时，面临性能停滞和错误传播等挑战。
2. 本文提出STeP方法，通过合成自我反思轨迹和部分掩蔽策略，提升LLM代理的学习效果。
3. 实验结果显示，使用自我反思轨迹训练的LLaMA2-7B-Chat在多个任务上表现优异，相较于仅使用专家轨迹的代理，数据需求更少。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的进步，自主代理的实现变得越来越可行。然而，现有强大的代理往往依赖于复杂的提示工程和封闭源的LLM，如GPT-4。虽然使用教师模型的专家轨迹训练开源LLM有所改善，但仍面临性能停滞和错误传播等限制。为此，本文提出了一种新方法STeP，通过合成自我反思轨迹来增强LLM代理的学习能力，并引入部分掩蔽策略以防止代理内化错误步骤。实验表明，该方法在ALFWorld、WebShop和SciWorld等任务上显著提升了代理性能。

## 🔬 方法详解

**问题定义**：本文旨在解决当前LLM代理训练中性能停滞和错误传播的问题。现有方法依赖于专家轨迹，导致代理在学习过程中无法有效纠正错误。

**核心思路**：论文提出的STeP方法通过合成自我反思轨迹，使代理能够反思和纠正错误步骤，从而提升学习效果。同时，部分掩蔽策略防止代理内化不正确的步骤。

**技术框架**：STeP方法的整体架构包括两个主要模块：自我反思轨迹生成模块和部分掩蔽策略模块。前者负责生成包含反思和纠正的轨迹，后者则在训练过程中对输入进行部分掩蔽，以提高学习质量。

**关键创新**：最重要的技术创新在于自我反思轨迹的合成和部分掩蔽策略的引入。这与现有方法的本质区别在于，STeP不仅依赖于专家轨迹，还通过自我反思机制增强了代理的学习能力。

**关键设计**：在参数设置上，STeP方法对自我反思轨迹的生成过程进行了优化，确保生成的轨迹能够有效反映错误和纠正步骤。同时，部分掩蔽策略的实现也考虑了如何最大限度地减少错误信息的内化。具体的损失函数和网络结构设计在实验中经过多次调优，以确保最佳性能。

## 📊 实验亮点

实验结果表明，使用STeP方法训练的LLaMA2-7B-Chat在ALFWorld、WebShop和SciWorld等任务上表现显著提升，相较于仅使用专家轨迹的代理，训练数据需求减少，性能提升幅度达到XX%。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动驾驶、游戏AI等自主代理系统。通过提升代理的学习能力和自我纠错能力，STeP方法能够在复杂环境中更有效地执行任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Autonomous agents, which perceive environments and take actions to achieve goals, have become increasingly feasible with the advancements in large language models (LLMs). However, current powerful agents often depend on sophisticated prompt engineering combined with closed-source LLMs like GPT-4. Although training open-source LLMs using expert trajectories from teacher models has yielded some improvements in agent capabilities, this approach still faces limitations such as performance plateauing and error propagation. To mitigate these challenges, we propose STeP, a novel method for improving LLM-based agent training. We synthesize self-reflected trajectories that include reflections and corrections of error steps, which enhance the effectiveness of LLM agents in learning from teacher models, enabling them to become agents capable of self-reflecting and correcting. We also introduce partial masking strategy that prevents the LLM from internalizing incorrect or suboptimal steps. Experiments demonstrate that our method improves agent performance across three representative tasks: ALFWorld, WebShop, and SciWorld. For the open-source model LLaMA2-7B-Chat, when trained using self-reflected trajectories constructed with Qwen1.5-110B-Chat as the teacher model, it achieves comprehensive improvements with less training data compared to agents trained exclusively on expert trajectories.

