---
layout: default
title: "MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation"
---

# MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01658" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01658v1</a>
  <a href="https://arxiv.org/pdf/2509.01658.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01658v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01658v1', 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenyu Wu, Angyuan Ma, Xiuwei Xu, Hang Yin, Yinan Liang, Ziwei Wang, Jiwen Lu, Haibin Yan

**分类**: cs.RO

**发布日期**: 2025-09-01

**备注**: Accepted to CoRL 2025. Project Page: https://gary3410.github.io/MoTo/

---

## 💡 一句话要点

**MoTo：一种零样本即插即用的交互感知导航方法，用于通用移动操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `移动操作` `零样本学习` `视觉-语言模型` `机器人导航` `运动规划`

## 📋 核心要点

1. 传统移动操作方法泛化性差，缺乏大规模训练，难以适应不同任务和环境。
2. MoTo通过交互感知导航策略和视觉-语言模型，实现零样本移动操作，无需专家数据。
3. 实验表明，MoTo在OVMM和真实世界中，成功率显著高于现有方法，无需额外训练。

## 📝 摘要（中文）

移动操作是机器人领域的核心挑战，它使机器人能够在各种任务和动态日常环境中协助人类。传统的移动操作方法由于缺乏大规模训练，难以在不同任务和环境中泛化。然而，最近操作基础模型的进展展示了在各种固定基座操作任务上的出色泛化能力，但仍局限于固定设置。因此，我们设计了一个名为MoTo的即插即用模块，它可以与任何现成的操作基础模型相结合，以赋予它们移动操作能力。具体来说，我们提出了一种交互感知导航策略，用于为通用移动操作生成机器人停靠点。为了实现零样本能力，我们提出了一个交互关键点框架，通过视觉-语言模型（VLM）在多视角一致性下，同时跟踪目标对象和机械臂的指令，从而可以使用固定基座操作基础模型。我们进一步提出了移动底座和机械臂的运动规划目标，以最小化两个关键点之间的距离，并保持轨迹的物理可行性。通过这种方式，MoTo引导机器人移动到可以成功执行固定基座操作的停靠点，并利用VLM生成和轨迹优化来实现零样本的移动操作，而无需任何移动操作专家数据。在OVMM和真实世界的广泛实验结果表明，MoTo的成功率分别比最先进的移动操作方法高2.68%和16.67%，而无需额外的训练数据。

## 🔬 方法详解

**问题定义**：论文旨在解决移动操作任务中，机器人如何在未知环境中，利用预训练的操作基础模型，实现零样本的通用操作。现有方法通常需要大量特定任务的训练数据，泛化能力差，难以适应复杂多变的环境。

**核心思路**：核心思路是将移动操作分解为导航到合适的交互位置和执行固定基座操作两个阶段。通过交互感知导航策略，机器人能够自主选择停靠点，使得后续的固定基座操作更容易成功。利用视觉-语言模型提取交互关键点，指导机器人运动，实现零样本操作。

**技术框架**：MoTo包含以下主要模块：1) 交互感知导航策略：根据环境信息和任务指令，生成机器人停靠点。2) 交互关键点框架：利用视觉-语言模型，提取目标对象和机械臂的关键点，用于指导运动规划。3) 运动规划：优化移动底座和机械臂的轨迹，最小化关键点距离，并保证轨迹的物理可行性。

**关键创新**：最重要的创新点在于提出了一个零样本的移动操作框架，无需任何移动操作的专家数据。通过将移动操作分解为导航和固定基座操作两个阶段，并利用视觉-语言模型提取交互关键点，实现了在未知环境中的通用操作能力。

**关键设计**：交互感知导航策略可能使用了强化学习或模仿学习，具体实现细节未知。交互关键点框架利用视觉-语言模型提取关键点，并采用多视角一致性约束，提高关键点的准确性。运动规划目标函数包含关键点距离最小化和轨迹平滑性约束，具体权重设置未知。

## 📊 实验亮点

实验结果表明，MoTo在OVMM和真实世界中，分别比最先进的移动操作方法提高了2.68%和16.67%的成功率。这些提升是在没有额外训练数据的情况下实现的，验证了MoTo的零样本泛化能力和实际应用价值。

## 🎯 应用场景

该研究成果可应用于各种需要移动操作的场景，例如家庭服务机器人、仓库自动化、医疗辅助机器人等。它可以使机器人在复杂环境中自主完成各种任务，例如物品拾取、放置、组装等，提高工作效率和安全性，并降低对人工干预的依赖。

## 📄 摘要（原文）

> Mobile manipulation stands as a core challenge in robotics, enabling robots to assist humans across varied tasks and dynamic daily environments. Conventional mobile manipulation approaches often struggle to generalize across different tasks and environments due to the lack of large-scale training. However, recent advances in manipulation foundation models demonstrate impressive generalization capability on a wide range of fixed-base manipulation tasks, which are still limited to a fixed setting. Therefore, we devise a plug-in module named MoTo, which can be combined with any off-the-shelf manipulation foundation model to empower them with mobile manipulation ability. Specifically, we propose an interaction-aware navigation policy to generate robot docking points for generalized mobile manipulation. To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base manipulation foundation models can be employed. We further propose motion planning objectives for the mobile base and robot arm, which minimize the distance between the two keypoints and maintain the physical feasibility of trajectories. In this way, MoTo guides the robot to move to the docking points where fixed-base manipulation can be successfully performed, and leverages VLM generation and trajectory optimization to achieve mobile manipulation in a zero-shot manner, without any requirement on mobile manipulation expert data. Extensive experimental results on OVMM and real-world demonstrate that MoTo achieves success rates of 2.68% and 16.67% higher than the state-of-the-art mobile manipulation methods, respectively, without requiring additional training data.

