---
layout: default
title: YoNoSplat: You Only Need One Model for Feedforward 3D Gaussian Splatting
---

# YoNoSplat: You Only Need One Model for Feedforward 3D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.07321" class="toolbar-btn" target="_blank">📄 arXiv: 2511.07321v1</a>
  <a href="https://arxiv.org/pdf/2511.07321.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.07321v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.07321v1', 'YoNoSplat: You Only Need One Model for Feedforward 3D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Botao Ye, Boqi Chen, Haofei Xu, Daniel Barath, Marc Pollefeys

**分类**: cs.CV

**发布日期**: 2025-11-10

**🔗 代码/项目**: [PROJECT_PAGE](https://botaoye.github.io/yonosplat/)

---

## 💡 一句话要点

**YoNoSplat：仅需单模型的前馈3D高斯溅射重建，适用于各种相机内外参场景**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D重建` `高斯溅射` `前馈网络` `相机位姿估计` `混合训练` `无位姿重建` `场景表示` `神经渲染`

## 📋 核心要点

1. 现有方法难以快速灵活地从无序图像集合中重建3D场景，尤其是在相机位姿未知的情况下。
2. YoNoSplat通过前馈网络直接预测局部高斯分布和相机参数，并采用混合训练策略解耦高斯分布和位姿的学习。
3. 实验表明，YoNoSplat在重建速度和质量上均达到了SOTA，仅需2.69秒即可重建包含100个视图的场景。

## 📝 摘要（中文）

本文提出YoNoSplat，一个前馈模型，用于从非结构化的图像集合中重建高质量的3D高斯溅射表示。该模型具有高度的通用性，可以有效地处理有位姿和无位姿、已标定和未标定的输入。YoNoSplat为每个视图预测局部高斯分布和相机位姿，然后使用预测的或提供的位姿将它们聚合为全局表示。为了克服联合学习3D高斯分布和相机参数的固有难度，我们引入了一种新颖的混合训练策略。该方法通过最初使用真实位姿来聚合局部高斯分布，并逐渐过渡到预测位姿和真实位姿的混合，从而缓解了两个任务之间的纠缠，防止了训练不稳定和暴露偏差。我们还通过一种新颖的成对相机距离归一化方案和将相机内参嵌入到网络中来解决尺度模糊问题。此外，YoNoSplat还预测内参，使其适用于未标定的输入。YoNoSplat展示了卓越的效率，在NVIDIA GH200 GPU上仅需2.69秒即可从100个视图（分辨率为280x518）重建场景。在无位姿和有位姿设置的标准基准测试中，它都实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决从无序图像集合中快速且灵活地重建高质量3D场景的问题。现有方法，特别是基于优化的方法，通常计算成本高昂，且对相机位姿的初始估计敏感。此外，联合优化3D高斯分布和相机参数是一个具有挑战性的问题，容易导致训练不稳定。

**核心思路**：论文的核心思路是使用一个前馈神经网络直接从图像中预测局部3D高斯分布和相机参数，避免了迭代优化过程。通过混合训练策略，逐步从依赖真实位姿过渡到依赖预测位姿，从而解耦3D高斯分布和相机参数的学习，提高训练的稳定性和泛化能力。

**技术框架**：YoNoSplat的整体框架包括以下几个主要模块：1) 特征提取模块，用于从输入图像中提取特征；2) 局部高斯分布预测模块，用于预测每个视图的局部3D高斯分布；3) 相机参数预测模块，用于预测每个视图的相机位姿和内参；4) 全局高斯分布聚合模块，用于将局部高斯分布聚合为全局3D场景表示。训练过程中，采用混合训练策略，逐步增加预测位姿的权重。

**关键创新**：论文的关键创新在于：1) 提出了一个完全前馈的3D高斯溅射重建模型，显著提高了重建速度；2) 引入了混合训练策略，有效解耦了3D高斯分布和相机参数的学习，提高了训练的稳定性和泛化能力；3) 提出了成对相机距离归一化方案，解决了尺度模糊问题。

**关键设计**：混合训练策略是关键设计之一，它通过控制真实位姿和预测位姿的比例来平衡训练的稳定性和泛化能力。具体来说，训练初期主要依赖真实位姿，随着训练的进行，逐渐增加预测位姿的权重。此外，成对相机距离归一化方案通过约束相机之间的相对距离来解决尺度模糊问题。损失函数包括高斯分布的重建损失和相机参数的损失。

## 📊 实验亮点

YoNoSplat在标准基准测试中取得了SOTA性能，尤其是在无位姿设置下。例如，在分辨率为280x518的100个视图的场景中，YoNoSplat仅需2.69秒即可完成重建，显著优于现有的基于优化的方法。此外，YoNoSplat还能够处理未标定的输入，进一步提高了其通用性。

## 🎯 应用场景

YoNoSplat具有广泛的应用前景，包括：1) 快速3D场景重建，可用于机器人导航、自动驾驶等领域；2) 虚拟现实/增强现实，可以快速生成高质量的3D场景；3) 视觉SLAM，可以提供更准确的相机位姿估计和地图构建。该研究的快速重建能力和对无位姿数据的处理能力，使其在实际应用中具有很高的价值。

## 📄 摘要（原文）

> Fast and flexible 3D scene reconstruction from unstructured image collections remains a significant challenge. We present YoNoSplat, a feedforward model that reconstructs high-quality 3D Gaussian Splatting representations from an arbitrary number of images. Our model is highly versatile, operating effectively with both posed and unposed, calibrated and uncalibrated inputs. YoNoSplat predicts local Gaussians and camera poses for each view, which are aggregated into a global representation using either predicted or provided poses. To overcome the inherent difficulty of jointly learning 3D Gaussians and camera parameters, we introduce a novel mixing training strategy. This approach mitigates the entanglement between the two tasks by initially using ground-truth poses to aggregate local Gaussians and gradually transitioning to a mix of predicted and ground-truth poses, which prevents both training instability and exposure bias. We further resolve the scale ambiguity problem by a novel pairwise camera-distance normalization scheme and by embedding camera intrinsics into the network. Moreover, YoNoSplat also predicts intrinsic parameters, making it feasible for uncalibrated inputs. YoNoSplat demonstrates exceptional efficiency, reconstructing a scene from 100 views (at 280x518 resolution) in just 2.69 seconds on an NVIDIA GH200 GPU. It achieves state-of-the-art performance on standard benchmarks in both pose-free and pose-dependent settings. Our project page is at https://botaoye.github.io/yonosplat/.

