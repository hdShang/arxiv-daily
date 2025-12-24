---
layout: default
title: "EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework"
---

# EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22200" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22200v5</a>
  <a href="https://arxiv.org/pdf/2506.22200.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22200v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22200v5', 'EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Wang, Lai Wei, Yanzhi Zhang, Chenyang Shao, Zedong Dan, Weiran Huang, Yuzhi Zhang, Yue Wang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-27 (更新: 2025-10-10)

**🔗 代码/项目**: [GITHUB](https://github.com/597358816/EFRame)

---

## 💡 一句话要点

**提出EFRame框架以解决GRPO在复杂推理任务中的不足**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `推理能力` `探索策略` `样本过滤` `经验重放` `自然语言处理` `深度学习`

## 📋 核心要点

1. 现有的GRPO方法在复杂推理任务中面临探索不足和训练不稳定的问题，限制了其有效性。
2. EFRame框架通过额外回合、在线过滤和经验重放三方面增强GRPO，旨在实现更深层次的推理能力。
3. 实验结果显示，EFRame在多个推理基准上表现优异，特别是在Geometry3K上相较于GRPO提升了37.9%。

## 📝 摘要（中文）

近年来，强化学习（RL）的进展显著提升了大型语言模型（LLMs）的推理能力。尽管相对策略优化（GRPO）作为一种轻量级的近端策略优化（PPO）变体提高了效率，但其探索能力有限和训练不稳定性限制了其在复杂推理任务中的有效性。为了解决这些挑战，我们提出了EFRame，一个探索-过滤-重放框架，通过额外的回合实现更深层次和更有针对性的探索，在线过滤去除低质量样本以稳定梯度并加速训练，以及经验重放放大稀有但信息丰富的轨迹以实现稳定收敛。实验表明，EFRame在多种推理基准上取得了一致的提升，包括在Geometry3K上相较于GRPO实现了37.9%的相对改善。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有GRPO方法在复杂推理任务中的探索不足和训练不稳定性问题，这些问题限制了其在实际应用中的有效性。

**核心思路**：EFRame框架通过引入额外的回合以实现更深层次的探索，同时通过在线过滤和经验重放来提高训练的稳定性和效率。这样的设计旨在平衡探索与效率，确保模型在复杂任务中的表现。

**技术框架**：EFRame的整体架构包括三个主要模块：1) 额外回合用于深度探索；2) 在线过滤模块用于去除低质量样本；3) 经验重放模块用于放大稀有且信息丰富的轨迹。这些模块共同构成了一个统一的训练循环。

**关键创新**：EFRame的主要创新在于其探索-过滤-重放的统一框架，显著提升了GRPO的训练效率和稳定性。这种设计与传统方法的本质区别在于其能够动态调整探索策略和样本质量。

**关键设计**：在参数设置上，EFRame采用了自适应的过滤阈值和重放策略，以确保在训练过程中始终保持高质量的样本流。此外，损失函数的设计也考虑了样本的多样性和信息量，以进一步提升模型的推理能力。

## 📊 实验亮点

在实验中，EFRame在多个推理基准上表现出色，特别是在Geometry3K数据集上实现了37.9%的相对提升，相较于GRPO显示出显著的性能改进。这一结果验证了EFRame在复杂推理任务中的有效性和优势。

## 🎯 应用场景

EFRame框架具有广泛的潜在应用场景，尤其是在需要复杂推理的自然语言处理任务中，如问答系统、对话生成和文本理解等。其提升的推理能力和训练稳定性将为实际应用提供更强的支持，推动智能助手和自动化系统的发展。未来，EFRame的设计理念也可能被应用于其他领域的强化学习任务中。

## 📄 摘要（原文）

> Recent advances in reinforcement learning (RL) have significantly enhanced the reasoning capabilities of large language models (LLMs). Group Relative Policy Optimization (GRPO), a lightweight variant of Proximal Policy Optimization (PPO), improves efficiency but suffers from limited exploration and training instability, limiting its effectiveness on complex reasoning tasks. To address these challenges, we introduce EFRame, an Exploration-Filter-Replay framework that augments GRPO across three dimensions: additional rollouts enable deeper and more targeted exploration, online filtering removes low-quality samples to stabilize gradients and accelerate training, and experience replay amplifies rare yet informative trajectories for stable convergence. This unified framework establishes a principled training cycle that balances exploration, efficiency, and stability. Experiments on diverse reasoning benchmarks demonstrate that EFRame achieves consistent gains, including a 37.9\% relative improvement on Geometry3K over GRPO. EFRame further supports fine-grained sample categorization and precise entropy control, highlighting it as a robust solution for advancing deeper reasoning in LLMs. Our code is available at https://github.com/597358816/EFRame.

