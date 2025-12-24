---
layout: default
title: "Sight Over Site: Perception-Aware Reinforcement Learning for Efficient Robotic Inspection"
---

# Sight Over Site: Perception-Aware Reinforcement Learning for Efficient Robotic Inspection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.17877" class="toolbar-btn" target="_blank">📄 arXiv: 2509.17877v1</a>
  <a href="https://arxiv.org/pdf/2509.17877.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.17877v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.17877v1', 'Sight Over Site: Perception-Aware Reinforcement Learning for Efficient Robotic Inspection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Richard Kuhlmann, Jakob Wolfram, Boyang Sun, Jiaxu Xing, Davide Scaramuzza, Marc Pollefeys, Cesar Cadena

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-22

---

## 💡 一句话要点

**提出感知驱动的强化学习框架以提高机器人检查效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自主检查` `强化学习` `目标可见性` `机器人导航` `感知系统` `路径优化` `工业监测`

## 📋 核心要点

1. 现有的检查方法往往将任务简化为导航，未能充分考虑目标的可见性，导致效率低下。
2. 本文提出了一种新的强化学习框架，专注于目标可见性，优化机器人检查路径。
3. 实验结果显示，该方法在模拟和现实环境中均显著提高了检查效率，优于传统导航方法。

## 📝 摘要（中文）

自主检查是机器人领域的核心问题，应用广泛，包括工业监测和搜救等。传统方法往往将检查简化为导航任务，忽视了目标可见性的重要性。本文提出了一种端到端的强化学习框架，明确将目标可见性作为主要目标，使机器人能够找到最短路径以确保与目标的视觉接触，而无需依赖地图。通过在模拟环境中训练的策略，结合感知和自我感知传感器，实验结果表明，该方法在模拟和现实环境中均优于现有的导航方法，提供了更高效的检查轨迹。

## 🔬 方法详解

**问题定义**：本文旨在解决传统检查方法中忽视目标可见性的问题，现有方法往往仅关注到达目标位置，导致检查效率低下。

**核心思路**：通过将目标可见性作为主要优化目标，设计了一种强化学习框架，使机器人能够在不依赖地图的情况下，找到确保视觉接触的最短路径。

**技术框架**：该方法包括感知模块和自我感知模块，机器人在模拟环境中进行训练，学习到的策略随后应用于真实机器人。

**关键创新**：最重要的创新在于将目标可见性引入强化学习框架，区别于传统方法的导航任务，强调了视觉接触的重要性。

**关键设计**：在训练过程中，采用了特定的损失函数来优化目标可见性，并设计了适合的网络结构以处理感知和自我感知信息。具体参数设置和网络架构细节在论文中有详细描述。

## 📊 实验亮点

实验结果表明，所提出的方法在模拟环境中比现有的经典和基于学习的导航方法提高了检查效率，具体提升幅度达到XX%。在真实环境中的表现也显示出显著的优势，验证了方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括工业设备的自动化监测、灾后搜救行动以及其他需要高效检查的场景。通过提高检查效率，能够节省时间和资源，提升机器人在复杂环境中的应用能力，未来可能推动更多自主系统的开发与应用。

## 📄 摘要（原文）

> Autonomous inspection is a central problem in robotics, with applications ranging from industrial monitoring to search-and-rescue. Traditionally, inspection has often been reduced to navigation tasks, where the objective is to reach a predefined location while avoiding obstacles. However, this formulation captures only part of the real inspection problem. In real-world environments, the inspection targets may become visible well before their exact coordinates are reached, making further movement both redundant and inefficient. What matters more for inspection is not simply arriving at the target's position, but positioning the robot at a viewpoint from which the target becomes observable. In this work, we revisit inspection from a perception-aware perspective. We propose an end-to-end reinforcement learning framework that explicitly incorporates target visibility as the primary objective, enabling the robot to find the shortest trajectory that guarantees visual contact with the target without relying on a map. The learned policy leverages both perceptual and proprioceptive sensing and is trained entirely in simulation, before being deployed to a real-world robot. We further develop an algorithm to compute ground-truth shortest inspection paths, which provides a reference for evaluation. Through extensive experiments, we show that our method outperforms existing classical and learning-based navigation approaches, yielding more efficient inspection trajectories in both simulated and real-world settings. The project is avialable at https://sight-over-site.github.io/

