---
layout: default
title: "VoxelSplat: Dynamic Gaussian Splatting as an Effective Loss for Occupancy and Flow Prediction"
---

# VoxelSplat: Dynamic Gaussian Splatting as an Effective Loss for Occupancy and Flow Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05563" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05563v1</a>
  <a href="https://arxiv.org/pdf/2506.05563.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05563v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05563v1', 'VoxelSplat: Dynamic Gaussian Splatting as an Effective Loss for Occupancy and Flow Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyue Zhu, Shenlong Wang, Jin Xie, Jiang-jiang Liu, Jingdong Wang, Jian Yang

**分类**: cs.CV

**发布日期**: 2025-06-05

**备注**: Accepted by CVPR 2025 Project Page: https://zzy816.github.io/VoxelSplat-Demo/

**🔗 代码/项目**: [PROJECT_PAGE](https://zzy816.github.io/VoxelSplat-Demo/)

---

## 💡 一句话要点

**提出VoxelSplat以解决动态环境下的占用与流预测问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态环境` `占用预测` `场景流` `3D高斯点云` `自监督学习` `语义理解` `计算机视觉`

## 📋 核心要点

1. 现有方法在动态环境下进行3D语义和场景流预测时，面临遮挡和环境不平衡等挑战，导致性能不足。
2. 提出的VoxelSplat框架通过2D投影增强语义监督，并利用自监督学习场景流，提升模型的学习能力。
3. 在多个基准数据集上的实验结果显示，VoxelSplat显著提高了语义占用和场景流估计的准确性。

## 📝 摘要（中文）

近年来，基于相机的占用预测在同时预测3D语义和场景流方面取得了进展，但面临诸如遮挡和动态环境不平衡等挑战。本文分析了这些挑战及其根本原因，并提出了一种新颖的正则化框架VoxelSplat。该框架利用3D高斯点云的最新发展，通过增强2D投影的语义监督和自监督学习场景流来提升模型性能。VoxelSplat可以无缝集成到现有的占用模型中，提升性能而不增加推理时间。大量实验表明，VoxelSplat在语义占用和场景流估计的准确性上均有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决在动态环境中进行3D语义和场景流预测时的遮挡和不平衡问题。现有方法在处理这些问题时效果不佳，导致预测准确性低下。

**核心思路**：VoxelSplat框架通过将稀疏的3D高斯语义投影到2D视图中，提供额外的监督信号，同时利用预测的场景流自监督学习运动物体的流动，从而提升模型性能。

**技术框架**：该框架主要包括两个模块：1) 2D投影模块，通过将3D高斯语义投影到2D空间来增强监督；2) 场景流学习模块，利用相邻帧的标签进行自监督学习，建模高斯的运动。

**关键创新**：VoxelSplat的创新在于结合了3D高斯点云的最新技术与自监督学习方法，能够有效解决动态环境中的占用和流预测问题，与传统方法相比，显著提升了模型的学习能力和准确性。

**关键设计**：在损失函数设计上，VoxelSplat引入了基于2D投影的语义损失和场景流损失，确保模型在训练过程中能够充分利用2D标签信息，同时优化高斯的运动建模。

## 📊 实验亮点

实验结果表明，VoxelSplat在多个基准数据集上显著提高了语义占用和场景流的估计准确性，具体提升幅度达到XX%（具体数据未知），并且在不增加推理时间的情况下，增强了模型的整体性能。

## 🎯 应用场景

该研究具有广泛的应用潜力，特别是在自动驾驶、机器人导航和增强现实等领域。通过提高动态环境下的占用和流预测准确性，VoxelSplat可以为智能系统提供更可靠的环境理解能力，进而提升其决策和行动的有效性。

## 📄 摘要（原文）

> Recent advancements in camera-based occupancy prediction have focused on the simultaneous prediction of 3D semantics and scene flow, a task that presents significant challenges due to specific difficulties, e.g., occlusions and unbalanced dynamic environments. In this paper, we analyze these challenges and their underlying causes. To address them, we propose a novel regularization framework called VoxelSplat. This framework leverages recent developments in 3D Gaussian Splatting to enhance model performance in two key ways: (i) Enhanced Semantics Supervision through 2D Projection: During training, our method decodes sparse semantic 3D Gaussians from 3D representations and projects them onto the 2D camera view. This provides additional supervision signals in the camera-visible space, allowing 2D labels to improve the learning of 3D semantics. (ii) Scene Flow Learning: Our framework uses the predicted scene flow to model the motion of Gaussians, and is thus able to learn the scene flow of moving objects in a self-supervised manner using the labels of adjacent frames. Our method can be seamlessly integrated into various existing occupancy models, enhancing performance without increasing inference time. Extensive experiments on benchmark datasets demonstrate the effectiveness of VoxelSplat in improving the accuracy of both semantic occupancy and scene flow estimation. The project page and codes are available at https://zzy816.github.io/VoxelSplat-Demo/.

