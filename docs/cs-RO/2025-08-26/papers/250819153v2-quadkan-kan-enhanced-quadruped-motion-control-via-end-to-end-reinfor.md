---
layout: default
title: "QuadKAN: KAN-Enhanced Quadruped Motion Control via End-to-End Reinforcement Learning"
---

# QuadKAN: KAN-Enhanced Quadruped Motion Control via End-to-End Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19153" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19153v2</a>
  <a href="https://arxiv.org/pdf/2508.19153.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19153v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19153v2', 'QuadKAN: KAN-Enhanced Quadruped Motion Control via End-to-End Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinuo Wang, Gavin Tao

**分类**: cs.RO, cs.AI, cs.CV, eess.IV, eess.SY

**发布日期**: 2025-08-26 (更新: 2025-09-07)

**备注**: 14pages, 9 figures, Journal paper

---

## 💡 一句话要点

**提出QuadKAN以解决四足机器人运动控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `四足机器人` `运动控制` `强化学习` `多模态融合` `样条参数化` `Kolmogorov-Arnold网络` `视觉引导` `鲁棒性`

## 📋 核心要点

1. 现有的四足机器人运动控制方法在复杂环境中表现不佳，尤其是在结合视觉与本体感知时的鲁棒性不足。
2. 论文提出的QuadKAN框架通过样条参数化策略结合本体感知与视觉输入，旨在提高运动控制的效率与稳定性。
3. 实验结果显示，QuadKAN在多种地形下的表现优于现有最先进方法，具体体现在更高的回报和更少的碰撞次数。

## 📝 摘要（中文）

本文针对视觉引导的四足机器人运动控制问题，强调结合本体感知与视觉的重要性。提出了QuadKAN，一个基于Kolmogorov-Arnold网络（KAN）的样条参数化跨模态策略框架。该框架通过样条编码器处理本体感知，并通过样条融合头处理本体感知与视觉输入。此结构化函数类使状态到动作的映射与步态的分段平滑特性相一致，提高了样本效率，减少了动作抖动和能耗，并提供了可解释的姿态-动作敏感性。通过多模态延迟随机化（MMDR）和近端策略优化（PPO）进行端到端训练。实验结果表明，QuadKAN在多种地形下表现优异，获得了更高的回报、更大的行驶距离和更少的碰撞，展示了样条参数化策略在视觉引导的运动控制中的有效性和可解释性。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉引导的四足机器人运动控制中的鲁棒性问题，现有方法在复杂环境中难以有效结合本体感知与视觉信息，导致控制效果不佳。

**核心思路**：QuadKAN框架通过样条参数化策略，将本体感知与视觉信息融合，利用Kolmogorov-Arnold网络（KAN）来实现高效的状态到动作映射，旨在提高运动控制的样本效率和稳定性。

**技术框架**：QuadKAN的整体架构包括样条编码器用于处理本体感知数据，以及样条融合头用于整合视觉输入和本体感知信息。通过多模态延迟随机化（MMDR）和近端策略优化（PPO）进行端到端训练。

**关键创新**：本研究的主要创新在于引入样条参数化策略，使得状态到动作的映射与步态的分段平滑特性相一致，从而显著提高了控制的可解释性和效率。

**关键设计**：在网络结构上，采用了样条编码器和样条融合头的设计，确保了多模态输入的有效整合。此外，损失函数的设计也考虑了动作抖动和能耗的最小化。通过这些设计，QuadKAN在复杂环境中的表现得到了显著提升。

## 📊 实验亮点

实验结果表明，QuadKAN在多种地形下的表现优于现有最先进方法，具体体现在获得了更高的回报（提升幅度未知）、更大的行驶距离（提升幅度未知）和更少的碰撞次数（提升幅度未知），展示了其在视觉引导运动控制中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自主四足机器人、智能物流、灾后救援等场景。通过提高四足机器人的运动控制能力，QuadKAN能够在复杂和动态环境中更有效地执行任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We address vision-guided quadruped motion control with reinforcement learning (RL) and highlight the necessity of combining proprioception with vision for robust control. We propose QuadKAN, a spline-parameterized cross-modal policy instantiated with Kolmogorov-Arnold Networks (KANs). The framework incorporates a spline encoder for proprioception and a spline fusion head for proprioception-vision inputs. This structured function class aligns the state-to-action mapping with the piecewise-smooth nature of gait, improving sample efficiency, reducing action jitter and energy consumption, and providing interpretable posture-action sensitivities. We adopt Multi-Modal Delay Randomization (MMDR) and perform end-to-end training with Proximal Policy Optimization (PPO). Evaluations across diverse terrains, including both even and uneven surfaces and scenarios with static or dynamic obstacles, demonstrate that QuadKAN achieves consistently higher returns, greater distances, and fewer collisions than state-of-the-art (SOTA) baselines. These results show that spline-parameterized policies offer a simple, effective, and interpretable alternative for robust vision-guided locomotion. A repository will be made available upon acceptance.

