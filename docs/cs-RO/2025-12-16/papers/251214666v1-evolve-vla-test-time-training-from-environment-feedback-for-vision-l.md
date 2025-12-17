---
layout: default
title: EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models
---

# EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14666" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14666v1</a>
  <a href="https://arxiv.org/pdf/2512.14666.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14666v1" onclick="toggleFavorite(this, '2512.14666v1', 'EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zechen Bai, Chen Gao, Mike Zheng Shou

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-16

**备注**: 15 pages

---

## 💡 一句话要点

**EVOLVE-VLA：基于环境反馈的VLA模型测试时训练框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉-语言-动作模型` `测试时训练` `环境反馈` `持续学习` `机器人` `强化学习` `自适应` `泛化`

## 📋 核心要点

1. 现有VLA模型依赖大量演示数据，泛化能力差，难以适应部署环境的变化。
2. EVOLVE-VLA通过环境交互进行测试时训练，利用学习到的进度估计器提供反馈，实现持续适应。
3. 实验表明，EVOLVE-VLA在长时程任务、单样本学习和跨任务泛化方面均有显著提升。

## 📝 摘要（中文）

本文提出EVOLVE-VLA，一个测试时训练框架，使视觉-语言-动作(VLA)模型能够通过环境交互持续适应，且只需极少甚至无需特定任务的演示。该框架旨在解决VLA模型依赖大量演示数据、记忆轨迹、以及在部署环境与训练环境不同时无法适应的问题。核心挑战在于用自主反馈替代测试时不可用的oracle奖励信号。为此，论文设计了一个学习到的进度估计器来提供密集反馈，并通过累积进度估计机制平滑噪声点估计，以及渐进式horizon扩展策略实现策略的逐步演进。实验表明，EVOLVE-VLA在长时程任务上取得+8.6%的提升，在单样本学习上取得+22.0%的提升，并实现了跨任务泛化，在未见任务上无需特定任务演示训练即可达到20.8%的成功率（纯SFT为0%）。定性分析揭示了演示数据中不存在的错误恢复和新策略等涌现能力。这项工作是VLA模型从静态模仿走向持续自我改进的关键一步。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作(VLA)模型主要依赖于监督微调(SFT)，需要大量特定任务的演示数据，并且容易过拟合训练数据，导致在部署环境中，特别是当环境与训练环境存在差异时，性能显著下降。此外，这些模型难以泛化到未见过的任务上，缺乏真正的适应性和自主学习能力。因此，如何使VLA模型能够在实际环境中持续学习和改进，摆脱对大量演示数据的依赖，是本文要解决的核心问题。

**核心思路**：EVOLVE-VLA的核心思路是在测试时利用环境反馈进行持续训练。由于在实际部署环境中，通常无法获得oracle奖励信号，因此需要设计一种自主的反馈机制。论文通过学习一个进度估计器来提供密集的反馈信号，并采用累积估计和渐进式horizon扩展策略来处理反馈信号中的噪声，从而实现策略的稳定演进。这种方法允许VLA模型在与环境交互的过程中不断优化自身策略，提高适应性和泛化能力。

**技术框架**：EVOLVE-VLA框架主要包含以下几个模块：1) VLA模型：作为基础策略模型，负责根据视觉和语言输入生成动作；2) 进度估计器：学习预测当前状态下任务的完成进度，提供密集的反馈信号；3) 累积进度估计机制：通过对一段时间内的进度估计进行累积，平滑噪声，提高反馈信号的可靠性；4) 渐进式horizon扩展策略：逐步增加训练时考虑的时间步长，使模型能够学习更长期的依赖关系；5) 策略优化器：根据累积的进度估计信号，更新VLA模型的参数，使其能够更好地完成任务。

**关键创新**：EVOLVE-VLA最重要的技术创新在于提出了一个基于环境反馈的测试时训练框架，该框架无需依赖oracle奖励信号，而是通过学习到的进度估计器提供自主反馈。此外，累积进度估计机制和渐进式horizon扩展策略有效地解决了反馈信号中的噪声问题，保证了策略的稳定演进。这种方法使得VLA模型能够在实际环境中持续学习和改进，摆脱了对大量演示数据的依赖。

**关键设计**：进度估计器通常采用神经网络结构，输入为当前状态的视觉信息和任务描述，输出为任务完成的进度估计值。累积进度估计机制可以通过滑动平均或指数加权平均等方法实现，用于平滑噪声。渐进式horizon扩展策略可以采用线性或指数方式增加训练时考虑的时间步长。策略优化器可以使用常见的强化学习算法，如PPO或SAC，根据累积的进度估计信号更新VLA模型的参数。

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

实验结果表明，EVOLVE-VLA在长时程任务上取得了8.6%的性能提升，在单样本学习上取得了22.0%的性能提升。更重要的是，EVOLVE-VLA实现了跨任务泛化，在未见任务上无需特定任务演示训练即可达到20.8%的成功率，而纯SFT方法在该场景下的成功率为0%。这些结果表明，EVOLVE-VLA能够有效地提高VLA模型的适应性和泛化能力。

## 🎯 应用场景

EVOLVE-VLA具有广泛的应用前景，例如在家庭服务机器人、工业自动化、医疗辅助机器人等领域。它可以使机器人在实际环境中不断学习和改进，适应不同的任务和环境变化，从而提高机器人的智能化水平和工作效率。此外，该方法还可以应用于虚拟环境中的智能体训练，加速智能体的学习过程。

## 📄 摘要（原文）

> Achieving truly adaptive embodied intelligence requires agents that learn not just by imitating static demonstrations, but by continuously improving through environmental interaction, which is akin to how humans master skills through practice. Vision-Language-Action (VLA) models have advanced robotic manipulation by leveraging large language models, yet remain fundamentally limited by Supervised Finetuning (SFT): requiring hundreds of demonstrations per task, rigidly memorizing trajectories, and failing to adapt when deployment conditions deviate from training. We introduce EVOLVE-VLA, a test-time training framework enabling VLAs to continuously adapt through environment interaction with minimal or zero task-specific demonstrations. The key technical challenge is replacing oracle reward signals (unavailable at test time) with autonomous feedback. We address this through a learned progress estimator providing dense feedback, and critically, we design our framework to ``tame'' this inherently noisy signal via two mechanisms: (1) an accumulative progress estimation mechanism smoothing noisy point-wise estimates, and (2) a progressive horizon extension strategy enabling gradual policy evolution. EVOLVE-VLA achieves substantial gains: +8.6\% on long-horizon tasks, +22.0\% in 1-shot learning, and enables cross-task generalization -- achieving 20.8\% success on unseen tasks without task-specific demonstrations training (vs. 0\% for pure SFT). Qualitative analysis reveals emergent capabilities absent in demonstrations, including error recovery and novel strategies. This work represents a critical step toward VLAs that truly learn and adapt, moving beyond static imitation toward continuous self-improvements.

