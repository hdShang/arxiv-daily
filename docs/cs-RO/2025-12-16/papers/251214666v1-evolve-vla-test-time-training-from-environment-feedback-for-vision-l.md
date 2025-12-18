---
layout: default
title: EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models
---

# EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14666" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14666v1</a>
  <a href="https://arxiv.org/pdf/2512.14666.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14666v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14666v1', 'EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zechen Bai, Chen Gao, Mike Zheng Shou

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-16

**备注**: 15 pages

---

## 💡 一句话要点

**提出EVOLVE-VLA以解决视觉-语言-动作模型适应性不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `自适应学习` `环境反馈` `机器人操作` `持续学习` `策略演化` `进度估计`

## 📋 核心要点

1. 现有视觉-语言-动作模型依赖于大量的演示数据，无法适应训练与部署条件的变化，限制了其自适应能力。
2. 本文提出EVOLVE-VLA框架，通过环境互动进行测试时训练，利用自主反馈替代传统的奖励信号，实现持续学习。
3. 实验结果表明，EVOLVE-VLA在长时间任务上提升8.6%，一次学习任务上提升22.0%，并在未见任务上实现20.8%的成功率。

## 📝 摘要（中文）

实现真正自适应的具身智能需要代理不仅通过模仿静态演示学习，还需通过与环境的持续互动不断改进。视觉-语言-动作（VLA）模型在机器人操作中取得了进展，但仍受限于监督微调（SFT），需要大量演示并无法适应训练条件的变化。本文提出EVOLVE-VLA，一个在测试时通过环境互动进行持续适应的训练框架，能够在最少或零任务特定演示的情况下进行学习。关键技术挑战在于用自主反馈替代不可用的奖励信号。我们通过学习的进度估计器提供密集反馈，并设计了两种机制来“驯服”这种噪声信号。EVOLVE-VLA在长时间任务上提升了8.6%，在一次学习中提升了22.0%，并实现了跨任务泛化，成功率达到20.8%。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉-语言-动作模型在测试阶段缺乏适应性的问题。现有方法依赖于大量的演示数据，无法灵活应对环境变化，导致学习效果不佳。

**核心思路**：提出EVOLVE-VLA框架，通过环境反馈进行测试时训练，替代传统的奖励信号，利用学习的进度估计器提供密集反馈，从而实现持续自我改进。

**技术框架**：EVOLVE-VLA框架包括两个主要模块：进度估计器和策略演化机制。进度估计器负责提供环境反馈，而策略演化机制则通过平滑反馈和逐步扩展策略来优化学习过程。

**关键创新**：最重要的创新在于用自主反馈替代不可用的奖励信号，并通过进度估计器和策略演化机制有效处理噪声信号。这一设计使得模型能够在没有任务特定演示的情况下进行学习和适应。

**关键设计**：在进度估计器中，采用累积进度估计机制来平滑噪声反馈，同时引入渐进式视野扩展策略，以实现策略的逐步演化。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14666v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14666v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14666v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，EVOLVE-VLA在长时间任务上提升了8.6%，在一次学习任务中提升了22.0%。此外，该模型在未见任务上实现了20.8%的成功率，显著优于传统的监督微调方法（0%成功率）。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动化操作和人机交互等。通过实现持续学习和适应能力，EVOLVE-VLA能够在动态环境中更有效地执行复杂任务，提升机器人在实际应用中的灵活性和智能化水平。

## 📄 摘要（原文）

> Achieving truly adaptive embodied intelligence requires agents that learn not just by imitating static demonstrations, but by continuously improving through environmental interaction, which is akin to how humans master skills through practice. Vision-Language-Action (VLA) models have advanced robotic manipulation by leveraging large language models, yet remain fundamentally limited by Supervised Finetuning (SFT): requiring hundreds of demonstrations per task, rigidly memorizing trajectories, and failing to adapt when deployment conditions deviate from training. We introduce EVOLVE-VLA, a test-time training framework enabling VLAs to continuously adapt through environment interaction with minimal or zero task-specific demonstrations. The key technical challenge is replacing oracle reward signals (unavailable at test time) with autonomous feedback. We address this through a learned progress estimator providing dense feedback, and critically, we design our framework to ``tame'' this inherently noisy signal via two mechanisms: (1) an accumulative progress estimation mechanism smoothing noisy point-wise estimates, and (2) a progressive horizon extension strategy enabling gradual policy evolution. EVOLVE-VLA achieves substantial gains: +8.6\% on long-horizon tasks, +22.0\% in 1-shot learning, and enables cross-task generalization -- achieving 20.8\% success on unseen tasks without task-specific demonstrations training (vs. 0\% for pure SFT). Qualitative analysis reveals emergent capabilities absent in demonstrations, including error recovery and novel strategies. This work represents a critical step toward VLAs that truly learn and adapt, moving beyond static imitation toward continuous self-improvements.

