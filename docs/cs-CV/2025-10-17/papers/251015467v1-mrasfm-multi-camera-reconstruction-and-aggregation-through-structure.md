---
layout: default
title: MRASfM: Multi-Camera Reconstruction and Aggregation through Structure-from-Motion in Driving Scenes
---

# MRASfM: Multi-Camera Reconstruction and Aggregation through Structure-from-Motion in Driving Scenes

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.15467" target="_blank" class="toolbar-btn">arXiv: 2510.15467v1</a>
    <a href="https://arxiv.org/pdf/2510.15467.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15467v1" 
            onclick="toggleFavorite(this, '2510.15467v1', 'MRASfM: Multi-Camera Reconstruction and Aggregation through Structure-from-Motion in Driving Scenes')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Lingfeng Xuan, Chang Nie, Yiqing Xu, Zhe Liu, Yanzi Miao, Hesheng Wang

**分类**: cs.CV

**发布日期**: 2025-10-17

**备注**: 8 pages, 11 figures

---

## 💡 一句话要点

**MRASfM：提出多相机SfM框架，解决自动驾驶场景重建难题。**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `多相机系统` `SfM` `三维重建` `自动驾驶` `位姿估计`

## 📋 核心要点

1. 现有SfM方法在自动驾驶场景中，由于多相机系统位姿估计不稳定，路面重建易受干扰，重建效率较低。
2. MRASfM利用多相机系统固定空间关系提升位姿估计，采用平面模型去除路面重建异常值，并将多相机作为一个整体优化。
3. 实验表明，MRASfM在真实场景中具有良好的泛化性和鲁棒性，并在nuScenes数据集上取得了SOTA性能。

## 📝 摘要（中文）

本文提出了一种名为多相机重建与聚合的SfM（MRASfM）框架，专为自动驾驶场景设计。针对多相机系统在驾驶场景中应用SfM时面临的位姿估计不可靠、路面重建异常值过多以及重建效率低下的问题，MRASfM在注册过程中利用多相机系统固定的空间关系来提高相机位姿估计的可靠性。为了提升路面重建质量，该框架采用平面模型有效地去除三角化路面中的错误点。此外，将多相机组视为一个整体进行Bundle Adjustment (BA) 有助于减少优化变量，从而提高效率。MRASfM还通过由粗到精的场景关联和组装模块实现多场景聚合。通过在实际车辆上部署多相机系统，验证了MRASfM在各种场景中的泛化能力以及在具有挑战性条件下的鲁棒性。在公共数据集上的大规模验证结果表明，MRASfM 具有最先进的性能，在 nuScenes 数据集上实现了 0.124 的绝对位姿误差。

## 🔬 方法详解

**问题定义**：现有的SfM方法在应用于自动驾驶场景的多相机系统时，面临着三个主要问题：一是相机位姿估计的可靠性不足，容易受到噪声和遮挡的影响；二是路面重建过程中存在大量的异常值，导致重建质量下降；三是重建效率较低，难以满足大规模场景的需求。这些问题限制了SfM在自动驾驶领域的应用。

**核心思路**：MRASfM的核心思路是充分利用多相机系统固有的几何约束关系，并结合场景的先验知识，来提高SfM的性能和效率。具体来说，通过在位姿估计过程中引入多相机系统的固定空间关系，可以增强位姿估计的鲁棒性。利用平面模型对路面进行约束，可以有效地去除异常值。将多相机系统作为一个整体进行优化，可以减少优化变量，提高计算效率。

**技术框架**：MRASfM框架主要包含以下几个模块：1) 多相机系统标定：获取相机之间的相对位姿关系。2) 特征提取与匹配：提取图像中的特征点，并在不同图像之间进行匹配。3) 位姿估计：利用特征匹配和多相机系统的几何约束，估计相机的位姿。4) 路面重建：利用三角化方法重建路面，并使用平面模型去除异常值。5) Bundle Adjustment：对相机位姿和三维点进行全局优化。6) 多场景聚合：通过场景关联和组装模块，实现多场景的拼接。

**关键创新**：MRASfM的关键创新在于：1) 利用多相机系统的固定空间关系来提高位姿估计的可靠性。2) 采用平面模型来约束路面重建，有效地去除异常值。3) 将多相机系统作为一个整体进行Bundle Adjustment，减少优化变量，提高效率。这些创新使得MRASfM在自动驾驶场景中能够实现更准确、更鲁棒、更高效的重建。

**关键设计**：在位姿估计模块中，使用了RANSAC算法来去除错误的特征匹配。在路面重建模块中，使用了最小二乘法来拟合平面模型。在Bundle Adjustment模块中，使用了稀疏Bundle Adjustment算法来提高优化效率。多场景聚合模块采用了由粗到精的策略，首先进行粗略的场景关联，然后进行精细的场景组装。

## 📊 实验亮点

MRASfM在nuScenes数据集上取得了显著的性能提升，绝对位姿误差降低至0.124，优于现有方法。实验结果表明，MRASfM在各种驾驶场景中具有良好的泛化能力和鲁棒性，能够有效地处理光照变化、遮挡等挑战性情况。在实际车辆上的部署验证也证明了该方法的实用性。

## 🎯 应用场景

MRASfM在自动驾驶领域具有广泛的应用前景，可用于高精度地图构建、车辆定位、环境感知等任务。高质量的三维重建结果可以为自动驾驶系统提供更准确的环境信息，从而提高驾驶安全性。此外，该方法还可以应用于其他多相机系统相关的场景，例如无人机航拍、机器人导航等。

## 📄 摘要（原文）

> Structure from Motion (SfM) estimates camera poses and reconstructs point clouds, forming a foundation for various tasks. However, applying SfM to driving scenes captured by multi-camera systems presents significant difficulties, including unreliable pose estimation, excessive outliers in road surface reconstruction, and low reconstruction efficiency. To address these limitations, we propose a Multi-camera Reconstruction and Aggregation Structure-from-Motion (MRASfM) framework specifically designed for driving scenes. MRASfM enhances the reliability of camera pose estimation by leveraging the fixed spatial relationships within the multi-camera system during the registration process. To improve the quality of road surface reconstruction, our framework employs a plane model to effectively remove erroneous points from the triangulated road surface. Moreover, treating the multi-camera set as a single unit in Bundle Adjustment (BA) helps reduce optimization variables to boost efficiency. In addition, MRASfM achieves multi-scene aggregation through scene association and assembly modules in a coarse-to-fine fashion. We deployed multi-camera systems on actual vehicles to validate the generalizability of MRASfM across various scenes and its robustness in challenging conditions through real-world applications. Furthermore, large-scale validation results on public datasets show the state-of-the-art performance of MRASfM, achieving 0.124 absolute pose error on the nuScenes dataset.

