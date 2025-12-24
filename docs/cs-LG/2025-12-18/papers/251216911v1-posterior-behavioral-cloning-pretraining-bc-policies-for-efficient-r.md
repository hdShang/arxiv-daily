---
layout: default
title: "Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning"
---

# Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16911" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16911v1</a>
  <a href="https://arxiv.org/pdf/2512.16911.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16911v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16911v1', 'Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrew Wagenmaker, Perry Dong, Raymond Tsao, Chelsea Finn, Sergey Levine

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出后验行为克隆(PostBC)方法，提升RL微调的预训练策略效果**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `后验行为克隆` `强化学习微调` `预训练策略` `机器人控制` `行为克隆` `生成模型` `策略优化`

## 📋 核心要点

1. 现有行为克隆(BC)方法在预训练策略时，无法保证覆盖演示者的所有行为，导致强化学习微调效果不佳。
2. 论文提出后验行为克隆(PostBC)方法，通过建模演示者行为的后验分布，确保预训练策略覆盖演示者的行为。
3. 实验表明，PostBC在机器人控制任务中，显著提升了强化学习微调的性能，优于标准行为克隆。

## 📝 摘要（中文）

本文研究了预训练策略如何影响强化学习(RL)微调的性能，以及如何预训练策略以确保它们是有效的微调初始化。理论上证明，标准行为克隆(BC)无法确保覆盖演示者的行为，这是有效RL微调的必要条件。因此，提出后验行为克隆(PostBC)策略，该策略训练模型来模拟给定演示数据集的演示者行为的后验分布，从而确保覆盖演示者的行为，并实现更有效的微调。PostBC在保证预训练性能不低于BC策略的同时，通过标准监督学习即可在机器人控制领域实际应用，并且与标准行为克隆相比，在真实的机器人控制基准和真实世界的机器人操作任务上，显著提高了RL微调的性能。

## 🔬 方法详解

**问题定义**：现有方法，特别是标准行为克隆(BC)，在预训练策略时，目标是直接模仿演示者的动作。这种方法的痛点在于，它可能无法充分覆盖演示者行为的整个分布，导致预训练策略泛化能力不足，从而限制了后续强化学习(RL)微调的性能。换句话说，如果预训练策略无法探索到演示者可能采取的所有动作，那么RL微调就难以找到更优的策略。

**核心思路**：论文的核心解决思路是，不再仅仅模仿演示者的动作，而是学习演示者行为的后验分布。这意味着，给定演示数据集，模型需要学习生成与演示数据相似的行为，而不是简单地复制。通过建模后验分布，可以确保预训练策略能够覆盖演示者行为的更广泛范围，从而为RL微调提供更好的初始化。

**技术框架**：PostBC的整体框架仍然基于监督学习，但训练目标不同于传统的BC。主要流程包括：1) 收集演示数据集；2) 使用生成模型（如变分自编码器VAE或生成对抗网络GAN）来建模演示者行为的后验分布；3) 使用学习到的后验分布来生成预训练策略。在RL微调阶段，使用预训练的PostBC策略作为RL算法的初始化策略。

**关键创新**：最重要的技术创新点在于，将预训练策略的学习目标从模仿单个动作转变为建模整个行为分布的后验概率。与现有方法的本质区别在于，PostBC不再追求精确匹配演示数据，而是学习生成与演示数据相似的行为，从而提高策略的泛化能力和探索能力。

**关键设计**：PostBC的关键设计包括：1) 选择合适的生成模型来建模后验分布，例如可以使用变分自编码器(VAE)，其中编码器用于推断潜在变量，解码器用于生成动作；2) 设计合适的损失函数，例如可以使用VAE的重构损失和KL散度损失，以确保生成的动作与演示数据相似，并且潜在变量的分布接近先验分布；3) 在RL微调阶段，可以使用各种RL算法，例如PPO或SAC，并调整学习率和探索策略，以充分利用预训练策略的优势。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16911v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16911v1/im/corn_in_pot2.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16911v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，PostBC在多个机器人控制任务中显著优于标准行为克隆。例如，在真实机器人操作任务中，PostBC策略作为RL微调的初始化，能够更快地收敛到更高的性能，并且最终性能也优于使用标准BC策略初始化的RL算法。具体提升幅度取决于任务的复杂程度和RL算法的选择，但总体而言，PostBC能够带来显著的性能提升。

## 🎯 应用场景

PostBC方法可广泛应用于机器人控制、自动驾驶、游戏AI等领域。在机器人控制中，可以利用大量人类演示数据预训练机器人策略，然后通过RL微调，使机器人能够完成复杂的任务。在自动驾驶中，可以利用驾驶员的驾驶数据预训练自动驾驶策略，提高自动驾驶系统的安全性和可靠性。在游戏AI中，可以利用玩家的游戏数据预训练游戏AI策略，提高游戏AI的智能水平和挑战性。

## 📄 摘要（原文）

> Standard practice across domains from robotics to language is to first pretrain a policy on a large-scale demonstration dataset, and then finetune this policy, typically with reinforcement learning (RL), in order to improve performance on deployment domains. This finetuning step has proved critical in achieving human or super-human performance, yet while much attention has been given to developing more effective finetuning algorithms, little attention has been given to ensuring the pretrained policy is an effective initialization for RL finetuning. In this work we seek to understand how the pretrained policy affects finetuning performance, and how to pretrain policies in order to ensure they are effective initializations for finetuning. We first show theoretically that standard behavioral cloning (BC) -- which trains a policy to directly match the actions played by the demonstrator -- can fail to ensure coverage over the demonstrator's actions, a minimal condition necessary for effective RL finetuning. We then show that if, instead of exactly fitting the observed demonstrations, we train a policy to model the posterior distribution of the demonstrator's behavior given the demonstration dataset, we do obtain a policy that ensures coverage over the demonstrator's actions, enabling more effective finetuning. Furthermore, this policy -- which we refer to as the posterior behavioral cloning (PostBC) policy -- achieves this while ensuring pretrained performance is no worse than that of the BC policy. We then show that PostBC is practically implementable with modern generative models in robotic control domains -- relying only on standard supervised learning -- and leads to significantly improved RL finetuning performance on both realistic robotic control benchmarks and real-world robotic manipulation tasks, as compared to standard behavioral cloning.

