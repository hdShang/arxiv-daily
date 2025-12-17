---
layout: default
title: PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization
---

# PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01708" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01708v3</a>
  <a href="https://arxiv.org/pdf/2510.01708.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01708v3" onclick="toggleFavorite(this, '2510.01708v3', 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixing Lei, Zibo Zhou, Sheng Yin, Yueru Chen, Qingyao Xu, Weixin Li, Yunhong Wang, Bowei Tang, Wei Jing, Siheng Chen

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-02 (更新: 2025-10-14)

**备注**: 8 pages, 5 figures

---

## 💡 一句话要点

**PolySim：通过多模拟器动态随机化弥合人形机器人控制的Sim-to-Real差距**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `人形机器人控制` `Sim-to-Real` `领域随机化` `多模拟器` `强化学习`

## 📋 核心要点

1. 现有方法受限于单一模拟器的归纳偏置，导致Sim-to-Real迁移性能不佳，难以在真实机器人上直接应用。
2. PolySim通过集成多个异构模拟器，实现动力学层面的领域随机化，从而减轻单一模拟器的归纳偏置。
3. 实验表明，PolySim显著降低了Sim-to-Sim运动跟踪误差，并在真实Unitree G1机器人上实现了零样本部署。

## 📝 摘要（中文）

人形机器人全身控制（WBC）策略在仿真环境中训练时，常常受到Sim-to-Real差距的影响，这根本上源于模拟器的归纳偏置，即任何单一模拟器固有的假设和局限性。这些偏置导致了模拟器之间以及仿真与现实世界之间的显著差异。为了减轻模拟器归纳偏置的影响，关键思想是在多个模拟器上联合训练策略，鼓励学习到的控制器捕获能够泛化到任何单一模拟器假设之外的动力学。因此，我们引入了PolySim，一个集成了多个异构模拟器的WBC训练平台。PolySim可以在单个训练运行中同时启动来自不同引擎的并行环境，从而实现动力学层面的领域随机化。理论上，我们证明PolySim产生的模拟器归纳偏置的上界比单模拟器训练更紧。在实验中，PolySim显著降低了Sim-to-Sim评估中的运动跟踪误差；例如，在MuJoCo上，它比IsaacSim基线提高了52.8%的执行成功率。PolySim进一步实现了在真实Unitree G1上的零样本部署，无需额外的微调，显示了从仿真到现实世界的有效迁移。我们将在接受本文后发布PolySim代码。

## 🔬 方法详解

**问题定义**：现有的人形机器人全身控制策略在仿真环境中训练后，难以直接迁移到真实机器人上，主要原因是单一仿真器存在固有的归纳偏置，即对物理世界的简化和假设，导致仿真环境与真实环境存在差异。这种差异使得在仿真环境中训练的策略在真实环境中表现不佳，需要大量的微调才能适应。

**核心思路**：PolySim的核心思路是通过同时利用多个异构的仿真器进行训练，从而让策略能够学习到更加鲁棒和泛化的动力学模型。通过在不同的仿真器中进行随机化，策略可以避免过度拟合于某个特定的仿真环境，从而更好地适应真实世界的复杂性和不确定性。

**技术框架**：PolySim是一个集成了多个异构模拟器的全身控制训练平台。它允许在单个训练过程中同时启动来自不同引擎的并行环境。整体流程包括：1) 定义机器人任务和目标；2) 在多个仿真器中创建并行环境；3) 使用强化学习算法训练控制策略；4) 在仿真环境中评估策略性能；5) 在真实机器人上进行零样本部署或微调。

**关键创新**：PolySim最重要的创新点在于其多模拟器集成和动力学层面的领域随机化。与传统的单模拟器训练方法相比，PolySim能够有效地减少模拟器归纳偏置，提高策略的泛化能力。通过同时利用多个异构模拟器，PolySim能够让策略学习到更加鲁棒和泛化的动力学模型，从而更好地适应真实世界的复杂性和不确定性。

**关键设计**：PolySim的关键设计包括：1) 异构模拟器集成：支持多种主流的机器人仿真器，如MuJoCo、IsaacSim等；2) 并行环境管理：能够高效地管理和同步多个仿真环境；3) 动态领域随机化：在训练过程中随机化仿真器的参数，如摩擦系数、质量、惯性等；4) 强化学习算法：可以使用各种强化学习算法进行训练，如PPO、SAC等；5) 奖励函数设计：根据具体的任务设计合适的奖励函数，引导策略学习到期望的行为。

## 📊 实验亮点

PolySim在Sim-to-Sim评估中显著降低了运动跟踪误差。例如，在MuJoCo上，PolySim比IsaacSim基线提高了52.8%的执行成功率。更重要的是，PolySim实现了在真实Unitree G1机器人上的零样本部署，无需额外的微调，证明了其从仿真到现实世界的有效迁移能力。这些实验结果表明，PolySim能够有效地减少模拟器归纳偏置，提高策略的泛化能力。

## 🎯 应用场景

PolySim具有广泛的应用前景，可用于开发各种人形机器人的控制策略，例如：双足行走、物体操作、复杂地形导航等。该平台能够显著降低Sim-to-Real的差距，加速机器人控制算法的开发和部署，并有望推动人形机器人在工业、医疗、服务等领域的应用。此外，PolySim的设计思想也可以推广到其他类型的机器人和控制任务中。

## 📄 摘要（原文）

> Humanoid whole-body control (WBC) policies trained in simulation often suffer from the sim-to-real gap, which fundamentally arises from simulator inductive bias, the inherent assumptions and limitations of any single simulator. These biases lead to nontrivial discrepancies both across simulators and between simulation and the real world. To mitigate the effect of simulator inductive bias, the key idea is to train policies jointly across multiple simulators, encouraging the learned controller to capture dynamics that generalize beyond any single simulator's assumptions. We thus introduce PolySim, a WBC training platform that integrates multiple heterogeneous simulators. PolySim can launch parallel environments from different engines simultaneously within a single training run, thereby realizing dynamics-level domain randomization. Theoretically, we show that PolySim yields a tighter upper bound on simulator inductive bias than single-simulator training. In experiments, PolySim substantially reduces motion-tracking error in sim-to-sim evaluations; for example, on MuJoCo, it improves execution success by 52.8 over an IsaacSim baseline. PolySim further enables zero-shot deployment on a real Unitree G1 without additional fine-tuning, showing effective transfer from simulation to the real world. We will release the PolySim code upon acceptance of this work.

