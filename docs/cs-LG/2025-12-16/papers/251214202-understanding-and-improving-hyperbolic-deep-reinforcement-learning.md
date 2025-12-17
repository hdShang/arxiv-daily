---
layout: default
title: Understanding and Improving Hyperbolic Deep Reinforcement Learning
---

# Understanding and Improving Hyperbolic Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14202" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14202</a>
  <a href="https://arxiv.org/pdf/2512.14202.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14202" onclick="toggleFavorite(this, '2512.14202', 'Understanding and Improving Hyperbolic Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Timo Klein, Thomas Lang, Andrii Shkabrii, Alexander Sturm, Kevin Sidak, Lukas Miklautz, Claudia Plant, Yllka Velaj, Sebastian Tschiatschek

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出Hyper++，稳定双曲深度强化学习，提升ProcGen和Atari性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `双曲强化学习` `深度强化学习` `庞加莱球` `特征表示` `近端策略优化` `ProcGen` `Atari` `梯度稳定`

## 📋 核心要点

1. 现有双曲深度强化学习方法在非平稳环境中面临优化挑战，大范数嵌入导致梯度不稳定和信任域违规。
2. Hyper++通过分类价值损失、特征正则化和优化友好的双曲网络层公式，稳定训练过程，避免维度灾难。
3. 实验表明，Hyper++在ProcGen上保证稳定学习，减少运行时间，并在Atari-5上显著优于欧几里德和双曲基线。

## 📝 摘要（中文）

强化学习（RL）智能体的性能严重依赖于底层特征表示的质量。双曲特征空间非常适合此目的，因为它们自然地捕获了复杂RL环境中常见的层级和关系结构。然而，利用这些空间通常面临由于RL的非平稳性带来的优化挑战。在这项工作中，我们确定了决定双曲深度RL智能体训练成功与失败的关键因素。通过分析庞加莱球和双曲面模型中核心操作的梯度，我们表明大范数嵌入会破坏基于梯度的训练，导致近端策略优化（PPO）中的信任域违规。基于这些见解，我们引入了Hyper++，一种新的双曲PPO智能体，它由三个组件组成：（i）通过分类价值损失而非回归实现稳定的评论家训练；（ii）特征正则化，保证有界范数，同时避免了裁剪带来的维度灾难；（iii）使用更优化友好的双曲网络层公式。在ProcGen上的实验表明，Hyper++保证了稳定的学习，优于先前的双曲智能体，并将实际运行时间减少了约30%。在Atari-5上使用Double DQN，Hyper++显著优于欧几里德和双曲基线。我们在此URL发布了我们的代码。

## 🔬 方法详解

**问题定义**：论文旨在解决双曲深度强化学习中训练不稳定的问题。现有方法在利用双曲空间的层级结构优势时，容易受到大范数嵌入的影响，导致梯度爆炸或消失，进而破坏策略优化过程的稳定性。特别是在使用PPO等算法时，信任域容易被违反，导致训练崩溃。

**核心思路**：论文的核心思路是通过稳定评论家训练、正则化特征范数以及优化双曲网络层公式来解决训练不稳定性问题。通过限制嵌入的范数，避免梯度爆炸，并采用更适合优化的网络结构，从而提高双曲深度强化学习的性能。

**技术框架**：Hyper++框架主要包含三个核心模块：(1) 稳定的评论家训练：使用分类价值损失代替回归，避免了回归损失对异常值的敏感性，从而稳定了评论家的训练。(2) 特征正则化：通过正则化项约束特征的范数，防止其过大，从而避免梯度爆炸，同时避免了直接裁剪可能导致的维度灾难。(3) 优化友好的双曲网络层：采用更适合优化的双曲网络层公式，例如使用黎曼梯度下降等方法，提高训练效率。

**关键创新**：Hyper++的关键创新在于其综合性的稳定训练方法。它不仅关注了评论家的训练，还通过特征正则化和网络层优化，从多个角度解决了双曲深度强化学习中的训练不稳定性问题。与之前的双曲强化学习方法相比，Hyper++更加注重优化过程的稳定性，从而能够更好地利用双曲空间的优势。

**关键设计**：(1) 分类价值损失：将价值函数的回归问题转化为分类问题，使用交叉熵损失函数进行训练。(2) 特征正则化：在损失函数中添加L2正则化项，约束特征的范数。(3) 双曲网络层：使用Poincaré Ball或Hyperboloid模型，并采用黎曼梯度下降等优化方法。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14202/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14202/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14202/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Hyper++在ProcGen环境上实现了稳定的学习，并且相比之前的双曲智能体，运行时间减少了约30%。在Atari-5环境上，Hyper++使用Double DQN算法，显著优于欧几里德和双曲基线方法，表明了其在复杂环境下的优越性能。这些实验结果验证了Hyper++在稳定训练和提升性能方面的有效性。

## 🎯 应用场景

该研究成果可应用于具有层级结构和关系结构的复杂强化学习任务，例如机器人导航、游戏AI、推荐系统等。通过利用双曲空间的优势，可以更有效地学习到环境的抽象表示，从而提高智能体的决策能力和泛化性能。未来，该方法有望在更多实际场景中得到应用，例如自动驾驶、金融交易等。

## 📄 摘要（原文）

> The performance of reinforcement learning (RL) agents depends critically on the quality of the underlying feature representations. Hyperbolic feature spaces are well-suited for this purpose, as they naturally capture hierarchical and relational structure often present in complex RL environments. However, leveraging these spaces commonly faces optimization challenges due to the nonstationarity of RL. In this work, we identify key factors that determine the success and failure of training hyperbolic deep RL agents. By analyzing the gradients of core operations in the Poincaré Ball and Hyperboloid models of hyperbolic geometry, we show that large-norm embeddings destabilize gradient-based training, leading to trust-region violations in proximal policy optimization (PPO). Based on these insights, we introduce Hyper++, a new hyperbolic PPO agent that consists of three components: (i) stable critic training through a categorical value loss instead of regression; (ii) feature regularization guaranteeing bounded norms while avoiding the curse of dimensionality from clipping; and (iii) using a more optimization-friendly formulation of hyperbolic network layers. In experiments on ProcGen, we show that Hyper++ guarantees stable learning, outperforms prior hyperbolic agents, and reduces wall-clock time by approximately 30%. On Atari-5 with Double DQN, Hyper++ strongly outperforms Euclidean and hyperbolic baselines. We release our code atthis https URL.

