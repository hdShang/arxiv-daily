---
layout: default
title: "Reinforcement learning meets bioprocess control through behaviour cloning: Real-world deployment in an industrial photobioreactor"
---

# Reinforcement learning meets bioprocess control through behaviour cloning: Real-world deployment in an industrial photobioreactor

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06853" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06853v1</a>
  <a href="https://arxiv.org/pdf/2509.06853.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06853v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06853v1', 'Reinforcement learning meets bioprocess control through behaviour cloning: Real-world deployment in an industrial photobioreactor')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juan D. Gil, Ehecatl Antonio Del Rio Chanona, José L. Guzmán, Manuel Berenguel

**分类**: eess.SY, cs.AI, cs.LG

**发布日期**: 2025-09-08

---

## 💡 一句话要点

**提出基于行为克隆的强化学习方法，用于工业光生物反应器中的pH值控制。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `行为克隆` `生物过程控制` `光生物反应器` `pH值控制`

## 📋 核心要点

1. 开放式光生物反应器面临环境波动带来的挑战，传统控制方法难以维持稳定和最佳的生物过程条件。
2. 采用行为克隆引导的强化学习方法，离线学习PID控制器的轨迹，在线微调以适应环境变化。
3. 实验结果表明，该方法在降低误差、减少控制工作量和保持系统鲁棒性方面优于传统PID和标准强化学习方法。

## 📝 摘要（中文）

本文提出了一种结合行为克隆（BC）的强化学习（RL）控制方法，用于开放式光生物反应器（PBR）系统中的pH调节。据我们所知，这是基于RL的控制策略首次应用于这种非线性且易受干扰的生物过程中。该方法首先进行离线训练，RL智能体从标称比例-积分-微分（PID）控制器生成的轨迹中学习，无需与真实系统直接交互。然后进行每日在线微调，以适应不断变化的工艺动态并更有效地抑制快速瞬态干扰。这种混合离线-在线策略能够部署自适应控制策略，以处理开放式PBR中固有的非线性和外部扰动。仿真研究表明，与PID控制相比，绝对误差积分（IAE）降低了8%，与标准离策略RL相比降低了5%。此外，控制工作量显著减少，与PID相比减少了54%，与标准RL相比减少了7%，这对于最小化运营成本非常重要。最后，在不同环境条件下进行的为期8天的实验验证证实了该方法的鲁棒性和可靠性。总的来说，这项工作证明了基于RL的方法在生物过程控制中的潜力，并为它们更广泛地应用于其他非线性、易受干扰的系统铺平了道路。

## 🔬 方法详解

**问题定义**：论文旨在解决开放式光生物反应器（PBR）中pH值精确控制的问题。由于生物过程的非线性和环境扰动的存在，传统的PID控制难以实现稳定和最优的控制效果，尤其是在面对快速瞬态干扰时。现有方法难以兼顾控制性能和控制成本。

**核心思路**：论文的核心思路是利用行为克隆（BC）加速强化学习（RL）的训练过程，并结合在线微调，使控制策略能够适应不断变化的系统动态和外部扰动。通过模仿PID控制器的行为，RL智能体可以快速学习到初步的控制策略，避免了从零开始探索的低效性。在线微调则进一步提升了策略的适应性和鲁棒性。

**技术框架**：该方法包含两个主要阶段：离线训练和在线微调。在离线训练阶段，RL智能体通过模仿PID控制器的轨迹进行学习，无需与真实系统交互。在在线微调阶段，RL智能体每天与真实系统进行交互，并根据实际的系统状态和反馈，对控制策略进行微调，以适应不断变化的系统动态和外部扰动。

**关键创新**：该方法的关键创新在于将行为克隆与强化学习相结合，并应用于开放式光生物反应器的pH值控制。行为克隆加速了强化学习的训练过程，在线微调则提升了策略的适应性和鲁棒性。此外，该方法首次将RL应用于这种非线性且易受干扰的生物过程。

**关键设计**：论文中使用了某种具体的强化学习算法（原文未明确指出，此处假设为某种off-policy算法），并设计了合适的奖励函数，以鼓励智能体实现精确的pH值控制，并减少控制工作量。行为克隆阶段，使用PID控制器的历史数据作为训练样本。在线微调阶段，需要仔细设计探索策略，以平衡探索和利用。

## 📊 实验亮点

实验结果表明，与传统的PID控制相比，该方法在绝对误差积分（IAE）方面降低了8%，控制工作量减少了54%。与标准离策略强化学习相比，IAE降低了5%，控制工作量减少了7%。为期8天的实验验证也证实了该方法在不同环境条件下的鲁棒性和可靠性。

## 🎯 应用场景

该研究成果可应用于各种生物过程控制领域，尤其是在开放式、易受环境干扰的生物反应器中。通过自适应地调节控制策略，可以提高生物过程的稳定性、优化生产效率，并降低运营成本。该方法也为强化学习在其他非线性、时变系统中的应用提供了借鉴。

## 📄 摘要（原文）

> The inherent complexity of living cells as production units creates major challenges for maintaining stable and optimal bioprocess conditions, especially in open Photobioreactors (PBRs) exposed to fluctuating environments. To address this, we propose a Reinforcement Learning (RL) control approach, combined with Behavior Cloning (BC), for pH regulation in open PBR systems. This represents, to the best of our knowledge, the first application of an RL-based control strategy to such a nonlinear and disturbance-prone bioprocess. Our method begins with an offline training stage in which the RL agent learns from trajectories generated by a nominal Proportional-Integral-Derivative (PID) controller, without direct interaction with the real system. This is followed by a daily online fine-tuning phase, enabling adaptation to evolving process dynamics and stronger rejection of fast, transient disturbances. This hybrid offline-online strategy allows deployment of an adaptive control policy capable of handling the inherent nonlinearities and external perturbations in open PBRs. Simulation studies highlight the advantages of our method: the Integral of Absolute Error (IAE) was reduced by 8% compared to PID control and by 5% relative to standard off-policy RL. Moreover, control effort decreased substantially-by 54% compared to PID and 7% compared to standard RL-an important factor for minimizing operational costs. Finally, an 8-day experimental validation under varying environmental conditions confirmed the robustness and reliability of the proposed approach. Overall, this work demonstrates the potential of RL-based methods for bioprocess control and paves the way for their broader application to other nonlinear, disturbance-prone systems.

