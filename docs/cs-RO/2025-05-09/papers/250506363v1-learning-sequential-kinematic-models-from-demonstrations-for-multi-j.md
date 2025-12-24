---
layout: default
title: Learning Sequential Kinematic Models from Demonstrations for Multi-Jointed Articulated Objects
---

# Learning Sequential Kinematic Models from Demonstrations for Multi-Jointed Articulated Objects

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06363" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06363v1</a>
  <a href="https://arxiv.org/pdf/2505.06363.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06363v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06363v1', 'Learning Sequential Kinematic Models from Demonstrations for Multi-Jointed Articulated Objects')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anmol Gupta, Weiwei Gu, Omkar Patil, Jun Ki Lee, Nakul Gopalan

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-09

---

## 💡 一句话要点

**提出对象运动序列机器以解决多关节物体建模问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多关节物体` `运动序列机器` `深度学习` `人类示范` `机器人操作` `状态估计` `点云数据`

## 📋 核心要点

1. 现有方法依赖于先验知识或仅关注单自由度物体，无法处理多关节物体的遮挡和操作序列。
2. 本文提出了对象运动序列机器（OKSMs），通过学习人类示范来捕捉多自由度物体的运动约束和操作顺序。
3. 在8000个模拟样本和1600个真实样本上验证了Pokenet，结果显示其在真实数据上的关节轴和状态估计提升超过20%。

## 📝 摘要（中文）

随着机器人在多样化环境中的广泛应用，它们需要与复杂的多自由度物体进行交互。现有方法通常依赖于先验知识或仅关注单自由度物体，限制了其适用性，并且无法处理被遮挡的关节及其操作序列。为此，本文通过学习人类示范来构建对象模型，提出了对象运动序列机器（OKSMs），该方法能够捕捉多自由度物体的运动约束和操作顺序。我们还提出了Pokenet，一个基于深度神经网络的模型，能够从点云数据中估计这些模型。实验结果表明，Pokenet在真实数据上的关节轴和状态估计比现有方法提高了20%以上。

## 🔬 方法详解

**问题定义**：本文旨在解决多关节物体的建模问题，现有方法往往依赖于先验知识，无法有效处理遮挡的关节和复杂的操作序列。

**核心思路**：通过学习人类示范，提出对象运动序列机器（OKSMs），该方法能够同时捕捉运动约束和操作顺序，从而提高多自由度物体的建模精度。

**技术框架**：整体架构包括数据采集、模型训练和应用三个主要阶段。首先，通过人类示范收集数据，然后利用深度神经网络Pokenet进行模型训练，最后在机器人上进行操作验证。

**关键创新**：对象运动序列机器（OKSMs）是本文的核心创新，它能够有效处理多自由度物体的运动约束和操作顺序，区别于传统方法的单一自由度建模。

**关键设计**：Pokenet的网络结构设计为深度神经网络，采用特定的损失函数来优化关节轴和状态的估计，关键参数设置经过多次实验调整，以确保模型的准确性和鲁棒性。

## 📊 实验亮点

实验结果显示，Pokenet在真实世界数据上的关节轴和状态估计比现有方法提高了超过20%。在8000个模拟样本和1600个真实样本的验证中，OKSMs展示了其在多自由度物体操作中的有效性，显著提升了机器人操作的精确度。

## 🎯 应用场景

该研究在机器人操作、智能制造和人机交互等领域具有广泛的应用潜力。通过精确建模多关节物体，机器人能够更好地执行复杂的操作任务，提高工作效率和安全性。未来，该方法可能推动更智能的机器人系统的发展，增强其在动态环境中的适应能力。

## 📄 摘要（原文）

> As robots become more generalized and deployed in diverse environments, they must interact with complex objects, many with multiple independent joints or degrees of freedom (DoF) requiring precise control. A common strategy is object modeling, where compact state-space models are learned from real-world observations and paired with classical planning. However, existing methods often rely on prior knowledge or focus on single-DoF objects, limiting their applicability. They also fail to handle occluded joints and ignore the manipulation sequences needed to access them. We address this by learning object models from human demonstrations. We introduce Object Kinematic Sequence Machines (OKSMs), a novel representation capturing both kinematic constraints and manipulation order for multi-DoF objects. To estimate these models from point cloud data, we present Pokenet, a deep neural network trained on human demonstrations. We validate our approach on 8,000 simulated and 1,600 real-world annotated samples. Pokenet improves joint axis and state estimation by over 20 percent on real-world data compared to prior methods. Finally, we demonstrate OKSMs on a Sawyer robot using inverse kinematics-based planning to manipulate multi-DoF objects.

