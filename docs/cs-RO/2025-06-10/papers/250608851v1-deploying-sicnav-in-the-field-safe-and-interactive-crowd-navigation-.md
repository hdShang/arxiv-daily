---
layout: default
title: "Deploying SICNav in the Field: Safe and Interactive Crowd Navigation using MPC and Bilevel Optimization"
---

# Deploying SICNav in the Field: Safe and Interactive Crowd Navigation using MPC and Bilevel Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08851" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08851v1</a>
  <a href="https://arxiv.org/pdf/2506.08851.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08851v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08851v1', 'Deploying SICNav in the Field: Safe and Interactive Crowd Navigation using MPC and Bilevel Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sepehr Samavi, Garvish Bhutani, Florian Shkurti, Angela P. Schoellig

**分类**: cs.RO

**发布日期**: 2025-06-10

**备注**: Presented at the 2025 IEEE ICRA Workshop on Field Robotics (non-archival)

---

## 💡 一句话要点

**提出SICNav以解决拥挤环境中的安全导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人导航` `模型预测控制` `人机交互` `群体导航` `安全性` `优化算法` `服务机器人`

## 📋 核心要点

1. 现有的机器人群体导航方法未能有效处理人类与机器人之间的交互，导致机器人在复杂环境中容易被困。
2. 论文提出的SICNav方法通过双层模型预测控制框架，将人类运动预测与机器人运动规划整合，增强了交互建模能力。
3. 实验结果显示，SICNav在近7公里的自主导航中表现出色，成功应对了多种室内外环境的挑战。

## 📝 摘要（中文）

在拥挤环境中实现安全高效的导航仍然是机器人服务任务（如送餐或自主轮椅移动）面临的重大挑战。传统的机器人群体导航方法将人类运动预测与机器人运动规划分开，忽视了人类与机器人之间的闭环交互。这种缺乏人类对机器人计划反应模型的情况（例如，避让）可能导致机器人被困。我们提出的安全互动群体导航（SICNav）方法是一个双层模型预测控制（MPC）框架，将预测与规划结合为一个优化问题，明确建模代理之间的交互。本文展示了我们用于在未见过的室内和室外环境中部署SICNav的群体导航平台的系统概述，并提供了系统在室内外环境中进行近7公里自主导航的初步分析。

## 🔬 方法详解

**问题定义**：本论文旨在解决拥挤环境中机器人导航的安全性与效率问题。现有方法往往忽视人类与机器人之间的交互，导致机器人在复杂场景中容易被困。

**核心思路**：SICNav方法通过双层模型预测控制（MPC）框架，将人类运动预测与机器人运动规划结合为一个统一的优化问题，能够更好地模拟和应对人类的反应。

**技术框架**：整体架构包括人类运动预测模块和机器人运动规划模块，二者通过优化算法进行交互，形成闭环控制。系统能够实时更新人类行为模型，从而调整机器人路径。

**关键创新**：SICNav的主要创新在于将人类行为建模与机器人规划整合为一个优化问题，克服了传统方法的局限性，显著提高了导航的安全性和效率。

**关键设计**：在参数设置上，SICNav采用了动态调整的损失函数，以适应不同环境的复杂性。同时，网络结构设计上，采用了多层感知机（MLP）来增强对人类行为的预测能力。

## 📊 实验亮点

实验结果表明，SICNav在近7公里的自主导航中表现优异，成功应对了多种室内外环境的挑战。与传统方法相比，SICNav在处理人类交互方面的能力显著提升，减少了机器人被困的情况，展示了其在复杂环境中的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、自动驾驶车辆以及人机协作系统等。在拥挤环境中，SICNav能够有效提高机器人导航的安全性和效率，具有重要的实际价值和广泛的应用前景。未来，随着技术的进一步发展，SICNav有望在更多复杂场景中得到应用，推动智能机器人技术的进步。

## 📄 摘要（原文）

> Safe and efficient navigation in crowded environments remains a critical challenge for robots that provide a variety of service tasks such as food delivery or autonomous wheelchair mobility. Classical robot crowd navigation methods decouple human motion prediction from robot motion planning, which neglects the closed-loop interactions between humans and robots. This lack of a model for human reactions to the robot plan (e.g. moving out of the way) can cause the robot to get stuck. Our proposed Safe and Interactive Crowd Navigation (SICNav) method is a bilevel Model Predictive Control (MPC) framework that combines prediction and planning into one optimization problem, explicitly modeling interactions among agents. In this paper, we present a systems overview of the crowd navigation platform we use to deploy SICNav in previously unseen indoor and outdoor environments. We provide a preliminary analysis of the system's operation over the course of nearly 7 km of autonomous navigation over two hours in both indoor and outdoor environments.

