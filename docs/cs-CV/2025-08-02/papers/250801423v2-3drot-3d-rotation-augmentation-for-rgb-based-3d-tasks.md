---
layout: default
title: "3DRot: 3D Rotation Augmentation for RGB-Based 3D Tasks"
---

# 3DRot: 3D Rotation Augmentation for RGB-Based 3D Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01423" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01423v2</a>
  <a href="https://arxiv.org/pdf/2508.01423.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01423v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01423v2', '3DRot: 3D Rotation Augmentation for RGB-Based 3D Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shitian Yang, Deyu Li, Xiaoke Jiang, Lei Zhang

**分类**: cs.CV, cs.LG, cs.RO

**发布日期**: 2025-08-02 (更新: 2025-08-05)

---

## 💡 一句话要点

**提出3DRot以解决RGB基础3D任务的增强不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `3D检测` `数据增强` `几何一致性` `RGB图像` `深度估计` `单目视觉` `计算机视觉`

## 📋 核心要点

1. 现有的RGB基础3D任务在数据增强方面面临挑战，常用的图像变换会破坏几何一致性。
2. 3DRot通过围绕相机光心进行旋转和镜像，同时更新相关参数，确保几何一致性，解决了现有方法的不足。
3. 在实验中，3DRot显著提升了单目3D检测的性能，$IoU_{3D}$和$mAP_{0.5}$均有明显提高。

## 📝 摘要（中文）

RGB基础的3D任务（如3D检测、深度估计和3D关键点估计）面临着稀缺且昂贵的标注和有限的增强工具箱的问题。本文提出了3DRot，这是一种即插即用的增强方法，通过围绕相机光心旋转和镜像图像，同时同步更新RGB图像、相机内参、物体姿态和3D标注，以保持投影几何的一致性。我们在经典的单目3D检测任务上验证了3DRot的有效性。在SUN RGB-D数据集上，3DRot将$IoU_{3D}$从43.21提升至44.51，将旋转误差（ROT）从22.91$^	heta$降低至20.93$^	heta$，并将$mAP_{0.5}$从35.70提升至38.11。

## 🔬 方法详解

**问题定义**：本文旨在解决RGB基础3D任务中数据增强不足的问题。现有方法在进行图像变换时，常常会破坏几何一致性，导致性能下降。

**核心思路**：3DRot的核心思路是围绕相机光心进行图像的旋转和镜像，同时同步更新RGB图像、相机内参、物体姿态和3D标注，以保持投影几何的一致性。这样的设计使得增强过程不依赖于场景深度信息。

**技术框架**：3DRot的整体架构包括图像旋转、镜像处理和参数同步更新三个主要模块。首先，对输入图像进行旋转和镜像处理；然后，更新相机内参和物体姿态；最后，生成与之对应的3D标注。

**关键创新**：3DRot的主要创新在于其通过相机空间变换实现几何一致的旋转和反射，而不依赖于场景深度。这一方法与传统的增强技术有本质区别，后者往往无法保持几何一致性。

**关键设计**：在实现过程中，3DRot采用了特定的参数设置以确保旋转和镜像的准确性，并设计了相应的损失函数来优化模型性能。具体的网络结构和参数设置在论文中进行了详细描述。

## 📊 实验亮点

在实验中，3DRot在SUN RGB-D数据集上显著提升了性能，$IoU_{3D}$从43.21提升至44.51，旋转误差（ROT）从22.91$^	heta$降低至20.93$^	heta$，$mAP_{0.5}$从35.70提升至38.11，展示了其有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人视觉和增强现实等3D感知任务。通过提升RGB基础3D任务的性能，3DRot能够在实际应用中提高系统的准确性和鲁棒性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> RGB-based 3D tasks, e.g., 3D detection, depth estimation, 3D keypoint estimation, still suffer from scarce, expensive annotations and a thin augmentation toolbox, since most image transforms, including resize and rotation, disrupt geometric consistency. In this paper, we introduce 3DRot, a plug-and-play augmentation that rotates and mirrors images about the camera's optical center while synchronously updating RGB images, camera intrinsics, object poses, and 3D annotations to preserve projective geometry-achieving geometry-consistent rotations and reflections without relying on any scene depth. We validate 3DRot with a classical 3D task, monocular 3D detection. On SUN RGB-D dataset, 3DRot raises $IoU_{3D}$ from 43.21 to 44.51, cuts rotation error (ROT) from 22.91$^\circ$ to 20.93$^\circ$, and boosts $mAP_{0.5}$ from 35.70 to 38.11. As a comparison, Cube R-CNN adds 3 other datasets together with SUN RGB-D for monocular 3D estimation, with a similar mechanism and test dataset, increases $IoU_{3D}$ from 36.2 to 37.8, boosts $mAP_{0.5}$ from 34.7 to 35.4. Because it operates purely through camera-space transforms, 3DRot is readily transferable to other 3D tasks.

