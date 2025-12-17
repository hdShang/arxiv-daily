---
layout: default
title: RL-AVIST: Reinforcement Learning for Autonomous Visual Inspection of Space Targets
---

# RL-AVIST: Reinforcement Learning for Autonomous Visual Inspection of Space Targets

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22699" target="_blank" class="toolbar-btn">arXiv: 2510.22699v1</a>
    <a href="https://arxiv.org/pdf/2510.22699.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22699v1" 
            onclick="toggleFavorite(this, '2510.22699v1', 'RL-AVIST: Reinforcement Learning for Autonomous Visual Inspection of Space Targets')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Matteo El-Hariry, Andrej Orsula, Matthieu Geist, Miguel Olivares-Mendez

**分类**: cs.RO

**发布日期**: 2025-10-26

---

## 💡 一句话要点

**提出RL-AVIST框架，用于航天器目标自主视觉检测的强化学习控制。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `自主视觉检测` `航天器控制` `在轨服务` `DreamerV3`

## 📋 核心要点

1. 传统航天器控制系统在模型不确定和任务动态变化时适应性不足，难以满足日益增长的在轨服务需求。
2. RL-AVIST框架利用强化学习，通过学习复杂机动策略，实现航天器对空间目标的自主视觉检测。
3. 实验表明，基于模型的强化学习在轨迹保真度和样本效率方面表现出色，为空间任务控制提供了新思路。

## 📝 摘要（中文）

本文提出了一种用于航天器目标自主视觉检测的强化学习框架RL-AVIST。针对日益增长的在轨服务需求，如检测、维护和状态感知，需要智能航天器能够围绕大型轨道目标进行复杂机动。传统控制系统在适应性方面存在不足，尤其是在模型不确定性、多航天器配置或动态演变的 मिशन 环境下。该框架利用Space Robotics Bench (SRB)模拟高保真6自由度航天器动力学，并使用DreamerV3（一种先进的基于模型的强化学习算法）以及PPO和TD3（作为无模型基线）训练智能体。研究重点是围绕月球门户等目标进行3D近距离机动任务。评估了两种互补模式下的任务性能：在随机速度向量上训练的广义智能体，以及训练用于遵循模拟已知检测轨道的固定轨迹的专用智能体。此外，评估了策略在多种航天器形态和任务领域中的鲁棒性和泛化能力。结果表明，基于模型的强化学习在轨迹保真度和样本效率方面具有良好的能力，为未来空间行动的可扩展、可再训练的控制解决方案铺平了道路。

## 🔬 方法详解

**问题定义**：论文旨在解决航天器在复杂空间环境中，如何自主地进行视觉检测的问题。现有控制方法在面对模型不确定性、多航天器协同以及动态变化的任务环境时，适应性较差，难以保证检测任务的精度和效率。

**核心思路**：论文的核心思路是利用强化学习，特别是基于模型的强化学习算法，让航天器智能体通过与环境的交互学习最优的控制策略。通过学习，智能体能够适应不同的航天器形态和任务环境，实现自主的视觉检测。

**技术框架**：RL-AVIST框架主要包含以下几个部分：1) 基于Space Robotics Bench (SRB) 的高保真6自由度航天器动力学仿真环境；2) 基于DreamerV3的强化学习智能体，以及PPO和TD3作为基线算法；3) 奖励函数的设计，用于引导智能体学习期望的检测行为；4) 策略评估和泛化能力测试，验证智能体在不同环境下的性能。

**关键创新**：论文的关键创新在于将基于模型的强化学习算法DreamerV3应用于航天器自主视觉检测任务。与传统的无模型强化学习算法相比，DreamerV3能够学习环境的模型，从而提高样本效率和泛化能力。此外，论文还研究了策略在不同航天器形态和任务环境下的鲁棒性。

**关键设计**：论文使用了DreamerV3算法，这是一种基于隐变量模型的强化学习算法。奖励函数的设计至关重要，需要综合考虑航天器的轨迹精度、与目标的距离、以及能量消耗等因素。此外，论文还对智能体的网络结构进行了优化，以提高学习效率和泛化能力。

## 📊 实验亮点

实验结果表明，基于模型的强化学习算法DreamerV3在航天器自主视觉检测任务中表现出色，在轨迹保真度和样本效率方面优于无模型强化学习算法PPO和TD3。通过在随机速度向量和固定轨迹上进行训练，验证了智能体在不同任务环境下的泛化能力和鲁棒性。

## 🎯 应用场景

该研究成果可应用于多种在轨服务任务，如空间站和卫星的自主检测、维护和维修，以及空间碎片清除等。通过强化学习训练的智能体能够自主规划航天器的运动轨迹，提高任务效率和安全性，降低对地面控制的依赖，为未来的深空探测和空间资源利用提供技术支持。

## 📄 摘要（原文）

> The growing need for autonomous on-orbit services such as inspection, maintenance, and situational awareness calls for intelligent spacecraft capable of complex maneuvers around large orbital targets. Traditional control systems often fall short in adaptability, especially under model uncertainties, multi-spacecraft configurations, or dynamically evolving mission contexts. This paper introduces RL-AVIST, a Reinforcement Learning framework for Autonomous Visual Inspection of Space Targets. Leveraging the Space Robotics Bench (SRB), we simulate high-fidelity 6-DOF spacecraft dynamics and train agents using DreamerV3, a state-of-the-art model-based RL algorithm, with PPO and TD3 as model-free baselines. Our investigation focuses on 3D proximity maneuvering tasks around targets such as the Lunar Gateway and other space assets. We evaluate task performance under two complementary regimes: generalized agents trained on randomized velocity vectors, and specialized agents trained to follow fixed trajectories emulating known inspection orbits. Furthermore, we assess the robustness and generalization of policies across multiple spacecraft morphologies and mission domains. Results demonstrate that model-based RL offers promising capabilities in trajectory fidelity, and sample efficiency, paving the way for scalable, retrainable control solutions for future space operations

