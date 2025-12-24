---
layout: default
title: "Offline vs. Online Learning in Model-based RL: Lessons for Data Collection Strategies"
---

# Offline vs. Online Learning in Model-based RL: Lessons for Data Collection Strategies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05735" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05735v1</a>
  <a href="https://arxiv.org/pdf/2509.05735.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05735v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05735v1', 'Offline vs. Online Learning in Model-based RL: Lessons for Data Collection Strategies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaqi Chen, Ji Shi, Cansu Sancaktar, Jonas Frey, Georg Martius

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-06

**备注**: Accepted at Reinforcement Learning Conference (RLC 2025); Code available at: https://github.com/swsychen/Offline_vs_Online_in_MBRL

---

## 💡 一句话要点

**模型强化学习中离线与在线学习对比研究，揭示数据收集策略对性能的影响**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模型强化学习` `离线学习` `在线学习` `数据收集策略` `世界模型`

## 📋 核心要点

1. 基于模型的强化学习依赖高质量数据，但在线和离线数据收集策略对世界模型的影响尚不明确。
2. 该研究对比了在线和离线学习范式，发现离线智能体由于分布外状态导致性能下降。
3. 通过引入额外的在线交互或探索数据，可以有效缓解离线智能体的性能问题，恢复在线训练的优势。

## 📝 摘要（中文）

数据收集对于在基于模型的强化学习中学习鲁棒的世界模型至关重要。最常见的策略是在在线训练期间通过与环境交互来主动收集轨迹，或者在离线数据集上进行训练。乍一看，学习与任务无关的环境动态的性质使得世界模型成为有效离线训练的良好候选者。然而，在线与离线数据对世界模型以及由此产生的任务性能的影响尚未在文献中得到彻底研究。在这项工作中，我们研究了基于模型的设置中的这两种范例，在31种不同的环境中进行了实验。首先，我们展示了在线智能体优于离线智能体。我们确定了离线智能体性能下降背后的一个关键挑战：在测试时遇到分布外（Out-Of-Distribution）状态。这个问题出现的原因是，在没有在线智能体中的自我纠正机制的情况下，状态空间覆盖有限的离线数据集会导致智能体的想象和真实轨迹之间的不匹配，从而损害策略训练。我们证明，通过在固定或自适应的时间表中允许额外的在线交互，可以缓解这个问题，从而恢复具有有限交互数据的在线训练的性能。我们还展示了结合探索数据有助于减轻离线智能体的性能下降。根据我们的见解，我们建议在收集大型数据集时添加探索数据，因为目前的努力主要集中在专家数据上。

## 🔬 方法详解

**问题定义**：论文旨在解决基于模型的强化学习中，离线数据训练的世界模型在实际应用中性能不佳的问题。现有方法主要依赖专家数据，忽略了探索数据的重要性，导致模型泛化能力不足，无法应对真实环境中未曾遇到的状态。

**核心思路**：论文的核心思路是对比在线和离线学习范式，分析离线学习性能下降的原因，并提出通过引入在线交互或探索数据来缓解这一问题。通过在线交互，智能体可以自我纠正，适应环境变化；而探索数据可以扩展状态空间覆盖，提高模型的鲁棒性。

**技术框架**：该研究采用基于模型的强化学习框架，包括世界模型学习和策略优化两个主要阶段。首先，使用离线或在线数据训练世界模型，用于预测环境的动态变化。然后，利用训练好的世界模型进行策略优化，学习如何在环境中采取最优动作。实验在31个不同的环境中进行，对比了不同数据收集策略下的智能体性能。

**关键创新**：论文的关键创新在于揭示了离线学习中分布外状态问题对世界模型性能的影响，并提出了通过引入在线交互或探索数据来缓解这一问题的有效方法。这为离线强化学习的数据收集策略提供了新的思路。

**关键设计**：论文设计了不同的数据收集策略，包括纯离线数据、纯在线数据、以及混合策略（离线数据+少量在线交互或探索数据）。通过对比这些策略下的智能体性能，分析了不同数据收集方式对世界模型学习的影响。具体参数设置和网络结构未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，在线智能体在31个不同环境中均优于离线智能体。通过引入少量在线交互或探索数据，可以显著提升离线智能体的性能，使其接近甚至达到在线智能体的水平。这表明，在离线强化学习中，数据收集策略的选择至关重要。

## 🎯 应用场景

该研究成果可应用于机器人控制、自动驾驶、游戏AI等领域。通过结合离线数据和少量在线交互，可以降低数据收集成本，提高智能体的泛化能力和鲁棒性。未来的研究可以进一步探索更有效的探索策略和数据融合方法，以提升离线强化学习的性能。

## 📄 摘要（原文）

> Data collection is crucial for learning robust world models in model-based reinforcement learning. The most prevalent strategies are to actively collect trajectories by interacting with the environment during online training or training on offline datasets. At first glance, the nature of learning task-agnostic environment dynamics makes world models a good candidate for effective offline training. However, the effects of online vs. offline data on world models and thus on the resulting task performance have not been thoroughly studied in the literature. In this work, we investigate both paradigms in model-based settings, conducting experiments on 31 different environments. First, we showcase that online agents outperform their offline counterparts. We identify a key challenge behind performance degradation of offline agents: encountering Out-Of-Distribution states at test time. This issue arises because, without the self-correction mechanism in online agents, offline datasets with limited state space coverage induce a mismatch between the agent's imagination and real rollouts, compromising policy training. We demonstrate that this issue can be mitigated by allowing for additional online interactions in a fixed or adaptive schedule, restoring the performance of online training with limited interaction data. We also showcase that incorporating exploration data helps mitigate the performance degradation of offline agents. Based on our insights, we recommend adding exploration data when collecting large datasets, as current efforts predominantly focus on expert data alone.

