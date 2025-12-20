---
layout: default
title: ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement Learning
---

# ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16861" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16861v1</a>
  <a href="https://arxiv.org/pdf/2512.16861.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16861v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16861v1', 'ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Zhou, Animesh Garg, Ajay Mandlekar, Caelan Garrett

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**ReinforceGen：结合自动数据生成与强化学习的混合技能策略，解决机器人长时程操作难题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作` `强化学习` `模仿学习` `任务分解` `运动规划` `数据生成` `长时程任务`

## 📋 核心要点

1. 长时程操作是机器人领域的长期挑战，现有方法难以有效分解任务和进行长期规划。
2. ReinforceGen通过任务分解、数据生成、模仿学习和运动规划相结合，并使用强化学习进行微调，从而提升性能。
3. 在Robosuite数据集上，ReinforceGen在所有任务上达到了80%的成功率，并且微调方法平均提高了89%的性能。

## 📝 摘要（中文）

本文提出了一种名为ReinforceGen的系统，用于解决机器人领域中长期存在的长时程操作难题。ReinforceGen结合了任务分解、数据生成、模仿学习和运动规划，以形成初始解决方案，并通过基于强化学习的微调来改进每个组件。具体而言，ReinforceGen首先将任务分割成多个局部技能，这些技能通过运动规划连接。技能和运动规划目标通过模仿学习在由10个人类演示生成的数据集上进行训练，然后通过在线自适应和强化学习进行微调。在Robosuite数据集上的基准测试表明，ReinforceGen在最高重置范围设置下，使用视觉运动控制在所有任务上达到了80%的成功率。额外的消融研究表明，我们的微调方法平均提高了89%的性能。

## 🔬 方法详解

**问题定义**：长时程操作任务需要机器人完成一系列复杂的动作，现有方法通常难以有效地分解任务，并且在长期规划中容易出现误差累积，导致任务失败。此外，从零开始训练机器人策略需要大量的样本，而真实世界数据的获取成本很高。

**核心思路**：ReinforceGen的核心思路是将长时程任务分解为多个局部技能，并利用模仿学习从少量人类演示数据中学习这些技能的初始策略。然后，通过强化学习对这些策略进行微调，以提高其鲁棒性和泛化能力。运动规划用于连接这些局部技能，从而完成整个长时程任务。

**技术框架**：ReinforceGen的整体框架包括以下几个主要模块：1) 任务分解：将长时程任务分解为多个局部技能。2) 数据生成：利用少量人类演示数据生成大量的训练数据。3) 模仿学习：使用生成的数据训练局部技能和运动规划目标的初始策略。4) 运动规划：使用运动规划算法连接局部技能，形成完整的任务执行序列。5) 强化学习微调：使用强化学习算法对局部技能和运动规划目标的策略进行微调，以提高其鲁棒性和泛化能力。

**关键创新**：ReinforceGen的关键创新在于将模仿学习和强化学习相结合，并利用自动数据生成来提高训练效率。通过模仿学习，可以从少量人类演示数据中快速学习到初始策略，而强化学习则可以进一步提高策略的性能。自动数据生成可以有效地扩充训练数据集，从而提高策略的泛化能力。

**关键设计**：ReinforceGen使用了一种混合技能策略，其中每个局部技能都由一个独立的策略控制。这些策略可以使用不同的网络结构和损失函数进行训练。强化学习微调使用了PPO算法，并设计了合适的奖励函数来引导策略的学习。运动规划使用了RRT算法，并根据任务的特点进行了优化。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16861v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16861v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16861v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ReinforceGen在Robosuite数据集上取得了显著的成果，在最高重置范围设置下，使用视觉运动控制在所有任务上达到了80%的成功率。消融研究表明，强化学习微调方法对性能提升贡献巨大，平均提高了89%。这些结果表明ReinforceGen是一种有效的长时程操作解决方案。

## 🎯 应用场景

ReinforceGen具有广泛的应用前景，可以应用于各种需要机器人完成复杂操作的任务中，例如装配、抓取、导航等。该研究可以降低机器人部署的成本，提高机器人的智能化水平，并促进机器人技术在工业、医疗、服务等领域的应用。

## 📄 摘要（原文）

> Long-horizon manipulation has been a long-standing challenge in the robotics community. We propose ReinforceGen, a system that combines task decomposition, data generation, imitation learning, and motion planning to form an initial solution, and improves each component through reinforcement-learning-based fine-tuning. ReinforceGen first segments the task into multiple localized skills, which are connected through motion planning. The skills and motion planning targets are trained with imitation learning on a dataset generated from 10 human demonstrations, and then fine-tuned through online adaptation and reinforcement learning. When benchmarked on the Robosuite dataset, ReinforceGen reaches 80% success rate on all tasks with visuomotor controls in the highest reset range setting. Additional ablation studies show that our fine-tuning approaches contributes to an 89% average performance increase. More results and videos available in https://reinforcegen.github.io/

