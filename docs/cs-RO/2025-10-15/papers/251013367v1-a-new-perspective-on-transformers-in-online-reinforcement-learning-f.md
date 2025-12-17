---
layout: default
title: A New Perspective on Transformers in Online Reinforcement Learning for Continuous Control
---

# A New Perspective on Transformers in Online Reinforcement Learning for Continuous Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13367" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13367v1</a>
  <a href="https://arxiv.org/pdf/2510.13367.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13367v1" onclick="toggleFavorite(this, '2510.13367v1', 'A New Perspective on Transformers in Online Reinforcement Learning for Continuous Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikita Kachaev, Daniil Zelezetsky, Egor Cherepanov, Alexey K. Kovelev, Aleksandr I. Panov

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-10-15

---

## 💡 一句话要点

**探索Transformer在在线强化学习中的应用，实现连续控制**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Transformer` `在线强化学习` `连续控制` `Actor-Critic` `序列建模`

## 📋 核心要点

1. Transformer在离线RL中表现优异，但在在线无模型RL中应用受限，主要挑战在于其对训练设置和模型设计的敏感性。
2. 本文探索了Transformer在在线无模型RL中连续控制的应用，重点研究了输入调节、组件共享和序列数据切分等关键设计问题。
3. 实验结果表明，通过稳定的架构和训练策略，Transformer可以在多种在线RL任务中实现有竞争力的性能，包括完全和部分可观察环境。

## 📝 摘要（中文）

尽管Transformer在离线或基于模型的强化学习(RL)中表现出色且应用广泛，但在在线无模型RL中，由于其对训练设置和模型设计决策的敏感性，仍未得到充分探索。这些设计决策包括如何构建策略和价值网络、共享组件或处理时间信息。本文表明，Transformer可以作为在线无模型RL中连续控制的强大基线。我们研究了关键的设计问题：如何调节输入、在Actor和Critic之间共享组件以及如何切分序列数据进行训练。实验结果表明，稳定的架构和训练策略能够在完全和部分可观察的任务中，以及在基于向量和图像的环境中实现有竞争力的性能。这些发现为在在线RL中应用Transformer提供了实践指导。

## 🔬 方法详解

**问题定义**：论文旨在解决Transformer在在线无模型强化学习中应用于连续控制任务时面临的挑战。现有方法通常难以训练Transformer，且对超参数敏感，导致性能不稳定。现有研究较少关注如何有效利用Transformer处理在线RL中的序列数据，以及如何设计合适的Actor-Critic结构。

**核心思路**：论文的核心思路是通过系统地研究Transformer在在线RL中的关键设计选择，找到稳定的架构和训练策略。具体而言，探索了不同的输入调节方法、Actor-Critic组件共享策略以及序列数据切分方式，旨在克服Transformer在在线RL中的训练困难，并提升其性能。

**技术框架**：整体框架采用Actor-Critic结构，其中Actor和Critic均基于Transformer构建。输入状态序列经过嵌入层处理后，输入到Transformer编码器中。Actor网络输出动作的均值和方差，Critic网络输出状态-动作值函数。训练过程采用常见的策略梯度算法，如PPO或SAC。论文重点关注Transformer内部的设计，而非具体的RL算法。

**关键创新**：论文的关键创新在于系统地研究了Transformer在在线RL中的应用，并提出了实用的设计指导。通过实验验证了不同设计选择对性能的影响，并找到了相对稳定的架构和训练策略。这为后续研究者在在线RL中使用Transformer提供了有价值的参考。

**关键设计**：论文研究了以下关键设计：1) 输入调节：探索了不同的状态表示方法，如直接使用原始状态或使用状态的差分。2) Actor-Critic组件共享：研究了Actor和Critic之间共享Transformer编码器的不同方式，如完全共享、部分共享或不共享。3) 序列数据切分：探索了不同的序列长度和切分方式，以平衡计算效率和时间依赖性建模能力。此外，论文还关注了学习率、批量大小等超参数的设置。

## 📊 实验亮点

实验结果表明，通过合理的设计选择，Transformer可以在多种在线RL任务中取得与传统方法相当甚至更优的性能。论文在完全和部分可观察的环境中，以及在基于向量和图像的输入下，验证了所提出方法的有效性。这些结果表明，Transformer有潜力成为在线RL中连续控制的强大基线。

## 🎯 应用场景

该研究成果可应用于机器人控制、自动驾驶、游戏AI等领域。通过利用Transformer强大的序列建模能力，可以提升智能体在复杂环境中的决策能力和适应性。未来的研究可以进一步探索Transformer在多智能体强化学习、部分可观察马尔可夫决策过程等更具挑战性的场景中的应用。

## 📄 摘要（原文）

> Despite their effectiveness and popularity in offline or model-based reinforcement learning (RL), transformers remain underexplored in online model-free RL due to their sensitivity to training setups and model design decisions such as how to structure the policy and value networks, share components, or handle temporal information. In this paper, we show that transformers can be strong baselines for continuous control in online model-free RL. We investigate key design questions: how to condition inputs, share components between actor and critic, and slice sequential data for training. Our experiments reveal stable architectural and training strategies enabling competitive performance across fully and partially observable tasks, and in both vector- and image-based settings. These findings offer practical guidance for applying transformers in online RL.

