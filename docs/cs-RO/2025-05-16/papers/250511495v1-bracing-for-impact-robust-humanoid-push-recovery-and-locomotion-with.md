---
layout: default
title: Bracing for Impact: Robust Humanoid Push Recovery and Locomotion with Reduced Order Models
---

# Bracing for Impact: Robust Humanoid Push Recovery and Locomotion with Reduced Order Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11495" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11495v1</a>
  <a href="https://arxiv.org/pdf/2505.11495.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11495v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11495v1', 'Bracing for Impact: Robust Humanoid Push Recovery and Locomotion with Reduced Order Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lizhi Yang, Blake Werner, Adrian B. Ghansah, Aaron D. Ames

**分类**: cs.RO

**发布日期**: 2025-05-16

---

## 💡 一句话要点

**提出统一框架以增强类人机器人在行走中的推力恢复能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `类人机器人` `推力恢复` `动态行走` `模型预测控制` `环境交互` `鲁棒性` `仿真研究`

## 📋 核心要点

1. 现有方法在类人机器人行走过程中对推力的恢复能力不足，限制了其在复杂环境中的应用。
2. 本文提出的框架通过结合SRB-MPC与HLIP动力学，利用环境特征和机器人手臂实现动态推力恢复。
3. 仿真结果显示，该方法在扰动拒绝和跟踪性能上显著优于HLIP，能够有效应对多种推力场景。

## 📝 摘要（中文）

在行走过程中进行推力恢复将促进类人机器人在以人为中心的环境中的应用。本文提出了一种统一的行走控制与推力恢复框架，利用机器人的手臂在动态行走中进行推力恢复。关键创新在于结合单刚体模型预测控制（SRB-MPC）与混合线性倒立摆（HLIP）动力学，利用环境（如墙壁）来辅助推力恢复，动态调整接触力和步态模式。大量仿真结果表明，与单独使用HLIP相比，该方法在扰动拒绝和跟踪性能上有显著提升，机器人能够在行走速度达到0.5m/s的情况下，从高达100N的推力中恢复，且在倾斜墙面和多方向推力的场景中也表现出良好的鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决类人机器人在行走过程中对外部推力的恢复能力不足的问题。现有方法在动态环境中难以有效应对突发的推力，影响了机器人的稳定性和安全性。

**核心思路**：论文的核心思路是利用机器人的手臂与环境（如墙壁）进行互动，以增强推力恢复能力。通过结合SRB-MPC与HLIP动力学，动态调整接触力和步态模式，从而实现更为稳健的行走控制。

**技术框架**：整体架构包括环境感知模块、推力检测模块、控制决策模块和执行模块。环境感知模块负责获取周围环境信息，推力检测模块识别外部推力，控制决策模块基于感知信息生成控制指令，执行模块则实现具体的运动控制。

**关键创新**：最重要的技术创新在于将SRB-MPC与HLIP动力学相结合，利用环境特征进行推力恢复。这种方法与传统的单一控制策略相比，能够更好地应对动态变化的环境和突发的推力。

**关键设计**：在设计中，关键参数包括接触力的动态调整范围和步态模式的实时优化。损失函数设计考虑了稳定性和响应速度的平衡，确保机器人在受到推力时能够迅速做出反应。

## 📊 实验亮点

实验结果显示，提出的方法在扰动拒绝和跟踪性能上显著优于HLIP，机器人能够在行走速度达到0.5m/s的情况下，从高达100N的推力中恢复。该方法在倾斜墙面和多方向推力的场景中也表现出良好的鲁棒性，验证了其广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人和人机协作系统等。通过提高类人机器人在复杂环境中的稳定性和适应能力，能够更好地满足人类需求，推动机器人技术在实际生活中的广泛应用。

## 📄 摘要（原文）

> Push recovery during locomotion will facilitate the deployment of humanoid robots in human-centered environments. In this paper, we present a unified framework for walking control and push recovery for humanoid robots, leveraging the arms for push recovery while dynamically walking. The key innovation is to use the environment, such as walls, to facilitate push recovery by combining Single Rigid Body model predictive control (SRB-MPC) with Hybrid Linear Inverted Pendulum (HLIP) dynamics to enable robust locomotion, push detection, and recovery by utilizing the robot's arms to brace against such walls and dynamically adjusting the desired contact forces and stepping patterns. Extensive simulation results on a humanoid robot demonstrate improved perturbation rejection and tracking performance compared to HLIP alone, with the robot able to recover from pushes up to 100N for 0.2s while walking at commanded speeds up to 0.5m/s. Robustness is further validated in scenarios with angled walls and multi-directional pushes.

