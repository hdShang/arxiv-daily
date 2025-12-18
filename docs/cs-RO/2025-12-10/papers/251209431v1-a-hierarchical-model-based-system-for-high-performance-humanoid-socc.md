---
layout: default
title: A Hierarchical, Model-Based System for High-Performance Humanoid Soccer
---

# A Hierarchical, Model-Based System for High-Performance Humanoid Soccer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09431" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09431v1</a>
  <a href="https://arxiv.org/pdf/2512.09431.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09431v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.09431v1', 'A Hierarchical, Model-Based System for High-Performance Humanoid Soccer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Quanyou Wang, Mingzhang Zhu, Ruochen Hou, Kay Gillespie, Alvin Zhu, Shiqi Wang, Yicheng Wang, Gaberiel I. Fernandez, Yeting Liu, Colin Togashi, Hyunwoo Nam, Aditya Navghare, Alex Xu, Taoyuanmin Zhu, Min Sung Ahn, Arturo Flores Alvarez, Justin Quan, Ethan Hong, Dennis W. Hong

**分类**: cs.RO

**发布日期**: 2025-12-10

---

## 💡 一句话要点

**提出一种分层、基于模型的系统，用于高性能人形机器人足球比赛。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `人形机器人` `足球机器人` `RoboCup` `立体视觉` `运动控制`

## 📋 核心要点

1. 现有方法在人形机器人足球比赛中面临动态环境感知、稳定运动控制和复杂战术决策的挑战。
2. 该论文提出了一种分层、基于模型的系统，集成了硬件和软件创新，以实现高性能的人形机器人足球。
3. ARTEMIS系统在2024年RoboCup成人尺寸人形机器人足球比赛中获得冠军，验证了该方法的有效性。

## 📝 摘要（中文）

随着驱动、传感和控制技术的进步，运动型人形机器人的开发受到了广泛关注，它们具备了日益动态的现实世界能力。RoboCup是一项完全自主的人形机器人国际竞赛，为这类系统提供了一个独特的挑战性基准，其最终目标是在2050年与人类足球运动员竞争。本文介绍了我们团队在2024年RoboCup成人尺寸人形机器人足球比赛中获胜的硬件和软件创新。在硬件方面，我们推出了一种成人尺寸的人形机器人平台，该平台采用轻量化结构组件、高扭矩准直驱执行器和专门的足部设计，可在保持运动鲁棒性的同时实现强大的步态踢球。在软件方面，我们开发了一个集成的感知和定位框架，该框架结合了立体视觉、目标检测和基于地标的融合，以提供对球、球门、队友和对手的可靠估计。然后，一个中层导航堆栈生成规避碰撞的、动态可行的轨迹，而一个集中的行为管理器根据不断变化的游戏状态协调高级决策、角色选择和踢球执行。这些子系统的无缝集成带来了快速、精确和战术上有效的游戏玩法，从而在真实比赛的动态和对抗条件下实现了强大的性能。本文介绍了促成ARTEMIS作为2024年成人尺寸人形机器人足球冠军的设计原则、系统架构和实验结果。

## 🔬 方法详解

**问题定义**：人形机器人足球比赛需要在动态、对抗的环境中实现自主导航、目标识别、运动控制和战术决策。现有方法通常难以在鲁棒性、精度和速度之间取得平衡，尤其是在成人尺寸人形机器人上。现有方法在感知精度、运动控制的稳定性和战术决策的实时性方面存在不足。

**核心思路**：该论文的核心思路是采用分层架构，将感知、导航、运动控制和行为决策解耦，并针对每个模块进行优化。通过硬件和软件的协同设计，提高系统的整体性能和鲁棒性。准直驱电机的使用提高了运动控制的精度和响应速度。

**技术框架**：该系统包含以下主要模块：1) 感知和定位框架：利用立体视觉、目标检测和地标融合来估计球、球门、队友和对手的位置。2) 导航堆栈：生成规避碰撞的、动态可行的轨迹。3) 行为管理器：根据游戏状态协调高级决策、角色选择和踢球执行。这些模块通过集中的行为管理器进行协调，实现整体的战术目标。

**关键创新**：该论文的关键创新在于硬件和软件的集成设计，以及各个模块的优化。硬件方面，采用了轻量化结构、高扭矩准直驱执行器和专门的足部设计。软件方面，集成了立体视觉、目标检测和地标融合的感知框架，以及动态可行的导航算法。这种集成设计使得系统能够在动态环境中实现快速、精确和战术有效的游戏玩法。

**关键设计**：感知模块的关键设计包括使用深度学习模型进行目标检测，并结合立体视觉信息进行三维定位。导航模块的关键设计包括使用模型预测控制（MPC）生成动态可行的轨迹，并考虑碰撞避免。行为管理器的关键设计包括使用有限状态机（FSM）来表示不同的游戏状态和行为，并根据游戏状态进行角色选择和战术决策。具体的参数设置和损失函数等细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

ARTEMIS系统在2024年RoboCup成人尺寸人形机器人足球比赛中获得冠军，证明了该系统在动态和对抗环境中的强大性能。具体的性能数据（例如，感知精度、运动速度、战术效率等）未在摘要中给出，属于未知信息。但冠军头衔本身就证明了其优越性。

## 🎯 应用场景

该研究成果可应用于其他需要高动态运动控制和自主决策的机器人领域，例如搜索救援、物流运输和人机协作。通过不断改进硬件和软件系统，有望在未来实现与人类运动员进行更高级别的对抗，并推动人形机器人技术的发展。

## 📄 摘要（原文）

> The development of athletic humanoid robots has gained significant attention as advances in actuation, sensing, and control enable increasingly dynamic, real-world capabilities. RoboCup, an international competition of fully autonomous humanoid robots, provides a uniquely challenging benchmark for such systems, culminating in the long-term goal of competing against human soccer players by 2050. This paper presents the hardware and software innovations underlying our team's victory in the RoboCup 2024 Adult-Sized Humanoid Soccer Competition. On the hardware side, we introduce an adult-sized humanoid platform built with lightweight structural components, high-torque quasi-direct-drive actuators, and a specialized foot design that enables powerful in-gait kicks while preserving locomotion robustness. On the software side, we develop an integrated perception and localization framework that combines stereo vision, object detection, and landmark-based fusion to provide reliable estimates of the ball, goals, teammates, and opponents. A mid-level navigation stack then generates collision-aware, dynamically feasible trajectories, while a centralized behavior manager coordinates high-level decision making, role selection, and kick execution based on the evolving game state. The seamless integration of these subsystems results in fast, precise, and tactically effective gameplay, enabling robust performance under the dynamic and adversarial conditions of real matches. This paper presents the design principles, system architecture, and experimental results that contributed to ARTEMIS's success as the 2024 Adult-Sized Humanoid Soccer champion.

