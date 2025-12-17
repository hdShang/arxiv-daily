---
layout: default
title: Model-Based Reinforcement Learning in Discrete-Action Non-Markovian Reward Decision Processes
---

# Model-Based Reinforcement Learning in Discrete-Action Non-Markovian Reward Decision Processes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14617" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14617</a>
  <a href="https://arxiv.org/pdf/2512.14617.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14617" onclick="toggleFavorite(this, '2512.14617', 'Model-Based Reinforcement Learning in Discrete-Action Non-Markovian Reward Decision Processes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alessandro Trapasso, Luca Iocchi, Fabio Patrizi

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出QR-MAX算法，解决离散动作非马尔可夫奖励决策过程中的模型学习与策略优化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `非马尔可夫决策过程` `模型学习` `奖励机器` `样本效率`

## 📋 核心要点

1. 传统马尔可夫强化学习难以处理奖励依赖于历史状态的决策问题，非马尔可夫奖励决策过程(NMRDPs)强化学习缺乏理论保证。
2. QR-MAX算法通过奖励机器分解马尔可夫转移学习和非马尔可夫奖励处理，实现高效学习。
3. 实验表明，QR-MAX在样本效率和寻找最优策略的鲁棒性方面，显著优于现有基于模型的强化学习方法。

## 📝 摘要（中文）

许多实际决策问题依赖于整个系统历史，而非仅依赖于达到具有期望属性的状态。马尔可夫强化学习(RL)方法不适用于此类任务，而非马尔可夫奖励决策过程(NMRDPs)的RL使智能体能够处理时间依赖性任务。然而，这种方法长期以来缺乏关于(近)最优性和样本效率的形式保证。我们提出了QR-MAX，一种用于离散NMRDPs的新型基于模型的算法，它通过奖励机器将马尔可夫转移学习与非马尔可夫奖励处理分解开来，从而解决了这两个问题。据我们所知，这是第一个用于离散动作NMRDPs的基于模型的RL算法，它利用这种分解来获得PAC收敛到具有多项式样本复杂度的ε-最优策略。然后，我们将QR-MAX扩展到具有Bucket-QR-MAX的连续状态空间，Bucket-QR-MAX是一种基于SimHash的离散器，它保留了相同的分解结构，并在没有手动网格划分或函数逼近的情况下实现了快速稳定的学习。我们在复杂度不断增加的环境中，将我们的方法与现代最先进的基于模型的RL方法进行了实验比较，结果表明在样本效率方面有显著提高，并且在寻找最优策略方面具有更高的鲁棒性。

## 🔬 方法详解

**问题定义**：论文旨在解决离散动作非马尔可夫奖励决策过程(NMRDPs)中的强化学习问题。传统强化学习方法基于马尔可夫假设，无法有效处理奖励依赖于历史状态的任务。现有NMRDPs强化学习方法缺乏理论保证，如样本效率和收敛性，限制了其在实际问题中的应用。

**核心思路**：论文的核心思路是将马尔可夫转移学习与非马尔可夫奖励处理进行解耦。具体而言，利用奖励机器(Reward Machine)来建模非马尔可夫奖励函数，从而将复杂的奖励函数分解为一系列状态转移。同时，采用基于模型的强化学习方法，学习环境的马尔可夫转移模型。通过这种分解，可以更有效地学习和优化策略。

**技术框架**：QR-MAX算法的整体框架包括以下几个主要模块：1) 环境交互：智能体与环境进行交互，收集状态、动作和奖励数据。2) 模型学习：利用收集到的数据，学习环境的马尔可夫转移模型。3) 奖励机器学习：学习奖励机器的状态转移和奖励函数。4) 策略优化：基于学习到的环境模型和奖励机器，使用Q-learning算法优化策略。对于连续状态空间，论文提出了Bucket-QR-MAX算法，使用SimHash进行状态离散化。

**关键创新**：论文的关键创新在于提出了基于奖励机器的NMRDPs分解方法，以及相应的QR-MAX算法。这种分解方法使得可以独立地学习环境的马尔可夫转移模型和非马尔可夫奖励函数，从而提高了学习效率和泛化能力。此外，论文还提供了QR-MAX算法的PAC收敛性证明，保证了算法的理论性能。

**关键设计**：QR-MAX算法的关键设计包括：1) 奖励机器的表示和学习方法。2) Q-learning算法的更新规则，需要考虑奖励机器的状态。3) Bucket-QR-MAX算法中SimHash的参数设置，例如哈希函数的数量和哈希桶的大小。论文中没有明确给出损失函数和网络结构等细节，可能使用了标准的Q-learning损失函数和简单的网络结构。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14617/Experiments/map0_exp0_model_based.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14617/Experiments/map1_exp5_model_based.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14617/Experiments/map4_exp7.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，QR-MAX算法在多个NMRDPs环境中，显著优于现有的基于模型的强化学习方法。具体而言，QR-MAX算法在样本效率方面有显著提高，能够在更少的交互次数下找到最优策略。此外，QR-MAX算法在寻找最优策略的鲁棒性方面也表现更好，能够在不同的环境参数下稳定地学习到最优策略。

## 🎯 应用场景

该研究成果可应用于需要考虑历史信息的决策问题，例如机器人导航、任务规划、游戏AI等。在这些场景中，智能体的奖励不仅取决于当前状态，还取决于之前的行为序列。通过使用QR-MAX算法，可以更有效地学习和优化策略，提高智能体的性能。未来，该方法有望应用于更复杂的实际问题，例如自动驾驶、金融交易等。

## 📄 摘要（原文）

> Many practical decision-making problems involve tasks whose success depends on the entire system history, rather than on achieving a state with desired properties. Markovian Reinforcement Learning (RL) approaches are not suitable for such tasks, while RL with non-Markovian reward decision processes (NMRDPs) enables agents to tackle temporal-dependency tasks. This approach has long been known to lack formal guarantees on both (near-)optimality and sample efficiency. We contribute to solving both issues with QR-MAX, a novel model-based algorithm for discrete NMRDPs that factorizes Markovian transition learning from non-Markovian reward handling via reward machines. To the best of our knowledge, this is the first model-based RL algorithm for discrete-action NMRDPs that exploits this factorization to obtain PAC convergence to $\varepsilon$-optimal policies with polynomial sample complexity. We then extend QR-MAX to continuous state spaces with Bucket-QR-MAX, a SimHash-based discretiser that preserves the same factorized structure and achieves fast and stable learning without manual gridding or function approximation. We experimentally compare our method with modern state-of-the-art model-based RL approaches on environments of increasing complexity, showing a significant improvement in sample efficiency and increased robustness in finding optimal policies.

