---
layout: default
title: "Disentangled Multi-Context Meta-Learning: Unlocking robust and Generalized Task Learning"
---

# Disentangled Multi-Context Meta-Learning: Unlocking robust and Generalized Task Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01297" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01297v1</a>
  <a href="https://arxiv.org/pdf/2509.01297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01297v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01297v1', 'Disentangled Multi-Context Meta-Learning: Unlocking robust and Generalized Task Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seonsoo Kim, Jun-Gill Kang, Taehong Kim, Seongil Hong

**分类**: cs.RO

**发布日期**: 2025-09-01

**备注**: Accepted to The Conference on Robot Learning (CoRL) 2025 Project Page: seonsoo-p1.github.io/DMCM

---

## 💡 一句话要点

**提出解耦多上下文元学习框架，提升任务泛化性和鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `元学习` `解耦表示` `上下文向量` `泛化能力` `鲁棒性` `机器人控制` `sim-to-real`

## 📋 核心要点

1. 现有元学习方法依赖于隐式适应任务变化，多种因素混合在单一表征中，限制了泛化能力。
2. 论文提出解耦多上下文元学习框架，将每个任务因素显式分配到独立的上下文向量。
3. 实验表明，该方法在正弦回归和四足机器人运动任务中，均提升了鲁棒性和泛化能力。

## 📝 摘要（中文）

本文提出了一种解耦多上下文元学习框架，旨在解决元学习中任务变异因素混合在单一表征中导致的泛化性问题。该框架显式地将每个任务因素分配给一个独立的上下文向量，通过解耦这些变异，加深对任务的理解，从而提高鲁棒性。同时，通过在具有共享因素的任务之间共享上下文向量，增强泛化能力。在正弦回归任务中，该模型优于现有方法，并通过共享与幅度和相位移相关的上下文向量，泛化到未见过的正弦函数。在四足机器人运动任务中，该模型解耦了机器人特定属性和地形特征，并将从动力学模型中获得的解耦上下文向量迁移到强化学习中，从而在超出分布的条件下实现了更好的鲁棒性。此外，通过有效地共享上下文，该模型仅使用来自平坦地形的20秒真实数据，就实现了成功的模拟到真实策略迁移，解决了单任务自适应无法应对的具有超出分布机器人特定属性的复杂地形问题。

## 🔬 方法详解

**问题定义**：现有元学习方法通常将所有任务变异因素混合在单个表征中，导致难以解释哪些因素驱动性能，并且阻碍了模型的泛化能力。特别是在面对分布外（out-of-distribution）的任务时，这种耦合的表征方式难以适应新的任务环境，导致性能下降。

**核心思路**：论文的核心思路是将不同的任务因素（例如，正弦函数的幅度和相位，或者四足机器人的自身属性和地形特征）解耦，并分别用独立的上下文向量来表示。通过这种解耦，模型可以更好地理解每个因素对任务的影响，并且可以通过共享上下文向量来实现跨任务的知识迁移，从而提高泛化能力。

**技术框架**：整体框架包含一个元学习器和一个上下文向量生成器。元学习器负责学习如何利用上下文向量来适应不同的任务。上下文向量生成器负责将任务的观测信息编码成一组解耦的上下文向量，每个向量对应一个特定的任务因素。在训练过程中，模型会学习如何将任务因素解耦，并生成相应的上下文向量。在测试过程中，模型可以使用已学习到的上下文向量来适应新的任务，或者通过共享上下文向量来实现跨任务的知识迁移。

**关键创新**：最重要的创新点在于显式地解耦了任务中的不同因素，并使用独立的上下文向量来表示它们。这种解耦使得模型可以更好地理解任务的结构，并且可以通过共享上下文向量来实现跨任务的知识迁移。与现有方法相比，该方法能够更好地适应分布外的任务，并且具有更好的泛化能力。

**关键设计**：论文中使用了特定的网络结构来实现上下文向量的解耦。例如，在四足机器人运动任务中，使用了两个独立的编码器分别提取机器人属性和地形特征，并将它们的输出作为上下文向量。此外，论文还设计了特定的损失函数来鼓励上下文向量的解耦。例如，可以使用互信息最小化等方法来减少不同上下文向量之间的相关性。

## 📊 实验亮点

在正弦回归任务中，该模型在超出分布的任务上优于基线方法，并且能够通过共享上下文向量泛化到未见过的正弦函数。在四足机器人运动任务中，该模型仅使用20秒的真实数据，就实现了成功的模拟到真实策略迁移，解决了单任务自适应无法应对的复杂地形问题，显著提升了机器人在未知环境下的适应能力。

## 🎯 应用场景

该研究成果可应用于机器人控制、自动驾驶、医疗诊断等领域。通过解耦任务中的不同因素，可以提高模型在复杂环境下的鲁棒性和泛化能力，从而实现更可靠、更智能的系统。例如，在机器人控制中，可以解耦机器人自身属性和环境因素，从而使机器人能够更好地适应不同的环境。

## 📄 摘要（原文）

> In meta-learning and its downstream tasks, many methods rely on implicit adaptation to task variations, where multiple factors are mixed together in a single entangled representation. This makes it difficult to interpret which factors drive performance and can hinder generalization. In this work, we introduce a disentangled multi-context meta-learning framework that explicitly assigns each task factor to a distinct context vector. By decoupling these variations, our approach improves robustness through deeper task understanding and enhances generalization by enabling context vector sharing across tasks with shared factors. We evaluate our approach in two domains. First, on a sinusoidal regression task, our model outperforms baselines on out-of-distribution tasks and generalizes to unseen sine functions by sharing context vectors associated with shared amplitudes or phase shifts. Second, in a quadruped robot locomotion task, we disentangle the robot-specific properties and the characteristics of the terrain in the robot dynamics model. By transferring disentangled context vectors acquired from the dynamics model into reinforcement learning, the resulting policy achieves improved robustness under out-of-distribution conditions, surpassing the baselines that rely on a single unified context. Furthermore, by effectively sharing context, our model enables successful sim-to-real policy transfer to challenging terrains with out-of-distribution robot-specific properties, using just 20 seconds of real data from flat terrain, a result not achievable with single-task adaptation.

