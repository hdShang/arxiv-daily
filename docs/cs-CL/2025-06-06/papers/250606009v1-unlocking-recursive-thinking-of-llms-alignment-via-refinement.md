---
layout: default
title: "Unlocking Recursive Thinking of LLMs: Alignment via Refinement"
---

# Unlocking Recursive Thinking of LLMs: Alignment via Refinement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06009" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06009v1</a>
  <a href="https://arxiv.org/pdf/2506.06009.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06009v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06009v1', 'Unlocking Recursive Thinking of LLMs: Alignment via Refinement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoke Zhang, Xiaobo Liang, Cunxiang Wang, Juntao Li, Min Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06

**备注**: Accepted to the Findings of ACL 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Banner-Z/AvR.git)

---

## 💡 一句话要点

**提出AvR方法以提升大语言模型的递归推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `递归推理` `长形式思维链` `可微学习` `模型优化` `合成样本`

## 📋 核心要点

1. 现有方法在递归推理能力上存在局限，尤其缺乏高质量的专家数据进行有效蒸馏。
2. 本文提出AvR方法，通过精炼过程结合批评与改进，利用可微学习优化奖励，提升LLMs的递归推理能力。
3. 实验结果显示，AvR在使用3000个合成样本的情况下，显著提升了模型的性能，胜率提高超过20%。

## 📝 摘要（中文）

OpenAI的o1系列模型表明，利用长形式的思维链（CoT）可以显著提升性能。然而，大语言模型（LLMs）的递归思维能力仍然有限，尤其是在缺乏专家策划的数据进行蒸馏的情况下。本文提出了一种新方法AvR（Alignment via Refinement），旨在通过长形式的CoT解锁LLMs的递归推理潜力。AvR引入了一种整合批评和改进行动的精炼过程，通过可微学习技术优化精炼感知奖励。实验结果表明，AvR显著优于传统的偏好优化方法，仅使用3000个合成样本，就能使LLaMA-3-8B-Instruct模型在AlpacaEval 2.0上的胜率提升超过20%。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在递归推理能力上的不足，尤其是在缺乏专家策划数据的情况下，现有方法难以有效提升模型的推理能力。

**核心思路**：AvR方法通过引入精炼过程，结合批评和改进行动，利用可微学习技术来优化精炼感知奖励，从而提升模型的递归推理能力。

**技术框架**：AvR的整体架构包括数据合成、批评与改进模块，以及基于可微学习的奖励优化过程。数据合成阶段生成多轮数据，批评与改进模块则负责对生成的结果进行评估和优化。

**关键创新**：AvR的主要创新在于其精炼过程的设计，通过批评与改进的结合，显著提升了模型的递归思维能力，这与传统的偏好优化方法有本质区别。

**关键设计**：在参数设置上，AvR使用了精炼感知奖励作为优化目标，并设计了适应性损失函数，以确保模型在训练过程中能够有效学习递归推理的能力。

## 📊 实验亮点

实验结果表明，AvR方法在使用仅3000个合成样本的情况下，显著提升了LLaMA-3-8B-Instruct模型在AlpacaEval 2.0上的胜率，提升幅度超过20%。这一结果表明AvR在优化模型性能方面的有效性，超越了传统的偏好优化方法。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和教育技术等。通过提升大语言模型的递归推理能力，AvR方法能够在复杂问题求解、知识推理等任务中展现更高的智能水平，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The OpenAI o1-series models have demonstrated that leveraging long-form Chain of Thought (CoT) can substantially enhance performance. However, the recursive thinking capabilities of Large Language Models (LLMs) remain limited, particularly in the absence of expert-curated data for distillation. In this paper, we propose \textbf{AvR}: \textbf{Alignment via Refinement}, a novel method aimed at unlocking the potential of LLMs for recursive reasoning through long-form CoT. AvR introduces a refinement process that integrates criticism and improvement actions, guided by differentiable learning techniques to optimize \textbf{refinement-aware rewards}. As a result, the synthesized multi-round data can be organized as a long refinement thought, further enabling test-time scaling. Experimental results show that AvR significantly outperforms conventional preference optimization methods. Notably, with only 3k synthetic samples, our method boosts the performance of the LLaMA-3-8B-Instruct model by over 20\% in win rate on AlpacaEval 2.0. Our code is available at Github (https://github.com/Banner-Z/AvR.git).

