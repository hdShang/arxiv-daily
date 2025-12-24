---
layout: default
title: "CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives"
---

# CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14696" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14696v1</a>
  <a href="https://arxiv.org/pdf/2512.14696.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14696v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14696v1', 'CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Wang, Jiashun Wang, Jeff Tan, Yiwen Zhao, Jessica Hodgins, Shubham Tulsiani, Deva Ramanan

**分类**: cs.CV, cs.GR, cs.RO

**发布日期**: 2025-12-16

**备注**: Project page: https://crisp-real2sim.github.io/CRISP-Real2Sim/

---

## 💡 一句话要点

**CRISP：基于单目视频和平面场景原语的接触引导Real2Sim方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱四：生成式动作 (Generative Motion)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `Real2Sim` `单目视频重建` `人体-场景交互` `平面原语` `物理仿真` `强化学习` `接触建模`

## 📋 核心要点

1. 现有方法在人体-场景联合重建中，要么依赖数据先验和无物理优化，要么重建的几何体质量差，导致交互模拟失败。
2. CRISP通过平面原语拟合点云重建，并结合人体-场景接触建模来恢复干净、凸的、可用于仿真的场景几何。
3. 实验表明，CRISP显著降低了运动跟踪失败率，提高了强化学习模拟的吞吐量，并在真实视频中表现良好。

## 📝 摘要（中文）

CRISP是一种从单目视频中恢复可模拟的人体运动和场景几何的方法。现有的人体-场景联合重建工作依赖于数据驱动的先验和无物理引擎的联合优化，或者恢复的几何体存在噪声和伪影，导致基于场景交互的运动跟踪策略失败。CRISP的核心思想是通过拟合平面原语到场景的点云重建，来恢复凸的、干净的、可用于仿真的几何体，这通过一个简单的深度、法线和光流聚类流程实现。为了重建交互过程中可能被遮挡的场景几何，我们利用了人体-场景接触建模（例如，使用人体姿势来重建椅子被遮挡的座位）。最后，我们通过强化学习驱动人形控制器，确保人体和场景重建在物理上是合理的。在以人为中心的视频基准测试（EMDB、PROX）中，我们的方法将运动跟踪失败率从55.2％降低到6.9％，同时提供了快43％的RL模拟吞吐量。我们还在包括随意拍摄的视频、互联网视频甚至Sora生成的视频在内的真实视频中验证了它。这证明了CRISP大规模生成物理上有效的人体运动和交互环境的能力，极大地推进了机器人和AR/VR的real-to-sim应用。

## 🔬 方法详解

**问题定义**：现有方法在从单目视频重建可用于物理仿真的3D人体和场景时，存在以下痛点：一是依赖数据驱动的先验，泛化性不足；二是联合优化过程中缺乏物理约束，导致重建的几何体不真实，无法直接用于模拟；三是重建的场景几何体常常包含噪声和伪影，使得基于场景交互的运动跟踪策略容易失败。

**核心思路**：CRISP的核心思路是利用平面原语来表示场景几何，因为现实世界中很多场景都包含大量的平面结构。通过将点云重建结果拟合到平面原语，可以得到干净、凸的、易于仿真的场景几何。此外，CRISP还利用人体-场景接触信息来推断被遮挡的场景几何，并使用强化学习来保证重建结果的物理合理性。

**技术框架**：CRISP的整体流程包括以下几个主要阶段：1) 从单目视频中重建点云；2) 对点云进行聚类，提取平面原语；3) 利用人体-场景接触信息来推断被遮挡的场景几何；4) 使用重建的人体和场景来训练一个强化学习控制器，以保证重建结果的物理合理性。

**关键创新**：CRISP最重要的技术创新点在于将平面原语拟合与人体-场景接触建模相结合，从而能够从单目视频中重建出高质量的、可用于物理仿真的3D人体和场景。这种方法避免了对数据驱动先验的过度依赖，并且能够有效地处理遮挡问题。

**关键设计**：CRISP的关键设计包括：1) 使用深度、法线和光流信息进行点云聚类，以提取平面原语；2) 设计一个基于接触信息的场景几何推断模块，利用人体姿势来预测被遮挡的场景区域；3) 使用强化学习来优化人形控制器的参数，使得重建的人体和场景能够进行物理上合理的交互。

## 📊 实验亮点

CRISP在EMDB和PROX数据集上将运动跟踪失败率从55.2%降低到6.9%，显著提升了人体运动跟踪的鲁棒性。同时，CRISP还实现了43%的强化学习模拟吞吐量提升，表明其重建的场景几何更适合物理仿真。此外，CRISP在真实世界的视频（包括Sora生成的视频）上的成功应用，验证了其在复杂场景下的泛化能力。

## 🎯 应用场景

CRISP具有广泛的应用前景，包括机器人仿真、增强现实（AR）和虚拟现实（VR）。它可以用于创建逼真的虚拟环境，用于训练机器人或进行虚拟交互。此外，CRISP还可以用于将真实世界的人体运动和场景导入到虚拟环境中，从而实现更加沉浸式的AR/VR体验。该技术还有潜力应用于游戏开发、电影制作等领域。

## 📄 摘要（原文）

> We introduce CRISP, a method that recovers simulatable human motion and scene geometry from monocular video. Prior work on joint human-scene reconstruction relies on data-driven priors and joint optimization with no physics in the loop, or recovers noisy geometry with artifacts that cause motion tracking policies with scene interactions to fail. In contrast, our key insight is to recover convex, clean, and simulation-ready geometry by fitting planar primitives to a point cloud reconstruction of the scene, via a simple clustering pipeline over depth, normals, and flow. To reconstruct scene geometry that might be occluded during interactions, we make use of human-scene contact modeling (e.g., we use human posture to reconstruct the occluded seat of a chair). Finally, we ensure that human and scene reconstructions are physically-plausible by using them to drive a humanoid controller via reinforcement learning. Our approach reduces motion tracking failure rates from 55.2\% to 6.9\% on human-centric video benchmarks (EMDB, PROX), while delivering a 43\% faster RL simulation throughput. We further validate it on in-the-wild videos including casually-captured videos, Internet videos, and even Sora-generated videos. This demonstrates CRISP's ability to generate physically-valid human motion and interaction environments at scale, greatly advancing real-to-sim applications for robotics and AR/VR.

