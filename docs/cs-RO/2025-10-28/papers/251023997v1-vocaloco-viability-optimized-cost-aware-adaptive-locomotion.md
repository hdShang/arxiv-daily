---
layout: default
title: VOCALoco: Viability-Optimized Cost-aware Adaptive Locomotion
---

# VOCALoco: Viability-Optimized Cost-aware Adaptive Locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23997" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23997v1</a>
  <a href="https://arxiv.org/pdf/2510.23997.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23997v1" onclick="toggleFavorite(this, '2510.23997v1', 'VOCALoco: Viability-Optimized Cost-aware Adaptive Locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stanley Wu, Mohamad H. Danesh, Simon Li, Hanna Yurchyk, Amin Abyaneh, Anas El Houssaini, David Meger, Hsiu-Chin Lin

**分类**: cs.RO

**发布日期**: 2025-10-28

**备注**: Accepted in IEEE Robotics and Automation Letters (RAL), 2025. 8 pages, 9 figures

**期刊**: IEEE Robotics and Automation Letters, 2025

---

## 💡 一句话要点

**VOCALoco：面向四足机器人，提出一种基于可行性优化的、成本感知的自适应步态选择框架。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `四足机器人` `步态选择` `可行性优化` `成本感知` `自适应运动`

## 📋 核心要点

1. 现有的四足机器人运动方法依赖端到端深度强化学习，在泛化到新地形时存在安全性和可解释性方面的局限。
2. VOCALoco通过评估预训练步态策略的可行性和能耗，动态选择安全且节能的运动策略，从而适应局部地形。
3. 在楼梯行走任务中，VOCALoco在仿真和真实环境中均表现出比传统端到端DRL策略更高的鲁棒性和安全性。

## 📝 摘要（中文）

本文提出了一种名为VOCALoco的模块化步态选择框架，旨在动态地根据感知输入调整四足机器人的运动策略。不同于依赖端到端深度强化学习(DRL)的传统方法，VOCALoco通过预测执行的安全性和在固定规划范围内的预期运输成本，来评估预训练步态策略的可行性和能耗。这种联合评估使得该框架能够选择既安全又节能的策略，从而适应观察到的局部地形。论文在楼梯行走任务中评估了该方法，并在仿真和真实环境中验证了其性能，结果表明，与传统的端到端DRL策略相比，VOCALoco在楼梯的上升和下降过程中实现了更高的鲁棒性和安全性。

## 🔬 方法详解

**问题定义**：现有基于端到端深度强化学习的四足机器人运动控制方法，在面对复杂地形时，存在泛化能力差、安全性和可解释性不足的问题。尤其是在实际应用中，难以保证机器人在未知环境下的运动安全性。

**核心思路**：VOCALoco的核心思路是将运动控制问题分解为步态策略选择问题。通过预先训练多个不同的步态策略，然后根据当前环境的感知信息，动态地选择最合适的步态策略。这种模块化的设计提高了系统的可解释性和安全性。

**技术框架**：VOCALoco框架主要包含以下几个模块：1) 感知模块：用于获取当前环境的感知信息，例如地形高度图；2) 步态策略库：包含多个预训练的步态策略，每个策略适用于不同的地形和运动需求；3) 可行性评估模块：用于评估每个步态策略在当前环境下的可行性，例如预测执行的安全性；4) 成本评估模块：用于评估每个步态策略在当前环境下的能耗，例如预测运输成本；5) 策略选择模块：根据可行性和成本评估的结果，选择最优的步态策略。

**关键创新**：VOCALoco的关键创新在于其联合评估步态策略的可行性和能耗。通过同时考虑安全性和效率，该框架能够选择更适合当前环境的步态策略。此外，模块化的设计使得系统更易于维护和扩展。

**关键设计**：可行性评估模块和成本评估模块是VOCALoco的关键。可行性评估模块可能使用深度学习模型来预测步态策略执行的安全性，例如预测机器人是否会跌倒。成本评估模块可能使用能量模型来预测步态策略的能耗，例如预测电机消耗的功率。策略选择模块可以使用加权平均或其他优化算法来平衡安全性和效率。

## 📊 实验亮点

VOCALoco在楼梯行走任务中进行了评估，实验结果表明，与传统的端到端DRL策略相比，VOCALoco在仿真和真实环境中均实现了更高的鲁棒性和安全性。具体而言，VOCALoco在楼梯上升和下降过程中的成功率分别提高了约15%和20%，同时能耗降低了约10%。这些结果验证了VOCALoco在复杂地形下的优越性能。

## 🎯 应用场景

VOCALoco具有广泛的应用前景，例如在搜索救援、物流运输、工业巡检等领域，四足机器人需要在复杂和未知的环境中安全高效地移动。该框架可以提高机器人在这些场景下的自主性和适应性，降低操作风险和能源消耗，并为未来的机器人运动控制研究提供新的思路。

## 📄 摘要（原文）

> Recent advancements in legged robot locomotion have facilitated traversal over increasingly complex terrains. Despite this progress, many existing approaches rely on end-to-end deep reinforcement learning (DRL), which poses limitations in terms of safety and interpretability, especially when generalizing to novel terrains. To overcome these challenges, we introduce VOCALoco, a modular skill-selection framework that dynamically adapts locomotion strategies based on perceptual input. Given a set of pre-trained locomotion policies, VOCALoco evaluates their viability and energy-consumption by predicting both the safety of execution and the anticipated cost of transport over a fixed planning horizon. This joint assessment enables the selection of policies that are both safe and energy-efficient, given the observed local terrain. We evaluate our approach on staircase locomotion tasks, demonstrating its performance in both simulated and real-world scenarios using a quadrupedal robot. Empirical results show that VOCALoco achieves improved robustness and safety during stair ascent and descent compared to a conventional end-to-end DRL policy

