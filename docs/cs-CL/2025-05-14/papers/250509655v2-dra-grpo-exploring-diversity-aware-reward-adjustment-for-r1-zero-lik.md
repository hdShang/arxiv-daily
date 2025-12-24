---
layout: default
title: DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of Large Language Models
---

# DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.09655" class="toolbar-btn" target="_blank">📄 arXiv: 2505.09655v2</a>
  <a href="https://arxiv.org/pdf/2505.09655.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.09655v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.09655v2', 'DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiwen Chen, Wenhui Zhu, Peijie Qiu, Xuanzhao Dong, Hao Wang, Haiyu Wu, Huayu Li, Aristeidis Sotiras, Yalin Wang, Abolfazl Razi

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-14 (更新: 2025-05-16)

**🔗 代码/项目**: [GITHUB](https://github.com/xiwenc1/DRA-GRPO)

---

## 💡 一句话要点

**提出DRA-GRPO以解决语言模型训练中的多样性奖励调整问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `强化学习` `奖励调整` `多样性感知` `数学推理` `子模互信息` `低资源环境`

## 📋 核心要点

1. 现有的GRPO方法依赖于标量奖励信号，未能有效捕捉语义多样性，导致多样性-质量不一致问题。
2. 提出的DRA方法通过引入子模互信息，显著增强多样性完成的奖励，促进更好的探索与学习。
3. 在五个数学推理基准上，DRA-GRPO方法的平均准确率达到58.2%，表现优于多个强基线，显示出良好的效果。

## 📝 摘要（中文）

近年来，强化学习在语言模型后训练中的进展，如群体相对策略优化（GRPO），在低资源环境中展现出潜力。然而，GRPO通常依赖于解决方案级别和标量奖励信号，未能捕捉采样完成之间的语义多样性，导致我们识别出的多样性-质量不一致问题。为了解决这一局限性，我们提出了多样性感知奖励调整（DRA），该方法明确将语义多样性纳入奖励计算中。DRA使用子模互信息（SMI）来降低冗余完成的权重，并增强多样性完成的奖励，从而鼓励更好的探索，同时保持对高质量样本的稳定利用。我们的方法与GRPO及其变体DR.GRPO无缝集成，形成DRA-GRPO和DGA-DR.GRPO。我们在五个数学推理基准上评估了该方法，发现其超越了近期强基线，平均准确率达到58.2%，仅使用7000个微调样本，总训练成本约为55美元。

## 🔬 方法详解

**问题定义**：现有的GRPO方法在奖励信号上存在局限，未能有效反映不同推理路径的语义多样性，导致多样性-质量不一致的问题。

**核心思路**：DRA方法通过引入子模互信息（SMI），在奖励计算中显式考虑语义多样性，从而降低冗余完成的权重，增强多样性完成的奖励，促进更有效的探索。

**技术框架**：DRA-GRPO方法整合了DRA与GRPO的框架，主要包括奖励调整模块和策略优化模块。奖励调整模块负责计算多样性感知奖励，而策略优化模块则基于这些奖励进行模型训练。

**关键创新**：DRA的核心创新在于通过子模互信息来调整奖励，使得模型在训练过程中能够更好地探索多样性，从而提升整体性能。这一方法与传统的标量奖励机制有本质区别。

**关键设计**：在DRA中，关键参数包括冗余完成的权重调整因子和多样性奖励的放大因子。此外，损失函数设计上也考虑了多样性因素，以确保模型在学习过程中能够平衡探索与利用。

## 📊 实验亮点

在五个数学推理基准上，DRA-GRPO方法的平均准确率达到了58.2%，相比于近期的强基线有显著提升，且仅使用7000个微调样本，总训练成本约为55美元，展现出高效的学习能力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的对话系统、文本生成和自动问答等任务。通过提升模型在低资源环境下的学习能力，DRA-GRPO方法能够为实际应用提供更高质量的生成结果，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in reinforcement learning for language model post-training, such as Group Relative Policy Optimization (GRPO), have shown promise in low-resource settings. However, GRPO typically relies on solution-level and scalar reward signals that fail to capture the semantic diversity among sampled completions. This leads to what we identify as a diversity-quality inconsistency, where distinct reasoning paths may receive indistinguishable rewards. To address this limitation, we propose $\textit{Diversity-aware Reward Adjustment}$ (DRA), a method that explicitly incorporates semantic diversity into the reward computation. DRA uses Submodular Mutual Information (SMI) to downweight redundant completions and amplify rewards for diverse ones. This encourages better exploration during learning, while maintaining stable exploitation of high-quality samples. Our method integrates seamlessly with both GRPO and its variant DR.~GRPO, resulting in $\textit{DRA-GRPO}$ and $\textit{DGA-DR.~GRPO}$. We evaluate our method on five mathematical reasoning benchmarks and find that it outperforms recent strong baselines. It achieves state-of-the-art performance with an average accuracy of 58.2%, using only 7,000 fine-tuning samples and a total training cost of approximately $55. The code is available at https://github.com/xiwenc1/DRA-GRPO.

