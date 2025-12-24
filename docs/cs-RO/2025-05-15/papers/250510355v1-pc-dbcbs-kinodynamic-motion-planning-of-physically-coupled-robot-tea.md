---
layout: default
title: pc-dbCBS: Kinodynamic Motion Planning of Physically-Coupled Robot Teams
---

# pc-dbCBS: Kinodynamic Motion Planning of Physically-Coupled Robot Teams

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.10355" class="toolbar-btn" target="_blank">📄 arXiv: 2505.10355v1</a>
  <a href="https://arxiv.org/pdf/2505.10355.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.10355v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.10355v1', 'pc-dbCBS: Kinodynamic Motion Planning of Physically-Coupled Robot Teams')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Khaled Wahba, Wolfgang Hönig

**分类**: cs.RO, cs.MA, eess.SY

**发布日期**: 2025-05-15

**备注**: This work has been submitted to the IEEE for possible publication

---

## 💡 一句话要点

**提出pc-dbCBS以解决物理耦合机器人团队的运动规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `运动规划` `多机器人系统` `物理耦合` `冲突检测` `轨迹优化` `动力学规划` `复杂环境`

## 📋 核心要点

1. 现有的运动规划方法在处理物理耦合的多机器人系统时，往往面临高维度和次优解的问题，缺乏理论保证。
2. 本文提出的pc-dbCBS方法通过引入三层次冲突检测与解决框架，有效考虑了机器人之间的物理耦合，提升了运动规划的效率。
3. 实验结果表明，pc-dbCBS在解决实例数量和规划速度上均显著优于现有最先进方法，展示了其在复杂环境中的应用潜力。

## 📝 摘要（中文）

物理耦合的多机器人系统在复杂环境中的运动规划问题因其高维度而极具挑战性。现有结合采样规划与轨迹优化的方法往往产生次优结果且缺乏理论保证。本文提出了一种物理耦合的离散性界限冲突基搜索（pc-dbCBS），作为一种随时可用的动力学运动规划器，扩展了离散性界限CBS到刚性耦合系统。该方法提出了一个三层次的冲突检测与解决框架，考虑了机器人之间的物理耦合。此外，pc-dbCBS在状态空间表示之间进行迭代切换，从而在仅依赖单机器人运动原语的情况下，保持了概率完整性和渐近最优性。在25个模拟和6个真实世界的多旋翼载重和通过刚性杆连接的差分驱动机器人问题中，pc-dbCBS解决的实例比最先进的基线多出92%，并且规划轨迹速度提高了50-60%，规划时间减少了一个数量级。

## 🔬 方法详解

**问题定义**：本文旨在解决物理耦合多机器人系统在复杂环境中的运动规划问题。现有方法在处理高维度问题时，往往产生次优解且缺乏理论保证，限制了其应用。

**核心思路**：pc-dbCBS方法通过扩展离散性界限CBS，采用三层次冲突检测与解决框架，充分考虑机器人之间的物理耦合关系，从而提高运动规划的效率和可靠性。

**技术框架**：该方法的整体架构包括冲突检测、冲突解决和状态空间表示切换三个主要模块。通过迭代切换状态空间，pc-dbCBS能够在保持概率完整性和渐近最优性的同时，依赖单机器人运动原语进行规划。

**关键创新**：pc-dbCBS的主要创新在于其三层次的冲突检测与解决机制，能够有效处理物理耦合带来的复杂性，与现有方法相比，显著提升了规划效率和成功率。

**关键设计**：在设计中，pc-dbCBS依赖于单机器人运动原语，采用迭代切换的方式来优化状态空间表示，确保在高维度问题中仍能保持良好的性能。

## 📊 实验亮点

实验结果显示，pc-dbCBS在解决实例数量上比最先进的基线方法多出92%，规划速度提升50-60%，同时规划时间减少了一个数量级，展现了其优越的性能和效率。

## 🎯 应用场景

该研究的潜在应用领域包括多机器人协作任务、无人机编队、自动化物流等场景，能够显著提升机器人在复杂环境中的运动规划能力，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Motion planning problems for physically-coupled multi-robot systems in cluttered environments are challenging due to their high dimensionality. Existing methods combining sampling-based planners with trajectory optimization produce suboptimal results and lack theoretical guarantees. We propose Physically-coupled discontinuity-bounded Conflict-Based Search (pc-dbCBS), an anytime kinodynamic motion planner, that extends discontinuity-bounded CBS to rigidly-coupled systems. Our approach proposes a tri-level conflict detection and resolution framework that includes the physical coupling between the robots. Moreover, pc-dbCBS alternates iteratively between state space representations, thereby preserving probabilistic completeness and asymptotic optimality while relying only on single-robot motion primitives. Across 25 simulated and six real-world problems involving multirotors carrying a cable-suspended payload and differential-drive robots linked by rigid rods, pc-dbCBS solves up to 92% more instances than a state-of-the-art baseline and plans trajectories that are 50-60% faster while reducing planning time by an order of magnitude.

