---
layout: default
title: RoboArmGS: High-Quality Robotic Arm Splatting via Bézier Curve Refinement
---

# RoboArmGS: High-Quality Robotic Arm Splatting via Bézier Curve Refinement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.17961" class="toolbar-btn" target="_blank">📄 arXiv: 2511.17961v1</a>
  <a href="https://arxiv.org/pdf/2511.17961.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.17961v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.17961v1', 'RoboArmGS: High-Quality Robotic Arm Splatting via Bézier Curve Refinement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Wang, Xiaobao Wei, Ying Li, Qingpo Wuwu, Dongli Wu, Jiajun Cao, Ming Lu, Wenzhao Zheng, Shanghang Zhang

**分类**: cs.RO

**发布日期**: 2025-11-22

---

## 💡 一句话要点

**RoboArmGS：基于贝塞尔曲线优化的高质量机械臂高斯溅射**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机械臂` `高斯溅射` `贝塞尔曲线` `运动建模` `Real2Sim2Real`

## 📋 核心要点

1. 现有方法依赖URDF绑定3D高斯，无法准确建模真实机械臂的噪声运动，导致渲染伪影。
2. 提出RoboArmGS，利用可学习的贝塞尔曲线优化URDF运动，更精确地建模真实机械臂运动。
3. 在RoboArm4D数据集上验证，RoboArmGS在运动建模和渲染质量上达到SOTA。

## 📝 摘要（中文）

构建高质量的机械臂数字资产对于Real2Sim2Real流程至关重要，但也极具挑战性。现有方法通常根据URDF链接静态地绑定3D高斯分布，使其被动地跟随URDF装配的运动。然而，真实机械臂的运动存在噪声，理想化的URDF装配运动无法准确地建模，导致3D高斯渲染中出现严重的伪影。为了解决这些问题，我们提出了RoboArmGS，一种新颖的混合表示，它使用可学习的贝塞尔曲线来优化URDF装配的运动，从而实现更准确的真实运动建模。具体来说，我们提出了一种可学习的贝塞尔曲线运动优化器，用于校正每个关节的残差，以解决真实运动和URDF装配运动之间的不匹配。RoboArmGS能够学习更准确的真实运动，同时实现机械臂各部件之间3D高斯分布的连贯绑定。为了支持未来的研究，我们贡献了一个精心收集的数据集，名为RoboArm4D，其中包含几个广泛使用的机械臂，用于评估构建高质量数字资产的质量。我们在RoboArm4D上评估了我们的方法，RoboArmGS在真实运动建模和渲染质量方面实现了最先进的性能。代码和数据集将会开源。

## 🔬 方法详解

**问题定义**：论文旨在解决机械臂数字资产构建中，由于真实机械臂运动的噪声和URDF模型理想化运动之间的差异，导致现有方法渲染质量差的问题。现有方法简单地将3D高斯分布绑定到URDF链接上，无法捕捉真实运动的细微变化，产生明显的渲染瑕疵。

**核心思路**：论文的核心思路是利用可学习的贝塞尔曲线来优化URDF模型提供的运动轨迹。通过学习每个关节的残差，使模型能够更准确地拟合真实机械臂的运动，从而提高渲染质量。这种方法在URDF模型的基础上进行精细调整，避免了完全从头学习运动的复杂性。

**技术框架**：RoboArmGS采用混合表示，结合了URDF模型和可学习的贝塞尔曲线。整体流程如下：1) 使用URDF模型初始化机械臂的运动轨迹。2) 引入可学习的贝塞尔曲线运动优化器，对每个关节的运动轨迹进行调整。3) 将优化后的运动轨迹用于3D高斯分布的绑定和渲染。RoboArm4D数据集用于训练和评估模型。

**关键创新**：关键创新在于提出了可学习的贝塞尔曲线运动优化器。与直接使用URDF模型或完全依赖学习的方法不同，该方法利用贝塞尔曲线的灵活性，对URDF模型提供的运动轨迹进行局部调整，从而更准确地建模真实运动。这种混合方法在保证运动连贯性的同时，提高了模型的表达能力。

**关键设计**：贝塞尔曲线运动优化器针对每个关节学习一组控制点，这些控制点决定了贝塞尔曲线的形状，进而影响关节的运动轨迹。损失函数可能包含渲染损失（例如D-SSIM、L1 loss）和正则化项，以保证运动的平滑性和连贯性。网络结构可能包含MLP等模块，用于学习贝塞尔曲线的控制点。

## 📊 实验亮点

RoboArmGS在RoboArm4D数据集上取得了显著的性能提升，在真实运动建模和渲染质量方面均优于现有方法。具体指标（例如PSNR、SSIM等）的提升幅度需要在论文中查找。实验结果表明，所提出的贝塞尔曲线运动优化器能够有效地校正URDF模型的误差，提高渲染质量，并实现机械臂各部件之间3D高斯分布的连贯绑定。

## 🎯 应用场景

RoboArmGS可应用于机器人仿真、机器人控制、虚拟现实等领域。高质量的机械臂数字资产能够提升仿真环境的真实感，帮助开发者更有效地进行算法验证和模型训练。此外，该技术还可以用于创建逼真的虚拟机械臂，为用户提供沉浸式的交互体验。未来，该技术有望推动Real2Sim2Real流程的发展，加速机器人技术的落地应用。

## 📄 摘要（原文）

> Building high-quality digital assets of robotic arms is crucial yet challenging for the Real2Sim2Real pipeline. Current approaches naively bind static 3D Gaussians according to URDF links, forcing them to follow an URDF-rigged motion passively. However, real-world arm motion is noisy, and the idealized URDF-rigged motion cannot accurately model it, leading to severe rendering artifacts in 3D Gaussians. To address these challenges, we propose RoboArmGS, a novel hybrid representation that refines the URDF-rigged motion with learnable Bézier curves, enabling more accurate real-world motion modeling. To be more specific, we present a learnable Bézier Curve motion refiner that corrects per-joint residuals to address mismatches between real-world motion and URDF-rigged motion. RoboArmGS enables the learning of more accurate real-world motion while achieving a coherent binding of 3D Gaussians across arm parts. To support future research, we contribute a carefully collected dataset named RoboArm4D, which comprises several widely used robotic arms for evaluating the quality of building high-quality digital assets. We evaluate our approach on RoboArm4D, and RoboArmGS achieves state-of-the-art performance in real-world motion modeling and rendering quality. The code and dataset will be released.

