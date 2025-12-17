---
layout: default
title: Digital Twin-based Control Co-Design of Full Vehicle Active Suspensions via Deep Reinforcement Learning
---

# Digital Twin-based Control Co-Design of Full Vehicle Active Suspensions via Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.03891" class="toolbar-btn" target="_blank">📄 arXiv: 2512.03891v1</a>
  <a href="https://arxiv.org/pdf/2512.03891.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.03891v1" onclick="toggleFavorite(this, '2512.03891v1', 'Digital Twin-based Control Co-Design of Full Vehicle Active Suspensions via Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ying-Kuan Tsai, Yi-Ping Chen, Vispi Karkaria, Wei Chen

**分类**: cs.RO, cs.LG

**发布日期**: 2025-12-03

**备注**: 28 pages, 17 figures

---

## 💡 一句话要点

**提出基于数字孪生和深度强化学习的全车主动悬架控制协同设计框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `数字孪生` `深度强化学习` `主动悬架` `控制协同设计` `自动微分` `车辆动力学` `模型更新`

## 📋 核心要点

1. 传统主动悬架系统受限于固定设计和控制策略，难以适应复杂动态环境和驾驶员行为。
2. 论文提出基于数字孪生的控制协同设计框架，结合深度强化学习和自动微分，实现悬架组件和控制策略的联合优化。
3. 实验结果表明，优化后的系统在不同驾驶模式下均能有效降低控制工作量，同时保证乘坐舒适性和稳定性。

## 📝 摘要（中文）

主动悬架系统对于提升车辆的舒适性、安全性和稳定性至关重要，但其性能通常受限于固定的硬件设计和无法适应不确定和动态运行条件的控制策略。数字孪生(DT)和深度强化学习(DRL)的最新进展为车辆整个生命周期的实时、数据驱动优化提供了新的机会。然而，将这些技术集成到一个统一的框架中仍然是一个公开的挑战。本文提出了一种基于DT的控制协同设计(CCD)框架，用于使用多代设计概念的全车主动悬架。通过将自动微分集成到DRL中，我们在不同的驾驶员行为和环境不确定性下，共同优化物理悬架组件和控制策略。DRL还通过直接从可用的传感器信息中学习最优控制动作，解决了只能感知和反馈有限状态的部分可观测性挑战。该框架结合了使用分位数学习的模型更新，以捕获数据不确定性，从而实现实时决策和从数字-物理交互中的自适应学习。该方法展示了在两种不同的驾驶设置（温和和激进）下悬架系统的个性化优化。结果表明，优化的系统实现了更平滑的轨迹，并且在保持乘坐舒适性和稳定性的同时，分别将温和和激进驾驶的控制工作量减少了大约43%和52%。贡献包括：开发了一种DT支持的CCD框架，该框架集成了DRL和不确定性感知模型更新，用于全车主动悬架；引入了一种用于自我改进系统的多代设计策略；并展示了针对不同驾驶员类型的主动悬架系统的个性化优化。

## 🔬 方法详解

**问题定义**：论文旨在解决传统主动悬架系统难以适应复杂动态环境和驾驶员行为的问题。现有方法通常采用固定的硬件设计和控制策略，无法根据实际工况进行优化，导致车辆舒适性、安全性和稳定性受到限制。

**核心思路**：论文的核心思路是利用数字孪生技术构建车辆的虚拟模型，并结合深度强化学习算法，实现悬架系统硬件和控制策略的协同优化。通过在数字孪生环境中进行训练和优化，可以快速找到适应不同工况和驾驶员行为的最佳设计方案。

**技术框架**：该框架主要包含以下几个模块：1) 数字孪生模型：构建全车主动悬架系统的精确虚拟模型，用于模拟车辆的动态行为。2) 深度强化学习控制器：采用深度强化学习算法，学习最优的控制策略，以最小化车辆的振动和提高乘坐舒适性。3) 自动微分优化器：利用自动微分技术，计算悬架系统参数对性能指标的梯度，从而实现硬件参数的优化。4) 模型更新模块：使用分位数学习方法，根据实际数据更新数字孪生模型，提高模型的准确性和鲁棒性。

**关键创新**：论文的关键创新在于将数字孪生、深度强化学习和自动微分技术相结合，构建了一个控制协同设计框架。该框架能够同时优化悬架系统的硬件参数和控制策略，从而实现更好的性能。此外，论文还引入了多代设计策略，使系统能够不断自我改进。

**关键设计**：论文采用深度确定性策略梯度(DDPG)算法作为深度强化学习控制器。奖励函数的设计考虑了乘坐舒适性、车辆稳定性和控制能量消耗等因素。自动微分优化器采用Adam算法进行参数更新。数字孪生模型采用Simulink进行建模。

## 📊 实验亮点

实验结果表明，该方法能够有效降低车辆的振动和控制能量消耗。在温和驾驶模式下，控制工作量降低了约43%；在激进驾驶模式下，控制工作量降低了约52%。同时，优化后的系统能够保持良好的乘坐舒适性和车辆稳定性，验证了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于智能汽车主动悬架系统的设计与优化，提升车辆的乘坐舒适性、安全性和稳定性。通过数字孪生技术，可以实现个性化的悬架系统定制，满足不同驾驶员的需求。此外，该方法还可推广到其他车辆子系统的协同设计，例如动力系统、制动系统等，具有广阔的应用前景。

## 📄 摘要（原文）

> Active suspension systems are critical for enhancing vehicle comfort, safety, and stability, yet their performance is often limited by fixed hardware designs and control strategies that cannot adapt to uncertain and dynamic operating conditions. Recent advances in digital twins (DTs) and deep reinforcement learning (DRL) offer new opportunities for real-time, data-driven optimization across a vehicle's lifecycle. However, integrating these technologies into a unified framework remains an open challenge. This work presents a DT-based control co-design (CCD) framework for full-vehicle active suspensions using multi-generation design concepts. By integrating automatic differentiation into DRL, we jointly optimize physical suspension components and control policies under varying driver behaviors and environmental uncertainties. DRL also addresses the challenge of partial observability, where only limited states can be sensed and fed back to the controller, by learning optimal control actions directly from available sensor information. The framework incorporates model updating with quantile learning to capture data uncertainty, enabling real-time decision-making and adaptive learning from digital-physical interactions. The approach demonstrates personalized optimization of suspension systems under two distinct driving settings (mild and aggressive). Results show that the optimized systems achieve smoother trajectories and reduce control efforts by approximately 43% and 52% for mild and aggressive, respectively, while maintaining ride comfort and stability. Contributions include: developing a DT-enabled CCD framework integrating DRL and uncertainty-aware model updating for full-vehicle active suspensions, introducing a multi-generation design strategy for self-improving systems, and demonstrating personalized optimization of active suspension systems for distinct driver types.

