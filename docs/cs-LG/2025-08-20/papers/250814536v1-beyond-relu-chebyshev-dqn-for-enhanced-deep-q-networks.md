---
layout: default
title: "Beyond ReLU: Chebyshev-DQN for Enhanced Deep Q-Networks"
---

# Beyond ReLU: Chebyshev-DQN for Enhanced Deep Q-Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14536" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14536v1</a>
  <a href="https://arxiv.org/pdf/2508.14536.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14536v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14536v1', 'Beyond ReLU: Chebyshev-DQN for Enhanced Deep Q-Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saman Yazdannik, Morteza Tayefi, Shamim Sanisales

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出Chebyshev-DQN以提升深度Q网络性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度Q网络` `切比雪夫多项式` `强化学习` `函数逼近` `模型复杂性`

## 📋 核心要点

1. 现有的深度Q网络在复杂价值函数的近似上存在困难，影响了其学习效率和性能。
2. 本文提出的Chebyshev-DQN通过引入切比雪夫多项式基，改善了特征表示能力，从而提升学习效率。
3. 实验结果显示，Ch-DQN在CartPole-v1基准测试中，性能提升约39%，验证了其有效性和潜力。

## 📝 摘要（中文）

深度Q网络（DQN）的性能依赖于其神经网络准确近似动作价值函数的能力。标准的函数逼近器，如多层感知机，可能难以有效表示许多强化学习问题中复杂的价值景观。本文提出了一种新颖的架构——Chebyshev-DQN（Ch-DQN），将切比雪夫多项式基融入DQN框架，以创建更有效的特征表示。通过利用切比雪夫多项式强大的函数逼近特性，我们假设Ch-DQN能够更高效地学习并实现更高的性能。我们在CartPole-v1基准上评估了所提出的模型，并与具有相似参数数量的标准DQN进行了比较。结果表明，具有适中多项式度数（N=4）的Ch-DQN在渐近性能上显著优于基线，提升约39%。然而，我们也发现多项式度数的选择是一个关键超参数，较高的度数（N=8）可能对学习产生不利影响。

## 🔬 方法详解

**问题定义**：本文旨在解决深度Q网络在复杂强化学习问题中对动作价值函数近似能力不足的问题。现有的多层感知机等标准函数逼近器在表示复杂价值景观时存在局限性。

**核心思路**：论文提出的Chebyshev-DQN通过引入切比雪夫多项式基，利用其优越的函数逼近特性，来增强DQN的特征表示能力，从而提高学习效率和性能。

**技术框架**：Ch-DQN的整体架构包括输入层、切比雪夫多项式基层、隐藏层和输出层。通过切比雪夫多项式的线性组合，网络能够更有效地捕捉复杂的价值函数特征。

**关键创新**：最重要的技术创新在于将切比雪夫多项式基引入深度Q网络中，这一设计使得网络在处理复杂的价值函数时具有更强的表达能力，与传统方法相比，能够更好地适应复杂的强化学习环境。

**关键设计**：在模型设计中，选择了适中的多项式度数（N=4）以获得最佳性能，同时也探讨了高多项式度数（N=8）对学习的负面影响，强调了超参数选择的重要性。

## 📊 实验亮点

实验结果表明，Chebyshev-DQN在CartPole-v1基准测试中，使用N=4的多项式度数时，性能提升约39%，显著优于标准DQN。这一结果验证了切比雪夫多项式基在深度强化学习中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、游戏智能体和自动驾驶等强化学习任务。通过提升深度Q网络的性能，Chebyshev-DQN能够在更复杂的环境中实现更高效的决策，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The performance of Deep Q-Networks (DQN) is critically dependent on the ability of its underlying neural network to accurately approximate the action-value function. Standard function approximators, such as multi-layer perceptrons, may struggle to efficiently represent the complex value landscapes inherent in many reinforcement learning problems. This paper introduces a novel architecture, the Chebyshev-DQN (Ch-DQN), which integrates a Chebyshev polynomial basis into the DQN framework to create a more effective feature representation. By leveraging the powerful function approximation properties of Chebyshev polynomials, we hypothesize that the Ch-DQN can learn more efficiently and achieve higher performance. We evaluate our proposed model on the CartPole-v1 benchmark and compare it against a standard DQN with a comparable number of parameters. Our results demonstrate that the Ch-DQN with a moderate polynomial degree (N=4) achieves significantly better asymptotic performance, outperforming the baseline by approximately 39\%. However, we also find that the choice of polynomial degree is a critical hyperparameter, as a high degree (N=8) can be detrimental to learning. This work validates the potential of using orthogonal polynomial bases in deep reinforcement learning while also highlighting the trade-offs involved in model complexity.

