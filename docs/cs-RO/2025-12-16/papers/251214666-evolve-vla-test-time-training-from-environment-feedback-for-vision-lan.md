---
layout: default
title: EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models
---

# EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14666" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14666</a>
  <a href="https://arxiv.org/pdf/2512.14666.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14666" onclick="toggleFavorite(this, '2512.14666', 'EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zechen Bai, Chen Gao, Mike Zheng Shou

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出EVOLVE-VLA以解决视觉-语言-动作模型的适应性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `自适应学习` `环境反馈` `机器人操作` `持续学习`

## 📋 核心要点

1. 现有的视觉-语言-动作模型依赖于大量示范进行监督微调，导致适应性差，无法应对环境变化。
2. EVOLVE-VLA框架通过环境反馈进行测试时训练，允许模型在没有任务特定示范的情况下进行持续学习和适应。
3. 实验结果显示，EVOLVE-VLA在长时间任务上提升8.6%，在一次学习中提升22.0%，并在未见任务上实现20.8%的成功率。

## 📝 摘要（中文）

实现真正自适应的具身智能需要代理不仅通过模仿静态示范来学习，而是通过与环境的持续互动不断改进。尽管视觉-语言-动作（VLA）模型通过利用大型语言模型推动了机器人操作的发展，但仍然受到监督微调（SFT）的限制，需数百个示范，且在部署条件偏离训练时无法适应。我们提出了EVOLVE-VLA，一个在测试时通过环境互动持续适应的训练框架，能够在最小或零任务特定示范的情况下进行学习。关键技术挑战是用自主反馈替代不可用的oracle奖励信号。我们通过学习的进度估计器提供密集反馈，并设计了两个机制来“驯服”这种固有的噪声信号。EVOLVE-VLA在长时间任务上提升了8.6%，在一次学习中提升了22.0%，并实现了跨任务泛化，在没有任务特定示范训练的情况下，在未见任务上取得了20.8%的成功。

## 🔬 方法详解

**问题定义**：本论文旨在解决视觉-语言-动作模型在测试时缺乏适应性的具体问题。现有方法依赖于大量的示范进行监督微调，导致在环境变化时无法有效适应。

**核心思路**：我们提出的EVOLVE-VLA框架通过环境反馈进行测试时训练，允许模型在没有任务特定示范的情况下进行持续学习。通过学习的进度估计器提供密集反馈，并设计机制来处理噪声信号。

**技术框架**：EVOLVE-VLA的整体架构包括两个主要模块：进度估计器和反馈处理机制。进度估计器用于生成环境反馈，而反馈处理机制则通过平滑和逐步扩展策略来优化学习过程。

**关键创新**：本研究的关键创新在于用自主反馈替代传统的oracle奖励信号，并通过累积进度估计和平滑机制来处理噪声信号，从而实现模型的持续适应。

**关键设计**：在设计中，我们采用了累积进度估计机制来平滑噪声点估计，并引入了逐步扩展策略以促进策略的渐进演变。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14666/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14666/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14666/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，EVOLVE-VLA在长时间任务上提升了8.6%，在一次学习中提升了22.0%，并在未见任务上成功率达到20.8%，显著优于传统的监督微调方法（0%成功率）。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和智能家居等场景。通过实现持续学习和适应，EVOLVE-VLA能够在动态环境中提高机器人执行复杂任务的能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Achieving truly adaptive embodied intelligence requires agents that learn not just by imitating static demonstrations, but by continuously improving through environmental interaction, which is akin to how humans master skills through practice. Vision-Language-Action (VLA) models have advanced robotic manipulation by leveraging large language models, yet remain fundamentally limited by Supervised Finetuning (SFT): requiring hundreds of demonstrations per task, rigidly memorizing trajectories, and failing to adapt when deployment conditions deviate from training. We introduce EVOLVE-VLA, a test-time training framework enabling VLAs to continuously adapt through environment interaction with minimal or zero task-specific demonstrations. The key technical challenge is replacing oracle reward signals (unavailable at test time) with autonomous feedback. We address this through a learned progress estimator providing dense feedback, and critically, we design our framework to ``tame'' this inherently noisy signal via two mechanisms: (1) an accumulative progress estimation mechanism smoothing noisy point-wise estimates, and (2) a progressive horizon extension strategy enabling gradual policy evolution. EVOLVE-VLA achieves substantial gains: +8.6\% on long-horizon tasks, +22.0\% in 1-shot learning, and enables cross-task generalization -- achieving 20.8\% success on unseen tasks without task-specific demonstrations training (vs. 0\% for pure SFT). Qualitative analysis reveals emergent capabilities absent in demonstrations, including error recovery and novel strategies. This work represents a critical step toward VLAs that truly learn and adapt, moving beyond static imitation toward continuous self-improvements.

