---
layout: default
title: "From Imitation to Optimization: A Comparative Study of Offline Learning for Autonomous Driving"
---

# From Imitation to Optimization: A Comparative Study of Offline Learning for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07029" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07029v2</a>
  <a href="https://arxiv.org/pdf/2508.07029.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07029v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07029v2', 'From Imitation to Optimization: A Comparative Study of Offline Learning for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antonio Guillen-Perez

**分类**: cs.LG, cs.AI, cs.RO, eess.SY

**发布日期**: 2025-08-09 (更新: 2025-08-27)

---

## 💡 一句话要点

**提出离线强化学习方法以解决自动驾驶中的模仿学习局限性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自动驾驶` `模仿学习` `离线强化学习` `行为克隆` `保守Q学习` `长时间策略` `稳健性` `数据驱动`

## 📋 核心要点

1. 现有的模仿学习方法（如行为克隆）在自动驾驶中存在脆弱性，容易受到累积误差的影响。
2. 本文提出了一种基于保守Q学习的离线强化学习方法，旨在提高驾驶策略的稳健性，特别是在长时间模拟中。
3. 实验结果表明，CQL代理在1,000个未见场景中成功率提高了3.2倍，碰撞率降低了7.4倍，显著优于最强BC基线。

## 📝 摘要（中文）

从大规模现实数据集中学习稳健的驾驶策略是自动驾驶中的核心挑战，因为在线数据收集往往不安全且不切实际。尽管行为克隆（BC）提供了一种直接的模仿学习方法，但使用BC训练的策略通常脆弱，并在闭环执行中遭受累积误差。本文提出了一套综合管道和比较研究，首先开发了一系列日益复杂的BC基线，最终形成了基于Transformer的模型，采用结构化的实体中心状态表示。尽管该模型在模仿损失上表现良好，但在长时间模拟中仍然失败。通过将最先进的离线强化学习算法——保守Q学习（CQL）应用于相同的数据和架构，我们能够学习到显著更稳健的策略。在对1,000个来自Waymo开放运动数据集的未见场景进行的大规模评估中，最终的CQL代理实现了3.2倍的成功率提升和7.4倍的碰撞率降低，证明了离线RL方法在从静态专家数据中学习稳健的长时间驾驶策略中的关键性。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶中模仿学习方法（如行为克隆）在长时间执行中的脆弱性和累积误差问题。现有方法在复杂场景下的表现不佳，难以保证安全性和可靠性。

**核心思路**：论文的核心思路是通过引入保守Q学习（CQL）算法，利用离线强化学习来学习更稳健的驾驶策略。CQL能够在面对小错误时恢复并避免分布外状态，从而提高策略的可靠性。

**技术框架**：整体架构包括多个阶段：首先开发一系列BC基线模型，最后引入基于Transformer的模型，采用结构化的状态表示。随后，利用CQL算法对相同数据进行训练，优化策略。

**关键创新**：最重要的技术创新在于将CQL应用于自动驾驶领域，展示了离线强化学习在模仿学习中的优势，尤其是在长时间任务中的表现。与传统BC方法相比，CQL能够有效减少累积误差。

**关键设计**：在模型设计中，采用了结构化的实体中心状态表示，并精心设计了奖励函数，以引导CQL代理学习保守的价值函数。模型的参数设置和网络结构经过优化，以适应复杂的驾驶场景。

## 📊 实验亮点

实验结果显示，最终的CQL代理在1,000个未见场景中实现了3.2倍的成功率提升和7.4倍的碰撞率降低，相较于最强的BC基线，证明了离线强化学习在学习稳健驾驶策略中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车、智能交通系统和机器人导航等。通过提高驾驶策略的稳健性，能够显著提升自动驾驶系统在复杂和动态环境中的安全性和可靠性，未来可能推动更广泛的自动驾驶技术的应用和普及。

## 📄 摘要（原文）

> Learning robust driving policies from large-scale, real-world datasets is a central challenge in autonomous driving, as online data collection is often unsafe and impractical. While Behavioral Cloning (BC) offers a straightforward approach to imitation learning, policies trained with BC are notoriously brittle and suffer from compounding errors in closed-loop execution. This work presents a comprehensive pipeline and a comparative study to address this limitation. We first develop a series of increasingly sophisticated BC baselines, culminating in a Transformer-based model that operates on a structured, entity-centric state representation. While this model achieves low imitation loss, we show that it still fails in long-horizon simulations. We then demonstrate that by applying a state-of-the-art Offline Reinforcement Learning algorithm, Conservative Q-Learning (CQL), to the same data and architecture, we can learn a significantly more robust policy. Using a carefully engineered reward function, the CQL agent learns a conservative value function that enables it to recover from minor errors and avoid out-of-distribution states. In a large-scale evaluation on 1,000 unseen scenarios from the Waymo Open Motion Dataset, our final CQL agent achieves a 3.2x higher success rate and a 7.4x lower collision rate than the strongest BC baseline, proving that an offline RL approach is critical for learning robust, long-horizon driving policies from static expert data.

