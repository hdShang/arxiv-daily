---
layout: default
title: 3D Ground Truth Reconstruction from Multi-Camera Annotations Using UKF
---

# 3D Ground Truth Reconstruction from Multi-Camera Annotations Using UKF

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.17609" class="toolbar-btn" target="_blank">📄 arXiv: 2511.17609v1</a>
  <a href="https://arxiv.org/pdf/2511.17609.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.17609v1" onclick="toggleFavorite(this, '2511.17609v1', '3D Ground Truth Reconstruction from Multi-Camera Annotations Using UKF')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linh Van Ma, Unse Fatima, Tepy Sokun Chriv, Haroon Imran, Moongu Jeon

**分类**: cs.CV

**发布日期**: 2025-11-18

**备注**: International Conference on Control, Automation and Information Sciences (ICCAIS) 2025, October 27 - 29, 2025 \| Jeju, Korea

---

## 💡 一句话要点

**提出一种基于UKF的多相机2D标注融合3D重建方法，用于自动驾驶等场景。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D重建` `多相机系统` `Unscented Kalman Filter` `2D标注` `目标跟踪`

## 📋 核心要点

1. 现有方法难以从多相机2D标注中准确重建3D ground truth，尤其是在存在遮挡的情况下。
2. 该方法利用UKF融合多相机2D标注，通过单应性投影将2D坐标转换为鲁棒的3D世界坐标。
3. 实验表明，该方法在3D定位方面具有高精度，并能输出物体的完整3D形状，优于现有方法。

## 📝 摘要（中文）

本文提出了一种新颖的方法，利用Unscented Kalman Filter (UKF) 将来自多个校准相机的2D bounding box或姿态关键点标注融合为精确的3D ground truth。该方法利用人工标注的2D ground truth，通过基于单应性的投影和基于UKF的融合，将2D图像坐标转换为鲁棒的3D世界坐标，实现多相机单目标跟踪。该算法处理多视角数据以估计物体的位置和形状，同时有效处理遮挡等挑战。我们在CMC、Wildtrack和Panoptic数据集上评估了该方法，结果表明，与现有的3D ground truth相比，该方法在3D定位方面具有很高的精度。与仅提供地面信息的现有方法不同，我们的方法还输出每个物体的完整3D形状。此外，该算法为多相机系统提供了一个可扩展且完全自动化的解决方案，仅使用2D图像标注。

## 🔬 方法详解

**问题定义**：论文旨在解决从多相机系统的2D图像标注中准确重建3D ground truth的问题。现有方法通常只提供地面信息，无法提供物体的完整3D形状，并且在处理遮挡等问题时表现不佳。此外，现有方法可能需要复杂的标定或人工干预，难以实现自动化和扩展。

**核心思路**：论文的核心思路是利用Unscented Kalman Filter (UKF) 融合来自多个校准相机的2D标注信息，从而估计出精确的3D物体位置和形状。通过将2D图像坐标投影到3D世界坐标系，并利用UKF进行状态估计和噪声抑制，可以有效地处理多视角数据中的不确定性和遮挡问题。

**技术框架**：该方法主要包含以下几个阶段：1) 2D标注获取：从多个校准相机获取2D bounding box或姿态关键点标注。2) 单应性投影：利用相机内外参数和单应性矩阵，将2D图像坐标投影到3D世界坐标系。3) UKF融合：使用UKF将来自不同相机的3D坐标估计进行融合，得到最终的3D物体位置和形状估计。4) 状态更新：根据UKF的预测和更新步骤，不断优化3D物体状态估计。

**关键创新**：该方法的主要创新在于利用UKF框架有效地融合了多相机2D标注信息，从而实现了精确的3D ground truth重建。与现有方法相比，该方法不仅可以提供物体的3D位置，还可以估计物体的完整3D形状。此外，该方法具有可扩展性和自动化特性，只需2D图像标注即可实现多相机系统的3D重建。

**关键设计**：在UKF框架中，需要选择合适的状态向量、过程噪声和观测噪声。状态向量可以包含物体的位置、速度和形状参数。过程噪声用于模拟物体运动的不确定性，观测噪声用于模拟2D标注的误差。此外，单应性矩阵的计算精度也会影响最终的3D重建结果。论文可能还涉及一些参数调优，例如UKF的参数设置，以及单应性矩阵的鲁棒估计方法。

## 📊 实验亮点

该方法在CMC、Wildtrack和Panoptic数据集上进行了评估，实验结果表明，与现有的3D ground truth相比，该方法在3D定位方面具有很高的精度。此外，该方法能够输出物体的完整3D形状，而不仅仅是地面信息，这为后续的应用提供了更丰富的信息。实验结果验证了该方法在多相机3D重建方面的有效性和优越性。

## 🎯 应用场景

该研究成果可广泛应用于自动驾驶、智能监控、机器人等领域。在自动驾驶中，可以利用该方法从多相机数据中重建周围环境的3D模型，提高车辆的感知能力和安全性。在智能监控中，可以用于跟踪和识别人群中的目标，实现更智能的监控系统。在机器人领域，可以帮助机器人更好地理解和操作周围环境。

## 📄 摘要（原文）

> Accurate 3D ground truth estimation is critical for applications such as autonomous navigation, surveillance, and robotics. This paper introduces a novel method that uses an Unscented Kalman Filter (UKF) to fuse 2D bounding box or pose keypoint ground truth annotations from multiple calibrated cameras into accurate 3D ground truth. By leveraging human-annotated ground-truth 2D, our proposed method, a multi-camera single-object tracking algorithm, transforms 2D image coordinates into robust 3D world coordinates through homography-based projection and UKF-based fusion. Our proposed algorithm processes multi-view data to estimate object positions and shapes while effectively handling challenges such as occlusion. We evaluate our method on the CMC, Wildtrack, and Panoptic datasets, demonstrating high accuracy in 3D localization compared to the available 3D ground truth. Unlike existing approaches that provide only ground-plane information, our method also outputs the full 3D shape of each object. Additionally, the algorithm offers a scalable and fully automatic solution for multi-camera systems using only 2D image annotations.

