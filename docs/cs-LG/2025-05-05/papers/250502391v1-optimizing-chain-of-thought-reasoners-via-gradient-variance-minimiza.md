---
layout: default
title: Optimizing Chain-of-Thought Reasoners via Gradient Variance Minimization in Rejection Sampling and RL
---

# Optimizing Chain-of-Thought Reasoners via Gradient Variance Minimization in Rejection Sampling and RL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02391" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02391v1</a>
  <a href="https://arxiv.org/pdf/2505.02391.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02391v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02391v1', 'Optimizing Chain-of-Thought Reasoners via Gradient Variance Minimization in Rejection Sampling and RL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiarui Yao, Yifan Hao, Hanning Zhang, Hanze Dong, Wei Xiong, Nan Jiang, Tong Zhang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-05

**🔗 代码/项目**: [GITHUB](https://github.com/RLHFlow/GVM)

---

## 💡 一句话要点

**提出GVM-RAFT以优化链式推理模型的梯度方差**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `链式推理` `随机梯度` `动态样本分配` `强化学习` `模型训练` `效率提升`

## 📋 核心要点

1. 现有的链式推理训练方法未能有效处理不同提示的难度和收敛行为，导致随机梯度估计效率低下。
2. 论文提出GVM-RAFT，通过动态样本分配策略来最小化随机梯度方差，从而提高训练效率。
3. 实验结果表明，GVM-RAFT在数学推理任务上实现了2-4倍的速度提升和显著的准确性改善。

## 📝 摘要（中文）

链式推理（CoT）在大型语言模型（LLMs）中可以被形式化为一个潜变量问题，模型需要生成中间推理步骤。现有方法如迭代奖励排名微调（RAFT）通常在提示上应用均匀的推理预算，未能考虑难度和收敛行为的变异性。本研究识别出CoT训练的主要瓶颈在于由于静态采样策略导致的随机梯度估计效率低下。我们提出了GVM-RAFT，一种针对提示的动态样本分配策略，旨在在计算预算约束下最小化随机梯度方差。该方法通过监控提示接受率和随机梯度范数动态分配计算资源，确保最终的梯度方差最小化。理论分析表明，所提出的动态采样策略在适当条件下能够加速收敛。实验结果显示，GVM-RAFT在数学推理任务上实现了2-4倍的加速和显著的准确性提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决链式推理（CoT）训练中随机梯度估计效率低下的问题。现有方法如RAFT在处理不同提示时采用静态采样策略，未能有效应对提示的难度变化，导致训练效率低下。

**核心思路**：论文提出了一种动态样本分配策略（GVM-RAFT），通过实时监控提示的接受率和随机梯度范数，动态调整计算资源的分配，以最小化随机梯度方差，从而加速收敛。

**技术框架**：GVM-RAFT的整体架构包括动态样本分配模块、梯度计算模块和收敛监控模块。动态样本分配模块根据实时数据调整计算预算，梯度计算模块负责生成和更新模型的梯度，收敛监控模块则评估训练过程中的收敛情况。

**关键创新**：GVM-RAFT的主要创新在于其动态样本分配策略，能够根据提示的具体情况灵活调整计算资源。这一策略与现有的静态采样方法形成鲜明对比，显著提高了训练效率和模型性能。

**关键设计**：在GVM-RAFT中，关键参数包括动态调整的计算预算、提示接受率的阈值和随机梯度范数的监控机制。损失函数设计上，结合了传统的奖励信号与新的动态采样策略，以确保模型在训练过程中能够有效收敛。

## 📊 实验亮点

实验结果显示，GVM-RAFT在数学推理任务上实现了2-4倍的速度提升，相较于传统的RAFT方法，准确性也有显著改善。这表明动态样本分配策略在提升模型性能方面具有重要作用。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的推理任务、智能问答系统以及其他需要复杂推理能力的AI系统。通过提高链式推理的效率和准确性，GVM-RAFT能够为实际应用提供更强大的支持，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Chain-of-thought (CoT) reasoning in large language models (LLMs) can be formalized as a latent variable problem, where the model needs to generate intermediate reasoning steps. While prior approaches such as iterative reward-ranked fine-tuning (RAFT) have relied on such formulations, they typically apply uniform inference budgets across prompts, which fails to account for variability in difficulty and convergence behavior. This work identifies the main bottleneck in CoT training as inefficient stochastic gradient estimation due to static sampling strategies. We propose GVM-RAFT, a prompt-specific Dynamic Sample Allocation Strategy designed to minimize stochastic gradient variance under a computational budget constraint. The method dynamically allocates computational resources by monitoring prompt acceptance rates and stochastic gradient norms, ensuring that the resulting gradient variance is minimized. Our theoretical analysis shows that the proposed dynamic sampling strategy leads to accelerated convergence guarantees under suitable conditions. Experiments on mathematical reasoning show that GVM-RAFT achieves a 2-4x speedup and considerable accuracy improvements over vanilla RAFT. The proposed dynamic sampling strategy is general and can be incorporated into other reinforcement learning algorithms, such as GRPO, leading to similar improvements in convergence and test accuracy. Our code is available at https://github.com/RLHFlow/GVM.

