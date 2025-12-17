---
layout: default
title: CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives
---

# CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14696" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14696v1</a>
  <a href="https://arxiv.org/pdf/2512.14696.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14696v1" onclick="toggleFavorite(this, '2512.14696v1', 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Wang, Jiashun Wang, Jeff Tan, Yiwen Zhao, Jessica Hodgins, Shubham Tulsiani, Deva Ramanan

**分类**: cs.CV, cs.GR, cs.RO

**发布日期**: 2025-12-16

**备注**: Project page: https://crisp-real2sim.github.io/CRISP-Real2Sim/

---

## 💡 一句话要点

**CRISP：基于单目视频和平面场景原语的接触引导Real2Sim方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `Real2Sim` `单目视频重建` `人体场景交互` `平面原语` `强化学习` `物理仿真` `接触建模`

## 📋 核心要点

1. 现有方法在人体-场景联合重建中，要么依赖数据先验和无物理的优化，要么重建的几何体质量差，导致交互式运动跟踪失败。
2. CRISP通过平面原语拟合点云重建，恢复凸的、干净的几何体，并利用人体-场景接触建模来重建遮挡区域，确保重建结果可用于物理仿真。
3. 实验表明，CRISP显著降低了运动跟踪失败率，提高了强化学习模拟的吞吐量，并在真实视频和生成视频中验证了其有效性。

## 📝 摘要（中文）

CRISP是一种从单目视频中恢复可模拟的人体运动和场景几何结构的方法。现有的人体-场景联合重建工作依赖于数据驱动的先验和无物理引擎参与的联合优化，或者恢复的几何结构噪声大，导致带有场景交互的运动跟踪策略失败。CRISP的关键在于通过拟合平面原语到场景的点云重建，来恢复凸的、干净的、可用于仿真的几何结构，这通过一个简单的深度、法线和光流聚类流程实现。为了重建交互过程中可能被遮挡的场景几何结构，CRISP利用了人体-场景接触建模（例如，使用人体姿势来重建椅子被遮挡的座位）。最后，通过强化学习驱动人形控制器，确保人体和场景重建在物理上是合理的。在以人为中心的视频基准测试（EMDB、PROX）中，CRISP将运动跟踪失败率从55.2%降低到6.9%，同时实现了43%更快的RL模拟吞吐量。该方法还在包括随意拍摄的视频、互联网视频甚至Sora生成的视频在内的真实视频中得到了验证。这证明了CRISP大规模生成物理上有效的人体运动和交互环境的能力，极大地推进了机器人和AR/VR的real-to-sim应用。

## 🔬 方法详解

**问题定义**：论文旨在解决从单目视频中重建可用于物理仿真的、高质量的人体运动和场景几何结构的问题。现有方法要么依赖大量数据先验，要么重建的几何结构存在噪声和伪影，无法直接用于物理仿真，导致运动跟踪策略在交互场景中表现不佳。

**核心思路**：论文的核心思路是通过拟合平面原语来重建场景几何结构，从而获得凸的、干净的、易于仿真的几何体。同时，利用人体与场景的接触信息来推断被遮挡的场景部分，并使用强化学习来驱动人形控制器，确保重建结果在物理上是合理的。

**技术框架**：CRISP的整体流程包括以下几个阶段：1) 从单目视频中重建点云；2) 对点云进行聚类，拟合平面原语；3) 利用人体姿势和接触信息推断被遮挡的场景几何；4) 使用重建的人体和场景驱动人形控制器，并通过强化学习优化控制策略。

**关键创新**：CRISP的关键创新在于：1) 使用平面原语来表示场景几何，简化了场景的表示，使其更易于仿真；2) 利用人体-场景接触信息来推断被遮挡的场景部分，提高了场景重建的完整性；3) 使用强化学习来确保重建结果在物理上是合理的，提高了仿真的真实性。

**关键设计**：论文使用深度、法线和光流信息进行点云聚类，并采用RANSAC算法拟合平面原语。人体-场景接触建模基于预训练的人体姿态估计器和场景几何，通过优化能量函数来推断接触区域。强化学习部分使用PPO算法训练人形控制器，奖励函数包括模仿真实运动、保持平衡和避免碰撞等。

## 📊 实验亮点

CRISP在EMDB和PROX数据集上将运动跟踪失败率从55.2%降低到6.9%，显著提升了性能。同时，CRISP实现了43%更快的强化学习模拟吞吐量，提高了仿真效率。此外，该方法还在真实视频和Sora生成的视频中进行了验证，证明了其在不同场景下的泛化能力。

## 🎯 应用场景

CRISP具有广泛的应用前景，包括机器人仿真、增强现实/虚拟现实（AR/VR）内容生成、以及人机交互研究。该方法可以用于创建逼真的虚拟环境，用于训练机器人或进行虚拟实验，也可以用于增强AR/VR体验，例如将虚拟物体与真实场景进行交互。此外，CRISP还可以用于分析人类行为，例如研究人类在不同环境下的运动模式。

## 📄 摘要（原文）

> We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human-scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion tracking policies with scene interactions to fail. In contrast, our key insight is to recover convex, clean, and simulation-ready geometry by fitting planar primitives to a point cloud reconstruction of the scene, via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we make use of human-scene contact modeling (e.g., we use human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically-plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering a 43\% faster RL simulation throughput. We further validate it on in-the-wild videos including casually-captured videos, Internet videos, and even Sora-generated videos. This demonstrates CRISP's ability to generate physically-valid human motion and interaction environments at scale, greatly advancing real-to-sim applications for robotics and AR/VR.

