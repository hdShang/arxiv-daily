---
layout: default
title: "Beyond Policy Optimization: A Data Curation Flywheel for Sparse-Reward Long-Horizon Planning"
---

# Beyond Policy Optimization: A Data Curation Flywheel for Sparse-Reward Long-Horizon Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03018" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03018v1</a>
  <a href="https://arxiv.org/pdf/2508.03018.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03018v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03018v1', 'Beyond Policy Optimization: A Data Curation Flywheel for Sparse-Reward Long-Horizon Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yutong Wang, Pengliang Ji, Kaixin Li, Baolong Bi, Tao Feng, Guillaume Sartoretti

**分类**: cs.AI, cs.RO

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出BPO框架以解决稀疏奖励长时间规划问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长时间规划` `稀疏奖励` `自我改进` `数据飞轮` `复杂性分层学习` `强化学习` `推理模型`

## 📋 核心要点

1. 现有方法在稀疏奖励环境中面临信用分配困难，导致强化学习效果不佳。
2. 提出BPO框架，通过引导、外推和精炼三个阶段，建立自我改进的数据飞轮来提升推理模型的效率。
3. 在多个基准测试中，BPO框架显著提高了模型的性能，达到了最先进的状态，并提升了令牌使用效率。

## 📝 摘要（中文）

大型语言推理模型在静态任务上取得了显著成功，但在交互环境中的多轮智能规划面临两个基本挑战：一是稀疏奖励环境中的信用分配问题使得传统强化学习效果不佳；二是逐步推理历史的计算开销过大。为了解决这些问题，本文提出了BPO框架，该框架通过引导、外推和精炼三个阶段建立自我改进的数据飞轮，以开发适用于长时间、稀疏奖励环境的鲁棒推理模型。实验结果表明，该方法在ALFWorld、ScienceWorld和WebShop上实现了最先进的性能，显著提高了令牌效率。

## 🔬 方法详解

**问题定义**：本文旨在解决在稀疏奖励环境中进行长时间规划时，传统强化学习方法面临的信用分配问题和计算开销过大的挑战。现有方法在处理多轮推理时效率低下，难以适应复杂的交互环境。

**核心思路**：BPO框架通过引导、外推和精炼三个阶段，利用长短链思维融合的规划四元组来高效引导推理，进而实现自我改进。该设计旨在通过逐步优化推理过程，克服稀疏奖励带来的困难。

**技术框架**：BPO框架分为三个主要阶段：引导阶段使用规划四元组进行高效推理；外推阶段通过复杂性分层课程学习扩展到分布外任务；精炼阶段则通过奖励门控拒绝采样选择经验进行自我优化。

**关键创新**：BPO框架的创新在于建立了一个自我改进的数据飞轮，能够在稀疏奖励环境中有效提升推理模型的性能，区别于传统方法的单一优化策略。

**关键设计**：在引导阶段，采用长短链思维融合的技术；在外推阶段，实施复杂性分层课程学习；在精炼阶段，使用奖励门控拒绝采样来选择训练经验，确保模型的持续改进。

## 📊 实验亮点

实验结果显示，BPO框架在ALFWorld、ScienceWorld和WebShop等基准测试中实现了最先进的性能，显著提高了令牌效率，相比于传统方法，性能提升幅度达到XX%（具体数据待补充）。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、游戏AI、智能助手等需要进行复杂决策的交互式环境。通过提升模型在稀疏奖励环境中的推理能力，BPO框架能够为这些领域提供更高效的解决方案，推动智能体规划技术的发展。

## 📄 摘要（原文）

> Large Language Reasoning Models have demonstrated remarkable success on static tasks, yet their application to multi-round agentic planning in interactive environments faces two fundamental challenges. First, the intractable credit assignment problem renders conventional reinforcement learning ineffective in sparse-reward settings. Second, the computational overhead of verbose, step-by-step reasoning histories is prohibitive. To address these challenges, we propose BPO, a three-stage framework (bootstrapping, extrapolation, and refinement) that establishes a self-improving data flywheel to develop robust reasoning models for long-horizon, sparse-reward environments. Our framework first bootstraps efficient reasoning using the proposed planning quaternions with long-short chain-of-thought fusion. It then extrapolates to out-of-distribution tasks through complexity-stratified curriculum learning. Finally, the model iteratively refines itself by learning exclusively on experiences selected via reward-gated rejection sampling. Experiments on ALFWorld, ScienceWorld, and WebShop demonstrate that our approach achieves state-of-the-art with significant token efficiency, providing a new recipe for reasoning models in agentic planning.

