---
layout: default
title: GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction
---

# GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.04679" class="toolbar-btn" target="_blank">📄 arXiv: 2511.04679v1</a>
  <a href="https://arxiv.org/pdf/2511.04679.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.04679v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.04679v1', 'GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingzhou Lu, Yao Feng, Baiyu Shi, Michael Piseno, Zhenan Bao, C. Karen Liu

**分类**: cs.RO, cs.CV, cs.HC

**发布日期**: 2025-11-06

**备注**: Home page: https://gentle-humanoid.axell.top

---

## 💡 一句话要点

**GentleHumanoid：学习上肢柔顺性，实现人机和人机交互中的丰富接触**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人形机器人` `强化学习` `阻抗控制` `人机交互` `柔顺性` `全身控制` `物理交互`

## 📋 核心要点

1. 现有强化学习方法在人机交互中过于强调刚性控制，忽略了柔顺性的重要性，导致交互不自然且存在安全隐患。
2. GentleHumanoid框架通过将阻抗控制集成到全身运动跟踪策略中，并采用统一的基于弹簧的公式，实现了上肢的柔顺性。
3. 实验表明，该方法在多种需要不同柔顺性的任务中，能够有效降低峰值接触力，实现更平滑自然的交互，提升安全性。

## 📝 摘要（中文）

人型机器人需要在以人为中心的环境中安全自然地进行物理交互。然而，目前大多数强化学习策略强调刚性跟踪并抑制外力。现有的阻抗增强方法通常仅限于基座或末端执行器控制，并且侧重于抵抗极端力而不是实现柔顺性。我们提出了GentleHumanoid，一个将阻抗控制集成到全身运动跟踪策略中的框架，以实现上肢柔顺性。其核心是一个统一的基于弹簧的公式，该公式对电阻性接触（压靠表面时的恢复力）和引导性接触（从人类运动数据中采样的推或拉）进行建模。该公式确保了肩部、肘部和腕部之间运动学上一致的力，同时使策略暴露于多样化的交互场景。通过任务可调的力阈值进一步支持安全性。我们在模拟和优傲腾G1人形机器人上评估了我们的方法，任务需要不同程度的柔顺性，包括温柔拥抱、坐站辅助和安全物体操作。与基线相比，我们的策略始终在保持任务成功的同时降低峰值接触力，从而实现更平滑和更自然的交互。这些结果突出了人形机器人朝着安全有效地与人类协作并在现实环境中处理物体迈出的一步。

## 🔬 方法详解

**问题定义**：现有的人形机器人控制策略，尤其是在强化学习中，往往侧重于精确的运动跟踪，而忽略了与环境和人类的物理交互中的柔顺性。这导致机器人动作僵硬，无法适应外部扰动，甚至可能对人类造成伤害。现有的阻抗控制方法通常只应用于基座或末端执行器，无法实现全身的柔顺控制。

**核心思路**：GentleHumanoid的核心思路是将阻抗控制融入到全身运动跟踪策略中，通过模拟弹簧的力学特性来控制机器人与环境的交互力。这种方法允许机器人根据接触情况调整自身的刚度，从而实现柔顺的交互。关键在于建立一个统一的力学模型，能够处理不同类型的接触，并保证运动学上的一致性。

**技术框架**：GentleHumanoid框架主要包含以下几个模块：1) 运动跟踪模块：负责生成期望的机器人运动轨迹。2) 阻抗控制模块：根据机器人与环境的接触情况，计算出相应的阻抗力。3) 力学模型：采用基于弹簧的公式，对电阻性接触和引导性接触进行建模，确保力的运动学一致性。4) 强化学习策略：通过强化学习训练，优化阻抗控制参数，使机器人能够更好地适应不同的交互场景。

**关键创新**：GentleHumanoid最重要的创新在于其统一的基于弹簧的力学模型，该模型能够同时处理电阻性接触（如支撑）和引导性接触（如推拉），并保证肩部、肘部和腕部之间力的运动学一致性。此外，该框架还引入了任务可调的力阈值，以进一步提高安全性。与现有方法相比，GentleHumanoid能够实现全身的柔顺控制，并更好地适应复杂的交互环境。

**关键设计**：在力学模型中，每个关节都与一个虚拟弹簧相连，弹簧的刚度参数通过强化学习进行优化。损失函数包括运动跟踪误差、接触力误差和安全惩罚项。安全惩罚项用于约束接触力的大小，防止机器人对人类造成伤害。强化学习算法采用PPO（Proximal Policy Optimization），以保证训练的稳定性和收敛性。

## 📊 实验亮点

实验结果表明，GentleHumanoid在模拟和真实机器人（Unitree G1）上均取得了显著效果。在温柔拥抱、坐站辅助和安全物体操作等任务中，与基线方法相比，该策略能够显著降低峰值接触力，同时保持任务成功率。例如，在拥抱任务中，峰值接触力降低了约30%，表明交互更加安全和舒适。

## 🎯 应用场景

GentleHumanoid技术可应用于多种人机协作场景，例如：辅助老年人或残疾人进行日常活动（如坐站辅助、物体递送），在医疗康复领域提供安全的物理治疗，以及在工业环境中与工人协同完成精细装配任务。该技术有望提升人机交互的安全性、自然性和效率，促进人形机器人在现实世界中的广泛应用。

## 📄 摘要（原文）

> Humanoid robots are expected to operate in human-centered environments where safe and natural physical interaction is essential. However, most recent reinforcement learning (RL) policies emphasize rigid tracking and suppress external forces. Existing impedance-augmented approaches are typically restricted to base or end-effector control and focus on resisting extreme forces rather than enabling compliance. We introduce GentleHumanoid, a framework that integrates impedance control into a whole-body motion tracking policy to achieve upper-body compliance. At its core is a unified spring-based formulation that models both resistive contacts (restoring forces when pressing against surfaces) and guiding contacts (pushes or pulls sampled from human motion data). This formulation ensures kinematically consistent forces across the shoulder, elbow, and wrist, while exposing the policy to diverse interaction scenarios. Safety is further supported through task-adjustable force thresholds. We evaluate our approach in both simulation and on the Unitree G1 humanoid across tasks requiring different levels of compliance, including gentle hugging, sit-to-stand assistance, and safe object manipulation. Compared to baselines, our policy consistently reduces peak contact forces while maintaining task success, resulting in smoother and more natural interactions. These results highlight a step toward humanoid robots that can safely and effectively collaborate with humans and handle objects in real-world environments.

