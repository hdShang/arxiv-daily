---
layout: default
title: Understanding and Improving Hyperbolic Deep Reinforcement Learning
---

# Understanding and Improving Hyperbolic Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14202" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14202v1</a>
  <a href="https://arxiv.org/pdf/2512.14202.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14202v1" onclick="toggleFavorite(this, '2512.14202v1', 'Understanding and Improving Hyperbolic Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Timo Klein, Thomas Lang, Andrii Shkabrii, Alexander Sturm, Kevin Sidak, Lukas Miklautz, Claudia Plant, Yllka Velaj, Sebastian Tschiatschek

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/Probabilistic-and-Interactive-ML/hyper-rl)

---

## 💡 一句话要点

**提出Hyper++，解决双曲深度强化学习中梯度不稳定和训练困难的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `双曲强化学习` `深度强化学习` `庞加莱球` `特征表示` `梯度优化` `近端策略优化` `特征正则化` `分类价值损失`

## 📋 核心要点

1. 双曲空间能有效捕捉RL环境中的层级关系，但其非平稳性给训练带来挑战，现有方法存在梯度不稳定问题。
2. 论文提出Hyper++，通过稳定的评论家训练、特征正则化和优化友好的双曲网络层公式来解决双曲空间中的训练难题。
3. 实验表明，Hyper++在ProcGen和Atari-5上均优于现有方法，提升性能的同时降低了训练时间。

## 📝 摘要（中文）

强化学习（RL）智能体的性能严重依赖于底层特征表示的质量。双曲特征空间非常适合此目的，因为它们自然地捕获复杂RL环境中常见的层级和关系结构。然而，利用这些空间通常面临优化挑战，这是由于RL的非平稳性。本文确定了决定双曲深度RL智能体训练成功与失败的关键因素。通过分析庞加莱球和双曲面模型中核心操作的梯度，我们表明大范数嵌入会破坏基于梯度的训练，导致近端策略优化（PPO）中的信任域违规。基于这些见解，我们引入了Hyper++，这是一种新的双曲PPO智能体，它包含三个组成部分：（i）通过分类价值损失而非回归实现稳定的评论家训练；（ii）特征正则化，保证有界范数，同时避免了裁剪带来的维度灾难；（iii）使用更优化友好的双曲网络层公式。在ProcGen上的实验表明，Hyper++保证了稳定的学习，优于先前的双曲智能体，并将挂钟时间减少了约30%。在Atari-5上使用Double DQN，Hyper++明显优于欧几里德和双曲基线。我们在https://github.com/Probabilistic-and-Interactive-ML/hyper-rl 发布了我们的代码。

## 🔬 方法详解

**问题定义**：论文旨在解决双曲深度强化学习中训练不稳定和性能不佳的问题。现有方法在利用双曲空间的层级结构优势时，常常面临梯度爆炸或消失的困境，尤其是在使用基于梯度的优化算法时，大范数嵌入容易导致信任域违规，使得训练过程难以收敛。

**核心思路**：论文的核心思路是通过稳定评论家训练、特征正则化和优化友好的双曲网络层设计来缓解梯度不稳定问题。具体来说，通过分类价值损失替代回归损失来稳定评论家训练，使用特征正则化来限制嵌入的范数，并采用更易于优化的双曲网络层公式，从而提高训练的稳定性和效率。

**技术框架**：Hyper++框架基于近端策略优化（PPO），主要包含三个核心模块：1) 稳定的评论家训练模块，使用分类价值损失函数；2) 特征正则化模块，用于约束双曲空间中的嵌入范数；3) 优化友好的双曲网络层模块，采用改进的双曲几何计算公式。整体流程与PPO类似，但在特征表示和优化方式上进行了针对双曲空间的改进。

**关键创新**：论文的关键创新在于针对双曲空间的特性，提出了三种有效的策略来稳定训练过程。首先，使用分类价值损失避免了回归损失带来的梯度问题。其次，特征正则化在保证嵌入范数有界的同时，避免了直接裁剪可能导致的维度灾难。最后，优化友好的双曲网络层设计使得梯度传播更加平滑，提升了训练效率。

**关键设计**：在评论家训练中，将价值函数的回归问题转化为分类问题，使用交叉熵损失函数。特征正则化通过在损失函数中添加一个正则项来约束嵌入的范数，避免了直接裁剪。双曲网络层采用黎曼梯度下降，并使用指数映射和对数映射来更新参数。具体参数设置和损失函数权重需要根据具体任务进行调整。

## 📊 实验亮点

实验结果表明，Hyper++在ProcGen上相比之前的双曲智能体，保证了更稳定的学习过程，并将训练时间减少了约30%。在Atari-5上，Hyper++也显著优于欧几里德和双曲基线，证明了其在复杂环境中的有效性。这些结果表明，Hyper++成功解决了双曲深度强化学习中的训练难题，并取得了显著的性能提升。

## 🎯 应用场景

该研究成果可应用于具有层级结构和关系信息的复杂强化学习任务，例如知识图谱推理、社交网络建模、推荐系统和机器人导航等领域。通过更有效地利用双曲空间的表示能力，可以提升智能体的学习效率和决策能力，从而在实际应用中取得更好的效果。

## 📄 摘要（原文）

> The performance of reinforcement learning (RL) agents depends critically on the quality of the underlying feature representations. Hyperbolic feature spaces are well-suited for this purpose, as they naturally capture hierarchical and relational structure often present in complex RL environments. However, leveraging these spaces commonly faces optimization challenges due to the nonstationarity of RL. In this work, we identify key factors that determine the success and failure of training hyperbolic deep RL agents. By analyzing the gradients of core operations in the Poincaré Ball and Hyperboloid models of hyperbolic geometry, we show that large-norm embeddings destabilize gradient-based training, leading to trust-region violations in proximal policy optimization (PPO). Based on these insights, we introduce Hyper++, a new hyperbolic PPO agent that consists of three components: (i) stable critic training through a categorical value loss instead of regression; (ii) feature regularization guaranteeing bounded norms while avoiding the curse of dimensionality from clipping; and (iii) using a more optimization-friendly formulation of hyperbolic network layers. In experiments on ProcGen, we show that Hyper++ guarantees stable learning, outperforms prior hyperbolic agents, and reduces wall-clock time by approximately 30%. On Atari-5 with Double DQN, Hyper++ strongly outperforms Euclidean and hyperbolic baselines. We release our code at https://github.com/Probabilistic-and-Interactive-ML/hyper-rl .

