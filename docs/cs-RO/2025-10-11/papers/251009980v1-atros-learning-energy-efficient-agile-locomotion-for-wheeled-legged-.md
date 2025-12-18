---
layout: default
title: ATRos: Learning Energy-Efficient Agile Locomotion for Wheeled-legged Robots
---

# ATRos: Learning Energy-Efficient Agile Locomotion for Wheeled-legged Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09980" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09980v1</a>
  <a href="https://arxiv.org/pdf/2510.09980.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09980v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.09980v1', 'ATRos: Learning Energy-Efficient Agile Locomotion for Wheeled-legged Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingyuan Sun, Hongyu Ji, Zihan Qu, Chaoran Wang, Mingyu Zhang

**分类**: cs.RO

**发布日期**: 2025-10-11

**备注**: 4 pages, 2 figures, submitted to IROS 2025 wheeled-legged workshop

---

## 💡 一句话要点

**ATRos：一种基于强化学习的轮腿机器人高效敏捷混合运动控制框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `轮腿机器人` `混合运动` `强化学习` `机器人控制` `能量效率`

## 📋 核心要点

1. 轮腿机器人的混合运动结合了腿式运动的敏捷性和轮式运动的效率，但其全身控制面临挑战。
2. ATRos通过强化学习智能协调轮腿运动，无需预定义步态，提升地形适应性和能量效率。
3. 仿真和真实环境实验验证了ATRos在多种地形下的鲁棒性和泛化能力，效果显著。

## 📝 摘要（中文）

本文提出ATRos，一个基于强化学习(RL)的混合运动框架，旨在实现轮腿机器人的混合行走-驱动运动。该框架不依赖预定义的步态模式，而是智能地协调车轮和腿部的同步运动，从而提高地形适应性和能量效率。该方法基于强化学习技术，构建了一个预测策略网络，可以从本体感受感官信息中估计外部环境状态，然后将输出输入到Actor-Critic网络中，以生成最佳关节指令。通过仿真和真实世界的实验，在包括平地、楼梯和草地在内的各种地形上验证了所提出框架的可行性。混合运动框架在各种未见过的地形上表现出强大的性能，突出了其泛化能力。

## 🔬 方法详解

**问题定义**：轮腿机器人的混合运动控制旨在结合轮式和腿式运动的优点，但现有方法通常依赖于预定义的步态模式，难以适应复杂地形，且能量效率不高。全身控制的复杂性也使得设计鲁棒的控制器成为挑战。

**核心思路**：ATRos的核心在于利用强化学习，让机器人自主学习轮腿协同运动策略，无需人工设计步态。通过学习环境状态与最优动作之间的映射关系，实现对复杂地形的适应和能量效率的优化。

**技术框架**：ATRos框架包含两个主要模块：预测策略网络和Actor-Critic网络。预测策略网络接收来自机器人本体感受器的信息，用于估计外部环境状态。Actor-Critic网络则基于预测的环境状态，生成最优的关节指令，控制机器人的运动。整个框架通过强化学习进行端到端训练。

**关键创新**：ATRos的关键创新在于利用强化学习实现了轮腿机器人的自适应混合运动控制，摆脱了对预定义步态的依赖。通过预测策略网络，机器人能够根据自身感知到的信息推断环境状态，从而做出更合理的运动决策。

**关键设计**：预测策略网络和Actor-Critic网络的具体结构未知，但可以推测使用了深度神经网络。损失函数的设计目标是最大化机器人的运动效率和稳定性，同时考虑能量消耗。具体的参数设置和训练策略未知。

## 📊 实验亮点

ATRos在仿真和真实环境的实验中表现出良好的性能。在包括平地、楼梯和草地在内的各种地形上，ATRos能够实现鲁棒的混合运动，并展现出良好的泛化能力，即使在未见过的地形上也能有效工作。具体的性能数据和对比基线未知。

## 🎯 应用场景

ATRos框架可应用于搜索救援、物流运输、巡检等领域，尤其是在复杂地形或需要高能量效率的场景下。该研究为轮腿机器人的智能化和自主化提供了新的思路，有望推动机器人在更广泛领域的应用。

## 📄 摘要（原文）

> Hybrid locomotion of wheeled-legged robots has recently attracted increasing attention due to their advantages of combining the agility of legged locomotion and the efficiency of wheeled motion. But along with expanded performance, the whole-body control of wheeled-legged robots remains challenging for hybrid locomotion. In this paper, we present ATRos, a reinforcement learning (RL)-based hybrid locomotion framework to achieve hybrid walking-driving motions on the wheeled-legged robot. Without giving predefined gait patterns, our planner aims to intelligently coordinate simultaneous wheel and leg movements, thereby achieving improved terrain adaptability and improved energy efficiency. Based on RL techniques, our approach constructs a prediction policy network that could estimate external environmental states from proprioceptive sensory information, and the outputs are then fed into an actor critic network to produce optimal joint commands. The feasibility of the proposed framework is validated through both simulations and real-world experiments across diverse terrains, including flat ground, stairs, and grassy surfaces. The hybrid locomotion framework shows robust performance over various unseen terrains, highlighting its generalization capability.

