---
layout: default
title: PCIE_Pose Solution for EgoExo4D Pose and Proficiency Estimation Challenge
---

# PCIE_Pose Solution for EgoExo4D Pose and Proficiency Estimation Challenge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24411" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24411v1</a>
  <a href="https://arxiv.org/pdf/2505.24411.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24411v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24411v1', 'PCIE_Pose Solution for EgoExo4D Pose and Proficiency Estimation Challenge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feng Chen, Kanokphan Lertniphonphan, Qiancheng Yan, Xiaohui Fan, Jun Xie, Tao Zhang, Zhepeng Wang

**分类**: cs.CV

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出HP-ViT+解决RGB视频中的手部姿态估计问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手部姿态估计` `视觉变换器` `多模态融合` `动态环境` `深度学习`

## 📋 核心要点

1. 核心问题：现有方法在RGB自我中心视频中估计手部姿态时，面临微妙运动和频繁遮挡的挑战。
2. 方法要点：提出了HP-ViT+架构，结合视觉变换器与CNN，通过加权融合优化手部姿态预测。
3. 实验或效果：在手部姿态挑战中取得8.31 PA-MPJPE，在身体姿态挑战中取得11.25 MPJPE，均获得冠军。

## 📝 摘要（中文）

本报告介绍了我们团队（PCIE_EgoPose）在CVPR2025的EgoExo4D姿态和熟练度估计挑战中的解决方案。我们专注于从RGB自我中心视频中估计21个3D手关节的复杂任务，该任务受到微妙运动和频繁遮挡的影响。为此，我们开发了手部姿态视觉变换器（HP-ViT+），该架构结合了视觉变换器和CNN主干，通过加权融合来优化手部姿态预测。在EgoExo4D身体姿态挑战中，我们采用了多模态时空特征集成策略，以应对动态环境下身体姿态估计的复杂性。我们的方案在手部姿态挑战中取得了8.31 PA-MPJPE，在身体姿态挑战中取得了11.25 MPJPE，均获得了冠军头衔。我们将姿态估计解决方案扩展到熟练度估计任务，应用了基于变换器的核心技术，使我们在演示者熟练度估计比赛中实现了0.53的顶级准确率，达到了SOTA结果。

## 🔬 方法详解

**问题定义**：本论文旨在解决从RGB自我中心视频中准确估计21个3D手关节的问题。现有方法在处理微妙运动和频繁遮挡时表现不佳，导致姿态估计的准确性不足。

**核心思路**：论文提出的HP-ViT+架构结合了视觉变换器和卷积神经网络（CNN），通过加权融合策略来优化手部姿态的预测结果。这种设计旨在充分利用视觉变换器在捕捉全局特征方面的优势，同时保留CNN在局部特征提取上的强大能力。

**技术框架**：整体架构包括两个主要模块：手部姿态视觉变换器（HP-ViT+）和多模态时空特征集成策略。HP-ViT+负责手部姿态的估计，而多模态策略则用于处理动态环境下的身体姿态估计。

**关键创新**：最重要的技术创新在于HP-ViT+架构的设计，通过加权融合不同特征，显著提高了姿态估计的准确性。这一方法与传统的单一模型方法相比，能够更好地应对复杂场景中的遮挡和运动变化。

**关键设计**：在网络结构上，HP-ViT+采用了多层视觉变换器和CNN的组合，损失函数设计上则注重于加权融合不同来源的预测结果，以提升最终的姿态估计精度。

## 📊 实验亮点

在手部姿态挑战中，我们的方案实现了8.31 PA-MPJPE，在身体姿态挑战中实现了11.25 MPJPE，均获得了冠军头衔。此外，在演示者熟练度估计比赛中，我们的顶级准确率达到了0.53，创造了SOTA结果。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和人机交互等场景，能够为手势识别和动作捕捉提供更高的准确性和鲁棒性。未来，这项技术可能在医疗康复、游戏开发和智能家居等领域发挥重要作用。

## 📄 摘要（原文）

> This report introduces our team's (PCIE_EgoPose) solutions for the EgoExo4D Pose and Proficiency Estimation Challenges at CVPR2025. Focused on the intricate task of estimating 21 3D hand joints from RGB egocentric videos, which are complicated by subtle movements and frequent occlusions, we developed the Hand Pose Vision Transformer (HP-ViT+). This architecture synergizes a Vision Transformer and a CNN backbone, using weighted fusion to refine the hand pose predictions. For the EgoExo4D Body Pose Challenge, we adopted a multimodal spatio-temporal feature integration strategy to address the complexities of body pose estimation across dynamic contexts. Our methods achieved remarkable performance: 8.31 PA-MPJPE in the Hand Pose Challenge and 11.25 MPJPE in the Body Pose Challenge, securing championship titles in both competitions. We extended our pose estimation solutions to the Proficiency Estimation task, applying core technologies such as transformer-based architectures. This extension enabled us to achieve a top-1 accuracy of 0.53, a SOTA result, in the Demonstrator Proficiency Estimation competition.

