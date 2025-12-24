---
layout: default
title: "ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes"
---

# ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14317" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14317v3</a>
  <a href="https://arxiv.org/pdf/2506.14317.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14317v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14317v3', 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeyuan Chen, Qiyang Yan, Yuanpei Chen, Tianhao Wu, Jiyao Zhang, Zihan Ding, Jinzhou Li, Yaodong Yang, Hao Dong

**分类**: cs.RO

**发布日期**: 2025-06-17 (更新: 2025-09-04)

**备注**: Accepted at CoRL 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://clutterdexgrasp.github.io/)

---

## 💡 一句话要点

**提出ClutterDexGrasp以解决复杂场景中的灵巧抓取问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `灵巧抓取` `杂乱场景` `教师-学生框架` `模仿学习` `零-shot学习` `安全课程` `3D扩散策略`

## 📋 核心要点

1. 现有方法主要集中于单一物体抓取，无法有效处理复杂的杂乱场景，导致抓取性能不足。
2. 本文提出ClutterDexGrasp，一个两阶段的教师-学生框架，利用模拟学习和安全课程实现目标导向的灵巧抓取。
3. 该系统在多样物体和布局下表现出色，首次实现了零-shot的闭环抓取，展示了强大的泛化能力。

## 📝 摘要（中文）

灵巧抓取在复杂场景中面临显著挑战，主要由于物体几何形状多样、遮挡和潜在碰撞等因素。现有方法主要集中于单一物体抓取或抓取姿态预测，无法有效应对复杂的杂乱场景。为了解决这些局限性，本文提出ClutterDexGrasp，一个基于教师-学生框架的闭环目标导向灵巧抓取系统，能够在现实中实现零-shot部署，同时保持强大的泛化能力。该系统通过模仿学习将教师策略的知识提炼到学生3D扩散策略中，展示了在多样物体和布局下的稳健性能。

## 🔬 方法详解

**问题定义**：本文旨在解决复杂杂乱场景中的灵巧抓取问题。现有方法往往只关注单一物体的抓取，缺乏对多物体交互的处理能力，导致在实际应用中效果不佳。

**核心思路**：论文提出的ClutterDexGrasp框架通过教师-学生学习机制，结合模拟环境中的课程学习，旨在实现目标导向的灵巧抓取。该设计使得系统能够在真实环境中进行零-shot部署，克服了传统方法的局限性。

**技术框架**：ClutterDexGrasp框架分为两个阶段：首先，教师策略在模拟环境中进行训练，利用杂乱度课程学习和空间嵌入场景表示；其次，通过模仿学习将教师的知识转移到学生3D扩散策略（DP3）中，后者能够处理部分点云观测。

**关键创新**：本研究的最大创新在于提出了一个零-shot的闭环系统，能够在复杂场景中实现目标导向的灵巧抓取。这一方法与现有技术的本质区别在于其对多物体交互的有效处理和安全课程的引入。

**关键设计**：在教师策略的训练中，采用了几何和空间嵌入的场景表示，并设计了综合安全课程，以确保抓取行为的安全性和动态适应性。

## 📊 实验亮点

实验结果表明，ClutterDexGrasp在多样物体和布局下的抓取成功率显著高于传统方法，首次实现了在复杂场景中的零-shot闭环抓取，展示了强大的泛化能力和稳健性。

## 🎯 应用场景

该研究的潜在应用领域包括自动化仓库、家庭机器人以及服务机器人等场景，能够显著提升机器人在复杂环境中的抓取能力。未来，这一技术有望推动智能机器人在日常生活中的广泛应用，提升人机协作的效率和安全性。

## 📄 摘要（原文）

> Dexterous grasping in cluttered scenes presents significant challenges due to diverse object geometries, occlusions, and potential collisions. Existing methods primarily focus on single-object grasping or grasp-pose prediction without interaction, which are insufficient for complex, cluttered scenes. Recent vision-language-action models offer a potential solution but require extensive real-world demonstrations, making them costly and difficult to scale. To address these limitations, we revisit the sim-to-real transfer pipeline and develop key techniques that enable zero-shot deployment in reality while maintaining robust generalization. We propose ClutterDexGrasp, a two-stage teacher-student framework for closed-loop target-oriented dexterous grasping in cluttered scenes. The framework features a teacher policy trained in simulation using clutter density curriculum learning, incorporating both a geometry and spatially-embedded scene representation and a novel comprehensive safety curriculum, enabling general, dynamic, and safe grasping behaviors. Through imitation learning, we distill the teacher's knowledge into a student 3D diffusion policy (DP3) that operates on partial point cloud observations. To the best of our knowledge, this represents the first zero-shot sim-to-real closed-loop system for target-oriented dexterous grasping in cluttered scenes, demonstrating robust performance across diverse objects and layouts. More details and videos are available at https://clutterdexgrasp.github.io/.

