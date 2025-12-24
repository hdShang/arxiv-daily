---
layout: default
title: "FreeTacMan: Robot-free Visuo-Tactile Data Collection System for Contact-rich Manipulation"
---

# FreeTacMan: Robot-free Visuo-Tactile Data Collection System for Contact-rich Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.01941" class="toolbar-btn" target="_blank">📄 arXiv: 2506.01941v2</a>
  <a href="https://arxiv.org/pdf/2506.01941.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.01941v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.01941v2', 'FreeTacMan: Robot-free Visuo-Tactile Data Collection System for Contact-rich Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Longyan Wu, Checheng Yu, Jieji Ren, Li Chen, Yufei Jiang, Ran Huang, Guoying Gu, Hongyang Li

**分类**: cs.RO

**发布日期**: 2025-06-02 (更新: 2025-10-09)

---

## 💡 一句话要点

**提出FreeTacMan以解决机器人接触丰富操作的数据收集问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `接触丰富操作` `数据收集` `可穿戴传感器` `视觉-触觉融合` `机器人学习` `人机交互` `多模态数据集`

## 📋 核心要点

1. 现有方法在接触丰富的操作中面临数据收集效率低和传感器设置有限的问题，影响了机器人的学习能力。
2. 本文提出FreeTacMan，一个无机器人干预的可穿戴数据收集系统，利用双重视觉-触觉传感器实现直观控制。
3. FreeTacMan收集了超过300万对视觉-触觉图像和10,000条示范轨迹，显著提升了数据收集性能，支持有效的策略学习。

## 📝 摘要（中文）

实现机器人接触丰富的操作仍然是机器人学习中的一个关键挑战，主要受限于数据收集的低效和传感器设置的局限性。以往的手持设备虽然有所探索，但其刚性结构限制了触觉反馈，给人类操作员带来了挑战。为此，本文提出了FreeTacMan，一个以人为中心且无机器人干预的数据收集系统，旨在实现准确高效的机器人操作。我们设计了一种可穿戴的夹持器，配备双重视觉-触觉传感器，能够被人类手指穿戴以实现直观控制。同时，引入高精度光学追踪系统以同步捕捉末端执行器姿态和视觉触觉反馈。FreeTacMan收集了一个大规模的多模态数据集，包含超过300万对视觉-触觉图像及10,000条示范轨迹，涵盖50种多样的接触丰富操作任务。与以往工作相比，FreeTacMan在数据收集性能上实现了多项提升，并支持基于自收集数据集的有效策略学习。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在接触丰富操作中的数据收集低效和传感器局限性的问题。现有的手持设备结构刚性，触觉反馈不足，给人类操作员带来不便。

**核心思路**：论文提出FreeTacMan，一个以人为中心的无机器人数据收集系统，设计可穿戴夹持器以实现直观的控制和高效的数据收集。

**技术框架**：FreeTacMan系统包括可穿戴夹持器、双重视觉-触觉传感器和高精度光学追踪系统。夹持器由人类手指穿戴，传感器用于收集数据，光学系统用于同步捕捉姿态和反馈。

**关键创新**：FreeTacMan的主要创新在于其人性化设计和无机器人干预的数据收集方式，显著提高了触觉反馈的质量和数据收集的效率。

**关键设计**：系统中使用的双重传感器设计确保了视觉和触觉数据的同步，光学追踪系统的高精度设置使得末端执行器的姿态捕捉更加准确。

## 📊 实验亮点

FreeTacMan在数据收集性能上实现了显著提升，收集了超过300万对视觉-触觉图像和10,000条示范轨迹，支持50种接触丰富操作任务，极大地丰富了现有的数据集，为后续的策略学习提供了坚实基础。

## 🎯 应用场景

FreeTacMan的研究成果在机器人操作、智能制造和人机交互等领域具有广泛的应用潜力。通过提供高质量的多模态数据集，该系统能够促进机器人在复杂环境中的学习与适应，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Enabling robots with contact-rich manipulation remains a pivotal challenge in robot learning, which is substantially hindered by the data collection gap, including its inefficiency and limited sensor setup. While prior work has explored handheld paradigms, their rod-based mechanical structures remain rigid and unintuitive, providing limited tactile feedback and posing challenges for human operators. Motivated by the dexterity and force feedback of human motion, we propose FreeTacMan, a human-centric and robot-free data collection system for accurate and efficient robot manipulation. Concretely, we design a wearable gripper with dual visuo-tactile sensors for data collection, which can be worn by human fingers for intuitive control. A high-precision optical tracking system is introduced to capture end-effector poses while synchronizing visual and tactile feedback simultaneously. We leverage FreeTacMan to collect a large-scale multimodal dataset, comprising over 3000k paired visual-tactile images with end-effector poses, 10k demonstration trajectories across 50 diverse contact-rich manipulation tasks. FreeTacMan achieves multiple improvements in data collection performance compared to prior works, and enables effective policy learning for contact-rich manipulation tasks with self-collected dataset. The full suite of hardware specifications and the dataset will be released to facilitate reproducibility and support research in visuo-tactile manipulation.

