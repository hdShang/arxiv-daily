---
layout: default
title: "Greener Deep Reinforcement Learning: Analysis of Energy and Carbon Efficiency Across Atari Benchmarks"
---

# Greener Deep Reinforcement Learning: Analysis of Energy and Carbon Efficiency Across Atari Benchmarks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05273" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05273v1</a>
  <a href="https://arxiv.org/pdf/2509.05273.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05273v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05273v1', 'Greener Deep Reinforcement Learning: Analysis of Energy and Carbon Efficiency Across Atari Benchmarks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jason Gardner, Ayan Dutta, Swapnoneel Roy, O. Patrick Kreidl, Ladislau Boloni

**分类**: cs.LG, cs.PF

**发布日期**: 2025-09-05

**备注**: Submitted to a journal - under review

---

## 💡 一句话要点

**分析Atari基准测试中深度强化学习的能源和碳效率，为绿色DRL提供基准。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `能源效率` `碳排放` `基准测试` `Atari` `可持续性` `算法评估`

## 📋 核心要点

1. 现有深度强化学习算法的能耗和碳排放成本缺乏系统性评估，阻碍了绿色DRL的发展。
2. 通过基准测试七种主流DRL算法在Atari游戏上的能耗、碳排放和经济成本，揭示算法间的效率差异。
3. 实验结果表明，不同算法在能耗和成本上存在显著差异，为选择更环保的DRL算法提供了依据。

## 📝 摘要（中文）

深度强化学习（DRL）日益增长的计算需求引发了人们对训练大规模模型所带来的环境和经济成本的担忧。虽然在学习性能方面的算法效率已被广泛研究，但DRL算法的能源需求、温室气体排放和货币成本在很大程度上仍未被探索。本文对七种最先进的DRL算法（DQN、TRPO、A2C、ARS、PPO、RecurrentPPO和QR-DQN）的能耗进行了系统的基准测试研究，这些算法均使用Stable Baselines实现。每种算法在十个Atari 2600游戏中训练一百万步，并实时测量功耗，以根据美国全国平均电价估算总能源使用量、二氧化碳当量排放量和电力成本。结果表明，不同算法在能源效率和训练成本方面存在显著差异，有些算法在消耗高达24%更少能源（ARS vs. DQN）、排放近68%更少二氧化碳以及产生几乎68%更低货币成本（QR-DQN vs. RecurrentPPO）的情况下，实现了相当的性能。我们进一步分析了学习性能、训练时间、能源使用和财务成本之间的权衡，突出了算法选择可以在不牺牲学习性能的情况下减轻环境和经济影响的情况。这项研究为开发具有能源意识和成本效益的DRL实践提供了可操作的见解，并为将可持续性考虑因素纳入未来的算法设计和评估奠定了基础。

## 🔬 方法详解

**问题定义**：论文旨在解决深度强化学习算法训练过程中能源消耗高、碳排放量大以及经济成本高的问题。现有方法主要关注算法的学习性能，而忽略了其环境和经济影响，缺乏对不同算法能耗效率的系统性评估，导致无法选择更环保的算法。

**核心思路**：论文的核心思路是通过对主流DRL算法在标准Atari游戏环境下的能耗进行基准测试，量化不同算法的能源效率、碳排放量和经济成本，从而为选择和设计更环保的DRL算法提供依据。这种方法通过实证分析揭示了算法选择对环境和经济的影响。

**技术框架**：论文的技术框架主要包括以下几个阶段：
1.  选择七种具有代表性的DRL算法：DQN, TRPO, A2C, ARS, PPO, RecurrentPPO, QR-DQN。
2.  使用Stable Baselines实现这些算法。
3.  在十个Atari 2600游戏上训练这些算法，每个算法训练一百万步。
4.  实时测量训练过程中的功耗。
5.  根据功耗数据估算总能源使用量、二氧化碳当量排放量和电力成本。
6.  分析学习性能、训练时间、能源使用和财务成本之间的权衡。

**关键创新**：论文最重要的技术创新点在于对DRL算法的能源效率进行了系统性的基准测试，并量化了不同算法的碳排放和经济成本。以往的研究主要关注算法的学习性能，而忽略了其环境和经济影响。该研究首次将可持续性考虑因素纳入DRL算法的评估体系中。

**关键设计**：论文的关键设计包括：
1.  选择具有代表性的Atari游戏作为测试环境。
2.  使用Stable Baselines作为DRL算法的实现框架。
3.  实时测量功耗，并使用美国全国平均电价计算电力成本。
4.  采用二氧化碳排放因子将能源消耗转化为碳排放量。
5.  分析学习性能、训练时间、能源使用和财务成本之间的权衡。

## 📊 实验亮点

实验结果表明，不同DRL算法在能耗和成本方面存在显著差异。例如，ARS算法相比DQN算法，能耗降低了24%。QR-DQN算法相比RecurrentPPO算法，碳排放量和经济成本降低了近68%。这些数据突出了算法选择对环境和经济影响的重要性，并为选择更环保的DRL算法提供了依据。

## 🎯 应用场景

该研究成果可应用于各种需要使用深度强化学习的领域，例如机器人控制、游戏AI、自动驾驶、资源管理等。通过选择更节能的算法，可以降低训练成本，减少碳排放，从而实现更可持续的AI发展。该研究也为未来设计更环保的DRL算法提供了指导。

## 📄 摘要（原文）

> The growing computational demands of deep reinforcement learning (DRL) have raised concerns about the environmental and economic costs of training large-scale models. While algorithmic efficiency in terms of learning performance has been extensively studied, the energy requirements, greenhouse gas emissions, and monetary costs of DRL algorithms remain largely unexplored. In this work, we present a systematic benchmarking study of the energy consumption of seven state-of-the-art DRL algorithms, namely DQN, TRPO, A2C, ARS, PPO, RecurrentPPO, and QR-DQN, implemented using Stable Baselines. Each algorithm was trained for one million steps each on ten Atari 2600 games, and power consumption was measured in real-time to estimate total energy usage, CO2-Equivalent emissions, and electricity cost based on the U.S. national average electricity price. Our results reveal substantial variation in energy efficiency and training cost across algorithms, with some achieving comparable performance while consuming up to 24% less energy (ARS vs. DQN), emitting nearly 68% less CO2, and incurring almost 68% lower monetary cost (QR-DQN vs. RecurrentPPO) than less efficient counterparts. We further analyze the trade-offs between learning performance, training time, energy use, and financial cost, highlighting cases where algorithmic choices can mitigate environmental and economic impact without sacrificing learning performance. This study provides actionable insights for developing energy-aware and cost-efficient DRL practices and establishes a foundation for incorporating sustainability considerations into future algorithmic design and evaluation.

