---
layout: default
title: "M4Diffuser: Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation"
---

# M4Diffuser: Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14980" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14980v1</a>
  <a href="https://arxiv.org/pdf/2509.14980.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14980v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14980v1', 'M4Diffuser: Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ju Dong, Lei Zhang, Liding Zhang, Yao Ling, Yu Fu, Kaixin Bai, Zoltán-Csaba Márton, Zhenshan Bing, Zhaopeng Chen, Alois Christian Knoll, Jianwei Zhang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-09-18

**备注**: Project page: https://sites.google.com/view/m4diffuser, 10 pages, 9 figures

---

## 💡 一句话要点

**M4Diffuser：多视角扩散策略与可操作性感知控制，提升移动操作的鲁棒性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `移动操作` `多视角学习` `扩散模型` `二次规划控制` `机器人控制` `可操作性` `非结构化环境`

## 📋 核心要点

1. 现有移动操作方法受限于单视角视野，难以在复杂环境中有效探索和泛化，导致操作失败。
2. M4Diffuser融合多视角扩散策略与可操作性感知的QP控制器，生成全局目标并优化执行，提升鲁棒性。
3. 实验结果表明，M4Diffuser在成功率和碰撞率上显著优于基线方法，展现了良好的泛化能力。

## 📝 摘要（中文）

本文提出了一种名为M4Diffuser的混合框架，用于解决移动操作中单视角方法在非结构化环境中泛化能力不足以及传统控制器在奇异点附近效率和可操作性差的问题。该框架集成了多视角扩散策略和一个新型的简化且可操作性感知的二次规划(ReM-QP)控制器。扩散策略利用本体感受状态和互补的相机视角，结合近距离物体细节和全局场景上下文，生成世界坐标系中与任务相关的末端执行器目标。ReM-QP控制器通过消除松弛变量提高计算效率，并结合可操作性感知偏好，增强在奇异点附近的鲁棒性。在仿真和真实环境中的实验表明，M4Diffuser的成功率比基线方法高7%到56%，碰撞减少3%到31%。该方法展示了平滑全身协调的鲁棒性能，并对未见过的任务具有很强的泛化能力，为非结构化环境中可靠的移动操作铺平了道路。

## 🔬 方法详解

**问题定义**：移动操作需要移动底座和机械臂的协同控制，同时感知全局场景上下文和精细的物体细节。现有的单视角方法由于视野有限，在非结构化环境中常常失效，泛化能力不足。此外，传统的控制器虽然稳定，但在奇异点附近效率低下且可操作性差。

**核心思路**：M4Diffuser的核心思路是利用多视角信息来弥补单视角信息的不足，并结合扩散模型生成任务相关的末端执行器目标。然后，通过一个专门设计的QP控制器来高效且鲁棒地执行这些目标，特别是在奇异点附近。这种混合方法旨在结合扩散模型的泛化能力和QP控制器的精确控制能力。

**技术框架**：M4Diffuser框架包含两个主要模块：多视角扩散策略和简化且可操作性感知的QP (ReM-QP)控制器。首先，多视角扩散策略接收本体感受状态和来自多个摄像头的图像，生成末端执行器在世界坐标系中的目标位置。然后，ReM-QP控制器接收这些目标位置，并控制移动底座和机械臂协同运动，以达到目标位置。

**关键创新**：M4Diffuser的关键创新在于以下几点：1) 提出了一个多视角扩散策略，能够融合来自多个摄像头的互补信息，从而更好地理解场景。2) 设计了一个简化且可操作性感知的QP控制器，该控制器通过消除松弛变量提高了计算效率，并利用可操作性感知偏好增强了在奇异点附近的鲁棒性。3) 将扩散模型和QP控制器结合起来，充分利用了两种方法的优点。

**关键设计**：多视角扩散策略使用扩散模型来生成末端执行器的目标位置。该模型以本体感受状态和多视角图像作为输入，并学习生成与任务相关的目标位置。ReM-QP控制器通过最小化一个二次规划问题来控制移动底座和机械臂。该QP问题包含目标位置误差、关节力矩限制和可操作性感知偏好等约束。通过调整这些约束的权重，可以控制机器人的运动行为。

## 📊 实验亮点

M4Diffuser在仿真和真实环境中的实验结果表明，其性能显著优于基线方法。具体而言，M4Diffuser在成功率上比基线方法高7%到56%，碰撞减少3%到31%。这些结果表明，M4Diffuser能够有效地提升移动操作的鲁棒性和泛化能力，使其能够在非结构化环境中可靠地完成任务。

## 🎯 应用场景

M4Diffuser在非结构化环境中具有广泛的应用前景，例如家庭服务机器人、仓库自动化、灾难救援等。该方法能够提升机器人在复杂环境中的操作能力和鲁棒性，使其能够完成更复杂的任务，例如物体抓取、放置、组装等。未来，可以进一步研究如何将M4Diffuser应用于更广泛的机器人平台和任务。

## 📄 摘要（原文）

> Mobile manipulation requires the coordinated control of a mobile base and a robotic arm while simultaneously perceiving both global scene context and fine-grained object details. Existing single-view approaches often fail in unstructured environments due to limited fields of view, exploration, and generalization abilities. Moreover, classical controllers, although stable, struggle with efficiency and manipulability near singularities. To address these challenges, we propose M4Diffuser, a hybrid framework that integrates a Multi-View Diffusion Policy with a novel Reduced and Manipulability-aware QP (ReM-QP) controller for mobile manipulation. The diffusion policy leverages proprioceptive states and complementary camera perspectives with both close-range object details and global scene context to generate task-relevant end-effector goals in the world frame. These high-level goals are then executed by the ReM-QP controller, which eliminates slack variables for computational efficiency and incorporates manipulability-aware preferences for robustness near singularities. Comprehensive experiments in simulation and real-world environments show that M4Diffuser achieves 7 to 56 percent higher success rates and reduces collisions by 3 to 31 percent over baselines. Our approach demonstrates robust performance for smooth whole-body coordination, and strong generalization to unseen tasks, paving the way for reliable mobile manipulation in unstructured environments. Details of the demo and supplemental material are available on our project website https://sites.google.com/view/m4diffuser.

