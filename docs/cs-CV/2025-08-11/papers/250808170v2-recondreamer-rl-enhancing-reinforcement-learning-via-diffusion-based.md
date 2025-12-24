---
layout: default
title: "ReconDreamer-RL: Enhancing Reinforcement Learning via Diffusion-based Scene Reconstruction"
---

# ReconDreamer-RL: Enhancing Reinforcement Learning via Diffusion-based Scene Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08170" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08170v2</a>
  <a href="https://arxiv.org/pdf/2508.08170.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08170v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08170v2', 'ReconDreamer-RL: Enhancing Reinforcement Learning via Diffusion-based Scene Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaojun Ni, Guosheng Zhao, Xiaofeng Wang, Zheng Zhu, Wenkang Qin, Xinze Chen, Guanghong Jia, Guan Huang, Wenjun Mei

**分类**: cs.CV

**发布日期**: 2025-08-11 (更新: 2025-08-21)

---

## 💡 一句话要点

**提出ReconDreamer-RL以解决仿真与现实之间的差距问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `强化学习` `自动驾驶` `场景重建` `视频扩散` `仿真技术` `数据分布` `复杂场景生成`

## 📋 核心要点

1. 现有的自动驾驶仿真方法在真实世界条件下表现不佳，导致仿真与现实之间存在显著差距。
2. 本文提出ReconDreamer-RL框架，结合视频扩散先验和运动学模型，重建真实驾驶场景以改善强化学习效果。
3. 实验结果显示，ReconDreamer-RL在自动驾驶训练中优于模仿学习方法，碰撞率降低了5倍，显著提升了训练效果。

## 📝 摘要（中文）

随着强化学习在闭环仿真中训练端到端自动驾驶模型的关注度日益增加，现有的仿真环境与真实世界条件之间存在显著差距，形成了较大的仿真到现实（sim2real）差距。为了解决这一问题，本文提出了ReconDreamer-RL框架，通过将视频扩散先验融入场景重建，增强强化学习的效果。该框架引入了ReconSimulator，结合视频扩散先验进行外观建模，并结合运动学模型进行物理建模，从真实数据中重建驾驶场景。此外，动态对抗代理（DAA）能够自主生成复杂交通场景，最后，表亲轨迹生成器（CTG）解决了训练数据分布偏向简单直线运动的问题。实验结果表明，ReconDreamer-RL在端到端自动驾驶训练中表现优异，碰撞率降低了5倍。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自动驾驶仿真方法在真实世界条件下的不足，尤其是仿真与现实之间的差距，导致难以生成高质量的传感器数据。

**核心思路**：通过引入视频扩散先验进行场景重建，结合运动学模型以实现更真实的物理模拟，从而缩小仿真与现实之间的差距。

**技术框架**：ReconDreamer-RL框架包括ReconSimulator、动态对抗代理（DAA）和表亲轨迹生成器（CTG）。ReconSimulator负责场景重建，DAA生成复杂交通场景，CTG则调整训练数据分布。

**关键创新**：最重要的创新在于将视频扩散先验与运动学模型结合，能够在真实数据基础上重建驾驶场景，解决了传统方法在新轨迹或复杂场景下的局限性。

**关键设计**：在设计中，ReconSimulator采用了特定的损失函数以优化场景重建质量，DAA通过调整周围车辆轨迹生成复杂场景，CTG则通过生成多样化的训练数据来解决数据分布偏差问题。

## 📊 实验亮点

实验结果表明，ReconDreamer-RL在端到端自动驾驶训练中表现优异，相较于模仿学习方法，碰撞率降低了5倍，显著提升了模型的安全性与可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶系统的开发与测试，尤其是在复杂交通场景下的安全性评估与优化。通过提高仿真环境的真实性，能够有效提升自动驾驶模型在真实世界中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement learning for training end-to-end autonomous driving models in closed-loop simulations is gaining growing attention. However, most simulation environments differ significantly from real-world conditions, creating a substantial simulation-to-reality (sim2real) gap. To bridge this gap, some approaches utilize scene reconstruction techniques to create photorealistic environments as a simulator. While this improves realistic sensor simulation, these methods are inherently constrained by the distribution of the training data, making it difficult to render high-quality sensor data for novel trajectories or corner case scenarios. Therefore, we propose ReconDreamer-RL, a framework designed to integrate video diffusion priors into scene reconstruction to aid reinforcement learning, thereby enhancing end-to-end autonomous driving training. Specifically, in ReconDreamer-RL, we introduce ReconSimulator, which combines the video diffusion prior for appearance modeling and incorporates a kinematic model for physical modeling, thereby reconstructing driving scenarios from real-world data. This narrows the sim2real gap for closed-loop evaluation and reinforcement learning. To cover more corner-case scenarios, we introduce the Dynamic Adversary Agent (DAA), which adjusts the trajectories of surrounding vehicles relative to the ego vehicle, autonomously generating corner-case traffic scenarios (e.g., cut-in). Finally, the Cousin Trajectory Generator (CTG) is proposed to address the issue of training data distribution, which is often biased toward simple straight-line movements. Experiments show that ReconDreamer-RL improves end-to-end autonomous driving training, outperforming imitation learning methods with a 5x reduction in the Collision Ratio.

