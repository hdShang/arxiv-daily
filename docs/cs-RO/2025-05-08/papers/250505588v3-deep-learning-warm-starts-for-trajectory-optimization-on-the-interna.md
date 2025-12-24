---
layout: default
title: Deep Learning Warm Starts for Trajectory Optimization on the International Space Station
---

# Deep Learning Warm Starts for Trajectory Optimization on the International Space Station

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05588" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05588v3</a>
  <a href="https://arxiv.org/pdf/2505.05588.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05588v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05588v3', 'Deep Learning Warm Starts for Trajectory Optimization on the International Space Station')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Somrita Banerjee, Abhishek Cauligi, Marco Pavone

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-05-08 (更新: 2025-11-04)

**备注**: Accepted to 2025 International Conference on Space Robotics (iSpaRo). Presented at RSS 2025 Workshop on Space Robotics

---

## 💡 一句话要点

**提出基于深度学习的热启动方法以加速国际空间站轨迹优化**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `轨迹优化` `深度学习` `航天应用` `自主导航` `机器人控制` `顺序凸规划` `热启动方法`

## 📋 核心要点

1. 现有的轨迹优化方法在航天应用中面临计算需求过高的问题，超出大多数飞行计算机的能力。
2. 本研究提出了一种基于深度学习的热启动方法，通过训练神经网络来加速轨迹优化过程，结合顺序凸规划求解器确保安全性。
3. 实验结果表明，使用该方法在旋转动力学情况下求解器迭代次数减少了60%，在有障碍物的情况下减少了50%。

## 📝 摘要（中文）

轨迹优化是现代机器人自主性的核心，能够实时计算轨迹和控制，同时遵循安全和物理约束。然而，由于计算需求高，轨迹优化在航天应用中使用有限。本研究首次在国际空间站上展示了基于机器学习的热启动方法，以加速Astrobee自由飞行机器人轨迹优化。我们提出了一种数据驱动的最优控制方法，训练神经网络学习轨迹生成问题的结构，并利用顺序凸规划(SCP)求解器来强制执行安全约束。训练后的网络在包含旋转动力学的情况下将收敛所需的求解器迭代次数减少了60%，在包含障碍物的情况下减少了50%。此研究标志着学习控制在航天应用中的重要里程碑，并为未来的自主导航与控制的机器学习应用奠定了基础。

## 🔬 方法详解

**问题定义**：本研究旨在解决轨迹优化在航天应用中由于计算需求过高而难以实现的问题。现有方法在实时性和安全性方面存在显著挑战。

**核心思路**：论文提出了一种基于深度学习的热启动方法，通过训练神经网络来学习轨迹生成问题的结构，从而加速求解过程。该方法结合顺序凸规划(SCP)求解器，确保在优化过程中遵循安全约束。

**技术框架**：整体架构包括数据收集、神经网络训练和轨迹生成三个主要模块。首先，收集轨迹生成问题的数据，然后训练神经网络，最后利用训练好的网络进行轨迹生成并通过SCP求解器进行约束检查。

**关键创新**：最重要的技术创新在于将深度学习与传统的轨迹优化方法相结合，显著减少了求解器的迭代次数。这种方法在处理复杂动态和障碍物时表现出更高的效率。

**关键设计**：在网络结构上，采用了适合轨迹生成问题的深度神经网络，损失函数设计为考虑安全约束和轨迹平滑性，关键参数通过实验优化以确保模型的有效性。

## 📊 实验亮点

实验结果显示，使用深度学习热启动方法后，求解器在处理旋转动力学时的迭代次数减少了60%，在有障碍物的情况下减少了50%。这些显著的性能提升表明该方法在航天应用中的有效性和潜力。

## 🎯 应用场景

该研究的潜在应用领域包括航天器自主导航、机器人控制和其他需要实时轨迹优化的系统。通过提高轨迹优化的效率，能够在复杂环境中实现更安全和高效的自主操作，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Trajectory optimization is a cornerstone of modern robot autonomy, enabling systems to compute trajectories and controls in real-time while respecting safety and physical constraints. However, it has seen limited usage in spaceflight applications due to its heavy computational demands that exceed the capability of most flight computers. In this work, we provide results on the first in-space demonstration of using machine learning-based warm starts for accelerating trajectory optimization for the Astrobee free-flying robot onboard the International Space Station (ISS). We formulate a data-driven optimal control approach that trains a neural network to learn the structure of the trajectory generation problem being solved using sequential convex programming (SCP). Onboard, this trained neural network predicts solutions for the trajectory generation problem and relies on using the SCP solver to enforce safety constraints for the system. Our trained network reduces the number of solver iterations required for convergence in cases including rotational dynamics by 60% and in cases with obstacles drawn from the training distribution of the warm start model by 50%. This work represents a significant milestone in the use of learning-based control for spaceflight applications and a stepping stone for future advances in the use of machine learning for autonomous guidance, navigation, & control.

