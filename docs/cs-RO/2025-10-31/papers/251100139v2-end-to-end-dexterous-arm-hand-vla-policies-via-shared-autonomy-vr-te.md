---
layout: default
title: End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy for Efficient Data Collection
---

# End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy for Efficient Data Collection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00139" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00139v2</a>
  <a href="https://arxiv.org/pdf/2511.00139.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00139v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.00139v2', 'End-to-End Dexterous Arm-Hand VLA Policies via Shared Autonomy: VR Teleoperation Augmented by Autonomous Hand VLA Policy for Efficient Data Collection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Cui, Yujian Zhang, Lina Tao, Yang Li, Xinyu Yi, Zhibin Li

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-31 (更新: 2025-12-13)

---

## 💡 一句话要点

**提出基于共享自主的灵巧臂手VLA策略，用于高效数据收集。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `灵巧操作` `共享自主` `VR遥操作` `视觉语言动作模型` `机器人学习`

## 📋 核心要点

1. 现有灵巧操作数据收集方法面临人工遥操作负担重和自动规划动作不自然等挑战。
2. 提出共享自主框架，结合VR遥操作的手臂控制和自主VLA策略的手部控制，降低认知负荷。
3. 实验表明，该框架能高效生成高质量数据，训练的VLA策略在多种物体上达到90%的成功率。

## 📝 摘要（中文）

本文提出了一种共享自主框架，旨在解决通用机器人实现类人灵巧操作的挑战。该框架利用VR遥操作引导机器人手臂的宏观运动，同时采用自主的DexGrasp-VLA策略，通过实时触觉和视觉反馈处理精细的手部控制。这种分工显著降低了操作员的认知负荷，并能够高效收集高质量的臂手协同演示数据。利用这些数据，训练了一个端到端的VLA策略，并引入了臂手特征增强模块，该模块捕获宏观和微观运动的独特和共享表示，以实现更自然的协调。此外，还提出了纠正性遥操作系统，通过人机协作的失败恢复实现策略的持续改进。实验表明，该框架能够以最少的人力生成高质量的数据，并在各种物体（包括未见过的实例）上实现了90%的成功率。综合评估验证了该系统在开发灵巧操作能力方面的有效性。

## 🔬 方法详解

**问题定义**：现有方法在收集高质量的灵巧操作数据时面临挑战。人工遥操作需要操作员付出大量的认知努力，容易疲劳，且效率较低。而完全自动化的规划方法往往生成不自然的运动，难以泛化到复杂场景。因此，如何高效地收集高质量的臂手协同操作数据，是本文要解决的核心问题。

**核心思路**：本文的核心思路是将控制任务分解为宏观和微观两个层面，并分别由人类操作员和自主策略来控制。人类操作员通过VR遥操作负责引导机器人的手臂姿态，进行宏观的运动规划。而自主的DexGrasp-VLA策略则负责处理精细的手部控制，利用实时触觉和视觉反馈进行抓取和操作。这种分工协作的方式可以有效降低操作员的认知负荷，同时保证动作的自然性和高效性。

**技术框架**：整体框架包含三个主要模块：1) **共享自主控制模块**：人类操作员通过VR界面控制机械臂的全局姿态，自主DexGrasp-VLA策略控制机械手的精细动作。2) **臂手特征增强模块**：该模块用于增强VLA策略对臂手协同动作的理解，通过学习臂手动作的共享和独立特征，提升策略的泛化能力。3) **纠正性遥操作系统**：允许人类操作员在自主策略失败时介入，通过遥操作进行纠正，并将纠正数据用于策略的持续改进。

**关键创新**：本文的关键创新在于共享自主控制框架和臂手特征增强模块。共享自主控制框架通过人机协作的方式，实现了高效的数据收集。臂手特征增强模块则通过学习臂手动作的共享和独立特征，提升了VLA策略的泛化能力和鲁棒性。此外，纠正性遥操作系统也为策略的持续改进提供了有效的手段。

**关键设计**：DexGrasp-VLA策略使用Transformer架构，输入包括视觉图像、触觉传感器数据和语言指令。臂手特征增强模块采用双分支网络结构，分别提取手臂和手部的特征，并通过注意力机制进行融合。损失函数包括模仿学习损失和强化学习损失，用于训练VLA策略。纠正性遥操作系统使用户能够通过VR界面实时调整机器人的姿态和手部动作。

## 📊 实验亮点

实验结果表明，该框架能够以最少的人力生成高质量的数据，并且训练得到的VLA策略在各种物体（包括未见过的实例）上实现了90%的抓取成功率。与传统的遥操作方法相比，该方法显著降低了操作员的认知负荷，并提高了数据收集的效率。

## 🎯 应用场景

该研究成果可应用于各种需要灵巧操作的机器人任务中，例如：工业自动化中的精密装配、医疗机器人中的微创手术、家庭服务机器人中的物品整理等。通过高效的数据收集和策略学习，可以显著降低机器人部署的成本和难度，加速机器人在实际场景中的应用。

## 📄 摘要（原文）

> Achieving human-like dexterous manipulation remains a major challenge for general-purpose robots. While Vision-Language-Action (VLA) models show potential in learning skills from demonstrations, their scalability is limited by scarce high-quality training data. Existing data collection methods face inherent constraints: manual teleoperation overloads human operators, while automated planning often produces unnatural motions. We propose a Shared Autonomy framework that divides control between macro and micro motions. A human operator guides the robot's arm pose through intuitive VR teleoperation, while an autonomous DexGrasp-VLA policy handles fine-grained hand control using real-time tactile and visual feedback. This division significantly reduces cognitive load and enables efficient collection of high-quality coordinated arm-hand demonstrations. Using this data, we train an end-to-end VLA policy enhanced with our novel Arm-Hand Feature Enhancement module, which captures both distinct and shared representations of macro and micro movements for more natural coordination. Our Corrective Teleoperation system enables continuous policy improvement through human-in-the-loop failure recovery. Experiments demonstrate that our framework generates high-quality data with minimal manpower and achieves a 90% success rate across diverse objects, including unseen instances. Comprehensive evaluations validate the system's effectiveness in developing dexterous manipulation capabilities.

