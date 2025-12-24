---
layout: default
title: "Growing with Experience: Growing Neural Networks in Deep Reinforcement Learning"
---

# Growing with Experience: Growing Neural Networks in Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11706" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11706v1</a>
  <a href="https://arxiv.org/pdf/2506.11706.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11706v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11706v1', 'Growing with Experience: Growing Neural Networks in Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lukas Fehring, Marius Lindauer, Theresa Eimer

**分类**: cs.LG

**发布日期**: 2025-06-13

**备注**: 3 pages

---

## 💡 一句话要点

**提出GrowNN以解决深度强化学习中网络训练困难问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `神经网络增长` `策略学习` `动态网络` `性能提升`

## 📋 核心要点

1. 现有的强化学习方法在训练中型网络时面临困难，限制了策略的复杂性和表现能力。
2. GrowNN通过在训练过程中逐步增加网络层数，允许网络容量的增长，同时保持网络的可训练性。
3. 实验结果显示，GrowNN在MiniHack和Mujoco环境中显著提升了代理的性能，尤其在复杂任务中表现优越。

## 📝 摘要（中文）

尽管越来越大的模型在机器学习领域引发了革命，但训练中型网络进行强化学习仍然面临挑战。这限制了我们能够学习的策略复杂性。为此，本文提出GrowNN，一种在训练过程中利用渐进式网络增长的简单有效方法。我们首先训练一个小型网络以学习初始策略，然后在不改变编码函数的情况下添加层。后续更新可以利用新增的层来学习更具表现力的策略，随着策略复杂性的增加而增加网络容量。GrowNN可以无缝集成到大多数现有的强化学习代理中。实验结果表明，在MiniHack和Mujoco上的表现有所提升，GrowNN逐步加深的网络在MiniHack Room上比同等大小的静态网络性能提高了48%，在Ant上提高了72%。

## 🔬 方法详解

**问题定义**：本文旨在解决在强化学习中训练中型网络的困难，现有方法在网络容量和训练效率之间存在矛盾，限制了策略的复杂性和表现。

**核心思路**：GrowNN的核心思想是通过逐步增加网络层数来扩展网络容量，而不改变已编码的函数。这种设计使得网络能够在学习初始策略后，随着策略复杂性的增加而动态调整。

**技术框架**：GrowNN的整体架构包括初始的小型网络训练阶段，随后在不改变网络功能的情况下逐步添加新层。每次添加层后，网络可以利用新增的层进行更复杂策略的学习。

**关键创新**：GrowNN的主要创新在于其渐进式网络增长机制，这与传统的静态网络结构形成鲜明对比。通过这种方式，网络能够在训练过程中灵活适应策略的复杂性变化。

**关键设计**：在GrowNN中，关键设计包括层的添加策略、损失函数的选择以及网络结构的动态调整。具体参数设置和训练策略的细节在实验部分进行了详细描述，以确保网络的有效训练和性能提升。

## 📊 实验亮点

实验结果表明，GrowNN在MiniHack Room环境中比同等大小的静态网络性能提高了48%，在Ant环境中提高了72%。这些结果展示了GrowNN在提升强化学习代理性能方面的显著优势，验证了其有效性。

## 🎯 应用场景

GrowNN的研究成果在多个强化学习应用场景中具有潜在价值，包括机器人控制、游戏智能体和自动驾驶等领域。通过提高网络的表达能力，GrowNN能够帮助智能体在复杂环境中做出更优决策，推动智能系统的发展。

## 📄 摘要（原文）

> While increasingly large models have revolutionized much of the machine learning landscape, training even mid-sized networks for Reinforcement Learning (RL) is still proving to be a struggle. This, however, severely limits the complexity of policies we are able to learn. To enable increased network capacity while maintaining network trainability, we propose GrowNN, a simple yet effective method that utilizes progressive network growth during training. We start training a small network to learn an initial policy. Then we add layers without changing the encoded function. Subsequent updates can utilize the added layers to learn a more expressive policy, adding capacity as the policy's complexity increases. GrowNN can be seamlessly integrated into most existing RL agents. Our experiments on MiniHack and Mujoco show improved agent performance, with incrementally GrowNN-deeper networks outperforming their respective static counterparts of the same size by up to 48% on MiniHack Room and 72% on Ant.

