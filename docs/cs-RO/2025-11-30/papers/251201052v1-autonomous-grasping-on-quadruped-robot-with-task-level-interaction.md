---
layout: default
title: Autonomous Grasping On Quadruped Robot With Task Level Interaction
---

# Autonomous Grasping On Quadruped Robot With Task Level Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.01052" class="toolbar-btn" target="_blank">📄 arXiv: 2512.01052v1</a>
  <a href="https://arxiv.org/pdf/2512.01052.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.01052v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.01052v1', 'Autonomous Grasping On Quadruped Robot With Task Level Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhtadin, Mochammad Hilmi Rusydiansyah, Mauridhi Hery Purnomo, I Ketut Eddy Purnama, Chastine Fatichah

**分类**: cs.RO

**发布日期**: 2025-11-30

**备注**: This work has been submitted to the IEEE for possible publication

---

## 💡 一句话要点

**提出基于任务级交互的四足机器人自主抓取系统，提升复杂环境服务能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `四足机器人` `自主抓取` `任务级交互` `机器人操作系统` `GraspNet`

## 📋 核心要点

1. 现有四足机器人主要关注移动性，缺乏物体操作能力，难以满足复杂任务需求。
2. 本文提出一种基于任务级交互的自主抓取系统，将机械臂和夹爪集成到四足机器人上。
3. 实验结果表明，该系统能够实现自主导航、物体检测和抓取，抓取成功率达到75%。

## 📝 摘要（中文）

本文提出了一种基于任务级交互的四足机器人自主抓取系统。该系统集成了机械臂和夹爪，并搭载于四足机器人平台。通过ROS构建分层控制系统，并设计了基于Web的人机交互界面。该机器人能够自主执行导航、物体检测和抓取等任务，其中物体抓取使用了GraspNet算法。实验结果表明，该机器人能够准确且稳定地执行任务，在12次抓取尝试中成功率达到75%。该系统展示了四足机器人在现实环境中作为服务机器人的巨大潜力。

## 🔬 方法详解

**问题定义**：现有四足机器人主要关注移动能力，缺乏与环境交互的能力，尤其是在复杂地形下进行物体抓取。手动控制加装机械臂的四足机器人进行远程操作非常困难，需要复杂的指令才能完成任务。因此，需要开发一种自主抓取系统，使四足机器人能够在复杂环境中自主完成物体抓取任务。

**核心思路**：本文的核心思路是构建一个基于任务级交互的自主抓取系统，通过分层控制系统和人机交互界面，实现对四足机器人的高级指令控制。该系统将导航、物体检测和抓取等任务进行解耦，并使用GraspNet算法实现物体的精确抓取。

**技术框架**：该系统主要包含以下几个模块：1) 硬件集成：将机械臂和夹爪集成到四足机器人平台上。2) 分层控制系统：使用ROS构建分层控制系统，实现对机器人运动、感知和抓取的控制。3) 人机交互界面：设计基于Web的人机交互界面，允许用户发布高级指令，例如“导航到目标地点”或“抓取目标物体”。4) 自主抓取模块：使用GraspNet算法进行物体检测和抓取姿态估计。

**关键创新**：该研究的关键创新在于将任务级交互的概念引入到四足机器人的控制中，允许用户通过高级指令控制机器人执行复杂任务，而无需手动控制机器人的每一个关节。此外，该研究还成功地将GraspNet算法应用到四足机器人平台上，实现了对未知物体的自主抓取。

**关键设计**：该系统采用ROS作为软件框架，方便模块化开发和集成。GraspNet算法用于估计物体的抓取姿态，并生成抓取轨迹。人机交互界面采用Web技术，方便用户远程控制机器人。控制系统采用分层结构，将高级指令分解为低级控制指令，实现对机器人的精确控制。

## 📊 实验亮点

实验结果表明，该系统能够实现四足机器人的自主导航、物体检测和抓取。在12次抓取尝试中，该系统成功抓取物体的次数为9次，抓取成功率达到75%。这表明该系统具有较高的稳定性和可靠性，能够满足实际应用的需求。

## 🎯 应用场景

该研究成果可应用于物流、仓储、搜救、勘探等领域。例如，在灾难现场，配备自主抓取系统的四足机器人可以用于搜寻和搬运遇难者或重要物资。在物流和仓储领域，该机器人可以用于自动分拣和搬运货物。此外，该技术还可以应用于危险环境下的勘探任务，例如核电站检修或深海探测。

## 📄 摘要（原文）

> Quadruped robots are increasingly used in various applications due to their high mobility and ability to operate in diverse terrains. However, most available quadruped robots are primarily focused on mobility without object manipulation capabilities. Equipping a quadruped robot with a robotic arm and gripper introduces a challenge in manual control, especially in remote scenarios that require complex commands. This research aims to develop an autonomous grasping system on a quadruped robot using a task-level interaction approach. The system includes hardware integration of a robotic arm and gripper onto the quadruped robot's body, a layered control system designed using ROS, and a web-based interface for human-robot interaction. The robot is capable of autonomously performing tasks such as navigation, object detection, and grasping using GraspNet. Testing was conducted through real-world scenarios to evaluate navigation, object selection and grasping, and user experience. The results show that the robot can perform tasks accurately and consistently, achieving a grasping success rate of 75 % from 12 trials. Therefore, the system demonstrates significant potential in enhancing the capabilities of quadruped robots as service robots in real-world environments.

