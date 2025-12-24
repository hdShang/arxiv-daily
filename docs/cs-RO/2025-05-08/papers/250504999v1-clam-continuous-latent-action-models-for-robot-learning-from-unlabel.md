---
layout: default
title: CLAM: Continuous Latent Action Models for Robot Learning from Unlabeled Demonstrations
---

# CLAM: Continuous Latent Action Models for Robot Learning from Unlabeled Demonstrations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.04999" class="toolbar-btn" target="_blank">📄 arXiv: 2505.04999v1</a>
  <a href="https://arxiv.org/pdf/2505.04999.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.04999v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.04999v1', 'CLAM: Continuous Latent Action Models for Robot Learning from Unlabeled Demonstrations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anthony Liang, Pavel Czempin, Matthew Hong, Yutai Zhou, Erdem Biyik, Stephen Tu

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-05-08

**备注**: Latent Action Models, Self-supervised Pretraining, Learning from Videos

---

## 💡 一句话要点

**提出CLAM以解决机器人无标签示范学习中的动作标注问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模仿学习` `无标签学习` `机器人控制` `潜在动作模型` `动作解码器` `复杂任务` `深度学习`

## 📋 核心要点

1. 现有模仿学习方法依赖大量带标签的专家示范，限制了数据规模和学习效率。
2. CLAM模型采用连续潜在动作标签，并通过联合训练动作解码器来解决复杂控制任务。
3. 在DMControl和MetaWorld基准测试中，CLAM的任务成功率较最佳基线提高了2-3倍，表现显著优越。

## 📝 摘要（中文）

在模仿学习中，学习机器人策略通常需要大量昂贵的带标签专家示范，这限制了训练数据的规模。为了解决这一瓶颈，本文提出了一种利用无标签观察（如视频示范）来无监督学习潜在动作标签的方法。现有方法在处理复杂机器人任务时表现不佳，因此我们设计了连续潜在动作模型（CLAM），该模型采用连续潜在动作标签并联合训练动作解码器，以便在没有任何带标签专家数据的情况下，从非最优游戏数据中学习有效策略。实验结果表明，CLAM在DMControl和MetaWorld的连续控制基准测试中显著超越了现有最先进的方法，任务成功率提升了2-3倍。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人学习中对大量带标签示范的依赖问题。现有方法在复杂任务中难以有效处理细粒度动作，限制了学习效果。

**核心思路**：CLAM模型通过引入连续潜在动作标签，替代离散表示，能够更好地捕捉复杂动作的细节。同时，联合训练的动作解码器确保潜在动作空间能够与真实动作有效对接。

**技术框架**：CLAM的整体架构包括两个主要模块：潜在动作标签生成模块和动作解码器。潜在动作标签通过无标签观察数据生成，而动作解码器则通过少量带标签示范进行训练，以实现潜在动作与实际动作的映射。

**关键创新**：CLAM的主要创新在于采用连续潜在动作标签和联合训练的解码器，这与传统方法的离散标签表示形成鲜明对比，使得模型在复杂控制任务中表现更佳。

**关键设计**：在模型设计中，关键参数包括潜在动作空间的维度和解码器的网络结构，损失函数则结合了重构损失和动作预测损失，以确保模型的有效性和稳定性。

## 📊 实验亮点

在实验中，CLAM在DMControl和MetaWorld的连续控制任务中表现出色，任务成功率相比最佳基线提高了2-3倍，显著超越了现有最先进的方法，展示了其在复杂任务学习中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和人机协作等。通过减少对带标签数据的依赖，CLAM能够在资源有限的情况下，提升机器人学习的效率和灵活性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Learning robot policies using imitation learning requires collecting large amounts of costly action-labeled expert demonstrations, which fundamentally limits the scale of training data. A promising approach to address this bottleneck is to harness the abundance of unlabeled observations-e.g., from video demonstrations-to learn latent action labels in an unsupervised way. However, we find that existing methods struggle when applied to complex robot tasks requiring fine-grained motions. We design continuous latent action models (CLAM) which incorporate two key ingredients we find necessary for learning to solve complex continuous control tasks from unlabeled observation data: (a) using continuous latent action labels instead of discrete representations, and (b) jointly training an action decoder to ensure that the latent action space can be easily grounded to real actions with relatively few labeled examples. Importantly, the labeled examples can be collected from non-optimal play data, enabling CLAM to learn performant policies without access to any action-labeled expert data. We demonstrate on continuous control benchmarks in DMControl (locomotion) and MetaWorld (manipulation), as well as on a real WidowX robot arm that CLAM significantly outperforms prior state-of-the-art methods, remarkably with a 2-3x improvement in task success rate compared to the best baseline. Videos and code can be found at clamrobot.github.io.

