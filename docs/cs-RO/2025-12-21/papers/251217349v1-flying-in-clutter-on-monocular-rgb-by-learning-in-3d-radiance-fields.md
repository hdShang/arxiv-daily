---
layout: default
title: Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation
---

# Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17349" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17349v1</a>
  <a href="https://arxiv.org/pdf/2512.17349.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17349v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17349v1', 'Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xijie Huang, Jinhan Li, Tianyue Wu, Xin Zhou, Zhichao Han, Fei Gao

**分类**: cs.RO

**发布日期**: 2025-12-19

**备注**: 8 pages, 7 figures

---

## 💡 一句话要点

**提出基于3D辐射场和对抗域适应的单目RGB图像无人机复杂环境导航方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机导航` `单目视觉` `3D辐射场` `对抗域适应` `零样本迁移`

## 📋 核心要点

1. 现有自主导航系统依赖激光雷达和深度相机，但成本高昂，探索仅使用单目RGB图像在复杂环境中导航是挑战。
2. 该论文提出了一种基于3D高斯溅射和对抗域适应的框架，在高保真模拟环境中训练策略，并最小化特征差异。
3. 实验结果表明，该策略能够实现对物理世界的鲁棒零样本迁移，在非结构化环境中实现安全敏捷的飞行。

## 📝 摘要（中文）

现代自主导航系统主要依赖激光雷达和深度相机。然而，一个根本问题仍然存在：飞行机器人能否仅使用单目RGB图像在复杂环境中导航？考虑到真实世界数据收集的高昂成本，在模拟环境中学习策略提供了一条有希望的途径。然而，由于显著的模拟到真实世界的感知差距，将这些策略直接部署到物理世界受到阻碍。因此，我们提出了一个框架，将3D高斯溅射（3DGS）环境的光真实感与对抗域适应相结合。通过在高保真模拟中训练，同时显式地最小化特征差异，我们的方法确保策略依赖于领域不变的线索。实验结果表明，我们的策略实现了对物理世界的鲁棒零样本迁移，从而能够在具有不同光照的非结构化环境中进行安全和敏捷的飞行。

## 🔬 方法详解

**问题定义**：论文旨在解决仅使用单目RGB图像，无人机在复杂环境中自主导航的问题。现有方法依赖激光雷达或深度相机，成本较高且体积较大。直接在模拟环境中训练策略并迁移到真实世界，会受到模拟到真实世界（sim-to-real）的感知差距的影响，导致性能下降。

**核心思路**：论文的核心思路是利用3D高斯溅射（3DGS）生成高保真度的模拟环境，并结合对抗域适应技术，减小模拟环境和真实环境之间的特征差异。通过训练一个能够提取领域不变特征的策略，实现从模拟到真实的零样本迁移。

**技术框架**：整体框架包含两个主要部分：高保真模拟环境构建和对抗域适应策略学习。首先，使用3DGS构建逼真的模拟环境。然后，设计一个对抗域适应网络，该网络包含一个策略网络和一个判别器网络。策略网络负责学习导航策略，判别器网络负责区分输入来自模拟环境还是真实环境。通过对抗训练，策略网络学习提取领域不变的特征，从而提高策略在真实环境中的泛化能力。

**关键创新**：该论文的关键创新在于将3DGS和对抗域适应相结合，用于解决单目RGB图像的无人机复杂环境导航问题。3DGS提供了高保真度的模拟环境，对抗域适应减小了模拟和真实环境之间的差距。这种结合使得策略能够从模拟环境迁移到真实环境，而无需额外的真实数据训练。

**关键设计**：在对抗域适应方面，使用了梯度反转层（Gradient Reversal Layer, GRL）来训练策略网络，使其提取的特征难以被判别器区分。损失函数包括策略网络的导航损失（例如，模仿学习损失或强化学习奖励）和对抗损失。对抗损失鼓励策略网络学习领域不变的特征。具体的网络结构和参数设置（例如，学习率、批大小、网络层数）在论文中有详细描述，但此处未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17349v1/figures/3dgs.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17349v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17349v1/figures/rl_training_comparison.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文提出的方法实现了在复杂环境下的鲁棒零样本迁移。实验结果表明，该策略能够在具有不同光照的非结构化环境中进行安全和敏捷的飞行。具体的性能数据（例如，成功率、平均飞行速度、避障距离等）和对比基线（例如，不使用对抗域适应的策略）在论文中有详细描述，但此处未知。

## 🎯 应用场景

该研究成果可应用于低成本、轻量化的无人机自主导航系统，尤其适用于资源受限或环境复杂的场景，如灾后搜救、农业巡检、室内导航等。通过降低对昂贵传感器的依赖，可以扩展无人机的应用范围，并促进无人机技术的普及。

## 📄 摘要（原文）

> Modern autonomous navigation systems predominantly rely on lidar and depth cameras. However, a fundamental question remains: Can flying robots navigate in clutter using solely monocular RGB images? Given the prohibitive costs of real-world data collection, learning policies in simulation offers a promising path. Yet, deploying such policies directly in the physical world is hindered by the significant sim-to-real perception gap. Thus, we propose a framework that couples the photorealism of 3D Gaussian Splatting (3DGS) environments with Adversarial Domain Adaptation. By training in high-fidelity simulation while explicitly minimizing feature discrepancy, our method ensures the policy relies on domain-invariant cues. Experimental results demonstrate that our policy achieves robust zero-shot transfer to the physical world, enabling safe and agile flight in unstructured environments with varying illumination.

