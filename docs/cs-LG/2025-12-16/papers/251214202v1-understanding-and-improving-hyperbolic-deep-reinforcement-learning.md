---
layout: default
title: Understanding and Improving Hyperbolic Deep Reinforcement Learning
---

# Understanding and Improving Hyperbolic Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14202" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14202v1</a>
  <a href="https://arxiv.org/pdf/2512.14202.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14202v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14202v1', 'Understanding and Improving Hyperbolic Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Timo Klein, Thomas Lang, Andrii Shkabrii, Alexander Sturm, Kevin Sidak, Lukas Miklautz, Claudia Plant, Yllka Velaj, Sebastian Tschiatschek

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/Probabilistic-and-Interactive-ML/hyper-rl)

---

## 💡 一句话要点

**提出Hyper++，解决双曲深度强化学习中梯度不稳定和训练困难问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `双曲强化学习` `深度强化学习` `庞加莱球` `特征表示` `近端策略优化` `梯度稳定性` `特征正则化`

## 📋 核心要点

1. 双曲空间能有效捕捉RL环境中的层级关系，但其非平稳性给训练带来挑战，现有方法存在梯度不稳定的问题。
2. 论文提出Hyper++，通过稳定的评论家训练、特征正则化和优化友好的双曲网络层公式来解决双曲空间中的训练难题。
3. 实验表明，Hyper++在ProcGen上保证了稳定学习，性能优于现有方法，并减少了30%的训练时间；在Atari-5上显著优于基线。

## 📝 摘要（中文）

强化学习（RL）智能体的性能严重依赖于底层特征表示的质量。双曲特征空间非常适合此目的，因为它们自然地捕获复杂RL环境中常见的层级和关系结构。然而，利用这些空间通常面临优化挑战，这是由于RL的非平稳性。本文确定了决定双曲深度RL智能体训练成功与失败的关键因素。通过分析庞加莱球和双曲面模型中核心操作的梯度，我们表明大范数嵌入会破坏基于梯度的训练，导致近端策略优化（PPO）中的信任域违规。基于这些见解，我们引入了Hyper++，这是一种新的双曲PPO智能体，由三个组件组成：（i）通过分类值损失而非回归实现稳定的评论家训练；（ii）特征正则化，保证有界范数，同时避免裁剪带来的维度灾难；（iii）使用更优化友好的双曲网络层公式。在ProcGen上的实验表明，Hyper++保证了稳定的学习，优于先前的双曲智能体，并将挂钟时间减少了约30%。在Atari-5上使用Double DQN，Hyper++显著优于欧几里德和双曲基线。我们在https://github.com/Probabilistic-and-Interactive-ML/hyper-rl发布了我们的代码。

## 🔬 方法详解

**问题定义**：论文旨在解决双曲深度强化学习中训练不稳定和性能不佳的问题。现有方法在利用双曲空间的优势时，容易受到梯度爆炸或消失的影响，导致训练过程中的信任域违规，最终影响智能体的学习效果。特别是在高维空间中，直接应用现有的欧几里德空间的强化学习算法到双曲空间会遇到优化困难。

**核心思路**：论文的核心思路是通过分析双曲空间中梯度行为，找出导致训练不稳定的关键因素，并针对性地提出改进措施。具体来说，论文发现大范数嵌入是导致梯度不稳定的主要原因，因此通过特征正则化来约束嵌入的范数。此外，论文还通过改进评论家网络的训练方式和优化双曲网络层的公式来提高训练的稳定性。

**技术框架**：Hyper++的整体框架基于近端策略优化（PPO），并针对双曲空间进行了改进。主要包含三个核心模块：1) 稳定的评论家训练模块，使用分类值损失代替回归损失，提高训练稳定性；2) 特征正则化模块，通过正则化保证嵌入的范数有界，避免维度灾难；3) 优化的双曲网络层模块，使用更优化友好的公式，提高梯度传播效率。

**关键创新**：论文的关键创新在于针对双曲空间的特性，提出了三个相互配合的改进措施，共同解决了双曲深度强化学习中的训练难题。与现有方法相比，Hyper++不仅提高了训练的稳定性，还提升了智能体的性能。特征正则化避免了简单裁剪带来的维度灾难，分类值损失避免了回归损失带来的梯度问题，优化的双曲网络层公式则提高了梯度传播效率。

**关键设计**：在评论家网络训练中，使用分类值损失，将值函数的预测转化为分类问题，避免了回归损失带来的梯度不稳定问题。特征正则化采用L2正则化，约束嵌入的范数，防止梯度爆炸。双曲网络层使用Poincaré Ball模型的切空间近似，简化了计算，提高了优化效率。具体参数设置和损失函数权重需要根据具体环境进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14202v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14202v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14202v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Hyper++在ProcGen和Atari-5上进行了实验验证。在ProcGen上，Hyper++保证了稳定的学习，优于先前的双曲智能体，并将挂钟时间减少了约30%。在Atari-5上使用Double DQN，Hyper++显著优于欧几里德和双曲基线，证明了其在复杂环境中的有效性。

## 🎯 应用场景

该研究成果可应用于具有层级和关系结构的复杂强化学习任务，例如机器人导航、游戏AI、推荐系统等。通过利用双曲空间的优势，可以更有效地学习到环境的抽象表示，从而提高智能体的决策能力和泛化能力。未来，该方法有望扩展到其他需要处理复杂关系数据的领域。

## 📄 摘要（原文）

> The performance of reinforcement learning (RL) agents depends critically on the quality of the underlying feature representations. Hyperbolic feature spaces are well-suited for this purpose, as they naturally capture hierarchical and relational structure often present in complex RL environments. However, leveraging these spaces commonly faces optimization challenges due to the nonstationarity of RL. In this work, we identify key factors that determine the success and failure of training hyperbolic deep RL agents. By analyzing the gradients of core operations in the Poincaré Ball and Hyperboloid models of hyperbolic geometry, we show that large-norm embeddings destabilize gradient-based training, leading to trust-region violations in proximal policy optimization (PPO). Based on these insights, we introduce Hyper++, a new hyperbolic PPO agent that consists of three components: (i) stable critic training through a categorical value loss instead of regression; (ii) feature regularization guaranteeing bounded norms while avoiding the curse of dimensionality from clipping; and (iii) using a more optimization-friendly formulation of hyperbolic network layers. In experiments on ProcGen, we show that Hyper++ guarantees stable learning, outperforms prior hyperbolic agents, and reduces wall-clock time by approximately 30%. On Atari-5 with Double DQN, Hyper++ strongly outperforms Euclidean and hyperbolic baselines. We release our code at https://github.com/Probabilistic-and-Interactive-ML/hyper-rl .

