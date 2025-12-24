---
layout: default
title: DORA: Object Affordance-Guided Reinforcement Learning for Dexterous Robotic Manipulation
---

# DORA: Object Affordance-Guided Reinforcement Learning for Dexterous Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14819" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14819v1</a>
  <a href="https://arxiv.org/pdf/2505.14819.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14819v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14819v1', 'DORA: Object Affordance-Guided Reinforcement Learning for Dexterous Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lei Zhang, Soumya Mondal, Zhenshan Bing, Kaixin Bai, Diwen Zheng, Zhaopeng Chen, Alois Christian Knoll, Jianwei Zhang

**分类**: cs.RO

**发布日期**: 2025-05-20

**备注**: 8 pages

---

## 💡 一句话要点

**提出基于物体可供性指导的强化学习框架以解决灵巧机器人操作问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `灵巧机器人` `物体可供性` `强化学习` `抓取策略` `多指机器人手`

## 📋 核心要点

1. 灵巧机器人操作面临控制空间高维性和物体交互复杂性的问题，现有方法难以有效应对。
2. 本文提出了一种基于物体可供性指导的强化学习框架，利用可供性图生成抓取姿态候选，提升学习效率。
3. 实验结果显示，所提方法在多项操作任务中成功率平均提高15.4%，验证了物体可供性先验的重要性。

## 📝 摘要（中文）

灵巧机器人操作因控制空间的高维性和物体交互的语义复杂性而面临长期挑战。本文提出了一种基于物体可供性指导的强化学习框架，使多指机器人手能够更高效地学习类人操作策略。通过利用物体可供性图，我们的方法生成语义上有意义的抓取姿态候选，作为训练过程中的策略约束和先验。此外，我们引入了一种基于投票的抓取分类机制，以确保抓取配置与物体可供性区域之间的功能对齐。实验结果表明，与基线相比，我们的方法在立方体抓取、壶抓取和提升、锤子使用等三项操作任务中平均提高了15.4%的成功率。这些发现突显了物体可供性先验在提高样本效率和学习可推广、语义基础的操作策略中的关键作用。

## 🔬 方法详解

**问题定义**：本文旨在解决灵巧机器人操作中的高维控制空间和物体交互的语义复杂性问题。现有方法在抓取策略学习上效率低下，难以实现类人操作。

**核心思路**：提出基于物体可供性指导的强化学习框架，通过物体可供性图生成语义抓取姿态候选，作为训练中的策略约束和先验，从而提高学习效率和成功率。

**技术框架**：整体架构包括物体可供性图生成、抓取姿态候选生成、投票分类机制和强化学习训练模块。每个模块相互配合，形成一个完整的学习流程。

**关键创新**：引入物体可供性先验作为抓取策略的约束，确保抓取配置与物体功能区域的对齐，这是与现有方法的本质区别。

**关键设计**：设计了基于投票的抓取分类机制，确保抓取姿态的功能性，同时构建了统一的奖励函数，将可供性意识与任务特定目标结合，提升了学习的样本效率。

## 📊 实验亮点

实验结果显示，所提的物体可供性指导方法在立方体抓取、壶抓取和锤子使用等任务中，成功率平均提高了15.4%。这一显著提升表明了物体可供性先验在强化学习中的重要作用。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和人机协作等场景。通过提升机器人在复杂环境中的操作能力，能够实现更高效的物体处理和交互，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Dexterous robotic manipulation remains a longstanding challenge in robotics due to the high dimensionality of control spaces and the semantic complexity of object interaction. In this paper, we propose an object affordance-guided reinforcement learning framework that enables a multi-fingered robotic hand to learn human-like manipulation strategies more efficiently. By leveraging object affordance maps, our approach generates semantically meaningful grasp pose candidates that serve as both policy constraints and priors during training. We introduce a voting-based grasp classification mechanism to ensure functional alignment between grasp configurations and object affordance regions. Furthermore, we incorporate these constraints into a generalizable RL pipeline and design a reward function that unifies affordance-awareness with task-specific objectives. Experimental results across three manipulation tasks - cube grasping, jug grasping and lifting, and hammer use - demonstrate that our affordance-guided approach improves task success rates by an average of 15.4% compared to baselines. These findings highlight the critical role of object affordance priors in enhancing sample efficiency and learning generalizable, semantically grounded manipulation policies. For more details, please visit our project website https://sites.google.com/view/dora-manip.

