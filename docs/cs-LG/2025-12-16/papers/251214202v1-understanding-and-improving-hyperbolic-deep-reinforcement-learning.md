---
layout: default
title: Understanding and Improving Hyperbolic Deep Reinforcement Learning
---

# Understanding and Improving Hyperbolic Deep Reinforcement Learning

**arXiv**: [2512.14202v1](https://arxiv.org/abs/2512.14202) | [PDF](https://arxiv.org/pdf/2512.14202.pdf)

**作者**: Timo Klein, Thomas Lang, Andrii Shkabrii, Alexander Sturm, Kevin Sidak, Lukas Miklautz, Claudia Plant, Yllka Velaj, Sebastian Tschiatschek

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/Probabilistic-and-Interactive-ML/hyper-rl)

---

## 💡 一句话要点

**提出Hyper++方法以解决双曲深度强化学习中的优化不稳定问题，在ProcGen和Atari-5环境中实现稳定高效训练。**

**关键词**: `双曲几何` `深度强化学习` `近端策略优化` `特征正则化` `梯度稳定` `程序生成环境` `Atari游戏` `优化挑战`

## 📋 核心要点

1. 核心问题：双曲深度强化学习面临优化挑战，大范数嵌入导致梯度训练不稳定，破坏PPO的信任区域约束。
2. 方法要点：提出Hyper++智能体，结合分类值损失、特征正则化和优化友好双曲层，确保稳定训练和高效性能。
3. 实验或效果：在ProcGen和Atari-5环境中，Hyper++实现稳定学习，性能优于基线，训练时间减少约30%。

## 📝 摘要（中文）

强化学习（RL）智能体的性能关键取决于底层特征表示的质量。双曲特征空间非常适合此目的，因为它们能自然捕捉复杂RL环境中常见的层次和关系结构。然而，由于RL的非平稳性，利用这些空间通常面临优化挑战。在这项工作中，我们确定了决定双曲深度RL智能体训练成败的关键因素。通过分析双曲几何的庞加莱球和双曲面模型中核心操作的梯度，我们发现大范数嵌入会破坏基于梯度的训练稳定性，导致近端策略优化（PPO）中的信任区域违反。基于这些见解，我们引入了Hyper++，一种新的双曲PPO智能体，包含三个组件：（i）通过分类值损失而非回归实现稳定的评论家训练；（ii）特征正则化保证有界范数，同时避免裁剪带来的维度诅咒；（iii）使用更优化友好的双曲网络层公式。在ProcGen实验中，我们表明Hyper++保证了稳定学习，优于先前的双曲智能体，并将挂钟时间减少了约30%。在Atari-5与Double DQN中，Hyper++显著优于欧几里得和双曲基线。我们在https://github.com/Probabilistic-and-Interactive-ML/hyper-rl 发布了代码。

## 🔬 方法详解

Hyper++的整体框架基于近端策略优化（PPO），在双曲特征空间中操作。关键技术创新点包括：使用分类值损失替代回归损失来稳定评论家训练，避免梯度爆炸；引入特征正则化机制，约束嵌入范数在合理范围内，防止大范数问题，同时避免传统裁剪方法导致的维度诅咒；采用更优化友好的双曲网络层设计，改进梯度流。与现有方法的主要区别在于，它系统解决了双曲RL中的优化不稳定问题，通过理论分析和工程优化，实现了更鲁棒和高效的双曲深度强化学习。

## 📊 实验亮点

在ProcGen实验中，Hyper++保证稳定学习，优于先前双曲智能体，并将挂钟时间减少约30%。在Atari-5与Double DQN中，Hyper++显著超越欧几里得和双曲基线，展示了其高效性和泛化能力。

## 🎯 应用场景

该研究可应用于复杂强化学习环境，如视频游戏（如Atari）、程序生成环境（如ProcGen）和机器人控制，其中环境具有层次或关系结构。通过稳定双曲特征学习，能提升智能体在结构化任务中的性能和训练效率，具有实际价值于自动化决策和智能系统开发。

## 📄 摘要（原文）

> The performance of reinforcement learning (RL) agents depends critically on the quality of the underlying feature representations. Hyperbolic feature spaces are well-suited for this purpose, as they naturally capture hierarchical and relational structure often present in complex RL environments. However, leveraging these spaces commonly faces optimization challenges due to the nonstationarity of RL. In this work, we identify key factors that determine the success and failure of training hyperbolic deep RL agents. By analyzing the gradients of core operations in the Poincaré Ball and Hyperboloid models of hyperbolic geometry, we show that large-norm embeddings destabilize gradient-based training, leading to trust-region violations in proximal policy optimization (PPO). Based on these insights, we introduce Hyper++, a new hyperbolic PPO agent that consists of three components: (i) stable critic training through a categorical value loss instead of regression; (ii) feature regularization guaranteeing bounded norms while avoiding the curse of dimensionality from clipping; and (iii) using a more optimization-friendly formulation of hyperbolic network layers. In experiments on ProcGen, we show that Hyper++ guarantees stable learning, outperforms prior hyperbolic agents, and reduces wall-clock time by approximately 30%. On Atari-5 with Double DQN, Hyper++ strongly outperforms Euclidean and hyperbolic baselines. We release our code at https://github.com/Probabilistic-and-Interactive-ML/hyper-rl .

