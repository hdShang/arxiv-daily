---
layout: default
title: "BOW: Bayesian Optimization over Windows for Motion Planning in Complex Environments"
---

# BOW: Bayesian Optimization over Windows for Motion Planning in Complex Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13052" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13052v1</a>
  <a href="https://arxiv.org/pdf/2508.13052.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13052v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13052v1', 'BOW: Bayesian Optimization over Windows for Motion Planning in Complex Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sourav Raxit, Abdullah Al Redwan Newaz, Paulo Padrao, Jose Fuentes, Leonardo Bobadilla

**分类**: cs.RO

**发布日期**: 2025-08-18

---

## 💡 一句话要点

**提出BOW规划器以解决复杂环境中的运动规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `运动规划` `贝叶斯优化` `机器人导航` `复杂环境` `安全约束` `高效采样` `轨迹生成`

## 📋 核心要点

1. 现有运动规划方法在处理复杂环境中的动力学约束时，常常面临效率低下和安全性不足的问题。
2. BOW规划器通过集中于可达速度的规划窗口，利用约束贝叶斯优化高效采样控制输入，从而实现更优的运动规划。
3. 实验结果表明，BOW规划器在计算时间、轨迹长度和解决时间上均显著优于现有技术，展示了其实际应用价值。

## 📝 摘要（中文）

本文介绍了BOW规划器，这是一种可扩展的运动规划算法，旨在通过约束贝叶斯优化（CBO）帮助机器人在复杂环境中导航。与传统方法相比，BOW规划器能够更好地处理速度和加速度限制等动力学约束。该算法专注于可达速度的规划窗口，并高效地采样控制输入，从而在高维目标函数和严格安全约束下实现快速安全的轨迹生成。理论分析确认了该算法的渐近收敛性，并在拥挤和受限环境中进行了广泛评估，显示出在计算时间、轨迹长度和解决时间方面的显著改善。BOW规划器已成功应用于多种真实机器人系统，展现出其在样本效率、安全优化和快速规划能力方面的实际意义，并作为开源包发布。

## 🔬 方法详解

**问题定义**：本文旨在解决复杂环境中的运动规划问题，现有方法在处理速度和加速度等动力学约束时，往往效率低下且难以保证安全性。

**核心思路**：BOW规划器的核心思想是通过约束贝叶斯优化（CBO）集中于可达速度的规划窗口，从而高效地采样控制输入，确保快速且安全的轨迹生成。

**技术框架**：该方法的整体架构包括规划窗口的定义、CBO的实施以及轨迹生成的优化过程。主要模块包括状态空间的建模、目标函数的设计和控制输入的采样策略。

**关键创新**：BOW规划器的主要创新在于其使用CBO来处理高维目标函数和严格的安全约束，这与传统方法的采样策略有本质区别，显著提高了样本效率。

**关键设计**：在设计上，BOW规划器设置了特定的参数来定义规划窗口，并采用了适应性采样策略以优化控制输入的选择，确保在复杂环境中实现高效的轨迹生成。

## 📊 实验亮点

实验结果显示，BOW规划器在拥挤和受限环境中的计算时间比现有技术减少了显著比例，轨迹长度和解决时间也有显著改善。具体而言，BOW规划器在样本效率和安全优化方面的表现优于传统方法，展示了其在实际应用中的巨大潜力。

## 🎯 应用场景

BOW规划器具有广泛的应用潜力，特别是在自主机器人、无人驾驶汽车和工业自动化等领域。其高效的运动规划能力可以显著提升机器人在复杂环境中的导航和操作能力，推动相关技术的进步与应用。未来，该方法可能会在更复杂的动态环境中得到进一步应用，提升机器人系统的智能化水平。

## 📄 摘要（原文）

> This paper introduces the BOW Planner, a scalable motion planning algorithm designed to navigate robots through complex environments using constrained Bayesian optimization (CBO). Unlike traditional methods, which often struggle with kinodynamic constraints such as velocity and acceleration limits, the BOW Planner excels by concentrating on a planning window of reachable velocities and employing CBO to sample control inputs efficiently. This approach enables the planner to manage high-dimensional objective functions and stringent safety constraints with minimal sampling, ensuring rapid and secure trajectory generation. Theoretical analysis confirms the algorithm's asymptotic convergence to near-optimal solutions, while extensive evaluations in cluttered and constrained settings reveal substantial improvements in computation times, trajectory lengths, and solution times compared to existing techniques. Successfully deployed across various real-world robotic systems, the BOW Planner demonstrates its practical significance through exceptional sample efficiency, safety-aware optimization, and rapid planning capabilities, making it a valuable tool for advancing robotic applications. The BOW Planner is released as an open-source package and videos of real-world and simulated experiments are available at https://bow-web.github.io.

