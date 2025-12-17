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

**提出Hyper++以解决双曲深度强化学习中梯度不稳定和优化挑战的问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `双曲几何` `深度强化学习` `近端策略优化` `梯度稳定` `特征正则化` `ProcGen基准` `Atari游戏` `优化挑战`

## 📋 核心要点

1. 核心问题：双曲深度强化学习中，大范数嵌入导致梯度不稳定，破坏训练，尤其在PPO中引发信任区域违反。
2. 方法要点：提出Hyper++，结合分类值损失稳定评论家训练、特征正则化控制范数，以及优化友好的双曲层设计。
3. 实验或效果：在ProcGen上实现稳定学习，性能优于基线，挂钟时间减少30%；在Atari-5上显著超越欧几里得和双曲方法。

## 📝 摘要（中文）

强化学习（RL）智能体的性能关键取决于底层特征表示的质量。双曲特征空间非常适合此目的，因为它们能自然捕捉复杂RL环境中常见的层次和关系结构。然而，由于RL的非平稳性，利用这些空间通常面临优化挑战。在本工作中，我们确定了决定双曲深度RL智能体训练成功与失败的关键因素。通过分析双曲几何的Poincaré Ball和Hyperboloid模型中核心操作的梯度，我们表明大范数嵌入会破坏基于梯度的训练稳定性，导致近端策略优化（PPO）中的信任区域违反。基于这些见解，我们引入了Hyper++，一种新的双曲PPO智能体，包含三个组件：（i）通过分类值损失而非回归实现稳定的评论家训练；（ii）特征正则化保证有界范数，同时避免裁剪带来的维度诅咒；（iii）使用更优化友好的双曲网络层公式。在ProcGen实验中，我们表明Hyper++保证了稳定学习，优于先前的双曲智能体，并将挂钟时间减少了约30%。在Atari-5上使用Double DQN，Hyper++显著优于欧几里得和双曲基线。我们在https://github.com/Probabilistic-and-Interactive-ML/hyper-rl 发布了代码。

## 🔬 方法详解

Hyper++的整体框架基于近端策略优化（PPO），针对双曲特征空间设计。关键技术创新点包括：使用分类值损失替代回归损失以稳定评论家训练，避免梯度爆炸；引入特征正则化机制，确保嵌入范数有界，防止维度诅咒；采用更优化友好的双曲网络层公式，提升训练效率。与现有方法的主要区别在于，它系统解决了双曲RL中的梯度不稳定问题，通过综合组件优化而非单一调整，实现了稳定且高效的训练。

## 📊 实验亮点

在ProcGen基准测试中，Hyper++保证稳定学习，性能优于先前双曲智能体，挂钟时间减少约30%；在Atari-5上使用Double DQN，显著超越欧几里得和双曲基线，验证了方法的有效性和泛化能力。

## 🎯 应用场景

该研究可应用于复杂强化学习环境，如视频游戏（如ProcGen、Atari）、机器人导航和决策系统，其中环境具有层次或关系结构。实际价值在于提升智能体学习效率和稳定性，减少训练时间，推动双曲几何在AI中的实际部署。

## 📄 摘要（原文）

> The performance of reinforcement learning (RL) agents depends critically on the quality of the underlying feature representations. Hyperbolic feature spaces are well-suited for this purpose, as they naturally capture hierarchical and relational structure often present in complex RL environments. However, leveraging these spaces commonly faces optimization challenges due to the nonstationarity of RL. In this work, we identify key factors that determine the success and failure of training hyperbolic deep RL agents. By analyzing the gradients of core operations in the Poincaré Ball and Hyperboloid models of hyperbolic geometry, we show that large-norm embeddings destabilize gradient-based training, leading to trust-region violations in proximal policy optimization (PPO). Based on these insights, we introduce Hyper++, a new hyperbolic PPO agent that consists of three components: (i) stable critic training through a categorical value loss instead of regression; (ii) feature regularization guaranteeing bounded norms while avoiding the curse of dimensionality from clipping; and (iii) using a more optimization-friendly formulation of hyperbolic network layers. In experiments on ProcGen, we show that Hyper++ guarantees stable learning, outperforms prior hyperbolic agents, and reduces wall-clock time by approximately 30%. On Atari-5 with Double DQN, Hyper++ strongly outperforms Euclidean and hyperbolic baselines. We release our code at https://github.com/Probabilistic-and-Interactive-ML/hyper-rl .

