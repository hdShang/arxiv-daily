---
layout: default
title: "ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations"
---

# ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.10911" class="toolbar-btn" target="_blank">📄 arXiv: 2505.10911v2</a>
  <a href="https://arxiv.org/pdf/2505.10911.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.10911v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.10911v2', 'ReWiND: Language-Guided Rewards Teach Robot Policies without New Demonstrations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahui Zhang, Yusen Luo, Abrar Anwar, Sumedh Anand Sontakke, Joseph J Lim, Jesse Thomason, Erdem Biyik, Jesse Zhang

**分类**: cs.RO

**发布日期**: 2025-05-16 (更新: 2025-09-19)

**备注**: CoRL 2025 Oral

**🔗 代码/项目**: [PROJECT_PAGE](https://rewind-reward.github.io/)

---

## 💡 一句话要点

**提出ReWiND框架以解决机器人任务学习中的演示依赖问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人学习` `强化学习` `语言指导` `奖励函数` `任务适应性` `数据效率` `无演示学习`

## 📋 核心要点

1. 现有的强化学习和模仿学习方法依赖于专家演示，限制了机器人在新任务上的学习能力。
2. ReWiND框架通过语言指令生成奖励函数，允许机器人在没有新演示的情况下进行任务学习。
3. 实验结果表明，ReWiND在奖励泛化和策略对齐上超越了基线，展示了其在新任务适应性上的优势。

## 📝 摘要（中文）

我们介绍了ReWiND，一个仅通过语言指令学习机器人操作任务的框架，而无需每个任务的演示。传统的强化学习和模仿学习方法需要专家监督，通过人为设计的奖励函数或每个新任务的演示来进行训练。相反，ReWiND从小型演示数据集开始，学习（1）一个数据高效的、语言条件的奖励函数，为数据集标注奖励，以及（2）一个使用这些奖励进行离线强化学习预训练的语言条件策略。对于未见的任务变体，ReWiND使用学习到的奖励函数微调预训练策略，所需的在线交互极少。我们展示了ReWiND的奖励模型在未见任务上有效泛化，在奖励泛化和策略对齐指标上超越基线，提升幅度高达2.4倍。最后，我们证明ReWiND能够高效适应新任务，在仿真中超越基线2倍，并将现实世界的双手预训练策略提升5倍，朝着可扩展的现实世界机器人学习迈出了一步。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人操作任务学习中对专家演示的依赖问题。现有方法需要为每个新任务提供演示，限制了学习的灵活性和效率。

**核心思路**：ReWiND框架的核心思路是通过语言指令生成奖励函数，利用少量演示数据进行学习，从而实现无需新演示的任务适应。这样的设计使得机器人能够在未见任务上进行有效学习。

**技术框架**：ReWiND的整体架构包括两个主要模块：首先是数据高效的语言条件奖励函数生成模块，其次是基于这些奖励进行离线强化学习的策略预训练模块。对于新任务，系统通过微调预训练策略来适应。

**关键创新**：ReWiND的主要创新在于其奖励模型的设计，能够有效泛化到未见任务，显著提升了奖励泛化和策略对齐的性能，与传统方法相比，减少了对新演示的需求。

**关键设计**：在技术细节上，ReWiND采用了特定的损失函数来优化奖励生成，并设计了适合语言条件的网络结构，以确保奖励函数的准确性和有效性。

## 📊 实验亮点

实验结果显示，ReWiND在奖励泛化和策略对齐指标上超越了基线，提升幅度高达2.4倍。在仿真环境中，ReWiND的任务适应性比基线提高了2倍，并在现实世界的双手预训练策略上实现了5倍的提升，展示了其在实际应用中的有效性。

## 🎯 应用场景

ReWiND框架具有广泛的应用潜力，尤其是在需要快速适应新任务的机器人操作场景中，如家庭服务机器人、工业自动化和医疗辅助机器人等。其高效的学习能力将推动机器人在复杂环境中的自主性和灵活性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce ReWiND, a framework for learning robot manipulation tasks solely from language instructions without per-task demonstrations. Standard reinforcement learning (RL) and imitation learning methods require expert supervision through human-designed reward functions or demonstrations for every new task. In contrast, ReWiND starts from a small demonstration dataset to learn: (1) a data-efficient, language-conditioned reward function that labels the dataset with rewards, and (2) a language-conditioned policy pre-trained with offline RL using these rewards. Given an unseen task variation, ReWiND fine-tunes the pre-trained policy using the learned reward function, requiring minimal online interaction. We show that ReWiND's reward model generalizes effectively to unseen tasks, outperforming baselines by up to 2.4x in reward generalization and policy alignment metrics. Finally, we demonstrate that ReWiND enables sample-efficient adaptation to new tasks, beating baselines by 2x in simulation and improving real-world pretrained bimanual policies by 5x, taking a step towards scalable, real-world robot learning. See website at https://rewind-reward.github.io/.

