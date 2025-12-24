---
layout: default
title: Contact-Aware Safety in Soft Robots Using High-Order Control Barrier and Lyapunov Functions
---

# Contact-Aware Safety in Soft Robots Using High-Order Control Barrier and Lyapunov Functions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03841" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03841v3</a>
  <a href="https://arxiv.org/pdf/2505.03841.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03841v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03841v3', 'Contact-Aware Safety in Soft Robots Using High-Order Control Barrier and Lyapunov Functions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kiwan Wong, Maximilian Stölzle, Wei Xiao, Cosimo Della Santina, Daniela Rus, Gioele Zardini

**分类**: cs.RO, eess.SY

**发布日期**: 2025-05-05 (更新: 2025-10-17)

**备注**: 8 pages

**期刊**: K. Wong, M. Stölzle, W. Xiao, C. D. Santina, D. Rus and G. Zardini, "Contact-Aware Safety in Soft Robots Using High-Order Control Barrier and Lyapunov Functions," in IEEE Robotics and Automation Letters

**DOI**: [10.1109/LRA.2025.3621965](https://doi.org/10.1109/LRA.2025.3621965)

---

## 💡 一句话要点

**提出高阶控制障碍与李雅普诺夫函数以解决软机器人安全问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `软机器人` `安全性` `控制障碍函数` `李雅普诺夫函数` `人机交互` `碰撞检测` `高阶控制`

## 📋 核心要点

1. 现有软机器人在与人类交互时，安全性不足，尤其在高精度和高负载的应用中，受伤风险增加。
2. 提出高阶控制障碍函数与李雅普诺夫函数的框架，确保在环境交互中严格限制接触力，提升安全性。
3. 通过广泛的平面仿真实验，验证了方法在保持安全接触的同时，实现了精确的形状和任务空间调节。

## 📝 摘要（中文）

在与人类共同工作的场景中，尤其是帮助老年人或在制造业中协作时，机器人必须确保安全并建立用户信任。尽管连续软操纵器因材料的柔性而具有安全性，但随着设计向更高的精度、负载能力和速度演进，刚性元素的引入使得受伤风险重新浮现。本文提出了一种综合的高阶控制障碍函数（HOCBF）与高阶控制李雅普诺夫函数（HOCLF）框架，在环境交互中强制执行整个软机器人身体的接触力限制。通过结合可微分的分段科塞拉特动力学模型与基于软机器人几何形状的凸多边形距离近似度量，本文实现了实时的全身碰撞检测、解决和安全约束的执行。

## 🔬 方法详解

**问题定义**：本研究旨在解决软机器人在与人类交互时的安全性问题，现有方法在高精度和高负载应用中面临受伤风险。

**核心思路**：提出高阶控制障碍函数（HOCBF）与高阶控制李雅普诺夫函数（HOCLF）相结合的框架，通过限制接触力来确保安全性。

**技术框架**：整体架构包括可微分的分段科塞拉特动力学模型和基于凸多边形的距离近似度量，形成实时碰撞检测和安全约束执行的模块。

**关键创新**：最重要的创新在于将HOCBF嵌入优化过程中，确保在HOCLF驱动的运动目标下实现安全导航，与现有方法相比，提供了可证明的安全性和性能。

**关键设计**：采用了可微分的分段科塞拉特动力学模型，结合凸多边形距离近似度量（DCSAT），实现了高效的碰撞检测和安全约束执行。

## 📊 实验亮点

实验结果表明，所提方法在保持安全接触的同时，能够实现精确的形状和任务空间调节。具体而言，方法在多个仿真场景中表现出优越的安全性，成功避免了潜在的碰撞风险，提升了操作的安全性和效率。

## 🎯 应用场景

该研究的潜在应用领域包括老年人辅助、医疗机器人、制造业协作机器人等人机交互场景。通过确保安全性，该框架能够增强用户信任，促进软机器人在复杂环境中的广泛应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Robots operating alongside people, particularly in sensitive scenarios such as aiding the elderly with daily tasks or collaborating with workers in manufacturing, must guarantee safety and cultivate user trust. Continuum soft manipulators promise safety through material compliance, but as designs evolve for greater precision, payload capacity, and speed, and increasingly incorporate rigid elements, their injury risk resurfaces. In this letter, we introduce a comprehensive High-Order Control Barrier Function (HOCBF) + High-Order Control Lyapunov Function (HOCLF) framework that enforces strict contact force limits across the entire soft-robot body during environmental interactions. Our approach combines a differentiable Piecewise Cosserat-Segment (PCS) dynamics model with a convex-polygon distance approximation metric, named Differentiable Conservative Separating Axis Theorem (DCSAT), based on the soft robot geometry to enable real-time, whole-body collision detection, resolution, and enforcement of the safety constraints. By embedding HOCBFs into our optimization routine, we guarantee safety, allowing, for instance, safe navigation in operational space under HOCLF-driven motion objectives. Extensive planar simulations demonstrate that our method maintains safety-bounded contacts while achieving precise shape and task-space regulation. This work thus lays a foundation for the deployment of soft robots in human-centric environments with provable safety and performance.

